# ZhongchunChen.github.io

Personal academic website for Zhongchun Chen.

## Quick Start

```bash
conda activate github_io
python build_site.py
python -m http.server 8000
```

Open `http://localhost:8000` to preview the site.

Important rule: `build_site.py` only reads `site_data.py` for visible Note/Life entries. Files placed under `assets/`, `notes/`, or `life/` will not be shown automatically. You must add the corresponding item in `site_data.py`.

## 中文说明

### 内容配置入口

网站内容主要通过 `site_data.py` 控制：

- `SITE`：个人简介、邮箱、GitHub、Scholar、人像、研究兴趣
- `PUBLICATIONS`：论文
- `PROJECTS`：项目
- `REWARDS`：奖项
- `EDUCATION`：教育经历
- `EXPERIENCE`：实习经历
- `NOTES`：Note 页面条目
- `COURSES`：SJTU 课程内容，会显示在 Note 页面
- `LIFE_RECORDS`：Life 页面条目

修改配置后运行：

```bash
conda activate github_io
python build_site.py
```

### 修改个人简介

修改 `site_data.py` 中的 `SITE`：

```python
SITE = {
    "name": "Zhongchun Chen",
    "role": "Undergraduate Researcher",
    "affiliation": "Shanghai Jiao Tong University",
    "location": "Shanghai, China",
    "email": "your.email@sjtu.edu.cn",
    "github": "https://github.com/ZhongchunChen",
    "scholar": "#",
    "avatar": "assets/img/profile.jpg",
    "intro": "Your English self-introduction.",
    "interests": ["Robot Learning", "Generative Model"],
}
```

人像图片放到 `assets/img/`，然后修改 `"avatar"` 路径。

### 添加 Publication / Project / Reward

Publication：

```python
{
    "title": "Paper Title",
    "authors": "Zhongchun Chen, ...",
    "venue": "Conference / Journal, Year",
    "description": "One short paragraph about the paper.",
    "image": "assets/img/my-paper-teaser.gif",
    "links": {"paper": "https://...", "code": "https://..."},
    "tags": ["publication", "rl"],
}
```

Project：

```python
{
    "title": "Project Title",
    "period": "2025 - Present",
    "description": "Project summary.",
    "image": "assets/img/my-project-demo.gif",
    "links": {"demo": "https://...", "code": "https://..."},
    "tags": ["robotics", "rl"],
}
```

Reward：

```python
{
    "title": "Award Name",
    "date": "2025",
    "description": "Short award description.",
}
```

### 添加 Note

Note 页面只显示 `site_data.py` 中 `NOTES` 和 `COURSES` 的内容。添加一个 Note 时，在 `NOTES` 中追加：

```python
{
    "title": "Flow-Matching Note",
    "date": "2026-05-19",
    "summary": "flow matching and diffusion generative model's mathematical principles.",
    "image": "assets/img/project-rl.svg",
    "tags": ["flow matching", "learning-note"],
    "url": "notes/flow-matching-note.html",
}
```

新 label 的添加方式：直接在 `tags` 里写新的字符串。筛选按钮会根据 `tags` 自动生成。

### 添加 Life

Life 页面只显示 `site_data.py` 中 `LIFE_RECORDS` 的内容。添加一个 Life record 时，在 `LIFE_RECORDS` 中追加：

```python
{
    "title": "Campus Memory",
    "date": "2025-10-08",
    "summary": "A short life record.",
    "image": "assets/img/campus-memory.jpg",
    "tags": ["campus", "life"],
    "url": "life/campus-memory.html",
}
```

### 上传图片 / GIF

把本地图片或 GIF 放到 `assets/img/`，例如：

```text
assets/img/flow-cover.png
assets/img/demo.gif
```

然后在 `site_data.py` 对应条目的 `image` 字段中引用：

```python
"image": "assets/img/flow-cover.png"
```

支持常见格式：`.jpg`, `.jpeg`, `.png`, `.gif`, `.webp`, `.svg`。

### 使用 PDF 或 HTML

PDF 和 HTML 不需要转换器。把文件放到 `notes/` 或 `life/`，然后在 `site_data.py` 的 `url` 字段手动引用。

例如：

```text
notes/flow_matching_note.pdf
life/campus-memory.html
```

配置：

```python
"url": "notes/flow_matching_note.pdf"
```

或者：

```python
"url": "life/campus-memory.html"
```

### 使用 Markdown 转换器

如果你本地只有 `.md` 文件，先把它放到 `assets/content/notes/` 或 `assets/content/life/` 作为源文件保存。然后手动运行转换器。

Note 示例：

```bash
conda activate github_io
python content_converter.py assets/content/notes/flow-matching-note.md --collection notes
```

Life 示例：

```bash
conda activate github_io
python content_converter.py assets/content/life/campus-memory.md --collection life
```

转换器会：

- 只处理 `.md`
- 输出 HTML 到 `notes/` 或 `life/`
- 在终端打印一段 `site_data.py` 配置片段
- 不会自动修改 `site_data.py`
- 不会自动把内容加入 Note/Life 页面

Markdown 文件推荐写 front matter：

```markdown
---
title: Flow-Matching Note
date: 2026-05-19
summary: flow matching and diffusion generative model's mathematical principles.
tags: flow matching, learning-note
image: assets/img/project-rl.svg
---

# Flow-Matching Note

Your Markdown content here.
```

转换后，把终端打印出来的配置复制到 `site_data.py` 的 `NOTES` 或 `LIFE_RECORDS` 中，然后运行：

```bash
python build_site.py
```

## English Guide

### Content Configuration

The site is configured through `site_data.py`:

- `SITE`: profile, email, GitHub, Scholar, portrait, interests
- `PUBLICATIONS`: papers
- `PROJECTS`: projects
- `REWARDS`: awards
- `EDUCATION`: education
- `EXPERIENCE`: internships
- `NOTES`: Note page entries
- `COURSES`: SJTU course entries shown on the Note page
- `LIFE_RECORDS`: Life page entries

After editing:

```bash
conda activate github_io
python build_site.py
```

### Add Notes

The Note page only shows entries configured in `NOTES` and `COURSES` in `site_data.py`.

```python
{
    "title": "Flow-Matching Note",
    "date": "2026-05-19",
    "summary": "flow matching and diffusion generative model's mathematical principles.",
    "image": "assets/img/project-rl.svg",
    "tags": ["flow matching", "learning-note"],
    "url": "notes/flow-matching-note.html",
}
```

New labels are added through the `tags` list.

### Add Life Records

The Life page only shows entries configured in `LIFE_RECORDS`.

```python
{
    "title": "Campus Memory",
    "date": "2025-10-08",
    "summary": "A short life record.",
    "image": "assets/img/campus-memory.jpg",
    "tags": ["campus", "life"],
    "url": "life/campus-memory.html",
}
```

### Images And GIFs

Place images or GIFs under `assets/img/`, then reference them in the `image` field:

```python
"image": "assets/img/flow-cover.png"
```

### PDF Or HTML Content

PDF and HTML files do not need conversion. Put them under `notes/` or `life/`, then manually reference them in `site_data.py`:

```python
"url": "notes/flow_matching_note.pdf"
```

### Markdown Converter

If you have a `.md` file, keep the source under `assets/content/notes/` or `assets/content/life/`, then convert it manually.

For Note:

```bash
conda activate github_io
python content_converter.py assets/content/notes/flow-matching-note.md --collection notes
```

For Life:

```bash
conda activate github_io
python content_converter.py assets/content/life/campus-memory.md --collection life
```

The converter:

- only supports `.md`
- writes HTML into `notes/` or `life/`
- prints a `site_data.py` snippet
- does not modify `site_data.py`
- does not auto-add anything to Note/Life pages

Recommended Markdown front matter:

```markdown
---
title: Flow-Matching Note
date: 2026-05-19
summary: flow matching and diffusion generative model's mathematical principles.
tags: flow matching, learning-note
image: assets/img/project-rl.svg
---

# Flow-Matching Note

Your Markdown content here.
```

After conversion, paste the printed item into `NOTES` or `LIFE_RECORDS`, then run:

```bash
python build_site.py
```

## Publish

```bash
git add .
git commit -m "Update personal website"
git push
```
