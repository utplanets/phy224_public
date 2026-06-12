#!/usr/bin/env python3
"""
Convert Quarto callout blocks in .ipynb files to HTML alert/details elements.

Usage:
    python3 fix_callouts.py episodes/basics.ipynb
    python3 fix_callouts.py episodes/          # all .ipynb in directory
"""

import json
import re
import sys
from pathlib import Path

import yaml

ALERT_CLASS = {
    'note':      'alert-info',
    'tip':       'alert-success',
    'caution':   'alert-warning',
    'warning':   'alert-warning',
    'important': 'alert-danger',
}

OPEN_RE  = re.compile(r'^(:{3,})\s*\{\.callout-(\w+)(.*?)\}\s*$')
CLOSE_RE = re.compile(r'^(:{3,})\s*$')


def parse_blocks(lines):
    """Return a list of segments: either {'type':'line','text':str}
    or {'type':'callout', 'kind':str, 'collapse':bool, 'title':str|None, 'body':[lines]}."""
    segments = []
    i = 0
    while i < len(lines):
        m = OPEN_RE.match(lines[i])
        if m:
            fence_len = len(m.group(1))
            kind      = m.group(2)
            attrs     = m.group(3)
            collapse  = 'collapse="true"' in attrs
            i += 1
            body = []
            depth = 1
            while i < len(lines) and depth > 0:
                cm = CLOSE_RE.match(lines[i])
                om = OPEN_RE.match(lines[i])
                if cm and len(cm.group(1)) == fence_len:
                    depth -= 1
                    if depth > 0:
                        body.append(lines[i])
                elif om and len(om.group(1)) == fence_len:
                    depth += 1
                    body.append(lines[i])
                else:
                    body.append(lines[i])
                i += 1
            # Pull out the first ## heading as the callout title
            title = None
            trimmed = []
            found_title = False
            for line in body:
                if not found_title and line.startswith('## '):
                    title = line[3:].rstrip('\n')
                    found_title = True
                else:
                    trimmed.append(line)
            segments.append({'type': 'callout', 'kind': kind,
                              'collapse': collapse, 'title': title,
                              'body': trimmed})
        else:
            segments.append({'type': 'line', 'text': lines[i]})
            i += 1
    return segments


def render_segments(segments):
    parts = []
    for seg in segments:
        if seg['type'] == 'line':
            parts.append(seg['text'])
        else:
            parts.append(render_callout(seg))
    return ''.join(parts)


def render_callout(seg):
    kind     = seg['kind']
    title    = seg['title'] or kind.capitalize()
    css      = ALERT_CLASS.get(kind, 'alert-secondary')
    # Recursively convert any nested callouts in the body
    inner = render_segments(parse_blocks(seg['body']))
    # Strip leading blank line inside block
    inner = inner.lstrip('\n')

    if seg['collapse']:
        return (
            '<details>\n'
            f'<summary><b>{title}</b></summary>\n\n'
            f'{inner}'
            '</details>\n'
        )
    return (
        f'<div class="alert alert-block {css}">\n'
        f'<b>{title}</b>\n\n'
        f'{inner}'
        '</div>\n'
    )


ORPHAN_FENCE_RE = re.compile(r'^:{3,}\s*$', re.MULTILINE)


def strip_orphan_fences(text):
    """Remove bare ::: lines left behind when quarto convert split a code block
    out of a callout, along with any run of 3+ blank lines they leave."""
    cleaned = ORPHAN_FENCE_RE.sub('', text)
    # Collapse runs of 3+ blank lines down to two
    cleaned = re.sub(r'\n{4,}', '\n\n\n', cleaned)
    return cleaned


def convert_source(source_list):
    """source_list: list[str] from ipynb cell. Returns new list[str]."""
    joined = ''.join(source_list)
    has_open  = bool(re.search(r'^:{3,}\s*\{\.callout-', joined, re.MULTILINE))
    has_close = bool(ORPHAN_FENCE_RE.search(joined))
    if not has_open and not has_close:
        return source_list

    lines = joined.splitlines(keepends=True)
    segs = parse_blocks(lines)
    new_text = render_segments(segs)
    new_text = strip_orphan_fences(new_text)

    # Reserialise as a list of lines the way Jupyter stores them
    new_lines = new_text.splitlines(keepends=True)
    return new_lines


YAML_FRONT_RE = re.compile(r'\A---\n(.*?\n)---\n', re.DOTALL)


def extract_yaml_title(nb):
    """If the first markdown cell starts with a YAML front matter block,
    remove it, set nb['metadata']['title'], and return the title string.
    Returns None if no front matter found."""
    if not nb['cells']:
        return None
    cell = nb['cells'][0]
    if cell['cell_type'] != 'markdown':
        return None
    source = ''.join(cell['source'])
    m = YAML_FRONT_RE.match(source)
    if not m:
        return None

    front = yaml.safe_load(m.group(1)) or {}
    title = front.get('title', '').strip('"').strip("'")

    # Remove the YAML block from the cell source
    remainder = source[m.end():].lstrip('\n')
    cell['source'] = remainder.splitlines(keepends=True)

    # Store title in notebook metadata
    nb['metadata']['title'] = title
    return title


def process_notebook(path: Path):
    nb = json.loads(path.read_text())
    changed = False

    title = extract_yaml_title(nb)
    if title:
        # Insert a standalone title cell at position 0
        nb['cells'].insert(0, {
            'cell_type': 'markdown',
            'metadata': {},
            'source': [f'# {title}'],
        })
        changed = True

    for cell in nb['cells']:
        if cell['cell_type'] != 'markdown':
            continue
        new_source = convert_source(cell['source'])
        if new_source != cell['source']:
            cell['source'] = new_source
            changed = True

    if changed:
        path.write_text(json.dumps(nb, indent=1, ensure_ascii=False) + '\n')
        print(f'updated  {path}')
    else:
        print(f'no change {path}')


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    target = Path(sys.argv[1])
    if target.is_dir():
        notebooks = sorted(target.glob('*.ipynb'))
    else:
        notebooks = [target]

    for nb_path in notebooks:
        process_notebook(nb_path)


if __name__ == '__main__':
    main()
