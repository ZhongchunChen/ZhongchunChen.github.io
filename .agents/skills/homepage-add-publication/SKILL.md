---
name: homepage-add-publication
description: Add or revise a publication shown on the homepage and Research page of this ZhongchunChen.github.io repository. Use for papers, manuscripts, workshop papers, and publication links or cover images.
---

# Add Publication

Publications live in PUBLICATIONS in site_data.py. Read the current renderer in pub_cards() before editing.

Require:

- Title.
- Authors in display order.
- Venue or status and year.
- Short factual summary.
- Cover or teaser image attached or already present under assets/img/.
- Link decision: supplied paper, project, or code links, or explicit confirmation that no link is available.

If any item is missing, ask for the missing information before editing. In particular, never silently use a placeholder cover or invent authors, status, venue, results, or URLs.

Use the existing fields title, authors, venue, description, image, links, and optional tags. Copy an attached cover into assets/img/ only when needed and use a descriptive filename. Preserve the user's author formatting and factual claims.

Run the site build, Python compile checks, and git diff --check. Verify the publication appears in both index.html and research.html, including its image, summary behavior, and links.
