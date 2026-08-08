# Adaptor: model local prin Ollama
# Verificat pe 2026-08-07 cu llama3.1:latest.
#
# Foloseste API-ul local (http://localhost:11434), nu comanda `ollama run`.
# Motivul, gasit la testare: `ollama run` scrie coduri de control de terminal in
# iesire si redeseneaza liniile pe masura ce genereaza, deci fisierul rezultat
# contine gunoi de tipul ESC[13D si fragmente de text duplicate. API-ul cu
# stream=false intoarce text curat.
#
# Atentie la greutate: un model local mic nu e o voce egala cu una de frontiera.
# E acolo pentru cine nu vrea sau nu poate trimite contextul in cloud. Judecatorul
# vede greutatea in semnatura opiniei si o cantareste corespunzator.
#
# Ollama ruleaza un model, nu un agent: nu poate deschide fisiere. Opinia lui se
# formeaza doar din briefing, de aceea ADAPTOR_CITESTE_FISIERE e "nu".

ADAPTOR_NUME="model local prin Ollama"
ADAPTOR_GREUTATE="slaba"
ADAPTOR_CITESTE_FISIERE="nu"

adaptor_disponibil() {
  command -v ollama >/dev/null 2>&1 || return 1
  command -v python3 >/dev/null 2>&1 || return 1
  curl -s -m 3 http://localhost:11434/api/tags >/dev/null 2>&1
}

adaptor_ruleaza() {
  prompt_file="$1"
  out_file="$2"

  # OPINION_MODEL_LOCAL alege modelul. Implicit, primul din lista instalata.
  model="${OPINION_MODEL_LOCAL:-}"
  if [ -z "$model" ]; then
    model="$(ollama list 2>/dev/null | awk 'NR==2 {print $1}')"
  fi
  if [ -z "$model" ]; then
    echo "Ollama nu are niciun model instalat. Ruleaza: ollama pull llama3.1" >&2
    return 1
  fi

  OLLAMA_MODEL="$model" OLLAMA_PROMPT_FILE="$prompt_file" OLLAMA_OUT_FILE="$out_file" \
  python3 -c '
import json, os, sys, urllib.request

model = os.environ["OLLAMA_MODEL"]
with open(os.environ["OLLAMA_PROMPT_FILE"], encoding="utf-8") as f:
    prompt = f.read()

req = urllib.request.Request(
    "http://localhost:11434/api/generate",
    data=json.dumps({"model": model, "prompt": prompt, "stream": False}).encode("utf-8"),
    headers={"Content-Type": "application/json"},
)
try:
    raspuns = json.loads(urllib.request.urlopen(req, timeout=3600).read())
except Exception as e:
    print("Ollama API a esuat: %s" % e, file=sys.stderr)
    sys.exit(1)

text = raspuns.get("response", "").strip()
if not text:
    print("Ollama a raspuns gol", file=sys.stderr)
    sys.exit(1)

with open(os.environ["OLLAMA_OUT_FILE"], "w", encoding="utf-8") as f:
    f.write(text + "\n")
'
}
