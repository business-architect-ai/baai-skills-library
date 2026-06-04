---
name: ortografie-ro
compatibility: codex-and-claude-code
---

# /ortografie-ro - Corectează ortografia română (sentence case)

Aplică regulile de ortografie pentru limba română pe fișierele specificate.

## Protocol strict de capitalizare

Când corectezi sau generezi text în limba română, respectă aceste reguli:

### 1. Sentence case obligatoriu
Folosește majusculă **DOAR** la prima literă a primului cuvânt din:
- Titluri și subtitluri (h1, h2, h3, etc.)
- Liste (bullet points)
- Capete de tabel (th)

### 2. Interdicție Title Case
NU scrie cu majusculă fiecare cuvânt.
- Corect: "Ghidul complet pentru operatorii de inteligență artificială"
- Greșit: "Ghidul Complet Pentru Operatorii De Inteligență Artificială"

### 3. Excepția unică
Majuscule în interiorul titlurilor doar pentru:
- Substantive proprii (nume, țări, instituții)
- Acronime (AI, GPT, API, RTF, etc.)
- Nume de framework-uri/produse (ChatGPT, Claude, Chain of Thought, etc.)

### 4. După două puncte (:) se scrie cu literă mică
- Corect: "Regula de aur: politețea ta introduce «zgomot» în sistem"
- Greșit: "Regula de aur: Politețea ta introduce «zgomot» în sistem"
- Excepție: substantive proprii după (:)

## Cum se aplică

Dacă userul dă un path la un fișier sau folder:
1. Citește fișierele markdown
2. Identifică toate titlurile, subtitlurile, listele și capetele de tabel
3. Corectează capitalizarea conform regulilor de mai sus
4. Afișează modificările propuse înainte de a le aplica
5. Aplică doar după confirmare

Dacă userul nu dă un path, aplică regulile pe textul generat în conversația curentă.

**Nu modifica:**
- Conținutul paragrafelor (doar titluri, liste, th)
- Cuvintele care sunt corect cu majusculă (substantive proprii, acronime)
- Text în alte limbi decât română
