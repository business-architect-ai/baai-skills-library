"""Citeste secrete din Infisical, la momentul folosirii lor.

Fara dependinte externe, doar biblioteca standard.

    from ia_secret import ia_secret

    cheie = ia_secret("STRIPE_SECRET_KEY")

Configurarea vine din mediu (vezi README). Poti trece explicit orice
parametru, daca ai nevoie de mai multe proiecte in acelasi proces.
"""

from __future__ import annotations

import json
import os
import urllib.error
import urllib.parse
import urllib.request

__all__ = ["ia_secret", "EroareInfisical"]

_API_IMPLICIT = "https://app.infisical.com"
_TIMEOUT = 15


class EroareInfisical(RuntimeError):
    """Infisical nu a putut livra secretul cerut."""


def _cere(url: str, *, date: bytes | None = None, token: str | None = None) -> dict:
    cerere = urllib.request.Request(url, data=date, method="POST" if date else "GET")
    if token:
        cerere.add_header("Authorization", f"Bearer {token}")
    if date:
        cerere.add_header("Content-Type", "application/x-www-form-urlencoded")

    try:
        with urllib.request.urlopen(cerere, timeout=_TIMEOUT) as raspuns:
            return json.loads(raspuns.read().decode("utf-8"))
    except urllib.error.HTTPError as eroare:
        corp = eroare.read().decode("utf-8", "replace")
        mesaj = corp
        try:
            mesaj = json.loads(corp).get("message", corp)
        except ValueError:
            pass
        mesaj = mesaj.strip().rstrip(".")
        raise _traduce_eroare(eroare.code, mesaj) from None
    except urllib.error.URLError as eroare:
        raise EroareInfisical(
            f"nu am putut contacta Infisical: {eroare.reason}. "
            "Verifica reteaua sau INFISICAL_API_URL."
        ) from None


def _traduce_eroare(cod: int, mesaj: str) -> EroareInfisical:
    if cod == 401:
        return EroareInfisical(f"credentiale lipsa sau respinse (HTTP 401): {mesaj}")
    if cod == 403:
        return EroareInfisical(
            f"acces refuzat (HTTP 403): {mesaj}. Tokenul e malformat, "
            "ori identitatea nu are drept de citire aici."
        )
    if cod == 404:
        # Infisical raspunde 404 si cand secretul lipseste, si cand tokenul
        # nu exista. Codul singur nu face diferenta, mesajul da.
        if "service token" in mesaj.lower():
            return EroareInfisical(
                f"tokenul nu a fost gasit in Infisical (HTTP 404): {mesaj}. "
                "A fost revocat sau e gresit."
            )
        return EroareInfisical(
            f"secretul nu exista (HTTP 404): {mesaj}. "
            "Numele e sensibil la majuscule."
        )
    return EroareInfisical(f"cerere esuata (HTTP {cod}): {mesaj}")


def _obtine_token(api_url: str, client_id: str, client_secret: str) -> str:
    date = urllib.parse.urlencode(
        {"clientId": client_id, "clientSecret": client_secret}
    ).encode("utf-8")

    raspuns = _cere(f"{api_url}/api/v1/auth/universal-auth/login", date=date)
    token = raspuns.get("accessToken")
    if not token:
        raise EroareInfisical("login a reusit, dar raspunsul nu contine accessToken.")
    return token


def ia_secret(
    nume: str,
    *,
    project_id: str | None = None,
    environment: str | None = None,
    secret_path: str | None = None,
    api_url: str | None = None,
    token: str | None = None,
) -> str:
    """Intoarce valoarea unui secret. Ridica EroareInfisical daca nu reuseste.

    Nu pastra valoarea intoarsa mai mult decat apelul care o foloseste, si
    nu o scrie in loguri, in memorie sau in raspunsul agentului.
    """
    if not nume:
        raise EroareInfisical("numele secretului lipseste.")

    api_url = (api_url or os.environ.get("INFISICAL_API_URL") or _API_IMPLICIT).rstrip("/")
    project_id = project_id or os.environ.get("INFISICAL_PROJECT_ID", "")
    environment = environment or os.environ.get("INFISICAL_ENV") or "dev"
    secret_path = secret_path or os.environ.get("INFISICAL_SECRET_PATH") or "/"

    if not project_id:
        raise EroareInfisical(
            "INFISICAL_PROJECT_ID nu e setat. Il gasesti la Project Settings."
        )

    token = token or os.environ.get("INFISICAL_TOKEN", "")
    if not token:
        client_id = os.environ.get("INFISICAL_CLIENT_ID", "")
        client_secret = os.environ.get("INFISICAL_CLIENT_SECRET", "")
        if not client_id or not client_secret:
            raise EroareInfisical(
                "nu am credentiale. Seteaza INFISICAL_TOKEN, sau perechea "
                "INFISICAL_CLIENT_ID si INFISICAL_CLIENT_SECRET."
            )
        token = _obtine_token(api_url, client_id, client_secret)

    interogare = urllib.parse.urlencode(
        {
            "workspaceId": project_id,
            "environment": environment,
            "secretPath": secret_path,
            "viewSecretValue": "true",
        }
    )
    url = (
        f"{api_url}/api/v3/secrets/raw/"
        f"{urllib.parse.quote(nume, safe='')}?{interogare}"
    )

    raspuns = _cere(url, token=token)
    valoare = (raspuns.get("secret") or {}).get("secretValue")

    if valoare is None:
        raise EroareInfisical(
            f"raspunsul pentru '{nume}' nu contine o valoare. Identitatea poate "
            "citi metadata secretului, dar nu si valoarea lui."
        )
    if valoare == "":
        raise EroareInfisical(f"secretul '{nume}' exista, dar are valoare goala.")

    return valoare


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Folosire: python3 ia_secret.py NUME_SECRET", file=sys.stderr)
        sys.exit(2)
    try:
        print(ia_secret(sys.argv[1]))
    except EroareInfisical as eroare:
        print(f"ia_secret: {eroare}", file=sys.stderr)
        sys.exit(1)
