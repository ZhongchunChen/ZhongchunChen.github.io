---
name: homepage-add-project
description: Add or revise a Projects-page card in this ZhongchunChen.github.io repository, including Robot projects, Course projects, and Notes. Use when new work should appear under the Course, Notes, or Robot filter.
---

# Add Project

First determine the displayed category:

- Robot: add to PROJECTS with title, period, description, image, url, links, and technical tags.
- Course: add to COURSES with title, date, summary, image, tags, and url.
- Notes: add to NOTES with title, date, summary, image, tags, and url.

Require the category, title, date or period, concise description, cover image, and destination decision. Ask for every missing field that changes the card. A destination may be explicitly none; do not invent one. A cover image is required—ask if none is attached or identified. Also ask whether the image should cover-crop or display completely when its composition makes that choice material.

Store images under assets/img/. Use cover_fit set to contain only for complete-image display; cover_zoom may be true when excess whitespace makes a contained cover unreadable. Preserve the existing Course, Notes, and Robot filters and Isotope-style animation.

For a custom detail page, require its content and media separately; do not infer that a card request authorizes inventing a detail page.

Run the site build, Python compile checks, and git diff --check. Verify the card, filter, cover behavior, and target in projects.html.
