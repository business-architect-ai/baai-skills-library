#!/usr/bin/env python3
"""Calculează scorul SUS (System Usability Scale) pentru un panel de persona.

Intrare: un fișier JSON cu o listă de obiecte, sau un obiect pe linie:
    {"persona": "Ana", "sus": [4, 2, 4, 1, 4, 2, 5, 2, 4, 1]}

Repetări: aceeași persona poate apărea de mai multe ori, câte o linie pe
rulare. Scriptul grupează rulările după numele persona și arată cât de stabil
e scorul fiecăreia. Media panelului se face pe mediile persona, ca fiecare
persona să conteze la fel, indiferent de câte ori a rulat.

Formula (Brooke, 1986):
    afirmațiile impare (1, 3, 5, 7, 9): răspuns - 1
    afirmațiile pare (2, 4, 6, 8, 10):  5 - răspuns
    suma × 2,5 → scor de la 0 la 100

Nota pe litere: scala curbată Sauro-Lewis (2016), unde 68 e media.

Folosire:
    python3 sus_scor.py raspunsuri.json
"""

import json
import statistics
import sys

# (prag minim, notă), de sus în jos
SCALA_NOTE = [
    (84.1, "A+"), (80.8, "A"), (78.9, "A-"),
    (77.2, "B+"), (74.1, "B"), (72.6, "B-"),
    (71.1, "C+"), (65.0, "C"), (62.7, "C-"),
    (51.7, "D"), (0.0, "F"),
]

# Peste atâtea puncte între rulările aceleiași persona, scorul ei e instabil.
PRAG_INSTABIL = 15.0


def nota(scor):
    for prag, litera in SCALA_NOTE:
        if scor >= prag:
            return litera
    return "F"


def scor_sus(raspunsuri):
    total = 0
    for i, r in enumerate(raspunsuri, start=1):
        total += (r - 1) if i % 2 == 1 else (5 - r)
    return total * 2.5


def valideaza(intrare, pozitie):
    """Întoarce (persona, răspunsuri, avertismente) sau ridică ValueError."""
    if not isinstance(intrare, dict):
        raise ValueError(f"intrarea {pozitie} nu e un obiect JSON")
    persona = intrare.get("persona") or f"persona {pozitie}"
    sus = intrare.get("sus")
    if not isinstance(sus, list) or len(sus) != 10:
        raise ValueError(f"{persona}: trebuie exact 10 răspunsuri, am primit {sus!r}")
    for i, r in enumerate(sus, start=1):
        if isinstance(r, bool) or not isinstance(r, int) or not 1 <= r <= 5:
            raise ValueError(f"{persona}: afirmația {i} are valoarea {r!r}, trebuie un întreg între 1 și 5")
    avertismente = []
    if len(set(sus)) == 1:
        avertismente.append(
            f"{persona}: același răspuns ({sus[0]}) la toate afirmațiile. "
            "Afirmațiile alternează pozitiv/negativ, deci răspunsul e probabil bifat mecanic."
        )
    return persona, sus, avertismente


def citeste(cale):
    with open(cale, encoding="utf-8") as f:
        continut = f.read().strip()
    if not continut:
        raise ValueError("fișierul e gol")
    if continut.startswith("["):
        return json.loads(continut)
    return [json.loads(linie) for linie in continut.splitlines() if linie.strip()]


def fmt(x):
    return f"{x:.1f}"


def main():
    if len(sys.argv) != 2:
        print(__doc__.strip())
        return 2
    try:
        intrari = citeste(sys.argv[1])
    except (OSError, ValueError) as e:
        print(f"Eroare la citire: {e}", file=sys.stderr)
        return 1

    pe_persona = {}  # nume -> listă de scoruri, în ordinea rulărilor
    avertismente, erori = [], []
    for poz, intrare in enumerate(intrari, start=1):
        try:
            persona, sus, av = valideaza(intrare, poz)
        except ValueError as e:
            erori.append(str(e))
            continue
        avertismente.extend(av)
        pe_persona.setdefault(persona, []).append(scor_sus(sus))

    for e in erori:
        print(f"RESPINS: {e}", file=sys.stderr)
    if not pe_persona:
        print("Niciun set de răspunsuri valid.", file=sys.stderr)
        return 1

    cu_repetari = any(len(s) > 1 for s in pe_persona.values())
    medii = {p: statistics.mean(s) for p, s in pe_persona.items()}
    media = statistics.mean(medii.values())

    if cu_repetari:
        print("| Persona | Rulări | Scoruri | Medie | Interval | Notă |")
        print("|---|---|---|---|---|---|")
        for p, scoruri in pe_persona.items():
            interval = max(scoruri) - min(scoruri)
            print(f"| {p} | {len(scoruri)} | {', '.join(fmt(s) for s in scoruri)} | "
                  f"{fmt(medii[p])} | {fmt(interval)} | {nota(medii[p])} |")
            if len(scoruri) == 1:
                avertismente.append(f"{p}: o singură rulare, stabilitatea scorului nu se poate judeca.")
            elif interval > PRAG_INSTABIL:
                avertismente.append(
                    f"{p}: scorul variază cu {fmt(interval)} puncte între rulări, "
                    f"peste pragul de {fmt(PRAG_INSTABIL)}. Tratează scorul acestei persona ca zgomot."
                )
        print(f"| **Media panelului** | | | **{fmt(media)}** | | **{nota(media)}** |")
    else:
        print("| Persona | Scor | Notă |")
        print("|---|---|---|")
        for p, scoruri in pe_persona.items():
            print(f"| {p} | {fmt(scoruri[0])} | {nota(scoruri[0])} |")
        print(f"| **Media** | **{fmt(media)}** | **{nota(media)}** |")

    print()
    valori = list(medii.values())
    total_rulari = sum(len(s) for s in pe_persona.values())
    if len(valori) > 1:
        print(f"Împrăștiere între persona: abatere standard {fmt(statistics.stdev(valori))}, "
              f"interval {fmt(min(valori))} - {fmt(max(valori))}, "
              f"{len(valori)} persona, {total_rulari} rulări.")
    else:
        print(f"O singură persona ({total_rulari} rulări), fără împrăștiere între persona.")
    for a in avertismente:
        print(f"ATENȚIE: {a}")
    if erori:
        print(f"ATENȚIE: {len(erori)} set(uri) de răspunsuri respinse, vezi mesajele de eroare.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
