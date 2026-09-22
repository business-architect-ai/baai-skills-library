---
name: "infisical-secrets"
compatibility: codex-and-claude-code
description: "Citește chei API din Infisical în momentul folosirii lor, ca să nu stea în .env, în contextul agentului sau în memoria lui. Folosește când agentul are nevoie de o credențială pentru un apel extern, când construiești un agent care rulează pe altă mașină decât a ta, sau când mai mulți agenți trebuie să folosească aceeași cheie."
license: MIT
---

# Secrete din Infisical, luate la nevoie

## Ce rezolvă

Un agent care are nevoie de chei API le ține, de obicei, într-un `.env` de
lângă cod. Fișierul ajunge în backup, în sincronizarea cloud, uneori în
istoricul git. Când cheia se schimbă, o schimbi pe fiecare mașină.

Skillul mută cheile într-un seif în rețea (Infisical) și le cere de acolo
exact înainte de apelul care are nevoie de ele. În mediul agentului rămâne
o singură credențială, cea care deschide seiful. Dacă scapă, o revoci
dintr-un singur loc și nicio altă cheie nu e atinsă.

## Când îl folosești

- Agentul apelează un serviciu extern care cere autentificare.
- Agentul rulează pe altă mașină decât a ta (server, VPS, laptopul unui coleg),
  unde seiful local al sistemului nu e accesibil.
- Mai mulți agenți folosesc aceeași cheie și vrei să o rotești o singură dată.
- Ai nevoie de valori diferite pentru același nume de cheie, pe medii diferite.

## Când NU îl folosești

Dacă lucrezi singur, pe o singură mașină, seiful sistemului de operare este
mai simplu și nu cere cont sau rețea. Pe macOS ai Keychain, pe Windows ai
SecretManagement din PowerShell. Infisical își merită complexitatea abia
când cheile trebuie să ajungă în mai multe locuri.

## Reguli de purtare pentru agent

Astea nu sunt opționale. Sunt motivul pentru care skillul există.

1. **Ceri valoarea imediat înainte de apelul care o folosește.** Nu la
   începutul sesiunii, nu „ca să o ai".
2. **Nu o pui într-o variabilă care trăiește după apel.** Iese din scope și
   gata.
3. **Nu o scrii nicăieri**: nu în răspunsul tău către utilizator, nu în
   fișiere de memorie, nu în note de task, nu în loguri, nu în mesaje către
   alți agenți. Dacă alt agent are nevoie de ea, o cere și el de la Infisical.
4. **Nu o afișezi ca să confirmi că a mers.** Confirmi că apelul a reușit,
   nu că valoarea arată cum trebuie.
5. **Când o cerere eșuează, raportezi eroarea așa cum e.** Nu încerci altă
   cheie, nu continui cu o valoare goală, nu inventezi un fallback.

## Configurare

În mediul agentului pun doar credențialele de acces la seif:

```
INFISICAL_PROJECT_ID      ID-ul proiectului, din Project Settings
INFISICAL_CLIENT_ID       Machine Identity, Universal Auth
INFISICAL_CLIENT_SECRET   Machine Identity, Universal Auth
```

Opțional:

```
INFISICAL_ENV             mediul, implicit "dev"
INFISICAL_SECRET_PATH     calea în proiect, implicit "/"
INFISICAL_API_URL         implicit https://app.infisical.com
                          UE: https://eu.infisical.com, sau instanța proprie
INFISICAL_TOKEN           un token gata obținut, în loc de perechea de mai sus
```

Perechea Client ID plus Client Secret e de preferat unui token fix: uneltele
o schimbă pe un token de scurtă durată la fiecare rulare.

## Folosire

### Bash

```bash
CHEIE=$(tools/ia-secret.sh SENDGRID_API_KEY) || exit 1

curl -sS -X POST https://api.sendgrid.com/v3/mail/send \
  -H "Authorization: Bearer ${CHEIE}" \
  -H "Content-Type: application/json" \
  -d '{"personalizations":[{"to":[{"email":"cineva@exemplu.ro"}]}]}'

unset CHEIE
```

Scriptul iese cu cod diferit de zero și scrie pe stderr când ceva nu merge.
Nu ignora asta, altfel trimiți un request cu antet gol.

### Python

```python
from ia_secret import ia_secret, EroareInfisical

def trimite_raport(continut: str) -> dict:
    cheie = ia_secret("SENDGRID_API_KEY")   # cerută aici, nu mai sus
    raspuns = requests.post(
        "https://api.sendgrid.com/v3/mail/send",
        headers={"Authorization": f"Bearer {cheie}"},
        json={"content": continut},
    )
    raspuns.raise_for_status()
    return raspuns.json()
    # cheie iese din scope aici
```

Prinde `EroareInfisical` doar ca să raportezi clar, nu ca să continui fără cheie.

## Cheia s-a rotit în timpul sesiunii

Dacă un apel întoarce 401 deși mergea înainte, cheia a fost probabil rotită
în Infisical. Ceri valoarea din nou și reîncerci **o singură dată**. Dacă și
a doua încercare dă 401, te oprești și raportezi. Nu intra într-o buclă.

```python
for incercare in range(2):
    cheie = ia_secret("SERVICE_API_KEY")
    raspuns = requests.post(endpoint, headers={"Authorization": f"Bearer {cheie}"})
    if raspuns.status_code == 401 and incercare == 0:
        continue          # poate s-a rotit, cere din nou
    raspuns.raise_for_status()
    break
else:
    raise RuntimeError("autentificare eșuată și după reîncercare")
```

## Ce înseamnă erorile

Codul HTTP singur nu spune adevărul la Infisical, mesajul contează.
Uneltele traduc deja, dar dacă citești răspunsuri brute:

| Cod | Ce înseamnă de fapt |
|---|---|
| 401 | Lipsește antetul de autorizare, sau credențialele de login sunt greșite |
| 403 | Token malformat, sau identitatea nu are drept de citire acolo |
| 404 | **Două cauze**: secretul nu există, **sau** tokenul nu există. Mesajul cu „Service token" arată a doua cauză |

Un 404 nu înseamnă automat că ai greșit numele secretului. Citește mesajul
înainte să cauți greșeala în altă parte.

## Verificare înainte de folosire reală

```bash
INFISICAL_PROJECT_ID=... INFISICAL_CLIENT_ID=... INFISICAL_CLIENT_SECRET=... \
  tools/ia-secret.sh UN_SECRET_DE_TEST
```

Dacă iese valoarea de test, configurarea e bună. Șterge secretul de test
după aceea, ca să nu rămână în proiect ceva fără rost.
