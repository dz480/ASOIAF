#!/usr/bin/env python3
"""Validate existing ROM document links and POV-to-chapter navigation."""
from __future__ import annotations

from collections import Counter
from pathlib import Path
from urllib.parse import unquote, urlsplit
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
CSRM = ROOT / "ROM_CSRM_AGOT.md"
INDEX = ROOT / "README.md"
MCM = ROOT / "ROM_MCM_AGOT.md"
LINK = re.compile(r'(?<!!)\[[^\]\n]+\]\(([^)\s]+)(?:\s+[^)]*)?\)')
HTML_HREF = re.compile(r'<a\b[^>]*\bhref=["\']([^"\']+)["\']', re.I)
EXPLICIT = re.compile(r'<a\b[^>]*\bid=["\']([^"\']+)["\']', re.I)
HEADING = re.compile(r'^#{1,6}\s+(.+?)\s*#*\s*$', re.M)
CHAPTER = re.compile(r'^### GOT Ch\. (\d+): (\w+) ([IVXLCDM]+)\s*$', re.M)
SCOPE = re.compile(r'^\*\*Scope:\*\*\s+\*\*GOT Ch\. ([\d,\s]+)\*\*', re.M)
FULL_POV_NAMES = {
    "Bran": "Bran Stark",
    "Catelyn": "Catelyn Stark",
    "Daenerys": "Daenerys Targaryen",
    "Eddard": "Eddard Stark",
}
errors = []


def fail(message: str) -> None:
    errors.append(message)


def git_slug(value: str) -> str:
    value = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', value)
    value = re.sub(r'<[^>]*>', '', value).lower().strip()
    value = re.sub(r'[^\w\s-]', '', value, flags=re.UNICODE)
    return re.sub(r'\s', '-', value)


def anchors(text: str, label: str) -> set[str]:
    ids = EXPLICIT.findall(text)
    counts = Counter(ids)
    for name, qty in counts.items():
        if qty > 1:
            fail(f"{label}: duplicate explicit anchor {name}")
    seen = Counter()
    for heading in HEADING.findall(text):
        slug = git_slug(heading)
        if slug:
            suffix = seen[slug]
            ids.append(slug if not suffix else f"{slug}-{suffix}")
            seen[slug] += 1
    return set(ids)


markdown = {p.resolve(): p.read_text(encoding="utf-8") for p in ROOT.rglob("*.md") if ".git" not in p.parts}
anchor_map = {p: anchors(text, str(p.relative_to(ROOT))) for p, text in markdown.items()}

# Enforce the GitHub-native right-aligned kbd-arrow button required by Section 15.4 of CHATGPT_GITHUB_WORKFLOW.md.
TOC_RETURN = re.compile(
    r'<p align="right"><a href="#[a-z0-9-]+" '
    r'title="Return to Table of Contents"><kbd>↑</kbd></a></p>'
)
toc_return_count = 0
for path, content in markdown.items():
    for line_number, line in enumerate(content.splitlines(), 1):
        if any(marker in line for marker in
               ("Back to TOC", "<kbd>↑</kbd>", "Return to Table of Contents", ">↑</a>")):
            if not TOC_RETURN.fullmatch(line.strip()):
                fail(f"{path.relative_to(ROOT)}:{line_number}: nonstandard TOC return control")
            else:
                toc_return_count += 1


for path, content in markdown.items():
    label = str(path.relative_to(ROOT))
    for destination in LINK.findall(content) + HTML_HREF.findall(content):
        if destination.startswith(("mailto:", "tel:")):
            continue
        if destination.startswith("https://github.com/dz480/ASOIAF/blob/main/"):
            destination = destination.split("/blob/main/", 1)[1]
        elif "://" in destination or destination.startswith("//"):
            continue
        parsed = urlsplit(destination)
        local = unquote(parsed.path)
        target = (path.parent / local).resolve() if local else path
        if not target.is_relative_to(ROOT) or not target.is_file():
            fail(f"{label}: missing local link destination {destination}")
            continue
        if parsed.fragment and unquote(parsed.fragment) not in anchor_map.get(target, set()):
            fail(f"{label}: unresolved anchor {destination}")

if not (CSRM.is_file() and MCM.is_file() and INDEX.is_file()):
    fail("Missing required index, CSRM or MCM.")
else:
    csrm = markdown[CSRM.resolve()]
    index = markdown[INDEX.resolve()]
    mcm = markdown[MCM.resolve()]
    chapter_rows = [(int(n), pov, roman) for n, pov, roman in CHAPTER.findall(csrm)]
    if [n for n, _, _ in chapter_rows] != list(range(1, 73)):
        fail("CSRM must contain GOT numbered chapters 1–72 in publication order.")
    if "### Prologue (Will)" not in csrm or '<a id="agot-prologue"></a>' not in csrm:
        fail("CSRM prologue or stable prologue anchor is missing.")
    chapter_to_pov = {n: pov for n, pov, _ in chapter_rows}
    for n in range(1, 73):
        if f'<a id="agot-ch-{n}"></a>' not in csrm:
            fail(f"CSRM stable anchor missing: GOT Ch. {n}")
    for label, content in [("CSRM", csrm), ("MCM", mcm)]:
        if "Full-book spoilers" not in content and "Whole-book foresight reference" not in content:
            fail(f"{label}: whole-book spoiler notice missing.")
        if "[Reading Index](README.md)" not in content:
            fail(f"{label}: missing reading-index link.")
    reports = sorted(ROOT.glob("SROMX_GOT_POV_*.md"))
    memberships = {}
    for report in reports:
        content = markdown[report.resolve()]
        pov = report.stem.split("_")[-1].capitalize()
        found = SCOPE.search(content)
        if not found:
            fail(f"{report.name}: explicit POV chapter Scope missing.")
            continue
        chapters = [int(v.strip()) for v in found.group(1).split(",")]
        if not chapters or chapters != sorted(set(chapters)):
            fail(f"{report.name}: Scope list out of publication order or repeated.")
            continue
        for number in chapters:
            if chapter_to_pov.get(number) != pov:
                fail(f"{report.name}: GOT Ch. {number} is not a {pov} chapter in CSRM.")
            if number in memberships:
                fail(f"GOT Ch. {number} allocated to multiple POV reconstructions.")
            memberships[number] = (pov, report.name)
        last, first = chapters[-1], chapters[0]
        if "**Full-book POV spoilers:**" not in content:
            fail(f"{report.name}: front-of-document POV spoiler notice absent.")
        timeline = re.search(r'^# 2\. Timeline\s*\n([\s\S]*?)(?=^# 3\. Major Narrative Threads)', content, re.M)
        overview = re.search(r'^# 4\. Narrative Overview\s*\n([\s\S]*?)(?=^# 5\. Roll Call)', content, re.M)
        if not timeline or f"(ROM_CSRM_AGOT.md#agot-ch-{first})" not in timeline.group(1):
            fail(f"{report.name}: Timeline does not link to first included CSRM chapter.")
        if not overview:
            fail(f"{report.name}: Narrative Overview missing.")
        else:
            navline = next((line for line in overview.group(1).splitlines()
                            if line.startswith("**CSRM chapters (publication order):**")), "")
            expected = [f"(ROM_CSRM_AGOT.md#agot-ch-{n})" for n in chapters]
            actual = re.findall(r'\(ROM_CSRM_AGOT\.md#agot-ch-\d+\)', navline)
            if actual != expected:
                fail(f"{report.name}: Narrative Overview chapter links do not match Scope and reading order.")
        full_name = FULL_POV_NAMES.get(pov)
        if full_name is None:
            fail(f"{report.name}: no full POV character name configured.")
            continue
        expected_link = f"[SROMX | {full_name} | Full Book]({report.name})"
        if expected_link not in index:
            fail(f"Reading Index does not use the canonical link label for {report.name}.")
    for n in range(1, 73):
        heading = re.search(rf'^### GOT Ch\. {n}: [^\n]+\n([\s\S]*?)(?=^### GOT Ch\. |^> ## Drafting)', csrm, re.M)
        if not heading:
            fail(f"CSRM chapter {n}: section cannot be isolated.")
            continue
        present = re.findall(r'\[SROMX \| ([^|\]\n]+) \| Full Book\]\((SROMX_GOT_POV_[A-Z]+\.md)\)', heading.group(1))
        expected = [(FULL_POV_NAMES[memberships[n][0]], memberships[n][1])] if n in memberships else []
        if present != expected:
            fail(f"CSRM chapter {n}: unexpected/missing SROMX back-reference {present} vs {expected}.")
    if "**POV reconstruction (" in csrm:
        fail("CSRM contains redundant standalone POV reconstruction labels.")
    if "[ROM CSRM | Prologue + Ch. 1–72](ROM_CSRM_AGOT.md)" not in index:
        fail("Reading Index missing whole-book CSRM entry.")
    if "[ROM MCM | Whole book](ROM_MCM_AGOT.md)" not in index:
        fail("Reading Index missing MCM entry.")

if errors:
    print(f"ROM navigation validation FAILED ({len(errors)} defects):")
    for issue in errors:
        print(" -", issue)
    sys.exit(1)
print(f"ROM navigation validation PASSED: {len(markdown)} Markdown documents, "
      f"{len(list(ROOT.glob('SROMX_GOT_POV_*.md')))} POV reports, "
      f"{len(memberships)} mapped chapter-to-POV links, 72 stable chapter anchors.")
