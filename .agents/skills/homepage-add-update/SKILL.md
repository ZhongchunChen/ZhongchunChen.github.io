---
name: homepage-add-update
description: Add or revise a dated homepage Updates entry in this ZhongchunChen.github.io repository. Use for research, internship, award, publication, or personal news shown under About.
---

# Add Update

Updates live in UPDATES in site_data.py with fields date and text.

Require the date in YYYY.MM and the event. Ask if either is missing or uncertain; do not guess a month, status, acceptance, institution, or future plan. If the user supplies Chinese prose, translate it into concise natural English while preserving the facts.

Insert entries in reverse chronological order. Avoid duplicating an existing update; revise it when the user is clearly correcting the same event.

Run python3 build_site.py, Python compile checks, and git diff --check. Verify the entry and ordering in index.html.
