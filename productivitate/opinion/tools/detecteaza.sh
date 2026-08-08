#!/usr/bin/env bash
# Spune ce familii de modele sunt disponibile pe masina asta.
#
# Utilizare: detecteaza.sh
# Iesire: o linie per familie, in forma "nume|stare|greutate|citeste-fisiere"
#         stare = disponibil sau lipsa
#
# Skill-ul cheama asta la inceput, ca sa stie cu cine poate vorbi si ce sa-i spuna
# omului. Fara asta ar cere pareri de la unelte care nu exista si ar raporta erori
# in loc sa se adapteze.

set -uo pipefail

SKILL_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
ADAPTOARE="$SKILL_DIR/tools/adaptoare"

if [ ! -d "$ADAPTOARE" ]; then
  echo "EROARE: lipseste folderul de adaptoare: $ADAPTOARE" >&2
  exit 1
fi

gasit=0

for adaptor in "$ADAPTOARE"/*.sh; do
  [ -f "$adaptor" ] || continue
  familie="$(basename "$adaptor" .sh)"

  # Fiecare adaptor se incarca intr-un subshell, ca o eroare intr-unul
  # sa nu darame detectia celorlalte.
  (
    # shellcheck source=/dev/null
    . "$adaptor" 2>/dev/null || exit 1
    if adaptor_disponibil 2>/dev/null; then
      stare="disponibil"
    else
      stare="lipsa"
    fi
    printf '%s|%s|%s|%s|%s\n' \
      "$familie" "$stare" "${ADAPTOR_NUME:-$familie}" \
      "${ADAPTOR_GREUTATE:-necunoscuta}" "${ADAPTOR_CITESTE_FISIERE:-nu}"
  )
  gasit=$((gasit + 1))
done

if [ "$gasit" -eq 0 ]; then
  echo "EROARE: nu exista niciun adaptor in $ADAPTOARE" >&2
  exit 1
fi

exit 0
