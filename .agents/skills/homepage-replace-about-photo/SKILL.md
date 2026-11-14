---
name: homepage-replace-about-photo
description: Replace and configure the About-page profile photo in this ZhongchunChen.github.io repository, including caption and crop behavior. Use when the user supplies or requests a new About portrait.
---

# Replace About Photo

The source image belongs under assets/img/; SITE avatar in site_data.py controls the image path. The caption and display behavior are currently rendered by home() and styled in assets/theme.css.

Require:

- An attached image or an existing repository image path.
- Crop preference: complete uncropped image, cover crop, or a clearly described focal point.

Ask before editing if the image is missing or crop intent cannot be inferred. If the user asks for a new caption but omits its text/date, ask for it. Otherwise preserve the existing caption. Do not fabricate when or where a photo was taken.

Confirm the image exists and inspect it before choosing object-fit or object-position. Preserve responsive mobile behavior and dark mode.

After editing, run the site build, Python compile checks, and git diff --check. Verify index.html references the intended image and caption. When browser preview is available, visually inspect the About section.
