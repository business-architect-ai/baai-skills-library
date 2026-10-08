# sus-panel: test de uzabilitate cu utilizatori simulați

Câțiva oameni simulați, fiecare cu alt profil, parcurg materialul tău și spun sincer unde
s-au împiedicat. La final primești frecările ordonate după gravitate și, pentru interfețe și
ghiduri, scorul SUS (System Usability Scale), calculat de un script, nu estimat de model.

Skillul nu știe nimic despre publicul tău până nu te întreabă. Pornește cu un onboarding
scurt despre cine se uită la material, propune persona diferite între ele (3-5 implicit,
până la 10 dacă vrei) și le scrie pe disc doar după ce le aprobi. Data viitoare le refolosești.

## Când îl folosești

- Ai un landing page, un site sau o aplicație și vrei să vezi unde se pierde un client
- Ai scris un ghid pas cu pas pentru cursanți sau clienți și vrei să știi unde se blochează
- Ai un articol și vrei să verifici dacă ajunge mesajul pe care voiai să-l transmiți
- Vrei un filtru ieftin înainte de un test cu oameni reali

## Ce nu este

Nu înlocuiește testul cu oameni reali. Persona sunt simulate de un model de limbaj: nu se
plictisesc cu adevărat, înțeleg aproape orice text și tind să dea scoruri mai mari decât
oamenii. Valoarea stă în frecările găsite, nu în cifră. Skillul îți recomandă la final să
verifici frecările grave cu 3-5 oameni reali.

## Cum ține persona sincere

- **Fiecare persona e un subagent separat**, care primește doar ce ar primi un om real: o
  sarcină și materialul. Nu află ce vrei tu să obții, deci nu-ți poate spune ce vrei să auzi.
- **Plafon de cunoaștere.** Fiecare persona are o secțiune „Ce știu și ce nu știu”. Un
  începător nu începe brusc să vorbească despre „arhitectura informației”.
- **Abandonul e un rezultat.** Persona se opresc unde s-ar opri un om real și spun de ce.
- **Două straturi separate.** Persona scrie doar reacția brută. Analiza, severitățile și
  recomandările le face sesiunea principală, după aceea.

## Mărimea panelului

| Variantă | Ce face | Când merită |
|---|---|---|
| **Standard** (implicit) | 3-5 persona, câte o rulare | Aproape mereu. Găsește majoritatea problemelor la un cost rezonabil |
| **Panel lărgit** | 6-10 persona, câte o rulare | Când publicul tău e foarte variat și 5 profiluri nu-l acoperă |
| **Repetări** | Fiecare persona rulează de 2-3 ori, independent | Când vrei să știi dacă scorul unei persona e stabil sau zgomot și care frecări apar de fiecare dată |

Panelul lărgit și repetările se pot combina. Înainte să pornească o variantă care nu e
standard, skillul îți spune câte rulări înseamnă și o estimare de tokeni, apoi așteaptă
confirmarea. Reper măsurat: în jur de 90.000 de tokeni pe persona pentru un ghid de ~150 de rânduri și 100.000-140.000 pentru o aplicație web mare.
Persona simulate vin din același model, deci câștigul de la persona în plus scade repede.

## Chestionarul, după tipul materialului

| Material | Chestionar |
|---|---|
| Interfață (site, aplicație, formular) | SUS, cu „website” / „app” în loc de „system” |
| Ghid de urmat (tutorial, instrucțiuni) | SUS, cu „guide” în loc de „system” |
| Text de citit (articol, newsletter) | Fără SUS. Test de înțelegere: ce a reținut fiecare persona, comparat cu mesajul tău |

Întrebările SUS rămân în engleză, în forma originală (Brooke, 1986). Nu există o traducere
românească validată, iar o traducere ad-hoc ar schimba ce măsoară scala.

## Ce conține

```
sus-panel/
├── skill.md                       instrucțiunile pe care le urmează agentul
├── references/
│   ├── onboarding.md              întrebările despre public și cum alegi persona
│   ├── persona-sablon.md          forma unui fișier de persona
│   ├── reactie-persona.md         ce primește fiecare persona: reacția + chestionarul
│   └── raport-sablon.md           forma raportului final
└── tools/
    └── sus_scor.py                calculul SUS, doar biblioteca standard Python
```

## Instalare

Skillul are nevoie de tot folderul, nu doar de `skill.md`. Din rădăcina librăriei:

```bash
mkdir -p ~/.claude/skills/sus-panel
cp design/sus-panel/skill.md ~/.claude/skills/sus-panel/SKILL.md
cp -R design/sus-panel/references design/sus-panel/tools ~/.claude/skills/sus-panel/
```

Cerințe:
- **Claude Code**, pentru subagenți
- **Python 3**, pentru scor (`python3 --version` ca să verifici)
- **Playwright MCP**, doar dacă testezi site-uri live

## Folosire

```
/sus-panel https://site-ul-meu.ro, programează-te la o consultație
/sus-panel ghidul din docs/instalare.md
/sus-panel articolul ăsta (și lipești textul)
```

Persona se salvează în proiect, în `persone/`, iar rapoartele în `teste-utilizatori/`.

## Origine

Scris de la zero pentru BAAI. Ideile despre briefingul curat, plafonul de cunoaștere și
separarea persona de analist vin din
[customer-panel](https://github.com/jasonfletchall1/customer-panel) (fără licență, deci doar
ideile, nu textul) și [synthetic-user-feedback](https://github.com/travisseh/synthetic-user-feedback).
Formula SUS și scala de note: Brooke (1986), Sauro și Lewis (2016).
