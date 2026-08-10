# /transcript-to-tool-miner — Din transcripturi în instrumente de lucru

Extrage din transcripturi, podcasturi, interviuri, note și corpuri de research lucrurile care merită transformate în instrumente, principii operaționale, workflow-uri sau evaluatoare. Nu face un rezumat convențional și nu confundă noutățile despre produse cu ideile reutilizabile.

## Când îl folosești

- Vrei să transformi un transcript în proceduri sau instrumente concrete.
- Cauți principii de lucru aplicabile, nu doar idei interesante.
- Ai mai multe transcripturi și vrei un raport deduplicat, cu surse și nivel de încredere.
- Materialul amestecă practici durabile cu lansări, prețuri, benchmarkuri și opinii despre furnizori.

## Ce produce

- Un shortlist de maximum cinci lucruri cu valoare bună raportată la efortul de construcție.
- Fișe complete pentru instrumente, workflow-uri și evaluatoare.
- Principii operaționale cu regulă, context, anti-pattern și mecanism de aplicare.
- Compoziții între capabilități distincte, fără să le contopească.
- Semnale respinse sau incomplete, cu motivul respingerii.
- Inventarul surselor procesate și limitele de acoperire.

## Compatibilitate

Testat end-to-end în Claude Code și Codex. Pachetul este agnostic față de runtime și nu depinde de subagenți, tooluri sau modele specifice unui furnizor.

## Instalare Claude Code

```bash
mkdir -p ~/.claude/skills/transcript-to-tool-miner/references
cp productivitate/transcript-to-tool-miner/skill.md ~/.claude/skills/transcript-to-tool-miner/SKILL.md
cp productivitate/transcript-to-tool-miner/references/*.md ~/.claude/skills/transcript-to-tool-miner/references/
```

## Instalare Codex

```bash
mkdir -p ~/.codex/skills/transcript-to-tool-miner/references
cp productivitate/transcript-to-tool-miner/skill.md ~/.codex/skills/transcript-to-tool-miner/SKILL.md
cp productivitate/transcript-to-tool-miner/references/*.md ~/.codex/skills/transcript-to-tool-miner/references/
```

## Utilizare

```text
/transcript-to-tool-miner pe transcript.md
```

Poate primi text lipit, un fișier, o listă explicită de fișiere sau un folder. Pentru corpusuri procesează loturi de maximum 25 de surse și declară ce a citit, ce a sărit și ce a rămas incomplet.

Implicit întoarce raportul în conversație. Dacă îi ceri un artifact fără să indici calea, îl salvează în `tool-extractions/YYYY-MM-DD-<source-slug>.md` în workspace-ul curent.
