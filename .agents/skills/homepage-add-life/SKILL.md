---
name: homepage-add-life
description: Add or revise a dated Lifes-page card in this ZhongchunChen.github.io repository. Use for Photo, Social, Hobby, or Travel memories with bilingual titles, cover images, descriptions, tags, and optional links.
---

# Add Life

Life cards live in LIFE_RECORDS in site_data.py and are sorted newest-first by build_site.py.

Require:

- English title; include the requested Chinese title in parentheses when supplied.
- Date in YYYY.MM.
- Enough facts for a concise English first-person description ending in [YYYY.MM].
- At least one tag from Photo, Social, Hobby, or Travel; multiple tags are supported.
- An attached image or existing path under assets/img/.
- Link decision: exact URL or explicit no-link.
- Image behavior: cover crop or complete image.

Ask for missing information before editing. A cover image is mandatory; never substitute an unrelated placeholder. Do not invent dates, companions, locations, relationships, or links. Translate Chinese into natural English without adding claims.

Use cover_fit set to contain only when the full image must remain visible; the existing contained-image background is white in both themes. Omit it for edge-to-edge cover crop. Use a hash URL only after the user explicitly says no jump is needed.

Keep equal-date items in the user's requested order. Preserve the Photo, Social, Hobby, and Travel filters and Isotope-style animation.

Run the site build, Python compile checks, and git diff --check. Verify title, description, image, tags, URL, and chronological position in life.html.
