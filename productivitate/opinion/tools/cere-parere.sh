#!/usr/bin/env bash
# Cere o opinie de la o familie de modele externa, prin adaptorul ei.
#
# Utilizare:
#   cere-parere.sh <familie> <folder-decizie> [folder-context]
#
# <familie> = numele unui adaptor din tools/adaptoare/ (fara .sh)
# <folder-decizie> trebuie sa contina deja briefing.md
#
# Scrie raspunsul in <folder-decizie>/opinie-<familie>.md
#
# Motorul face tot ce e comun: compune promptul, porneste adaptorul, tine
# cronometrul, verifica iesirea, raporteaza. Adaptorul stie doar sa cheme
# un CLI anume. Familie noua = un fisier de cincisprezece linii, nu un script nou.
#
# Cronometru: macOS nu are timeout/gtimeout, deci il facem in bash.
# Se schimba cu OPINION_TIMEOUT (secunde, implicit 600).
#
# Coduri de iesire:
#   0 = a mers
#   1 = familia nu e disponibila pe masina asta
#   2 = a depasit timpul
#   3 = CLI-ul a iesit cu eroare
#   4 = a raspuns dar fisierul de iesire e gol sau lipseste
#   5 = argumente gresite sau briefing lipsa
#   6 = nu exista adaptor cu numele cerut

set -uo pipefail

TIMEOUT_S="${OPINION_TIMEOUT:-600}"
SKILL_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
ADAPTOARE="$SKILL_DIR/tools/adaptoare"

if [ "$#" -lt 2 ]; then
  echo "EROARE: utilizare: cere-parere.sh <familie> <folder-decizie> [folder-context]" >&2
  exit 5
fi

FAMILIE="$1"
ADAPTOR="$ADAPTOARE/$FAMILIE.sh"

if [ ! -f "$ADAPTOR" ]; then
  echo "FARA-ADAPTOR: nu exista $ADAPTOR. Familii cunoscute: $(ls "$ADAPTOARE" 2>/dev/null | sed 's/\.sh$//' | tr '\n' ' ')" >&2
  exit 6
fi

DECISION_DIR="$(cd "$2" 2>/dev/null && pwd)" || {
  echo "EROARE: folderul deciziei nu exista: $2" >&2
  exit 5
}
CONTEXT_DIR="${3:-$DECISION_DIR}"
BRIEFING="$DECISION_DIR/briefing.md"
FORMAT="$SKILL_DIR/prompts/format-opinie.md"
OUT="$DECISION_DIR/opinie-$FAMILIE.md"
PROMPT="$DECISION_DIR/.prompt-$FAMILIE.md"
LOG="$DECISION_DIR/.log-$FAMILIE.txt"

[ -f "$BRIEFING" ] || { echo "EROARE: lipseste $BRIEFING" >&2; exit 5; }
[ -f "$FORMAT" ]   || { echo "EROARE: lipseste $FORMAT" >&2; exit 5; }

# Adaptorul declara: ADAPTOR_NUME, ADAPTOR_GREUTATE, ADAPTOR_CITESTE_FISIERE,
# plus functiile adaptor_disponibil() si adaptor_ruleaza().
# shellcheck source=/dev/null
. "$ADAPTOR"

if ! adaptor_disponibil; then
  echo "INDISPONIBIL: $ADAPTOR_NUME nu e disponibil pe masina asta" >&2
  exit 1
fi

# Promptul: contractul de format, briefingul, apoi calea de context.
# Adaptoarele care nu pot deschide fisiere (modele locale simple) nu primesc
# invitatia de a citi, ca sa nu inventeze ca au citit.
{
  cat "$FORMAT"
  printf '\n\n---\n\n# Briefingul deciziei\n\n'
  cat "$BRIEFING"
  if [ "${ADAPTOR_CITESTE_FISIERE:-nu}" = "da" ]; then
    printf '\n\n---\n\nFolderul de context, pentru citire, cale absoluta: %s\n' "$CONTEXT_DIR"
    printf 'Deschide de acolo ce ai nevoie. Ai voie sa citesti orice fisier prin cale absoluta.\n'
  else
    printf '\n\n---\n\nNu ai acces la fisiere. Formeaza-ti opinia doar din briefingul de mai sus\n'
    printf 'si scrie exact asta la sectiunea "Ce am citit".\n'
  fi
} > "$PROMPT"

# Rulam din folderul deciziei, nu din folderul de context. Motivul: unele unelte
# lasa fisiere in directorul curent (de exemplu un AGENTS.md de context), iar
# acelea nu au ce cauta in folderele de lucru ale omului. Adaptoarele care pot
# citi fisiere primesc calea absoluta in prompt, deci nu pierd nimic.
cd "$DECISION_DIR"

adaptor_ruleaza "$PROMPT" "$OUT" >"$LOG" 2>&1 &
pid=$!

# Fisier-martor pentru cronometru. Unele CLI-uri prind SIGTERM si ies cu 0,
# deci codul de iesire singur nu spune daca au fost oprite fortat.
MARTOR="$DECISION_DIR/.timeout-$FAMILIE"
rm -f "$MARTOR"

(
  sleep "$TIMEOUT_S"
  touch "$MARTOR"
  kill -TERM "$pid" 2>/dev/null
  sleep 5
  kill -KILL "$pid" 2>/dev/null
) &
watcher=$!

wait "$pid"
status=$?

kill -TERM "$watcher" 2>/dev/null
wait "$watcher" 2>/dev/null

rm -f "$PROMPT"

if [ -f "$MARTOR" ]; then
  rm -f "$MARTOR"
  echo "TIMEOUT: $ADAPTOR_NUME a depasit ${TIMEOUT_S}s, oprit fara raspuns" >&2
  exit 2
fi

# Plasa de siguranta: daca moare de la semnal, bash raporteaza 143.
if [ "$status" -eq 143 ]; then
  echo "TIMEOUT: $ADAPTOR_NUME oprit de semnal dupa ${TIMEOUT_S}s" >&2
  exit 2
fi

if [ "$status" -ne 0 ]; then
  echo "EROARE-CLI: $ADAPTOR_NUME a iesit cu codul $status. Detalii in $LOG" >&2
  exit 3
fi

if [ ! -s "$OUT" ]; then
  echo "IESIRE-GOALA: $ADAPTOR_NUME a terminat cu bine dar $OUT e gol sau lipseste" >&2
  exit 4
fi

# Semnatura, ca judecatorul sa stie cine a vorbit si cat cantareste vocea.
{
  printf '\n\n---\n'
  printf 'Sursa: %s. Greutate: %s. Acces la fisiere: %s.\n' \
    "$ADAPTOR_NUME" "$ADAPTOR_GREUTATE" "${ADAPTOR_CITESTE_FISIERE:-nu}"
} >> "$OUT"

echo "OK: $ADAPTOR_NUME a scris in $OUT ($(wc -c <"$OUT" | tr -d ' ') octeti)"
exit 0
