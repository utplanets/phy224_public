#!/usr/bin/env python3
"""Convert Sandpaper-style Carpentry markdown to Quarto .qmd files."""

import re
import sys
from pathlib import Path

CALLOUT_MAP = {
    "questions":   ("callout-note",      "Questions"),
    "objectives":  ("callout-note",      "Objectives"),
    "keypoints":   ("callout-tip",       "Key Points"),
    "challenge":   ("callout-caution",   "Challenge"),
    "solution":    ("callout-note",      "Solution"),
    "callout":     ("callout-note",      None),
    "prereq":      ("callout-important", "Prerequisites"),
    "discussion":  ("callout-note",      "Discussion"),
    "checklist":   ("callout-note",      "Checklist"),
    "warning":     ("callout-warning",   "Warning"),
    "tab":         ("panel-tabset",      None),
}

OPEN_DIV  = re.compile(r'^:{3,}\s+(\w[\w-]*)\s*$')
CLOSE_DIV = re.compile(r'^:{3,}\s*$')


def convert_frontmatter(fm: str, filename: str, is_index: bool) -> str:
    lines = fm.strip().splitlines()
    kept = []
    for line in lines:
        if line.startswith("site:"):
            continue
        if line.startswith("teaching:") or line.startswith("exercises:"):
            continue
        kept.append(line)
    if is_index and not any(l.startswith("title:") for l in kept):
        kept.insert(0, 'title: "PHY224 Python Review"')
    return "---\n" + "\n".join(kept) + "\n---"


def open_callout(div_type: str) -> str:
    if div_type not in CALLOUT_MAP:
        return f"::: {{{div_type}}}"
    kind, title = CALLOUT_MAP[div_type]
    if kind == "panel-tabset":
        return "::: {.panel-tabset}"
    attrs = f".{kind}"
    if div_type == "solution":
        attrs += ' collapse="true"'
    if title:
        attrs += f' title="{title}"'
    return f"::: {{{attrs}}}"


def convert_body(lines: list[str]) -> list[str]:
    out = []
    stack: list[str] = []

    for line in lines:
        stripped = line.rstrip()

        m_open = OPEN_DIV.match(stripped)
        if m_open:
            div_type = m_open.group(1).lower()
            stack.append(div_type)
            out.append(open_callout(div_type))
            continue

        if CLOSE_DIV.match(stripped) and stripped:
            if stack:
                stack.pop()
            out.append(":::")
            continue

        out.append(stripped)

    return out


def convert_file(src: Path, dst: Path, is_index: bool = False) -> None:
    text = src.read_text(encoding="utf-8")

    # Split frontmatter
    if text.startswith("---"):
        end = text.index("---", 3)
        fm_raw = text[3:end].strip()
        body_raw = text[end + 3:].lstrip("\n")
    else:
        fm_raw = ""
        body_raw = text

    fm = convert_frontmatter(fm_raw, src.name, is_index)
    body_lines = convert_body(body_raw.splitlines())
    body = "\n".join(body_lines)

    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_text(fm + "\n\n" + body + "\n", encoding="utf-8")
    print(f"  {src.name} -> {dst.relative_to(dst.parent.parent.parent)}")


if __name__ == "__main__":
    src_root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(".")
    dst_root = Path(sys.argv[2]) if len(sys.argv) > 2 else Path("quarto-site")

    # index
    convert_file(src_root / "index.md", dst_root / "index.qmd", is_index=True)

    # episodes
    for f in (src_root / "episodes").glob("*.md"):
        convert_file(f, dst_root / "episodes" / (f.stem + ".qmd"))

    # learners
    for f in (src_root / "learners").glob("*.md"):
        convert_file(f, dst_root / "learners" / (f.stem + ".qmd"))

    # instructors
    for f in (src_root / "instructors").glob("*.md"):
        convert_file(f, dst_root / "instructors" / (f.stem + ".qmd"))

    print("Done.")
