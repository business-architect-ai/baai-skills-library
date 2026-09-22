#!/usr/bin/env bash
#
# ia-secret.sh — citeste o singura valoare din Infisical si o scrie la stdout.
#
# Folosire:
#   ./ia-secret.sh NUME_SECRET
#
# Configurare prin variabile de mediu:
#   INFISICAL_PROJECT_ID    (obligatoriu) ID-ul proiectului din Project Settings
#   INFISICAL_TOKEN         token de acces, daca il ai deja
#   INFISICAL_CLIENT_ID     alternativa: Machine Identity (Universal Auth)
#   INFISICAL_CLIENT_SECRET alternativa: Machine Identity (Universal Auth)
#   INFISICAL_ENV           mediul, implicit "dev"
#   INFISICAL_SECRET_PATH   calea in proiect, implicit "/"
#   INFISICAL_API_URL       implicit https://app.infisical.com
#                           UE: https://eu.infisical.com, sau instanta self-hosted
#
# Dai fie INFISICAL_TOKEN, fie perechea CLIENT_ID + CLIENT_SECRET.
# A doua varianta e de preferat: scriptul schimba credentialele pe un token
# de scurta durata la fiecare rulare.
#
# Nici tokenul, nici secretul nu apar in linia de comanda, deci nu sunt
# vizibile altor utilizatori prin `ps`. Optiunile sensibile intra in curl
# prin stdin, cu `-K -`.

set -euo pipefail

NUME_SCRIPT=$(basename "$0")

moare() {
    echo "${NUME_SCRIPT}: $1" >&2
    exit "${2:-1}"
}

if [ $# -lt 1 ] || [ -z "${1:-}" ]; then
    moare "lipseste numele secretului. Folosire: ${NUME_SCRIPT} NUME_SECRET" 2
fi

NUME_SECRET="$1"

command -v curl >/dev/null 2>&1 || moare "curl nu e instalat."

API_URL="${INFISICAL_API_URL:-https://app.infisical.com}"
API_URL="${API_URL%/}"
MEDIU="${INFISICAL_ENV:-dev}"
CALE="${INFISICAL_SECRET_PATH:-/}"
PROIECT="${INFISICAL_PROJECT_ID:-}"

[ -n "$PROIECT" ] || moare "INFISICAL_PROJECT_ID nu e setat. Il gasesti in Infisical, la Project Settings."

# ---------------------------------------------------------------------------
# Extrage o cheie de nivel 1 dintr-un JSON. Prefera un parser real; cade
# pe sed doar daca nu gaseste nimic mai bun.
# ---------------------------------------------------------------------------
citeste_json() {
    local cheie="$1" text="$2"

    if command -v python3 >/dev/null 2>&1; then
        CHEIE_CAUTATA="$cheie" python3 -c '
import json, os, sys
cheie = os.environ["CHEIE_CAUTATA"]
try:
    date = json.load(sys.stdin)
except ValueError:
    sys.exit(1)

def cauta(nod):
    if isinstance(nod, dict):
        if cheie in nod:
            return nod[cheie]
        for valoare in nod.values():
            gasit = cauta(valoare)
            if gasit is not None:
                return gasit
    return None

rezultat = cauta(date)
if rezultat is None:
    sys.exit(1)
sys.stdout.write(str(rezultat))
' <<< "$text" && return 0
        return 1
    fi

    if command -v jq >/dev/null 2>&1; then
        local rezultat
        rezultat=$(printf '%s' "$text" | jq -re ".. | objects | select(has(\"${cheie}\")) | .${cheie}" 2>/dev/null | head -n 1) || return 1
        [ -n "$rezultat" ] || return 1
        printf '%s' "$rezultat"
        return 0
    fi

    # Ultima varianta: potrivire pe text. Merge pe valori fara ghilimele
    # escapate, ceea ce acopera cheile API obisnuite.
    local rezultat
    rezultat=$(printf '%s' "$text" | sed -n "s/.*\"${cheie}\"[[:space:]]*:[[:space:]]*\"\([^\"]*\)\".*/\1/p" | head -n 1)
    [ -n "$rezultat" ] || return 1
    printf '%s' "$rezultat"
}

# ---------------------------------------------------------------------------
# Face o cerere HTTP si separa corpul de codul de status.
# Optiunile sensibile vin pe stdin, nu prin argv.
# Scrie in variabilele globale CORP si COD.
# ---------------------------------------------------------------------------
cerere() {
    local url="$1" config="$2"
    shift 2

    local raspuns
    set +e
    raspuns=$(printf '%s' "$config" | curl -sS -K - -w $'\n%{http_code}' "$@" "$url" 2>&1)
    local iesire=$?
    set -e

    if [ $iesire -ne 0 ]; then
        moare "nu am putut contacta ${API_URL} (curl a iesit cu ${iesire}). Verifica reteaua sau INFISICAL_API_URL."
    fi

    # Codul de status e ultima linie. Taiat cu expansiune bash, nu cu
    # `head -n -1`, care nu exista pe macOS si BSD.
    COD="${raspuns##*$'\n'}"
    CORP="${raspuns%$'\n'*}"
    # Cand corpul e gol, raspunsul e doar codul, iar cele doua taieri dau
    # acelasi text. `if`, nu `&&`, ca functia sa nu intoarca 1 sub `set -e`.
    if [ "$CORP" = "$COD" ]; then
        CORP=""
    fi
    return 0
}

# ---------------------------------------------------------------------------
# Autentificare
# ---------------------------------------------------------------------------
TOKEN="${INFISICAL_TOKEN:-}"

if [ -z "$TOKEN" ]; then
    CLIENT_ID="${INFISICAL_CLIENT_ID:-}"
    CLIENT_SECRET="${INFISICAL_CLIENT_SECRET:-}"

    if [ -z "$CLIENT_ID" ] || [ -z "$CLIENT_SECRET" ]; then
        moare "nu am credentiale. Seteaza INFISICAL_TOKEN, sau perechea INFISICAL_CLIENT_ID si INFISICAL_CLIENT_SECRET."
    fi

    CONFIG_LOGIN=$(printf 'data-urlencode = "clientId=%s"\ndata-urlencode = "clientSecret=%s"\n' \
        "$CLIENT_ID" "$CLIENT_SECRET")

    cerere "${API_URL}/api/v1/auth/universal-auth/login" "$CONFIG_LOGIN" -X POST

    case "$COD" in
        200) ;;
        401) moare "credentiale respinse de Infisical. Verifica INFISICAL_CLIENT_ID si INFISICAL_CLIENT_SECRET." ;;
        *)   moare "login esuat (HTTP ${COD}): $(printf '%s' "$CORP" | head -c 200)" ;;
    esac

    TOKEN=$(citeste_json accessToken "$CORP") || moare "login a reusit, dar raspunsul nu contine accessToken."
    unset CLIENT_SECRET CONFIG_LOGIN
fi

# ---------------------------------------------------------------------------
# Citirea secretului
# ---------------------------------------------------------------------------
CONFIG_CITIRE=$(printf 'header = "Authorization: Bearer %s"\n' "$TOKEN")

cerere "${API_URL}/api/v3/secrets/raw/${NUME_SECRET}" "$CONFIG_CITIRE" \
    --get \
    --data-urlencode "workspaceId=${PROIECT}" \
    --data-urlencode "environment=${MEDIU}" \
    --data-urlencode "secretPath=${CALE}" \
    --data-urlencode "viewSecretValue=true"

unset TOKEN CONFIG_CITIRE

case "$COD" in
    200)
        ;;
    401)
        moare "token lipsa sau expirat (HTTP 401)."
        ;;
    403)
        moare "acces refuzat (HTTP 403). Tokenul e malformat, ori identitatea nu are drept de citire pe '${NUME_SECRET}' in mediul '${MEDIU}'."
        ;;
    404)
        # Infisical raspunde 404 si cand secretul lipseste, si cand tokenul
        # nu exista. Mesajul din corp face diferenta, codul singur nu.
        if printf '%s' "$CORP" | grep -qi "service token"; then
            moare "tokenul nu a fost gasit in Infisical (HTTP 404). A fost revocat sau e gresit."
        fi
        moare "secretul '${NUME_SECRET}' nu exista in mediul '${MEDIU}', pe calea '${CALE}' (HTTP 404). Numele e sensibil la majuscule."
        ;;
    *)
        moare "cerere esuata (HTTP ${COD}): $(printf '%s' "$CORP" | head -c 200)"
        ;;
esac

VALOARE=$(citeste_json secretValue "$CORP") || \
    moare "raspunsul nu contine o valoare. Identitatea poate citi metadata secretului, dar nu si valoarea lui."

[ -n "$VALOARE" ] || moare "secretul '${NUME_SECRET}' exista, dar are valoare goala."

printf '%s\n' "$VALOARE"
