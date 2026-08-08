#!/usr/bin/env bash
# Verifica daca skill-ul opinion e instalat corect si chiar functioneaza pe masina asta.
#
# Utilizare:
#   ~/.claude/skills/opinion/tools/autotest.sh
#
# Ruleaza-l o data, imediat dupa instalare. Iti spune in cuvinte simple daca poti
# folosi skill-ul, cu ce voci, si ce lipseste daca lipseste ceva.
#
# Iesire: 0 daca skill-ul e utilizabil, 1 daca nu.
#
# Optiuni prin variabile de mediu:
#   AUTOTEST_FARA_PROBA=1   sare peste proba reala (nu cheama niciun model)

set -uo pipefail

SKILL_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
probleme=0
avertismente=0

linie() { printf '%s\n' "------------------------------------------------------------"; }
ok()    { printf '  [ok]      %s\n' "$1"; }
lipsa() { printf '  [lipsa]   %s\n' "$1"; probleme=$((probleme + 1)); }
atent() { printf '  [atentie] %s\n' "$1"; avertismente=$((avertismente + 1)); }

echo
echo "Autotest pentru skill-ul opinion"
echo "Instalat in: $SKILL_DIR"
linie

# ---------------------------------------------------------------- 1. fisiere
echo "1. Fisierele skill-ului"
for f in SKILL.md prompts/format-opinie.md prompts/prompt-fuziune.md \
         tools/cere-parere.sh tools/detecteaza.sh; do
  if [ -f "$SKILL_DIR/$f" ]; then
    ok "$f"
  else
    lipsa "$f lipseste. Copiaza din nou folderul, a ramas incomplet."
  fi
done

if [ -d "$SKILL_DIR/tools/adaptoare" ]; then
  nr="$(ls -1 "$SKILL_DIR/tools/adaptoare"/*.sh 2>/dev/null | wc -l | tr -d ' ')"
  if [ "$nr" -gt 0 ]; then
    ok "tools/adaptoare ($nr familii)"
  else
    lipsa "tools/adaptoare e gol. Fara adaptoare nu exista a doua voce."
  fi
else
  lipsa "tools/adaptoare lipseste cu totul."
fi

for s in cere-parere.sh detecteaza.sh; do
  if [ -x "$SKILL_DIR/tools/$s" ]; then
    ok "$s are drept de executie"
  elif [ -f "$SKILL_DIR/tools/$s" ]; then
    atent "$s nu are drept de executie. Repara cu: chmod +x $SKILL_DIR/tools/*.sh"
  fi
done

# --------------------------------------------------------------- 2. locatie
linie
echo "2. Locul instalarii"
if [ "$SKILL_DIR" = "$HOME/.claude/skills/opinion" ]; then
  ok "e in ~/.claude/skills/opinion, unde il cauta Claude Code"
else
  atent "nu e in ~/.claude/skills/opinion. Claude Code s-ar putea sa nu-l gaseasca."
  atent "instrucțiunile din SKILL.md folosesc calea ~/.claude/skills/opinion/"
fi

# ---------------------------------------------------------------- 3. familii
linie
echo "3. Cu cine poate vorbi pe masina asta"
disponibile=""
if [ -x "$SKILL_DIR/tools/detecteaza.sh" ] || [ -f "$SKILL_DIR/tools/detecteaza.sh" ]; then
  while IFS='|' read -r familie stare nume greutate citeste; do
    [ -n "${familie:-}" ] || continue
    if [ "$stare" = "disponibil" ]; then
      ok "$nume (familie: $familie, greutate: $greutate, citeste fisiere: $citeste)"
      disponibile="$disponibile $familie"
    else
      printf '  [-]       %s nu e instalat\n' "$nume"
    fi
  done < <(bash "$SKILL_DIR/tools/detecteaza.sh" 2>/dev/null)
fi

if [ -z "$disponibile" ]; then
  atent "nicio familie externa disponibila."
  atent "skill-ul va merge, dar ambele voci vor fi Claude, deci diversitatea e mica."
  atent "ca sa ai o a doua familie adevarata, instaleaza una: Codex, Gemini sau Ollama."
fi

# ------------------------------------------------------------------- 4. proba
linie
echo "4. Proba reala"
if [ "${AUTOTEST_FARA_PROBA:-0}" = "1" ]; then
  echo "  sarita (AUTOTEST_FARA_PROBA=1)"
elif [ -z "$disponibile" ]; then
  echo "  sarita, nu exista familie externa de probat"
else
  familie="$(echo "$disponibile" | awk '{print $1}')"
  echo "  Cer o parere scurta de la: $familie. Poate dura un minut."
  proba="$(mktemp -d)"
  cat > "$proba/briefing.md" <<'BRIEF'
# Proba de instalare

## Întrebarea
Pentru o listă de cumpărături, e mai bine pe hârtie sau în telefon?

## Opțiunile pe care le vede
A. Pe hârtie.
B. În telefon.

## Context și constrângeri
Aceasta este o probă tehnică de instalare. Răspunde scurt, dar respectă structura cerută.

## Folderul de context
Nu există.
BRIEF

  if OPINION_TIMEOUT="${AUTOTEST_TIMEOUT:-300}" \
     bash "$SKILL_DIR/tools/cere-parere.sh" "$familie" "$proba" "$proba" >/dev/null 2>&1; then
    raspuns="$proba/opinie-$familie.md"
    titluri="$(grep -c '^## ' "$raspuns" 2>/dev/null || echo 0)"
    if [ "$titluri" -ge 4 ]; then
      ok "a raspuns si a respectat structura ($titluri sectiuni din 6)"
    else
      atent "a raspuns, dar structura e incompleta ($titluri sectiuni din 6)."
      atent "se intampla la modele mici. Judecatorul o va marca la fuziune."
    fi
  else
    cod=$?
    case "$cod" in
      1) lipsa "familia $familie s-a raportat indisponibila in timpul probei" ;;
      2) lipsa "familia $familie nu a raspuns in timpul alocat" ;;
      3) lipsa "unealta pentru $familie a iesit cu eroare. Vezi $proba/.log-$familie.txt" ;;
      4) lipsa "unealta pentru $familie a terminat, dar nu a scris nimic" ;;
      *) lipsa "proba a esuat cu codul $cod" ;;
    esac
    echo "  Fisierele probei au ramas in: $proba"
    proba=""
  fi
  [ -n "$proba" ] && rm -rf "$proba"
fi

# ------------------------------------------------------------------ verdict
linie
echo
plural() { # plural <numar> <singular> <plural>
  if [ "$1" -eq 1 ]; then printf '%s %s' "$1" "$2"; else printf '%s %s' "$1" "$3"; fi
}

if [ "$probleme" -gt 0 ]; then
  echo "VERDICT: nu e gata. $(plural "$probleme" "lucru de reparat" "lucruri de reparat"), vezi liniile [lipsa] de mai sus."
  echo "Daca nu iti dai seama ce sa faci, trimite tot textul asta celui de la care ai luat skill-ul."
  echo
  exit 1
fi

if [ "$avertismente" -gt 0 ]; then
  echo "VERDICT: merge, cu rezerve. $(plural "$avertismente" "lucru de stiut" "lucruri de stiut"), vezi liniile [atentie]."
  echo "Poti folosi skill-ul asa cum e. Scrie /opinion urmat de intrebarea ta."
  echo
  exit 0
fi

echo "VERDICT: gata de folosit."
echo "Scrie /opinion urmat de intrebarea ta, in sesiunea in care lucrezi la decizie."
echo
exit 0
