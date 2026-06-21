---
name: imagini-web-lp
description: Aplică automat toate regulile corecte de imagini și video pe landing pages. Folosește când adaugi orice imagine sau video, când construiești secțiuni hero/carduri/galerii/testimoniale, sau când auditezi o pagină existentă. Trigger keywords (RO/EN): "adaugă imagine", "secțiune hero", "galerie foto", "video background", "add image", "hero section", "image gallery", "optimize images", "lazy loading".
---

# Imagini și video pe landing pages

Aplică TOATE regulile de mai jos de fiecare dată când lucrezi cu imagini sau video pe o pagină web. Nu sări niciun punct.

## Reguli fundamentale (non-negociabile)

### Orice `<img>` trebuie să aibă obligatoriu:
- `width` și `height` cu valorile reale în pixeli (previne layout shift)
- `alt` cu descriere concretă (nu gol, nu "imagine", nu "foto") - EXCEPȚIE: imagini decorative au `alt=""` și `aria-hidden="true"`
- Pentru fotografii și imagini raster: AVIF/WebP când e posibil, cu fallback JPG/PNG sau optimizare nativă de framework
- `loading="lazy"` doar pe imaginile offscreen/sub fold; imaginile vizibile în primul viewport se încarcă eager

Nu începe `alt` cu "imagine cu", "poză cu" sau "fotografie cu". Descrie direct informația utilă: `Consultant financiar explicând un dashboard de venituri`, nu `Imagine cu consultant`.

SVG-urile nu se învelesc în `<picture>`. Pentru logo-uri, iconițe și ilustrații vectoriale, preferă SVG inline sau fișier `.svg` extern cu dimensiuni explicite.

### Hero/LCP image (imaginea principală deasupra foldului):
- `fetchpriority="high"` obligatoriu
- `loading="lazy"` INTERZIS
- Dacă există și alte imagini vizibile imediat în primul viewport, nu le pune `loading="lazy"`; marchează-le în HTML static cu `data-above-fold="true"` ca auditul să știe intenția
- Dimensiune default: 1920x1080px (full-width) sau 1280x720px (container)
- Dacă designul cere alt raport (produs vertical, screenshot, portret, mobile art direction), păstrează raportul corect și generează variante responsive
- Fișier: sub 300KB

### Imagini offscreen / sub fold:
- `loading="lazy"` obligatoriu
- Dimensiuni standard: carduri 800x500px, avatare 120x120px
- Fișier: sub 150KB

### Video autoplay:
- Cele 4 atribute obligatorii împreună: `autoplay muted loop playsinline`
- `poster` cu imagine fallback obligatoriu
- Surse duble: MP4 + WebM
- Pe mobile (max-width: 768px): ascunde `<video>`, afișează `poster` ca `<img>`

---

## Framework-uri moderne

Dacă proiectul folosește un framework cu image optimization nativ, folosește componenta framework-ului în loc să recreezi manual `<picture>`, dar păstrează aceleași principii:

| Framework | Preferință |
|-----------|------------|
| Next.js | `next/image` cu `width`, `height`, `alt`, `priority` pentru hero și lazy implicit pentru imaginile offscreen |
| Astro | `astro:assets` / `Image` cu dimensiuni și format modern |
| Nuxt | `NuxtImg` / provider image configurat |
| Shopify / Webflow / CMS | folosește transformările CDN disponibile, dar verifică HTML-ul final |

Mapare reguli:
- Hero: `priority` / `fetchpriority="high"` / preload framework-specific
- Offscreen/sub fold: lazy loading implicit sau explicit
- Raster: AVIF/WebP când framework-ul îl poate genera automat
- `alt`: scris manual, nu lăsat pe nume de fișier

---

## Template-uri HTML corecte

### Hero imagine
```html
<picture>
  <source srcset="hero.avif" type="image/avif">
  <source srcset="hero.webp" type="image/webp">
  <img
    src="hero.jpg"
    width="1920"
    height="1080"
    alt="[descriere concretă]"
    fetchpriority="high">
</picture>
```

### Imagine secțiune / card
```html
<picture>
  <source srcset="imagine.avif" type="image/avif">
  <source srcset="imagine.webp" type="image/webp">
  <img
    src="imagine.jpg"
    width="800"
    height="500"
    alt="[descriere concretă]"
    loading="lazy">
</picture>
```

### Avatar circular (testimoniale)
```html
<img
  src="avatar.webp"
  width="120"
  height="120"
  alt="[Numele persoanei]"
  loading="lazy"
  style="border-radius: 50%;">
```

### Imagine decorativă (fundal, separator)
```html
<img
  src="fundal.webp"
  width="1920"
  height="200"
  alt=""
  aria-hidden="true"
  loading="lazy">
```

### Imagine responsivă (srcset complet)
```html
<picture>
  <source
    type="image/avif"
    srcset="imagine-400.avif 400w, imagine-800.avif 800w, imagine-1280.avif 1280w"
    sizes="(max-width: 600px) 100vw, (max-width: 1024px) 80vw, 1280px">
  <source
    type="image/webp"
    srcset="imagine-400.webp 400w, imagine-800.webp 800w, imagine-1280.webp 1280w"
    sizes="(max-width: 600px) 100vw, (max-width: 1024px) 80vw, 1280px">
  <img
    src="imagine-1280.jpg"
    width="1280"
    height="720"
    alt="[descriere]"
    loading="lazy">
</picture>
```

### Logo / iconiță (Retina-safe)
```html
<!-- Preferință: SVG inline sau fișier .svg extern -->
<img
  src="logo.svg"
  width="200"
  height="60"
  alt="[Numele companiei]">

<!-- Dacă SVG nu e disponibil: srcset 1x / 2x -->
<img
  srcset="logo.webp 1x, logo@2x.webp 2x"
  src="logo.webp"
  width="200"
  height="60"
  alt="[Numele companiei]">
```

### Video hero
```html
<video autoplay muted loop playsinline poster="preview.jpg">
  <source src="hero.webm" type="video/webm">
  <source src="hero.mp4" type="video/mp4">
</video>
```

CSS obligatoriu pentru fallback mobile:
```css
@media (max-width: 768px) {
  .hero-video { display: none; }
  .hero-poster { display: block; }
}
```

### Meta tags sociale (în `<head>`, obligatorii pe orice LP)
```html
<meta property="og:image" content="https://domeniu.ro/og-image.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:title" content="[Titlul paginii]">
<meta property="og:description" content="[Descrierea paginii]">
<meta property="og:url" content="https://domeniu.ro">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image" content="https://domeniu.ro/og-image.jpg">
```

---

## Surse imagini gratuite (licență comercială)

Fotografii URL direct optimizat:
- **Unsplash**: `https://images.unsplash.com/photo-[ID]?w=1280&h=720&fit=crop&q=80&fm=webp`
- **Pexels**: descarcă manual, deja bine comprimate
- Pentru producție serioasă, preferă `auto=format` sau pipeline-ul framework-ului ca browserul/CDN-ul să poată alege AVIF sau WebP după suport.

Parametri Unsplash util:
- Hero: `?w=1920&h=1080&fit=crop&q=80&fm=webp`
- Card: `?w=800&h=500&fit=crop&q=75&fm=webp`
- Avatar: `?w=120&h=120&fit=crop&q=80&fm=webp&face=center`
- OG Image: `?w=1200&h=630&fit=crop&q=80&fm=webp`

Placeholder avatare: `https://i.pravatar.cc/120?img=[1-70]`

Video gratuite: coverr.co, mixkit.co

SVG ilustrații: undraw.co, storyset.com

Iconițe SVG: heroicons.com, lucide.dev

Nu folosi Google Images ca sursă de producție. Dacă utilizatorul cere o imagine specifică de brand/produs/persoană, folosește surse oficiale, asset-uri furnizate de utilizator sau cere confirmare privind drepturile.

---

## CSS vs img - regula de decizie

| Situație | Folosești |
|----------|-----------|
| Fotografie produs, persoană, grafic informativ | `<img>` cu alt descriptiv |
| Logo, iconiță cu sens | `<img>` sau SVG inline |
| Fundal decorativ, pattern, textură | `background-image` CSS |
| Hero cu text suprapus | `<img>` cu position absolute sau CSS |

Nu folosi `background-image` CSS pentru imagini cu informație - pierzi SEO și accesibilitate.

---

## Dimensiuni standard

| Element | Dimensiune | Fișier max |
|---------|-----------|------------|
| Hero full-width | 1920x1080px | 300KB |
| Hero cu container | 1280x720px | 300KB |
| Card / thumbnail | 800x500px | 150KB |
| Avatar | 120x120px | 30KB |
| OG Image | 1200x630px | 200KB |
| Logo | SVG sau 200x60px | - |
| Video hero | 1920x1080px | 15MB |
| Total pagină | - | 2MB |

---

## Audit - ce verifici înainte să declari pagina gata

Rulează auditul după orice modificare de imagini sau video. Pentru HTML static, folosește scriptul inclus:

```bash
node ~/.claude/skills/imagini-web-lp/scripts/audit-media-html.mjs path/to/page.html
```

Pentru aplicații build-uite sau pagini locale, inspectează HTML-ul final, nu doar componentele sursă. Dacă există Lighthouse disponibil, rulează și:

```bash
npx lighthouse http://localhost:3000 --only-categories=performance,accessibility,seo,best-practices
```

Checklist obligatoriu:

1. Fiecare `<img>` are `width`, `height` și `alt`?
2. Imaginile decorative au `alt=""` și `aria-hidden="true"`?
3. Hero image are `fetchpriority="high"` și NU are `loading="lazy"`?
4. Imaginile offscreen/sub fold au `loading="lazy"`?
5. Imaginile vizibile în primul viewport NU sunt lazy-loaded?
6. Fotografiile/rasterele sunt învelite în `<picture>` cu sursă AVIF/WebP sau optimizate nativ de framework?
7. Logo-urile și iconițele sunt SVG?
8. Video-urile au `muted`, `playsinline`, `loop`, `autoplay` și `poster`?
9. Există fallback CSS care ascunde video pe mobile?
10. Există `og:image` la 1200x630px în `<head>`?
11. Imaginile vin de pe surse cu licență comercială (Unsplash, Pexels, nu Google Images)?
12. Lighthouse/PageSpeed Insights nu raportează probleme evidente de LCP, CLS sau imagini neoptimizate?

Dacă oricare punct lipsește, corectează înainte să treci mai departe.

### Semnale Lighthouse de urmărit

- **LCP mare**: de obicei hero image prea grea, fără `fetchpriority`, sau servită la dimensiune greșită
- **CLS**: lipsește `width`/`height` sau containerul media nu are aspect ratio stabil
- **Properly size images**: fișierul livrat este mult mai mare decât dimensiunea afișată
- **Serve images in next-gen formats**: lipsește WebP/AVIF pentru rastere
- **Defer offscreen images**: imagini sub fold fără lazy loading

Lighthouse este test de laborator. Pentru site-uri publice cu trafic, compară rezultatul și cu PageSpeed Insights/CrUX; datele reale ale utilizatorilor sunt mai importante decât un singur test local.

---

## Explicații pentru utilizatori non-tehnici

Dacă utilizatorul întreabă "de ce" pentru oricare regulă, explică pe scurt:

- **AVIF/WebP**: același aspect vizual, fișier mai mic decât JPG/PNG, pagina se încarcă mai repede
- **width + height**: browserul rezervă spațiul din start, pagina nu "sare" când se încarcă imaginea
- **alt**: Google și cititoarele de ecran nu "văd" imaginile, citesc `alt`-ul
- **lazy loading**: browserul descarcă imaginile de jos abia când utilizatorul se apropie de ele; imaginile din primul ecran nu se amână
- **fetchpriority pe hero**: spune browserului "asta e prima prioritate", apare imediat la deschidere
- **muted pe video**: browserele blochează autoplay cu sunet, fără `muted` video-ul nu pornește
- **playsinline**: fără el, iOS intră în fullscreen forțat la redarea video
- **poster pe video**: fără el, utilizatorul vede un dreptunghi negru până se încarcă video-ul
- **OG image**: când cineva distribuie link-ul pe WhatsApp sau Facebook, asta e imaginea din preview
- **Licențiere**: imaginile de pe Google Images pot fi cu drepturi de autor, Unsplash/Pexels sunt sigure
