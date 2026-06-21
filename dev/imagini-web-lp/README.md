# /imagini-web-lp — Imagini și video corecte pe landing pages

Aplică automat regulile de performanță și accesibilitate pentru imagini și video
pe orice landing page HTML. Acoperă formate, dimensiuni, lazy loading, video autoplay
și meta tags sociale.

## Când îl folosești

- Adaugi o imagine sau secțiune hero pe un LP
- Construiești carduri, galerii, testimoniale sau secțiuni cu video
- Auditezi o pagină existentă pentru probleme de imagini
- Vrei să verifici că OG Image și meta tags sociale sunt corecte

## Ce face

- Alege automat formatul corect (AVIF/WebP, SVG, fallback JPG)
- Pune `fetchpriority="high"` pe hero și `loading="lazy"` pe imaginile sub fold
- Generează `<picture>` cu surse AVIF/WebP și fallback JPG
- Adaugă atributele obligatorii `width`, `height`, `alt` pe orice `<img>`
- Configurează video cu `muted playsinline loop autoplay poster`
- Știe să lucreze cu Next.js, Astro și Nuxt (nu generează `<picture>` manual când framework-ul se ocupă)
- Include surse gratuite Unsplash/Pexels cu parametri de optimizare direct în URL
- Poate explica orice regulă în termeni non-tehnici dacă ești la început

## Instalare

```bash
mkdir -p ~/.claude/skills/imagini-web-lp
cp skill.md ~/.claude/skills/imagini-web-lp/SKILL.md
```
