# Adaptor: GPT prin Codex CLI
# Verificat pe 2026-08-07 cu codex-cli 0.147.0, model gpt-5.6-sol, circa 40s per opinie.

ADAPTOR_NUME="GPT prin Codex"
ADAPTOR_GREUTATE="frontiera"
ADAPTOR_CITESTE_FISIERE="da"

adaptor_disponibil() {
  command -v codex >/dev/null 2>&1
}

adaptor_ruleaza() {
  prompt_file="$1"
  out_file="$2"
  # -s read-only interzice scrierea de catre model. -o e scris de procesul CLI,
  # nu de model, deci nu cade sub interdictie. --skip-git-repo-check e necesar
  # fiindca folderul deciziei nu e repo git.
  # Modelul se ia din ~/.codex/config.toml. OPINION_MODEL il forteaza, util cand
  # config.toml ajunge pe un model mai nou decat CLI-ul instalat (semn: eroare 400
  # cu "requires a newer version of Codex"; reparatie: npm install -g @openai/codex@latest).
  if [ -n "${OPINION_MODEL:-}" ]; then
    codex exec -s read-only --skip-git-repo-check -m "$OPINION_MODEL" -o "$out_file" - < "$prompt_file"
  else
    codex exec -s read-only --skip-git-repo-check -o "$out_file" - < "$prompt_file"
  fi
}
