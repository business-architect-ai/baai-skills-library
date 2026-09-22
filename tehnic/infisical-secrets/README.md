# infisical-secrets — chei API luate din seif, nu din .env

Agentul cere cheile de care are nevoie dintr-un proiect Infisical, exact
înainte de apelul care le folosește. În mediul lui rămâne o singură
credențială, cea care deschide seiful. Cheile nu mai stau în `.env`, nu ajung
în context și nu se scriu în memoria agentului.

Când o cheie se schimbă, o schimbi într-un singur loc. Toți agenții iau
valoarea nouă la următoarea cerere, fără redeploy și fără repornire.

## Când îl folosești

- Ai agenți care rulează pe alte mașini decât a ta (VPS, server, laptopul unui
  coleg), unde seiful sistemului tău nu e accesibil
- Mai mulți agenți folosesc aceeași cheie și vrei să o rotești o singură dată
- Ai nevoie de valori diferite pentru același nume de cheie, pe medii diferite
- Vrei să vezi cine a citit ce cheie și când

## Când nu îți trebuie

Dacă lucrezi singur, pe o singură mașină, seiful sistemului de operare
rezolvă aceeași problemă fără cont și fără rețea: Keychain pe macOS,
SecretManagement din PowerShell pe Windows. Infisical își merită complexitatea
abia când cheile trebuie să ajungă în mai multe locuri.

## Ce conține

```
infisical-secrets/
├── skill.md              instrucțiunile pe care le urmează agentul
├── README.md
└── tools/
    ├── ia-secret.sh      varianta bash, doar curl
    └── ia_secret.py      varianta Python, doar biblioteca standard
```

Ambele unelte fac același lucru și dau aceleași mesaje de eroare. Nu au
nevoie de `jq`, de `requests` sau de CLI-ul Infisical.

## Instalare

### Claude Code

```bash
mkdir -p ~/.claude/skills/infisical-secrets
cp skill.md ~/.claude/skills/infisical-secrets/SKILL.md
cp -R tools ~/.claude/skills/infisical-secrets/
```

### Codex

```bash
mkdir -p ~/.codex/skills/infisical-secrets
cp skill.md ~/.codex/skills/infisical-secrets/SKILL.md
cp -R tools ~/.codex/skills/infisical-secrets/
```

## Configurare

1. Fă-ți cont pe [infisical.com](https://infisical.com) (are plan gratuit) sau
   pornește o instanță proprie.
2. Creează un proiect și pune cheile în el, pe mediul potrivit.
3. Creează o Machine Identity cu metoda Universal Auth și dă-i drept de
   **citire** pe proiectul respectiv. Notează Client ID și Client Secret.
4. Pune în mediul agentului:

```
INFISICAL_PROJECT_ID      din Project Settings
INFISICAL_CLIENT_ID       de la Machine Identity
INFISICAL_CLIENT_SECRET   de la Machine Identity
```

Opțional: `INFISICAL_ENV` (implicit `dev`), `INFISICAL_SECRET_PATH` (implicit
`/`), `INFISICAL_API_URL` (implicit `https://app.infisical.com`, pentru UE
`https://eu.infisical.com`, sau adresa instanței tale).

Dă identității drept de citire, nu de scriere. Un agent care poate suprascrie
cheile e o problemă mai mare decât una care doar le citește.

### Unde ții credențiala de acces

Client Secret-ul rămâne un secret. Pe mașina ta, ia-l din seiful sistemului
la pornirea agentului, nu îl scrie în `.env`:

```bash
# macOS
export INFISICAL_CLIENT_SECRET=$(security find-generic-password -s infisical-client-secret -w)
```

Pe un server, folosește mecanismul de secrete al platformei (variabile de
mediu ale serviciului, nu fișiere în repo).

## Verificare

```bash
INFISICAL_PROJECT_ID=... INFISICAL_CLIENT_ID=... INFISICAL_CLIENT_SECRET=... \
  tools/ia-secret.sh UN_SECRET_DE_TEST
```

Dacă iese valoarea, configurarea e bună. Dacă nu, mesajul îți spune exact ce
lipsește.

## Note tehnice

**Secretele nu trec prin linia de comandă.** Tokenul și Client Secret-ul intră
în `curl` prin stdin, cu `-K -`, nu ca argumente. Altfel ar fi vizibile
oricărui utilizator al mașinii printr-un simplu `ps`.

**Un 404 de la Infisical are două cauze.** Ori secretul nu există, ori tokenul
nu există. Codul e identic, doar mesajul diferă. Uneltele fac distincția și îți
spun care dintre ele e, ca să nu cauți o greșeală de tipar într-un nume corect.

**Uneltele merg pe macOS, Linux și BSD.** Nimic din ele nu depinde de
extensii GNU.

## Despre sursă

Skillul e scris de la zero peste [API-ul public
Infisical](https://infisical.com/docs/api-reference/overview/introduction),
verificat direct pe endpointurile live, nu adaptat din alt repo.

Ideea a circulat public prin `grandamenium/infisical-skill`, care ne-a dat
punctul de plecare. Nu am importat codul de acolo din două motive: repoul nu
are licență, iar `CONTRIBUTING.md` al librăriei cere licență permisivă pentru
importuri; și implementarea lui se oprea pe macOS înainte să întoarcă vreo
valoare, din cauza unui `head -n -1` care nu există în afara GNU coreutils.

## Alternativă oficială

Infisical are CLI propriu și un server MCP oficial. Dacă ai nevoie de mai mult
decât citire de valori (scriere, sincronizare, gestionare de proiecte),
uită-te întâi la ele. Skillul ăsta acoperă intenționat un singur lucru: citirea
unei valori, în siguranță, din interiorul unui agent.
