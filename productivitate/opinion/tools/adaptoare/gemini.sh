# Adaptor: Gemini prin Gemini CLI
#
# NEVERIFICAT. Scris pe 2026-08-07 pe baza interfetei documentate, dar Gemini CLI
# nu era instalat pe masina pe care s-a construit skill-ul, deci nimeni nu l-a
# rulat inca. Trateaza-l ca pe o schita pana il testezi tu.
#
# Ce trebuie verificat la prima rulare, in ordinea asta:
#   1. Ca `gemini -p "text"` chiar raspunde non-interactiv si scrie la iesirea standard.
#      Daca versiunea ta cere alt flag, schimba doar linia din adaptor_ruleaza.
#   2. Ca nu cere aprobare pentru nimic. Daca se blocheaza asteptand o confirmare,
#      cauta in `gemini --help` modul non-interactiv si adauga flagul aici.
#   3. Daca poate citi fisiere de pe disc. Daca nu poate, schimba
#      ADAPTOR_CITESTE_FISIERE in "nu", altfel va pretinde ca a citit.
#
# Dupa ce l-ai verificat, sterge acest antet si scrie in loc data si versiunea testata.

ADAPTOR_NUME="Gemini prin Gemini CLI (neverificat)"
ADAPTOR_GREUTATE="frontiera"
ADAPTOR_CITESTE_FISIERE="da"

adaptor_disponibil() {
  command -v gemini >/dev/null 2>&1
}

adaptor_ruleaza() {
  prompt_file="$1"
  out_file="$2"
  if [ -n "${OPINION_MODEL_GEMINI:-}" ]; then
    gemini -m "$OPINION_MODEL_GEMINI" -p "$(cat "$prompt_file")" > "$out_file"
  else
    gemini -p "$(cat "$prompt_file")" > "$out_file"
  fi
}
