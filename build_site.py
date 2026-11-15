from html import escape
from pathlib import Path
from site_data import COURSES, EDUCATION, EXPERIENCE, LIFE_RECORDS, NOTES, PROJECTS, PUBLICATIONS, SITE, UPDATES

ROOT = Path(__file__).parent

def e(value): return escape(str(value), quote=True)
def href(value):
    value = str(value or "#").strip()
    if value == "#" or value.startswith(("http://", "https://", "mailto:", "/", "#")) or "/" in value or value.endswith((".html", ".pdf")): return value
    return f"https://{value}"

def nav(active, prefix=""):
    links = [("index.html", "About"), ("research.html", "Research"), ("experience.html", "Experience"), ("projects.html", "Projects"), ("life.html", "Lifes")]
    return "".join(f'<a class="{"active" if label == active else ""}" href="{prefix}{url}">{label}</a>' for url, label in links)

def layout(title, active, body, prefix=""):
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="description" content="{e(SITE['name'])} — academic homepage"><title>{e(title)} | {e(SITE['name'])}</title>
<script>document.documentElement.dataset.theme=localStorage.getItem("theme")||"light";</script>
<link rel="stylesheet" href="{prefix}assets/style.css?v=8"><link rel="stylesheet" href="{prefix}assets/theme.css?v=1"></head><body>
<header class="site-header"><div class="header-inner"><a class="brand" href="{prefix}index.html">{e(SITE['name'])}</a><div class="nav-actions"><nav>{nav(active,prefix)}</nav><button class="theme-toggle" type="button" aria-label="Switch to dark mode" title="Switch color theme"><span aria-hidden="true">☾</span></button></div></div></header>
<main>{body}</main><footer>© 2026 {e(SITE['name'])}. Built for GitHub Pages.</footer>
<script>
const themeButton=document.querySelector(".theme-toggle");
const applyTheme=theme=>{{document.documentElement.dataset.theme=theme;localStorage.setItem("theme",theme);const dark=theme==="dark";themeButton.innerHTML=dark?"<span aria-hidden='true'>☀</span>":"<span aria-hidden='true'>☾</span>";themeButton.setAttribute("aria-label",dark?"Switch to light mode":"Switch to dark mode");}};
applyTheme(document.documentElement.dataset.theme);
themeButton.addEventListener("click",()=>applyTheme(document.documentElement.dataset.theme==="dark"?"light":"dark"));
</script></body></html>'''

def social_links():
    links=[("CV",SITE.get("cv","#")),("Google Scholar",SITE.get("scholar","#")),("Github",SITE.get("github","#")),("Linkedin",SITE.get("linkedin","#")),("X",SITE.get("x","#"))]
    return ' <span>/</span> '.join(f'<a href="{e(href(url))}"{(" class=placeholder-link" if url=="#" else "")}>{label}</a>' for label,url in links)

def pub_cards(items, summaries=True):
    if not items:
        items=[{"title":"Publication title placeholder","authors":"Zhongchun Chen, Collaborator A, Collaborator B","venue":"Conference / Journal, 2026","description":"A short summary of the problem, approach, and key result will appear here.","image":"assets/img/project-robotics.svg","links":{"paper":"#","code":"#"}}]
    out=[]
    for p in items:
        links=' '.join(f'<a href="{e(href(u))}">[{e(k)}]</a>' for k,u in p.get("links",{}).items())
        summary=f'<p class="summary">{e(p.get("description","Summary placeholder."))}</p>' if summaries else ''
        out.append(f'''<article class="publication"><img src="{e(p.get('image','assets/img/project-robotics.svg'))}" alt=""><div><h3>{e(p['title'])}</h3><p class="authors">{e(p.get('authors','Zhongchun Chen, collaborators'))}</p><p class="venue">{e(p.get('venue','Manuscript, 2026'))}</p><div class="pub-links">{links}</div>{summary}</div></article>''')
    return ''.join(out)

def home():
    def update_text(item):
        rendered = e(item["text"])
        for label, url in item.get("links", {}).items():
            rendered = rendered.replace(e(label), f'<a href="{e(url)}">{e(label)}</a>')
        return rendered
    updates=''.join(f'<li><time>{e(x["date"])}</time><span>{update_text(x)}</span></li>' for x in UPDATES)
    greeting, introduction = SITE["intro"].split(" I am broadly", 1)
    greeting_html = e(greeting).replace("Pocket", "<strong>Pocket</strong>")
    introduction_html = e(introduction)
    for term in ("VLA", "active perception", "flow matching", "RL"):
        introduction_html = introduction_html.replace(term, f"<strong>{term}</strong>")
    body=f'''<section class="about"><figure class="portrait-figure"><img class="portrait" src="{e(SITE['avatar'])}" alt="Portrait of {e(SITE['name'])}"><figcaption>Picture taken in May 2025</figcaption></figure><div class="about-copy"><h1>{e(SITE['name'])}</h1><p class="role">{e(SITE['role'])} · {e(SITE['affiliation'])}</p><p class="intro-greeting">{greeting_html}</p><p>I am broadly{introduction_html}</p><p>Outside of research, I enjoy <strong>running</strong> 🏃, <strong>hiking</strong> 🧗, exploring good <strong>food</strong> 🍜, and playing <strong>Golden Spatula</strong> 🪏.</p><p>You're always <strong>welcome</strong> to chat with me about research or anything else!</p><p>Email: <a href="mailto:{e(SITE['email'])}">{e(SITE['email'])}</a></p><div class="socials">{social_links()}</div></div></section>
<section class="content-section"><h2>Updates</h2><ul class="updates">{updates}</ul></section>
<section class="content-section"><div class="heading-row"><h2>Publications</h2><a href="research.html">View all →</a></div>{pub_cards(PUBLICATIONS,False)}</section>'''
    return layout("About","About",body)

def research():
    intro="My research focuses on <strong>robot learning</strong>, with current interests in <strong>Vision-Language-Action models</strong>, <strong>active perception</strong>, <strong>flow matching</strong>, and <strong>reinforcement learning</strong>. I am particularly interested in developing <strong>reliable and generalizable robot policies</strong> that can learn from large-scale data and interact effectively with the physical world, including <strong>dexterous manipulation and grasping</strong>. Below is a complete list of my publications and ongoing manuscripts."
    return layout("Research","Research",f'<section class="page-intro"><h1>Research</h1><p>{intro}</p></section><section class="content-section"><h2>Publications</h2>{pub_cards(PUBLICATIONS,True)}</section>')

def experience():
    def rows(items):
        out=[]
        for x in items:
            title=x.get("school") or x.get("organization")
            title=f'<a href="{e(href(x.get("url")))}">{e(title)}</a>' if x.get("url") else e(title)
            details = x.get("details_html") or e(x.get("details", ""))
            details = f"<p>{details}</p>" if details else ""
            out.append(f'<article class="timeline-row"><time>{e(x["period"])}</time><div><div class="experience-heading"><h3>{title}</h3><span class="experience-role">| {e(x.get("degree") or x.get("role"))}</span></div>{details}</div></article>')
        return ''.join(out)
    body=f'<section class="page-intro"><h1>Experience</h1></section><section class="content-section"><h2>Experience</h2>{rows(EXPERIENCE)}</section><section class="content-section"><h2>Education</h2>{rows(EDUCATION)}</section>'
    return layout("Experience","Experience",body)

def grid_cards(items):
    cards=[]
    for x in items:
        tags='|'.join(x.get('tags',[]))
        fit_class = " cover-contain" if x.get("cover_fit") == "contain" else ""
        fit_class += " cover-zoom" if x.get("cover_zoom") else ""
        cards.append(f'''<a class="portfolio-card{fit_class}" data-tags="{e(tags)}" href="{e(href(x.get('url','#')))}"><img src="{e(x.get('image','assets/img/project-notes.svg'))}" alt=""><span class="card-overlay"><strong>{e(x['title'])}</strong><small>{e(x.get('summary') or x.get('description',''))}</small></span></a>''')
    return ''.join(cards)

def filters(items, extra_tags=None):
    tags=sorted({t for x in items for t in x.get('tags',[])} | set(extra_tags or []),key=str.lower)
    buttons='<button class="active" data-filter="all">All</button>'+''.join(f'<button data-filter="{e(t)}">{e(t)}</button>' for t in tags)
    return f'''<div class="filters">{buttons}</div><script>
window.addEventListener("DOMContentLoaded", () => {{
  const buttons = [...document.querySelectorAll(".filters button")];
  const cards = [...document.querySelectorAll(".portfolio-card")];
  const grid = document.querySelector(".portfolio-grid");
  const reducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  if (!grid || !cards.length) return;
  grid.classList.add("isotope-grid", "isotope-no-transition");
  let currentFilter = "all";
  const layout = () => {{
    const gap = 18;
    const columns = window.innerWidth <= 480 ? 1 : window.innerWidth <= 760 ? 2 : 3;
    const width = (grid.clientWidth - gap * (columns - 1)) / columns;
    const height = width * .75;
    let visibleIndex = 0;
    cards.forEach(card => {{
      const visible = currentFilter === "all" || card.dataset.tags.split("|").includes(currentFilter);
      card.style.width = width + "px";
      card.style.height = height + "px";
      if (visible) {{
        const column = visibleIndex % columns;
        const row = Math.floor(visibleIndex / columns);
        const x = column * (width + gap);
        const y = row * (height + gap);
        card.dataset.x = x;
        card.dataset.y = y;
        card.classList.remove("isotope-hidden");
        card.style.transform = "translate3d(" + x + "px," + y + "px,0) scale(1)";
        visibleIndex += 1;
      }} else {{
        const x = Number(card.dataset.x || 0);
        const y = Number(card.dataset.y || 0);
        card.classList.add("isotope-hidden");
        card.style.transform = "translate3d(" + x + "px," + y + "px,0) scale(.001)";
      }}
    }});
    const rows = Math.ceil(visibleIndex / columns);
    grid.style.height = (rows ? rows * height + (rows - 1) * gap : 0) + "px";
  }};
  layout();
  requestAnimationFrame(() => requestAnimationFrame(() => grid.classList.remove("isotope-no-transition")));
  buttons.forEach(button => button.addEventListener("click", event => {{
    event.preventDefault();
    currentFilter = button.dataset.filter;
    buttons.forEach(item => item.classList.toggle("active", item === button));
    layout();
  }}));
  let resizeTimer;
  window.addEventListener("resize", () => {{
    clearTimeout(resizeTimer);
    resizeTimer = setTimeout(layout, 80);
  }});
  if (reducedMotion) grid.classList.add("isotope-no-transition");
}});
</script>'''

def projects():
    robot_items = [{**item, "tags": ["Robot"]} for item in PROJECTS]
    course_items = [{**item, "tags": ["Course"]} for item in COURSES]
    note_items = [{**item, "tags": ["Notes"]} for item in NOTES]
    all_items=robot_items+course_items+note_items
    return layout("Projects","Projects",f'<section class="page-intro"><h1>Projects</h1><p>Selected research projects, course projects, and study notes.</p></section>{filters(all_items)}<section class="portfolio-grid">{grid_cards(all_items)}</section>')

def collection(title,desc,items,extra_tags=None):
    return layout(title,title if title == "Lifes" else "",f'<section class="page-intro"><h1>{title}</h1><p>{desc}</p></section>{filters(items, extra_tags)}<section class="portfolio-grid">{grid_cards(items)}</section>')

def reliable_grasp():
    project = next(item for item in PROJECTS if item.get("url") == "reliable_grasp/")
    labels = ["Top-view yellow target", "Top-view blue target", "Top-view white target", "Top-view black target", "FR3 grasping scene A", "FR3 grasping scene B", "Full workspace scene"]
    demos = []
    for index, label in enumerate(labels, 1):
        demos.append(f'''<article class="demo-card"><video class="autoplay-demo" autoplay loop muted playsinline preload="metadata" poster="../assets/content/projects/reliable_grasp/demo_{index:02d}.jpg"><source src="../assets/content/projects/reliable_grasp/demo_{index:02d}.mp4" type="video/mp4">Your browser does not support the video tag.</video><span>{e(label)}</span></article>''')
    tags = "".join(f"<span>{e(tag)}</span>" for tag in project.get("tags", []))
    body = f'''<link rel="stylesheet" href="../assets/project-detail.css?v=1">
<section class="project-hero"><p class="project-kicker"><a href="../projects.html">← Projects</a></p><h1>{e(project["title"])}</h1><p class="project-lead">{e(project["description"])}</p><div class="project-meta"><span>{e(project["period"])}</span><span aria-hidden="true">|</span><span>YOLO11 + pi_0.5</span><span aria-hidden="true">|</span><span>FR3 Robot</span></div><div class="project-tags">{tags}</div></section>
<section class="project-section"><div class="project-heading"><p>Demonstrations</p><h2>Reliable grasping across objects and viewpoints</h2></div><div class="demo-grid">{"".join(demos)}</div></section>
<section class="project-section"><div class="project-heading"><p>Results</p><h2>Segmentation and progress comparison</h2></div><div class="result-grid"><figure><img src="../assets/content/projects/reliable_grasp/chart_segmentation.png" alt="Segmentation result comparison chart"><figcaption>Figure 8. Segmentation Results</figcaption></figure><figure><img src="../assets/content/projects/reliable_grasp/chart_progress.png" alt="Progress comparison chart"><figcaption>Figure 9. Progress Comparison</figcaption></figure></div></section>
<section class="project-section"><div class="project-heading"><p>System</p><h2>Goal-conditioned grasping architecture</h2></div><figure class="architecture-figure"><img src="../assets/content/projects/reliable_grasp/system_architecture.png" alt="Goal-conditioned grasping system architecture"><figcaption>System Architecture</figcaption></figure></section>
<script>document.querySelectorAll(".autoplay-demo").forEach(video=>{{video.muted=true;video.play().catch(()=>{{}})}});</script>'''
    return layout("Reliable Grasp", "Projects", body, "../")

def build():
    life_items = sorted(
        enumerate(LIFE_RECORDS),
        key=lambda pair: (pair[1].get("date", ""), -pair[0]),
        reverse=True,
    )
    life_items = [item for _, item in life_items]
    outputs={"index.html":home(),"research.html":research(),"experience.html":experience(),"projects.html":projects(),"notes.html":collection("Notes","Technical notes, reading summaries, and course records.",NOTES+COURSES),"life.html":collection("Lifes","A visual archive of moments beyond research.",life_items,["Photo","Social","Hobby","Travel"]),"reliable_grasp/index.html":reliable_grasp()}
    for path,text in outputs.items(): (ROOT/path).write_text(text,encoding="utf-8")
    print("Built:",", ".join(outputs))

if __name__=="__main__": build()
