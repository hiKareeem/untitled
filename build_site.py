#!/usr/bin/env python3
"""Build Docsify site from manuscript files and AEGIS chapter sources.

Usage: python build_site.py

Splits manuscript-book{1,2,3}.md into individual chapter pages,
extracts AEGIS special chapters from source files, and generates
a complete Docsify site in the docs/ directory.

For GitHub Pages: push to main, set Pages source to /docs.
Preview locally:  npx docsify-cli serve docs
"""

import re
import shutil
from pathlib import Path

ROOT = Path(__file__).parent
DOCS = ROOT / "docs"
MANUSCRIPTS = ROOT / "_bmad-output"
CHAPTERS_BASE = ROOT / "_bmad-output" / "bbb-project"

AEGIS_CHAPTERS = {
    2: [
        {
            "source": CHAPTERS_BASE / "book-2" / "chapters" / "book2-aegis-blackweir.md",
            "filename": "aegis-i",
            "display": "AEGIS I: Unfired",
        }
    ],
    3: [
        {
            "source": CHAPTERS_BASE / "book-3" / "chapters" / "book3-aegis-ending.md",
            "filename": "aegis-terminus",
            "display": "AEGIS Terminus: The Last Observer",
        }
    ],
}


def split_manuscript(manuscript_path):
    """Split a manuscript file into individual chapters.

    Returns a list of dicts: {filename, display, content}
    """
    content = manuscript_path.read_text(encoding="utf-8")

    # Split on H1 headings (# at start of line)
    chunks = re.split(r"^(?=# )", content, flags=re.MULTILINE)

    chapters = []
    for chunk in chunks:
        chunk = chunk.strip()
        if not chunk:
            continue

        lines = chunk.split("\n")
        heading = lines[0]

        # Extract subtitle (## line) from first few lines
        subtitle = ""
        for line in lines[1:6]:
            m = re.match(r"^## (.+)$", line)
            if m:
                subtitle = m.group(1)
                break

        if heading.startswith("# Prologue"):
            filename = "prologue"
            display = f"Prologue: {subtitle}" if subtitle else "Prologue"
        elif heading.startswith("# Epilogue"):
            m = re.match(r"# Epilogue:?\s*(.+)", heading)
            if m and m.group(1).strip():
                display = f"Epilogue: {m.group(1).strip()}"
            elif subtitle:
                display = f"Epilogue: {subtitle}"
            else:
                display = "Epilogue"
            filename = "epilogue"
        elif heading.startswith("# Chapter"):
            m = re.match(r"# Chapter (\d+)", heading)
            if not m:
                continue
            num = int(m.group(1))
            filename = f"chapter-{num:02d}"
            display = f"Chapter {num}: {subtitle}" if subtitle else f"Chapter {num}"
        else:
            continue

        chapters.append(
            {
                "filename": filename,
                "display": display,
                "content": chunk,
            }
        )

    return chapters


def extract_aegis_chapter(source_path):
    """Extract clean prose from an AEGIS chapter source file.

    Strips YAML frontmatter and HTML comments. Returns clean markdown.
    """
    content = source_path.read_text(encoding="utf-8")

    # Extract title from frontmatter
    title = "AEGIS"
    fm_match = re.match(r"^---\n(.*?)\n---\n", content, re.DOTALL)
    if fm_match:
        fm = fm_match.group(1)
        t = re.search(r"title:\s*['\"]?(.+?)['\"]?\s*$", fm, re.MULTILINE)
        if t:
            title = t.group(1)
        content = content[fm_match.end() :]

    # Remove HTML comments
    content = re.sub(r"<!--.*?-->", "", content, flags=re.DOTALL)

    # Clean up leading separators
    content = content.strip()
    content = re.sub(r"^---\s*", "", content)
    content = content.strip()

    # Add title heading
    content = f"# {title}\n\n---\n\n{content}"

    # Collapse excessive blank lines
    content = re.sub(r"\n{3,}", "\n\n", content)

    return content


def build_landing_page():
    """Generate docs/README.md with book links + original README content."""
    readme_content = (ROOT / "README.md").read_text(encoding="utf-8")

    landing = """# Untitled

**Read Online:**

- **[Book 1](book-1/prologue)** — Prologue through Epilogue
- **[Book 2](book-2/chapter-01)** — Chapters 1–53 + AEGIS I
- **[Book 3](book-3/chapter-01)** — Chapters 1–53 + AEGIS Terminus

---

"""
    return landing + readme_content


def build_sidebar(all_books):
    """Generate the single _sidebar.md with all books and chapters."""
    lines = ["- [Home](/)\n"]

    for book_num, chapters in sorted(all_books.items()):
        lines.append(f"- **Book {book_num}**\n")
        for ch in chapters:
            lines.append(
                f"  - [{ch['display']}](book-{book_num}/{ch['filename']})\n"
            )

    return "".join(lines)


INDEX_HTML = """\
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Untitled</title>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet"
        href="https://cdn.jsdelivr.net/npm/docsify-themeable@0/dist/css/theme-simple-dark.min.css">
  <style>
    :root {
      --base-font-size: 18px;
      --base-line-height: 1.8;
      --content-max-width: 48em;
      --sidebar-width: 18rem;
    }
    .sidebar-nav > ul > li > p {
      font-weight: bold;
      margin: 1em 0 0.5em;
      color: #ccc;
    }
    .markdown-section blockquote {
      border-left: 3px solid #555;
      padding-left: 1em;
      color: #999;
      font-style: italic;
    }
    .markdown-section hr {
      margin: 2em 0;
      border: none;
      border-top: 1px solid #333;
    }
    .docsify-pagination-container {
      margin-top: 3em;
      border-top: 1px solid #333;
      padding-top: 1em;
    }
  </style>
</head>
<body>
  <div id="app">Loading...</div>
  <script>
    window.$docsify = {
      name: 'Untitled',
      loadSidebar: true,
      subMaxLevel: 1,
      auto2top: true,
      search: {
        placeholder: 'Search',
        noData: 'No results',
        depth: 3,
      },
      pagination: {
        previousText: 'Previous Chapter',
        nextText: 'Next Chapter',
        crossChapter: true,
        crossChapterText: true,
      },
    };
  </script>
  <script src="https://cdn.jsdelivr.net/npm/docsify@4/lib/docsify.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/docsify-pagination@2/dist/docsify-pagination.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/docsify@4/lib/plugins/search.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/docsify-sidebar-collapse/dist/docsify-sidebar-collapse.min.js"></script>
</body>
</html>
"""


def main():
    print("Building Docsify site...\n")

    if DOCS.exists():
        shutil.rmtree(DOCS)
    DOCS.mkdir(parents=True)

    all_books = {}

    for book_num in [1, 2, 3]:
        manuscript = MANUSCRIPTS / f"manuscript-book{book_num}.md"
        book_dir = DOCS / f"book-{book_num}"
        book_dir.mkdir(parents=True)

        if not manuscript.exists():
            print(f"  WARNING: {manuscript} not found, skipping")
            all_books[book_num] = []
            continue

        print(f"Book {book_num}: splitting {manuscript.name}...")
        chapters = split_manuscript(manuscript)

        for ch in chapters:
            out = book_dir / f"{ch['filename']}.md"
            out.write_text(ch["content"], encoding="utf-8")

        print(f"  {len(chapters)} chapters from manuscript")

        # AEGIS chapters (not in manuscripts)
        for aegis in AEGIS_CHAPTERS.get(book_num, []):
            src = aegis["source"]
            if src.exists():
                content = extract_aegis_chapter(src)
                out = book_dir / f"{aegis['filename']}.md"
                out.write_text(content, encoding="utf-8")
                chapters.append(
                    {"filename": aegis["filename"], "display": aegis["display"]}
                )
                print(f"  + {aegis['display']} (from {src.name})")
            else:
                print(f"  ! Missing: {src}")

        all_books[book_num] = chapters

    # Write site files
    (DOCS / ".nojekyll").touch()
    (DOCS / "index.html").write_text(INDEX_HTML, encoding="utf-8")
    (DOCS / "README.md").write_text(build_landing_page(), encoding="utf-8")
    (DOCS / "_sidebar.md").write_text(build_sidebar(all_books), encoding="utf-8")

    total = sum(len(chs) for chs in all_books.values())
    print(f"\nDone. {total} total chapters written to {DOCS}")
    print(f"\nPreview:       npx docsify-cli serve docs")
    print(f"GitHub Pages:  push to main, set source to /docs")


if __name__ == "__main__":
    main()
