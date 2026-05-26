from __future__ import annotations

import argparse
import re
from datetime import datetime
from html import escape
from pathlib import Path


ROOT = Path(__file__).parent


def slugify(value: str) -> str:
    slug = re.sub(r"[^A-Za-z0-9._-]+", "-", value.strip()).strip("-").lower()
    return slug or "untitled"


def parse_front_matter(text: str) -> tuple[dict[str, str], str]:
    if not text.startswith("---\n"):
        return {}, text
    end = text.find("\n---\n", 4)
    if end == -1:
        return {}, text

    meta: dict[str, str] = {}
    for line in text[4:end].splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        meta[key.strip().lower()] = value.strip().strip('"').strip("'")
    return meta, text[end + 5 :]


def inline_markdown(text: str) -> str:
    text = escape(text)
    text = re.sub(r"`([^`]+)`", r"<code>\1</code>", text)
    text = re.sub(r"!\[([^\]]*)\]\(([^)]+)\)", r'<img src="\2" alt="\1">', text)
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"\*([^*]+)\*", r"<em>\1</em>", text)
    return text


def markdown_to_html(markdown: str) -> str:
    lines = markdown.splitlines()
    html: list[str] = []
    paragraph: list[str] = []
    in_list = False
    in_code = False
    code_lines: list[str] = []

    def flush_paragraph() -> None:
        nonlocal paragraph
        if paragraph:
            html.append(f"<p>{inline_markdown(' '.join(paragraph))}</p>")
            paragraph = []

    def close_list() -> None:
        nonlocal in_list
        if in_list:
            html.append("</ul>")
            in_list = False

    for line in lines:
        stripped = line.strip()
        if stripped.startswith("```"):
            if in_code:
                html.append(f"<pre><code>{escape(chr(10).join(code_lines))}</code></pre>")
                code_lines = []
                in_code = False
            else:
                flush_paragraph()
                close_list()
                in_code = True
            continue
        if in_code:
            code_lines.append(line)
            continue
        if not stripped:
            flush_paragraph()
            close_list()
            continue
        if stripped.startswith("#"):
            flush_paragraph()
            close_list()
            level = min(len(stripped) - len(stripped.lstrip("#")), 3)
            title = stripped[level:].strip()
            html.append(f"<h{level}>{inline_markdown(title)}</h{level}>")
            continue
        if stripped.startswith(("- ", "* ")):
            flush_paragraph()
            if not in_list:
                html.append("<ul>")
                in_list = True
            html.append(f"<li>{inline_markdown(stripped[2:].strip())}</li>")
            continue
        paragraph.append(stripped)

    flush_paragraph()
    close_list()
    if in_code:
        html.append(f"<pre><code>{escape(chr(10).join(code_lines))}</code></pre>")
    return "\n".join(html)


def content_page(title: str, body: str, css_prefix: str = "../") -> str:
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{escape(title)}</title>
  <link rel="stylesheet" href="{css_prefix}assets/style.css">
</head>
<body>
  <main class="content-page">
    <a class="text-link" href="../index.html">Home</a>
    <article class="content-body">
      {body}
    </article>
  </main>
</body>
</html>
"""


def infer_output_path(source: Path, collection: str | None) -> Path:
    if collection is None:
        parts = source.parts
        if "notes" in parts:
            collection = "notes"
        elif "life" in parts:
            collection = "life"
        else:
            collection = "notes"
    return ROOT / collection / f"{slugify(source.stem)}.html"


def convert_markdown(source: Path, output: Path) -> dict[str, str]:
    if source.suffix.lower() != ".md":
        raise ValueError("Only .md files are supported by this converter.")

    raw = source.read_text(encoding="utf-8")
    meta, markdown = parse_front_matter(raw)
    title = meta.get("title") or source.stem.replace("-", " ").replace("_", " ").title()
    body = markdown_to_html(markdown)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(content_page(title, body), encoding="utf-8")

    relative_url = output.relative_to(ROOT).as_posix()
    collection = "life" if output.parts[-2] == "life" else "note"
    default_image = "assets/img/life-record.svg" if collection == "life" else "assets/img/project-notes.svg"
    return {
        "title": title,
        "date": meta.get("date") or datetime.fromtimestamp(source.stat().st_mtime).strftime("%Y-%m-%d"),
        "summary": meta.get("summary") or meta.get("description") or f"Converted from {source.name}.",
        "image": meta.get("image") or default_image,
        "tags": meta.get("tags") or ("life" if collection == "life" else "learning-note"),
        "url": relative_url,
    }


def print_site_data_snippet(meta: dict[str, str], collection: str) -> None:
    target = "LIFE_RECORDS" if collection == "life" else "NOTES"
    tags = [tag.strip() for tag in meta["tags"].split(",") if tag.strip()]
    print(f"\nAdd this item manually to {target} in site_data.py:\n")
    print("{")
    print(f'    "title": "{meta["title"]}",')
    print(f'    "date": "{meta["date"]}",')
    print(f'    "summary": "{meta["summary"]}",')
    print(f'    "image": "{meta["image"]}",')
    print(f'    "tags": {tags!r},')
    print(f'    "url": "{meta["url"]}",')
    print("},")


def main() -> None:
    parser = argparse.ArgumentParser(description="Convert one Markdown file to HTML for the personal website.")
    parser.add_argument("source", help="Path to a .md file.")
    parser.add_argument("-o", "--output", help="Output .html path. Defaults to notes/<filename>.html or life/<filename>.html.")
    parser.add_argument("--collection", choices=["notes", "life"], help="Target collection when output is omitted.")
    args = parser.parse_args()

    source = Path(args.source)
    if not source.is_absolute():
        source = ROOT / source
    output = Path(args.output) if args.output else infer_output_path(source, args.collection)
    if not output.is_absolute():
        output = ROOT / output

    meta = convert_markdown(source, output)
    collection = "life" if output.parent.name == "life" else "notes"
    print(f"Converted: {source.relative_to(ROOT)} -> {output.relative_to(ROOT)}")
    print_site_data_snippet(meta, "life" if collection == "life" else "notes")


if __name__ == "__main__":
    main()
