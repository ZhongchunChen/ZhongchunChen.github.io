from __future__ import annotations

from html import escape
from pathlib import Path
from typing import Iterable

from site_data import (
    COURSES,
    EDUCATION,
    EXPERIENCE,
    LIFE_RECORDS,
    NOTES,
    PROJECTS,
    PUBLICATIONS,
    REWARDS,
    SITE,
)


ROOT = Path(__file__).parent


def e(value: object) -> str:
    return escape(str(value), quote=True)


def href(value: object) -> str:
    url = str(value).strip()
    if (
        not url
        or url == "#"
        or url.startswith(("#", "/", "mailto:", "http://", "https://"))
        or url.endswith((".html", ".pdf"))
        or "/" in url
    ):
        return url or "#"
    return f"https://{url}"


def tag_list(tags: Iterable[str]) -> str:
    return "".join(f'<span class="tag">{e(tag)}</span>' for tag in tags)


def link_list(links: dict[str, str]) -> str:
    items = []
    for label, url in links.items():
        if url:
            items.append(f'<a class="text-link" href="{e(href(url))}">{e(label.title())}</a>')
    return "".join(items)


def nav(active: str, prefix: str = "") -> str:
    links = [
        ("index.html", "Home"),
        ("notes.html", "Note"),
        ("life.html", "Life"),
    ]
    return "".join(
        f'<a class="{"active" if label == active else ""}" href="{prefix}{href}">{label}</a>'
        for href, label in links
    )


def layout(title: str, active: str, body: str, prefix: str = "") -> str:
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="{e(SITE["name"])} personal academic homepage">
  <title>{e(title)} | {e(SITE["name"])}</title>
  <link rel="stylesheet" href="{prefix}assets/style.css">
</head>
<body>
  <header class="topbar">
    <a class="brand" href="{prefix}index.html">{e(SITE["name"])}</a>
    <nav>{nav(active, prefix)}</nav>
  </header>
  <main>
    {body}
  </main>
  <footer>
    <span>Built with Python for GitHub Pages.</span>
    <span>Last updated: 2026</span>
  </footer>
</body>
</html>
"""


def hero() -> str:
    interests = "".join(f"<li>{e(item)}</li>" for item in SITE["interests"])
    internship_title = e(EXPERIENCE[0]["organization"])
    internship_url = EXPERIENCE[0].get("url")
    if internship_url and internship_url != "#":
        internship_title = f'<a class="text-link" href="{e(href(internship_url))}">{internship_title}</a>'
    return f"""
<section class="hero">
  <aside class="profile-panel">
    <img src="{e(SITE["avatar"])}" alt="{e(SITE["name"])} portrait">
    <div>
      <strong>{e(SITE["location"])}</strong>
      <ul>{interests}</ul>
    </div>
  </aside>
  <div class="hero-copy">
    <p class="eyebrow">{e(SITE["role"])} · {e(SITE["affiliation"])}</p>
    <h1>{e(SITE["name"])}</h1>
    <p class="intro">{e(SITE["intro"])}</p>
    <p class="contact-line">Email: <a href="mailto:{e(SITE["email"])}">{e(SITE["email"])}</a></p>
    <div class="actions">
      <a class="button primary" href="mailto:{e(SITE["email"])}">Email</a>
      <a class="button primary" href="{e(SITE["github"])}">GitHub</a>
      <a class="button" href="{e(SITE["scholar"])}">Google Scholar</a>
    </div>
    <div class="hero-details">
      <section>
        <p class="mini-label">Education</p>
        <h2>{e(EDUCATION[0]["school"])}</h2>
        <p>{e(EDUCATION[0]["degree"])}</p>
        <span>{e(EDUCATION[0]["period"])}</span>
      </section>
      <section>
        <p class="mini-label">Internship</p>
        <h2>{internship_title}</h2>
        <p>{e(EXPERIENCE[0]["role"])}</p>
        <span>{e(EXPERIENCE[0]["period"])}</span>
      </section>
    </div>
  </div>
</section>
"""


def media_items(items: list[dict[str, object]]) -> str:
    rendered = []
    for item in items:
        title = e(item["title"])
        item_url = item.get("url")
        if item_url:
            title = f'<a href="{e(href(item_url))}">{title}</a>'
        rendered.append(
            f"""
<article class="media-item">
  <img src="{e(item["image"])}" alt="">
  <div>
    <div class="item-meta">{e(item.get("period") or item.get("venue") or "")}</div>
    <h3>{title}</h3>
    <p>{e(item["description"])}</p>
    <div class="item-row">{tag_list(item.get("tags", []))}</div>
    <div class="item-row">{link_list(item.get("links", {}))}</div>
  </div>
</article>
"""
        )
    return "".join(rendered)


def timeline(items: list[dict[str, str]], title_key: str, subtitle_key: str) -> str:
    rendered = []
    for item in items:
        rendered.append(
            f"""
<article class="timeline-item">
  <div class="date">{e(item["period"] if "period" in item else item["date"])}</div>
  <div>
    <h3>{e(item[title_key])}</h3>
    <p class="subtitle">{e(item[subtitle_key])}</p>
    <p>{e(item["details"] if "details" in item else item["description"])}</p>
  </div>
</article>
"""
        )
    return "".join(rendered)


def reward_items(items: list[dict[str, str]]) -> str:
    rendered = []
    for item in items:
        rendered.append(
            f"""
<article class="timeline-item">
  <div class="date">{e(item["date"])}</div>
  <div>
    <h3>{e(item["title"])}</h3>
    <p>{e(item["description"])}</p>
  </div>
</article>
"""
        )
    return "".join(rendered)


def index_page() -> str:
    body = f"""
{hero()}
<section class="section">
  <div class="section-heading">
    <p class="eyebrow">Publications</p>
  </div>
  <div class="stack">{media_items(PUBLICATIONS)}</div>
</section>
<section class="section">
  <div class="section-heading">
    <p class="eyebrow">Projects</p>
  </div>
  <div class="stack">{media_items(PROJECTS)}</div>
</section>
<section class="section">
  <div class="section-heading">
    <p class="eyebrow">Rewards</p>
  </div>
  <div class="timeline">{reward_items(REWARDS)}</div>
</section>
"""
    return layout("Home", "Home", body)


def reliable_grasp_page() -> str:
    project = next(
        item for item in PROJECTS if item.get("url") == "reliable_grasp/"
    )
    demo_cards = [
        ("demo_01.mp4", "demo_01.jpg", "Top-view yellow target"),
        ("demo_02.mp4", "demo_02.jpg", "Top-view blue target"),
        ("demo_03.mp4", "demo_03.jpg", "Top-view white target"),
        ("demo_04.mp4", "demo_04.jpg", "Top-view black target"),
        ("demo_05.mp4", "demo_05.jpg", "FR3 grasping scene A"),
        ("demo_06.mp4", "demo_06.jpg", "FR3 grasping scene B"),
        ("demo_07.mp4", "demo_07.jpg", "Full workspace scene"),
    ]
    demos = []
    for index, (video_name, poster_name, label) in enumerate(demo_cards, start=1):
        demos.append(
            f"""
<article class="demo-card">
  <video class="autoplay-demo" autoplay loop muted playsinline preload="auto" poster="../assets/content/projects/reliable_grasp/{poster_name}?v=2" aria-label="{e(label)}">
    <source src="../assets/content/projects/reliable_grasp/{video_name}?v=2" type="video/mp4">
    Your browser does not support the video tag.
  </video>
</article>
"""
        )
    body = f"""
<section class="reliable-hero">
  <div>
    <p class="eyebrow">Project Demo</p>
    <h1>{e(project["title"])}</h1>
    <p>{e(project["description"])}</p>
    <div class="item-row">{tag_list(project.get("tags", []))}</div>
  </div>
  <div class="project-facts" aria-label="Project facts">
    <span>{e(project["period"])}</span>
    <span>YOLO11-Seg + pi_0.5 VLA</span>
    <span>Physical FR3 Robot</span>
  </div>
</section>
<section class="demo-showcase">
  <div class="showcase-banner">
    <div class="seal">SJTU</div>
    <h2>Demo Display</h2>
    <div class="banner-mark" aria-hidden="true"><span></span><span></span></div>
  </div>
  <div class="demo-grid">{"".join(demos)}</div>
</section>
<section class="result-section">
  <div class="section-heading compact">
    <p class="eyebrow">Results</p>
    <h2>Segmentation and Progress Comparison</h2>
  </div>
  <div class="result-grid">
    <figure class="figure-placeholder large">
      <img src="../assets/content/projects/reliable_grasp/chart_segmentation.png" alt="Segmentation result comparison chart" onerror="this.hidden=true">
      <figcaption>
        <strong>Figure 8. Segmentation Results</strong>
      </figcaption>
    </figure>
    <figure class="figure-placeholder">
      <img src="../assets/content/projects/reliable_grasp/chart_progress.png" alt="Progress comparison chart" onerror="this.hidden=true">
      <figcaption>
        <strong>Figure 9. Progress Comparison</strong>
      </figcaption>
    </figure>
  </div>
</section>
<section class="architecture-section">
  <div class="section-heading compact">
    <p class="eyebrow">System</p>
    <h2>Goal-Conditioned Grasping System Architecture</h2>
  </div>
  <figure class="figure-placeholder architecture-figure">
    <img src="../assets/content/projects/reliable_grasp/system_architecture.png" alt="Goal-conditioned grasping system architecture" onerror="this.hidden=true">
    <figcaption>
      <strong>System Architecture</strong>
    </figcaption>
  </figure>
</section>
<script>
  const playDemos = () => {{
    document.querySelectorAll('.autoplay-demo').forEach((video) => {{
      video.muted = true;
      video.loop = true;
      video.playsInline = true;
      video.play().catch(() => {{}});
    }});
  }};
  document.addEventListener('DOMContentLoaded', playDemos);
  window.addEventListener('load', playDemos);
</script>
"""
    return layout("Reliable Grasp", "Home", body, prefix="../")


def reliable_grasp_redirect_page() -> str:
    return """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="refresh" content="0; url=reliable_grasp/">
  <title>Reliable Grasp | Redirect</title>
  <link rel="canonical" href="reliable_grasp/">
</head>
<body>
  <p><a href="reliable_grasp/">Open Reliable Grasp demo page</a></p>
</body>
</html>
"""


def filter_script() -> str:
    return """
<script>
  const filterToggle = document.querySelector('.filter-toggle');
  const filterPanel = document.querySelector('.filter-panel');
  const currentFilter = document.querySelector('.current-filter');
  const buttons = document.querySelectorAll('.filter-button');
  const cards = document.querySelectorAll('[data-tags]');
  if (filterToggle && filterPanel) {
    filterToggle.addEventListener('click', () => {
      const isOpen = !filterPanel.hidden;
      filterPanel.hidden = isOpen;
      filterToggle.setAttribute('aria-expanded', String(!isOpen));
    });
  }
  buttons.forEach((button) => {
    button.addEventListener('click', () => {
      buttons.forEach((item) => item.classList.remove('active'));
      button.classList.add('active');
      const filter = button.dataset.filter;
      if (currentFilter) {
        currentFilter.textContent = filter === 'all' ? 'All' : button.textContent;
      }
      cards.forEach((card) => {
        const cardTags = card.dataset.tags ? card.dataset.tags.split('|') : [];
        const visible = filter === 'all' || cardTags.includes(filter);
        card.hidden = !visible;
      });
      if (filterPanel && filter !== 'all') {
        filterPanel.hidden = true;
        filterToggle.setAttribute('aria-expanded', 'false');
      }
    });
  });
  document.addEventListener('click', (event) => {
    if (!filterPanel || !filterToggle || filterPanel.hidden) return;
    if (!filterPanel.contains(event.target) && !filterToggle.contains(event.target)) {
      filterPanel.hidden = true;
      filterToggle.setAttribute('aria-expanded', 'false');
    }
  });
</script>
"""


def tag_filter(tags: list[str]) -> str:
    grouped: dict[str, list[str]] = {}
    for tag in tags:
        initial = tag[0].upper() if tag and tag[0].isalnum() else "#"
        grouped.setdefault(initial, []).append(tag)

    groups = []
    for initial in sorted(grouped):
        tag_buttons = "".join(
            f'<button class="filter-button" data-filter="{e(tag)}">{e(tag)}</button>'
            for tag in grouped[initial]
        )
        groups.append(
            f"""
<div class="filter-group">
  <div class="filter-letter">{e(initial)}</div>
  <div class="filter-options">{tag_buttons}</div>
</div>
"""
        )

    return f"""
<section class="filters" aria-label="Tag filters">
  <div class="filter-summary">
    <button class="filter-toggle" type="button" aria-expanded="false" aria-controls="tag-filter-panel">
      Filter Tags
    </button>
    <span>Current: <strong class="current-filter">All</strong></span>
    <button class="filter-button reset-filter active" data-filter="all" type="button">All</button>
  </div>
  <div class="filter-panel" id="tag-filter-panel" hidden>
    {"".join(groups)}
  </div>
</section>
"""


def media_collection_page(
    title: str,
    active: str,
    intro: str,
    items: list[dict[str, object]],
    kind: str,
    heading: str | None = None,
) -> str:
    tags = sorted({tag for item in items for tag in item.get("tags", [])})
    cards = []
    for item in items:
        tags_attr = "|".join(item.get("tags", []))
        meta = item.get("date") or item.get("term") or ""
        prefix = f'{e(item.get("code", ""))} · ' if item.get("code") else ""
        cards.append(
            f"""
<article class="media-item note-item" data-tags="{e(tags_attr)}">
  <img src="{e(item.get("image", "assets/img/project-notes.svg"))}" alt="">
  <div>
    <div class="item-meta">{prefix}{e(meta)}</div>
    <h3><a href="{e(item.get("url", "#"))}">{e(item.get("title", ""))}</a></h3>
    <p>{e(item.get("summary", ""))}</p>
    <div class="item-row">{tag_list(item.get("tags", []))}</div>
  </div>
</article>
"""
        )
    section_title = f'<div class="section-heading"><p class="eyebrow">{e(kind)}</p><h2>{e(heading)}</h2></div>' if heading else ""
    body = f"""
<section class="page-hero">
  <p class="eyebrow">{e(kind)}</p>
  <h1>{e(title)}</h1>
  <p>{e(intro)}</p>
</section>
{tag_filter(tags)}
<section class="section collection-list">{section_title}<div class="stack">{"".join(cards)}</div></section>
{filter_script()}
"""
    return layout(title, active, body)


def main() -> None:
    pages = {
        "index.html": index_page(),
        "notes.html": media_collection_page(
            "Note",
            "Note",
            "Technical notes, reading summaries, course records, and implementation references.",
            NOTES + COURSES,
            "Notes",
        ),
        "life.html": media_collection_page(
            "Life",
            "Life",
            "Personal records and non-academic updates organized with lightweight tags.",
            LIFE_RECORDS,
            "Life",
        ),
        "reliable_grasp/index.html": reliable_grasp_page(),
        "reliable_grasp.html": reliable_grasp_redirect_page(),
    }
    for filename, content in pages.items():
        path = ROOT / filename
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")


if __name__ == "__main__":
    main()
