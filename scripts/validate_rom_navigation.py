#!/usr/bin/env python3
"""Validate existing ROM document links and POV-to-chapter navigation."""
from __future__ import annotations

from collections import Counter
from pathlib import Path
from urllib.parse import unquote, urlsplit
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
CSRM = ROOT / "01. GOT" / "ROM_CSRM_AGOT.md"
INDEX = ROOT / "README.md"
MCM = ROOT / "01. GOT" / "ROM_MCM_AGOT.md"
LINK = re.compile(r'(?<!!)\[[^\]\n]+\]\(([^)\s]+)(?:\s+[^)]*)?\)')
HTML_HREF = re.compile(r'<a\b[^>]*\bhref=["\']([^"\']+)["\']', re.I)
EXPLICIT = re.compile(r'<a\b[^>]*\bid=["\']([^"\']+)["\']', re.I)
HEADING = re.compile(r'^#{1,6}\s+(.+?)\s*#*\s*$', re.M)
CHAPTER = re.compile(r'^### GOT Ch\. (\d+): (\w+) ([IVXLCDM]+)\s*$', re.M)
SCOPE = re.compile(r'^\*\*Scope:\*\*\s+\*\*GOT Ch\. ([\d,\s]+)\*\*', re.M)
FULL_POV_NAMES = {
    "Will": "Will",
    "Bran": "Bran Stark",
    "Catelyn": "Catelyn Stark",
    "Daenerys": "Daenerys Targaryen",
    "Eddard": "Eddard Stark",
    "Jon": "Jon Snow",
    "Arya": "Arya Stark",
    "Tyrion": "Tyrion Lannister",
    "Sansa": "Sansa Stark",
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
            parsed = urlsplit(destination)
            target = (ROOT / unquote(parsed.path)).resolve()
        elif "://" in destination or destination.startswith("//"):
            continue
        else:
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
        if "[Reading Index](../README.md)" not in content:
            fail(f"{label}: missing reading-index link.")
    reports = sorted((ROOT / "01. GOT").glob("SROMX_GOT_POV_*.md"))
    memberships = {}
    if len(reports) != 9:
        fail(f"Expected 9 full-book POV reports (Will + eight numbered-chapter POVs), found {len(reports)}.")
    memberships = {}
    for report in reports:
        content = markdown[report.resolve()]
        pov = report.stem.split("_")[-1].capitalize()
        if pov not in FULL_POV_NAMES:
            fail(f"{report.name}: unknown POV narrator {pov}.")
            continue
        is_prologue = pov == "Will"
        found = SCOPE.search(content)
        if is_prologue:
            if "**Scope:** **GOT Prologue (Will)**" not in content:
                fail(f"{report.name}: explicit Will Prologue Scope is missing.")
            chapters = []
            entry_anchor = "agot-prologue"
        else:
            if not found:
                fail(f"{report.name}: explicit POV chapter Scope missing.")
                continue
            chapters = [int(v.strip()) for v in found.group(1).split(",")]
            if not chapters or chapters != sorted(set(chapters)):
                fail(f"{report.name}: Scope list out of publication order or repeated.")
                continue
            entry_anchor = f"agot-ch-{chapters[0]}"
        for number in chapters:
            if chapter_to_pov.get(number) != pov:
                fail(f"{report.name}: GOT Ch. {number} does not belong to {pov} in CSRM.")
            if number in memberships:
                fail(f"GOT Ch. {number} allocated to multiple POV reconstructions.")
            memberships[number] = (pov, report.name)
        if "**Full-book POV spoilers:**" not in content:
            fail(f"{report.name}: front-of-document spoiler notice absent.")
        timeline = re.search(r'^# 2\. Timeline\s*\n([\s\S]*?)(?=^# 3\. Major Narrative Threads)', content, re.M)
        overview = re.search(r'^# 4\. Narrative Overview\s*\n([\s\S]*?)(?=^# 5\. Roll Call)', content, re.M)
        if not timeline or f"(ROM_CSRM_AGOT.md#{entry_anchor})" not in timeline.group(1):
            fail(f"{report.name}: Timeline first-unit CSRM deep link is absent or wrong.")
        if not overview:
            fail(f"{report.name}: Narrative Overview missing.")
        else:
            navline = next((line for line in overview.group(1).splitlines()
                            if line.startswith("**CSRM chapters (publication order):**")), "")
            expected = ["(ROM_CSRM_AGOT.md#agot-prologue)"] if is_prologue else [
                f"(ROM_CSRM_AGOT.md#agot-ch-{n})" for n in chapters]
            actual = re.findall(r'\(ROM_CSRM_AGOT\.md#agot-(?:prologue|ch-\d+)\)', navline)
            if actual != expected:
                fail(f"{report.name}: Overview source-unit links do not match Scope order.")
        required_sections = ["Narrative Context", "Timeline", "Major Narrative Threads",
                             "Narrative Overview", "Roll Call", "Top Cinematic Scenes"]
        section_names = re.findall(r'^# [1-6]\. ([^\n]+)$', content, re.M)
        if section_names != required_sections:
            fail(f"{report.name}: six mandatory SROMX sections not in canonical order.")
        if len(re.findall(r'^---$', content, re.M)) != 6:
            fail(f"{report.name}: expected five section dividers plus appendix divider.")
        if len(TOC_RETURN.findall(content)) != 6:
            fail(f"{report.name}: expected six standardised section return controls.")
        census = re.search(
            r'^\*\*Character entries:\*\*\s*(\d+)(?: Total)?\s*(?:\(|\|)\s*'
            r'(\d+) Principal\s*\|\s*(\d+) Supporting\s*\|\s*'
            r'(\d+) Tertiary\s*\|\s*(\d+) Collective', content, re.M)
        roll = re.search(r'^# 5\. Roll Call\s*\n([\s\S]*?)(?=^# 6\. Top Cinematic Scenes)', content, re.M)
        if not census or not roll:
            fail(f"{report.name}: Roll Call or census header missing.")
        else:
            entries = re.findall(r'^\|\s*(🏅|🥈|\d+)\s*\|\s*\*\*[^*]+\*\*', roll.group(1), re.M)
            if len(entries) != int(census.group(1)):
                fail(f"{report.name}: census total differs from actual entries.")
            if entries.count("🏅") != int(census.group(2)) or entries.count("🥈") != int(census.group(3)):
                fail(f"{report.name}: Principal or Supporting census count differs from medals.")
            if len(entries) - entries.count("🏅") - entries.count("🥈") != int(census.group(4)) + int(census.group(5)):
                fail(f"{report.name}: Tertiary/Collective census count differs from rows.")
            numbers = [int(v) for v in entries if v.isdigit()]
            if len(numbers) != len(set(numbers)):
                fail(f"{report.name}: repeated Tertiary/Collective index.")
        expected_link = f"[SROMX | {FULL_POV_NAMES[pov]} | Full Book](01. GOT/{report.name})"
        if expected_link not in index:
            fail(f"Reading Index missing canonical link {expected_link}.")
    if len(memberships) != 72:
        fail(f"Expected complete 72-chapter POV coverage, mapped {len(memberships)} chapters.")
    will_link = "[SROMX | Will | Full Book](SROMX_GOT_POV_WILL.md)"
    prologue = re.search(r'^### Prologue \(Will\)\s*\n([\s\S]*?)(?=^---$|^<a id="agot-ch-1")', csrm, re.M)
    if not prologue or will_link not in prologue.group(1):
        fail("CSRM Prologue must link to Will's full-book SROMX.")
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
    if "[ROM CSRM | Prologue + Ch. 1–72](01. GOT/ROM_CSRM_AGOT.md)" not in index:
        fail("Reading Index missing whole-book CSRM entry.")
    if "[ROM MCM | Whole book](01. GOT/ROM_MCM_AGOT.md)" not in index:
        fail("Reading Index missing MCM entry.")

if errors:
    print(f"ROM navigation validation FAILED ({len(errors)} defects):")
    for issue in errors:
        print(" -", issue)
    sys.exit(1)
print(f"ROM navigation validation PASSED: {len(markdown)} Markdown documents, "
      f"{len(list((ROOT / '01. GOT').glob('SROMX_GOT_POV_*.md')))} POV reports, "
      f"{len(memberships)} mapped chapter-to-POV links, 72 stable chapter anchors and 1 Prologue anchor.")
