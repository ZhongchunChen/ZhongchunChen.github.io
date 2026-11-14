---
name: homepage-edit-about
description: Edit the About-page biography, role, affiliation, email, social links, hobbies, or photo caption in this ZhongchunChen.github.io repository. Use when the user asks to change About text or profile metadata; use homepage-replace-about-photo when the image itself changes.
---

# Edit About

Work only in the repository containing site_data.py and build_site.py.

Before editing, inspect the current SITE object and home() renderer. About content is split between SITE in site_data.py and markup in build_site.py; preserve the existing layout, selective bolding, links, and paragraph structure unless the user requests otherwise.

Required input depends on the requested field:

- Biography: replacement wording or enough facts to draft it.
- Role, affiliation, email, or social link: the exact new value.
- Hobby paragraph or caption: the desired fact/date and preferred language when unclear.

If the target paragraph or replacement fact is ambiguous, ask one concise question before editing. Never invent affiliations, research claims, dates, links, or contact details. Preserve facts the user did not ask to change.

After editing, run python3 build_site.py, python3 -m py_compile site_data.py build_site.py, and git diff --check. Verify the requested text and any link target in index.html.
