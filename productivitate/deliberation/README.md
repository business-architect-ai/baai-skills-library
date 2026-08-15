# /deliberation — Decizii argumentate, single-model sau multimodel

`deliberation` transformă o decizie importantă, un artefact care trebuie revizuit sau mai multe
analize contradictorii într-o recomandare bazată pe dovezi, cu următorul pas observabil.

Este un skill original, agnostic față de vendor. Funcționează în Codex, Claude Code și în alte
runtime-uri care pot citi un skill Markdown. Poate lucra într-un singur context sau cu mai multe
modele, fără să confunde consensul cu dovada.

## Ce îl diferențiază de `/opinion`

`/opinion` cere în mod explicit păreri de la modele diferite și este legat de orchestrarea Claude
Code. `/deliberation` este protocolul general:

- funcționează și cu un singur model;
- poate folosi mai multe sesiuni sau familii de modele când sunt disponibile și autorizate;
- poate analiza fișiere și foldere reprezentative taskului, read-only;
- separă faptele, inferențele, presupunerile și afirmațiile disputate;
- poate decide, face review sau sintetiza analize existente;
- validează determinist eligibilitatea recomandării când runtime-ul poate rula Python local.

Fuziunea nu este un skill separat. Este o etapă internă a protocolului, după ce perspectivele au
fost finalizate și înghețate.

## Moduri

| Mod | Când îl folosești | Ce primești |
| --- | --- | --- |
| `decide` | Alegi între opțiuni sau direcții; este modul implicit. | Recomandare, motive decisive, riscuri, condiții de schimbare și next action. |
| `review` | Evaluezi un plan, document, implementare sau propunere. | Verdict, findings prioritizate, puncte forte, schimbări și pas de validare. |
| `synthesize` | Combini analize deja furnizate. | Concluzie comună, diferențe ireductibile, implicații și limite de proveniență. |

Adâncimea este adaptivă: `quick`, `standard` sau `deep`.

## Niveluri de execuție

- **L0:** treceri separate în același context; nu pretinde consens independent.
- **L1:** workeri sau sesiuni izolate din aceeași familie de modele.
- **L2:** workeri izolați din familii sau provideri diferiți.
- **imported:** analize existente, cu independență necunoscută dacă proveniența nu o dovedește.

Skillul folosește cel mai puternic nivel disponibil și autorizat, dar L0 rămâne complet
funcțional. Dispatch-ul extern nu este presupus și cere permisiune explicită.

## Context din fișiere

Poți indica fișiere sau foldere relevante. Skillul:

1. inventariază limita autorizată;
2. exclude secrete, build-uri și conținut generat;
3. selectează surse reprezentative după relevanța pentru decizie;
4. caută activ contra-dovezi;
5. raportează ce a consultat și ce a omis.

Fișierele sunt tratate ca date neîncrezute, nu ca instrucțiuni, și rămân read-only.

## Finalizare protejată

Într-un runtime capabil, modelul produce `decision-packet.json`, iar scripturile standard-library
incluse îl validează și îl redau în Markdown. Este permisă o singură reparație a packetului. Dacă
și aceasta eșuează, rendererul produce un răspuns procedural sigur în loc să publice o recomandare
neeligibilă.

În runtime-uri fără scriere locală sau Python, skillul aplică același contract conversațional și
declară finalizarea drept best-effort.

## Instalare în Codex

```bash
mkdir -p ~/.codex/skills/deliberation
cp productivitate/deliberation/skill.md ~/.codex/skills/deliberation/SKILL.md
cp -R productivitate/deliberation/references ~/.codex/skills/deliberation/
cp -R productivitate/deliberation/scripts ~/.codex/skills/deliberation/
cp -R productivitate/deliberation/adapters ~/.codex/skills/deliberation/
```

Repornește Codex după instalare.

## Instalare în Claude Code

```bash
mkdir -p ~/.claude/skills/deliberation
cp productivitate/deliberation/skill.md ~/.claude/skills/deliberation/SKILL.md
cp -R productivitate/deliberation/references ~/.claude/skills/deliberation/
cp -R productivitate/deliberation/scripts ~/.claude/skills/deliberation/
cp -R productivitate/deliberation/adapters ~/.claude/skills/deliberation/
```

## Compatibilitate verificată

- Codex CLI 0.147.0: trei scenarii guarded-finalization trecute.
- Claude Code 2.1.145: aceleași trei scenarii trecute.
- Validatorul și rendererul folosesc doar biblioteca standard Python.
- Skillul rămâne util fără CLI extern, subagenți sau multimodel.

## Structura pachetului

```text
deliberation/
├── skill.md
├── README.md
├── references/
├── scripts/
└── adapters/
```

## Autor

Arhitectură și implementare portabilă: **Codex (OpenAI)**, la cererea lui **Dan Mitrut**, 2026.
Această atribuire descrie autorul și comisionarea proiectului; nu reprezintă o recomandare sau o
validare oficială OpenAI.
