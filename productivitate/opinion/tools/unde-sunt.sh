#!/usr/bin/env bash
# Spune unde e instalat skill-ul si unde isi scrie rezultatele.
#
# Utilizare: unde-sunt.sh
# Iesire, doua linii:
#   SKILL=<calea absoluta a folderului skill-ului>
#   REZULTATE=<calea absoluta unde se scriu deciziile>
#
# Exista ca sa nu fie nicio cale fixa in SKILL.md. Acelasi pachet merge si in
# ~/.claude/skills/opinion (Claude Code personal), si in folderul .claude/skills
# al unui agent din flota, fara sa se modifice nimic.
#
# Unde ajung rezultatele:
#   1. in $OPINION_HOME, daca variabila e setata
#   2. daca skill-ul e sub .claude/skills/ intr-un folder de agent, adica oriunde
#      altundeva decat direct in casa utilizatorului, atunci in <folder-agent>/opinions
#   3. altfel, in ~/.claude/opinions

set -uo pipefail

SKILL_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

# Radacina peste .claude/skills/<nume>: urcam trei niveluri.
# .../X/.claude/skills/opinion  ->  .../X
POSIBIL_AGENT="$(cd "$SKILL_DIR/../../.." 2>/dev/null && pwd)" || POSIBIL_AGENT=""

if [ -n "${OPINION_HOME:-}" ]; then
  REZULTATE="$OPINION_HOME"
elif [ -n "$POSIBIL_AGENT" ] && [ "$POSIBIL_AGENT" != "$HOME" ] \
     && [ "$(basename "$(dirname "$(dirname "$SKILL_DIR")")")" = ".claude" ]; then
  REZULTATE="$POSIBIL_AGENT/opinions"
else
  REZULTATE="$HOME/.claude/opinions"
fi

printf 'SKILL=%s\n' "$SKILL_DIR"
printf 'REZULTATE=%s\n' "$REZULTATE"
