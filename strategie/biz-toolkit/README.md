# biz-toolkit ★

Pachet complet de consultanță de business pentru soloprenori și antreprenori mici: 15 module conduse de specialiști virtuali (strateg, copywriter, analist, consultant de operațiuni), cu un router care alege modulul potrivit, memorie care învață și un context de afacere comun tuturor modulelor.

Spre deosebire de comenzile individuale `biz-*`, biz-toolkit le reunește pe toate într-un singur skill: nu re-întreabă bazele afacerii la fiecare modul și devine mai precis pe măsură ce îl folosești.

## Ce conține

| Modul | Ce face |
|---|---|
| review | Diagnostic de business pe 6 dimensiuni |
| pricing | Strategie de preț: valoare, benchmarking, tarife pe 3 niveluri, Van Westendorp |
| offer | Construcție de ofertă: Value Equation, denumirea ofertei, garanții |
| copy | Copy pe vocea brandului: unghiuri complete, email rece vs cald, cuvinte de evitat |
| customer | Avatar client din date reale sau, dacă nu ai date, interviu de discovery |
| competitor | Analiză competitivă cu tabel și hartă de poziționare 2x2 |
| funnel | Diagnostic de funnel plus checklist de structură landing page |
| campaign | Plan de campanie cu obiectiv, canale, KPI |
| decision | Framework de decizie: matrice de scor ponderat, pre-mortem |
| ops | Audit de procese și automatizări |
| pitch | Review și rescriere de pitch sau prezentare |
| meeting-prep | Pregătire ședință: agendă, decizii necesare, worst case |
| meeting-notes | Note brute transformate în acțiuni cu responsabili și deadline-uri |
| weekly | Retrospectivă săptămânală: ce a mers, ce nu, ce urmează |
| day | Ritual de dimineață: priorități, KPIs, focus |

## Cum învață

Fiecare modul are memorie persistentă în `~/.claude/skill-memory/biz-[modul].md`: reține corecțiile și preferințele tale și nu le repetă. Peste memoria per-modul stă un fișier comun, `business-context.md`, cu faptele durabile despre afacere (ce vinzi, cine e clientul, stadiul, obiectivul), citit de toate modulele înainte de propria memorie, ca să nu re-explici bazele la fiecare modul.

Memoria pornește goală pe calculatorul tău și se umple cu datele tale. Rămâne local, privat.

## Instalare (plugin skill, Claude Code)

```bash
mkdir -p ~/.claude/skills/biz-toolkit
cp strategie/biz-toolkit/skill.md ~/.claude/skills/biz-toolkit/SKILL.md
cp -R strategie/biz-toolkit/modules strategie/biz-toolkit/references strategie/biz-toolkit/templates ~/.claude/skills/biz-toolkit/
```

Apoi, într-o conversație nouă, scrie natural ce te frământă („ajută-mă cu prețul", „fă-mi un diagnostic de business") sau cere direct un modul. Skill-ul alege modulul potrivit și te ia cu întrebări pe rând.

## Compatibilitate

`claude-code-only`. Learning engine-ul și contextul comun scriu în `~/.claude/skill-memory/`, specific Claude Code. Pentru variante fără memorie, compatibile Codex, vezi comenzile `biz-*-portable` din bibliotecă (review, campaign, copy, customer).
