# ASOIAF — Master Reread Workflow

**Status:** Canonical project operating document  
**Version:** 1.0  
**Established:** 13 Oct 2026  
**Repository:** [dz480/ASOIAF](https://github.com/dz480/ASOIAF)  
**Permanent filename:** `ASOIAF_MASTER_WORKFLOW.md`  
**Scope:** Repeatable book-by-book reread, source analysis, ROM production, reconciliation and GitHub archival workflow

**Operating principle:** Prepare the entire book's reference architecture **before reading**; conduct the readthrough and POV SROMX construction **concurrently**; then reconcile all completed POV accounts and synthesise the final, whole-book ROM MNT. This document is the central operational guide for the ASOIAF repository.

**Authority boundary:** This document governs *which operations occur, in what order, with which prompts and completion conditions*. The canonical [RTE](https://github.com/dz480/CG-Protocols/blob/main/RTE/RTE.md), [ROM](https://github.com/dz480/CG-Protocols/tree/main/ROM) and [ChatGPT ↔ GitHub](https://github.com/dz480/CG-GitHub/blob/main/CHATGPT_GITHUB_WORKFLOW.md) manuals govern their respective protocol structures and GitHub mechanics. This project document does not replace those manuals.

<a id="asoiaf-workflow-toc"></a>
## Table of Contents

- [01. Purpose and Authority](#workflow-01)
- [02. Workflow at a Glance](#workflow-02)
- [03. Phase I — Preparation](#workflow-03)
- [04. Phase II — Reference Construction](#workflow-04)
- [05. Phase III — Concurrent Readthrough and POV Reconstruction](#workflow-05)
- [06. Phase IV — Cross-POV Reconciliation](#workflow-06)
- [07. Phase V — Whole-Book Synthesis and Completion](#workflow-07)
- [08. Command Conventions and Maintenance](#workflow-08)
- [09. Source Boundaries, Navigation and Quality Gates](#workflow-09)
- [10. Book Transition and Reuse](#workflow-10)
- [Appendix: Document Notes](#workflow-notes)

<a id="workflow-01"></a>
## 1. Purpose and Authority

The repository is an **operational record of a close reread of George R. R. Martin's *A Song of Ice and Fire***, with one coherent set of source, character, chronology, POV and whole-book narrative records for each completed novel.

This master workflow is the repository's **control document**: use it to plan the next novel, determine the appropriate invocation, identify a stage's prerequisites, decide when it is complete and prevent ambiguity between initial creation, maintenance, revision and final synthesis.

The **book** is the basic completion unit. Within each book, **source chapters** are the evidence units; **RTE reading units** may be chapters, Sequences or character POVs according to the authorised schedule; **SROMX POV selections** assemble the actual chapters narrated by a particular character, retaining their source-order coordinates. The final MNT is a **book-wide** reconstruction across those POV perspectives, not an aggregation of their rankings.

The completed *A Game of Thrones* workflow is the foundation for this repeatable process. Later books inherit its **method**, not its exact character counts, chapter totals, thread rankings, plot events or filenames.

<p align="right"><a href="#asoiaf-workflow-toc" title="Return to Table of Contents"><kbd>↑</kbd></a></p>

---

<a id="workflow-02"></a>
## 2. Workflow at a Glance

| Phase | Step | Action | Timing | Primary deliverable |
|---|---:|---|---|---|
| I — Preparation | 1 | Acquire complete EPUB | Before reading | Authoritative source file |
| I — Preparation | 2 | RTE Scan & Schedule | Before reading | Complete reading-unit plan |
| II — Reference Construction | 3 | BUILD ROM MCM | Before reading | Whole-book character map in GitHub |
| II — Reference Construction | 4 | B&P ROM CSRM | Before reading | Whole-book chronology in GitHub and chat |
| III — Readthrough & POV Reconstruction | 5 | Read the novel | **Concurrent with Step 6** | Chapters completed against RTE |
| III — Readthrough & POV Reconstruction | 6 | B&P SROMX by POV | **Concurrent with Step 5** | One complete POV record per narrator |
| IV — Reconciliation | 7 | Reconcile every POV SROMX | After all POV records are complete | Corrected, cross-consistent POV reports |
| V — Synthesis & Completion | 8 | B&P whole-book ROM MNT | After Step 7 | Unified, ranked macro-narrative record |
| V — Synthesis & Completion | 9 | Repository navigation & validation | After Step 8 | Indexed and verified book dossier |

**Critical timing rules:**

- Steps **3–4 precede 5–6**. The MCM and CSRM are whole-book preparatory reference materials, even though the user has not yet read that book in the current reread.
- Steps **5 and 6 are one ongoing parallel activity**. There is no requirement to finish the entire book before beginning POV reconstructions.
- A complete, full-book **POV** SROMX becomes ready when that POV's **last selected chapter** has been read; other POV reconstructions may continue.
- Steps **7–9** follow completion of the novel and all its POV records. Step 8 includes MNT creation **and** publication; Step 9 is a final audit, not a second publication step.
- **No manual MLRP / Reading Point update is required** for this project. Use the book's RTE plan and explicitly authorised source scope; never infer a current reading point from GitHub navigation.

<p align="right"><a href="#asoiaf-workflow-toc" title="Return to Table of Contents"><kbd>↑</kbd></a></p>

---

<a id="workflow-03"></a>
## 3. Phase I — Preparation

### Step 1 — Acquire the EPUB

Obtain the **complete, unabridged** EPUB of the novel and make it available as the authoritative source file. Confirm which edition is being used and that all literary source units (including any Prologue and Epilogue) are accounted for.

**Completion test:** The source can be opened, its narrative sections identified and its entire intended work processed.

### Step 2 — RTE Scan & Schedule

Run the source scan, then build and publish the full-book RTE record. Use RTE to identify the publication-order units, word counts and estimated reading times. Determine whether the practical reread units are **Sequences or POVs**, without converting a source chapter into a different canonical chapter merely for convenience.

**Invocations:**

```text
RTE SCAN: [BOOK]
```

```text
B&P RTE: [BOOK], WHOLE BOOK
```

**Completion test:** The schedule accounts for every eligible literary unit; chapter and narrator assignments are internally consistent; the plan can support both the subsequent readthrough and SROMX source selections.

**Source-of-truth rule:** The RTE record maps reading and source units. It does **not** itself define ROM MCM character classifications, CSRM historical chronology or whole-book MNT rankings.

<p align="right"><a href="#asoiaf-workflow-toc" title="Return to Table of Contents"><kbd>↑</kbd></a></p>

---

<a id="workflow-04"></a>
## 4. Phase II — Reference Construction

Complete **both** reference records before the live readthrough.

### Step 3 — BUILD ROM MCM

Construct the **whole-book Master Character Map**, using the primary text and, for later series books, eligible prior-book continuity. The MCM provides the authoritative book-level cast, character classifications, appearance evidence and supported continuity. Its source endpoint is the completed book, not the reader's present progress.

**Invocation:**

```text
BUILD ROM MCM: [BOOK], WHOLE BOOK
```

**Delivery rule:** **BUILD** creates and commits the record to GitHub, then returns only a **concise completion report and direct file link**. Do not print the full MCM in the ChatGPT conversation.

**Protocol constraint:** Follow the current [ROM MCM](https://github.com/dz480/CG-Protocols/blob/main/ROM/CHARACTERS/ROM_MASTER_CHARACTER_MAP.md) manual, including its **ten-minute creation/initialisation feasibility gate**. If the initial build exceeds that gate, stop and request the explicit authorisation the manual requires, rather than silently commencing an extended operation.

**Completion test:** A usable, priority-accurate MCM is committed to GitHub and its quality state is reported truthfully.

### Step 4 — B&P ROM CSRM

Construct the **whole-book Chapter Sequence Recall Map**, including every qualifying chapter and any Prologue/Epilogue. The CSRM establishes chapter coordinates, chronology, key events and the chapter-level reference structure used for later POV navigation.

**Invocation:**

```text
B&P ROM CSRM: [BOOK], WHOLE BOOK
```

**Delivery rule:** **B&P** both saves to GitHub and displays the substantive document in ChatGPT.

**Completion test:** All authorised narrative units have a stable chapter reference, chronological information is source-supported and the document is published.

**Spoiler separation:** Both preparatory documents may contain **whole-book foresight**. Their existence never authorises an unsolicited spoiler-bearing reading response or a change to the user's live readthrough position.

<p align="right"><a href="#asoiaf-workflow-toc" title="Return to Table of Contents"><kbd>↑</kbd></a></p>

---

<a id="workflow-05"></a>
## 5. Phase III — Concurrent Readthrough and POV Reconstruction

### Step 5 — Read the Novel

Read in accordance with the RTE schedule. The schedule defines the intended reading commitments and source-unit progression. Reading is an ongoing activity, not a separate ChatGPT publishing operation.

### Step 6 — B&P SROMX for Each POV

As reading progresses, build and publish a **SROMX for every POV narrator**. For a full-book POV-selected SROMX, gather **all and only** that narrator's authorised chapters, preserve their publication-order coordinates and reconstruct the continuous POV narrative. This can be completed when the reader reaches the **final chapter narrated by that POV**, rather than waiting for unrelated POV chapters to finish.

**Invocation:**

```text
B&P SROMX: [BOOK], FULL BOOK, POV [CHARACTER]
```

Repeat for all POVs, including a Prologue-only or Epilogue-only narrator where applicable. The SROMX's **Major Narrative Threads** section produces the **POV-local MNTs** as part of this same step; they are **not** a separate task performed later.

Each SROMX must follow the current [SROMX manual](https://github.com/dz480/CG-Protocols/blob/main/ROM/RECAPS/SROMX.md), including its narrative-context, timeline, POV-local MNT, narrative-overview, roll-call and cinematic-scene requirements. Reconcile character classifications to the MCM and chapter coordinates to the CSRM as each record is constructed.

**Completion test:** Every qualifying POV has a published, source-grounded SROMX covering its declared chapter list; all POV-local MNT assessments exist within their respective records.

**Scope rule:** The term **FULL BOOK, POV [CHARACTER]** identifies the **complete POV chapter selection** in the book, not permission to insert unexplained knowledge from chapters outside that POV or from later books. Handle wider-book context only as permitted by the current SROMX manual.

<p align="right"><a href="#asoiaf-workflow-toc" title="Return to Table of Contents"><kbd>↑</kbd></a></p>

---

<a id="workflow-06"></a>
## 6. Phase IV — Cross-POV Reconciliation

### Step 7 — Reconcile All Completed SROMX Records

Perform the book-level audit **after the book is finished and all POV SROMX reports exist**.

Check the records **against one another** and against the authoritative EPUB, the MCM, CSRM and the latest SROMX manual. Resolve conflicting facts, inconsistent dates or chapter coordinates, incorrect character participation or significance, divergent interpretations of shared events, broken internal links and out-of-date section formatting.

**Execution prompt:**

```text
Reconcile all completed [BOOK] POV SROMX records
against one another, the whole-book MCM, CSRM
and primary EPUB.

Correct source and continuity inconsistencies,
bring each record into compliance with the
latest SROMX manual, complete the applicable
cross-references, commit the corrected files
to ASOIAF and validate the results.
```

Use **UPDATE** / **UPDATE FORMATTING** for a specific existing ROM record when the objective is structural/manual compliance. Example:

```text
UPDATE SROMX: [BOOK], POV [CHARACTER]
```

An UPDATE is **record maintenance**, not rewriting its canonical Protocol Manual. Where reconciliation identifies an actual factual error, make the necessary source-grounded correction under the express reconciliation instruction and preserve unaffected material.

**Completion test:** All POV reports use the current applicable structure, align with the book-wide references and with one another, and retain complete, working navigation to existing applicable documents.

**Sequence distinction:** This is a **multi-record content and formatting audit**. Do not use the project convention **REVISE IN GITHUB** as a synonym for this step: that command is reserved here for substantive changes to **Protocol Manuals**.

<p align="right"><a href="#asoiaf-workflow-toc" title="Return to Table of Contents"><kbd>↑</kbd></a></p>

---

<a id="workflow-07"></a>
## 7. Phase V — Whole-Book Synthesis and Completion

### Step 8 — B&P ROM MNT

Extract the **Major Narrative Threads** from all completed POV SROMX records and reassess them at **Whole Book** scope. Identify common causal developments and converging interests; consolidate true overlaps, retain genuinely independent narrative lines, reconcile evidence and rank the resulting threads by **book-wide significance**, not by POV-local ranking or recency.

The finished ROM MNT must satisfy the current [ROM MNT manual](https://github.com/dz480/CG-Protocols/blob/main/ROM/ANALYSIS/ROM_MNT.md), including the appropriate participation tables, complete-book scope boundary, explanation limits and cross-thread **Flow Chart**.

**Invocation:**

```text
B&P ROM MNT: [BOOK], WHOLE BOOK

Synthesise and reconcile all completed POV-local
MNTs into the final book-wide hierarchy.
```

**Completion test:** One complete, independently ranked whole-book MNT is **created, committed to GitHub and published in ChatGPT**. There is **no separate MNT publication step** after this invocation.

### Step 9 — Final Repository Navigation and Validation

Apply the universal ROM navigation system to the repository, now that the whole-book MNT exists. Check the book's reading-index entries, genuine chapter/POV links, MCM/CSRM/SROMX/MNT relationships, spoiler labels, explicit anchors and validator results.

**Invocation:**

```text
APPLY ROM NAVIGATION: dz480/ASOIAF
```

Confirm the reading index offers an intelligible, spoiler-aware entry point to the newly completed book dossier. Where the existing repository supports validation, check `python3 scripts/validate_rom_navigation.py` and the corresponding GitHub Actions outcome; report any remaining failures rather than assuming a successful commit means full validation.

**Completion test:** The new book's expected files are present, links and applicable automated tests have been checked, and the committed repository is ready for the next novel.

**Finish condition:** A book is complete for this workflow **only when its source schedule, MCM, CSRM, all POV SROMX records and final MNT are present and reconciled, with validated repository navigation**.

<p align="right"><a href="#asoiaf-workflow-toc" title="Return to Table of Contents"><kbd>↑</kbd></a></p>

---

<a id="workflow-08"></a>
## 8. Command Conventions and Maintenance

These are the ASOIAF project's **operational command conventions**. Specialist protocols still determine the internal output requirements of their records.

| Command | Meaning in ASOIAF | ChatGPT delivery | GitHub action |
|---|---|---|---|
| **BUILD** | First-time creation of a record, **reserved here for MCM** | Concise completion report + direct file link; full MCM withheld from chat | Create and commit |
| **B&P** | First-time **Build & Publish** of RTE, CSRM, SROMX, MNT and similar records | Display complete substantive output, in addition to status and link | Create and commit |
| **UPDATE** or **UPDATE FORMATTING** | Bring an **existing ROM record file** into structural, formatting and terminology compliance with its latest canonical manual | Concise change report and file link, unless full publication is requested | Modify and commit existing record |
| **REVISE IN GITHUB** | User's convention for **rewriting or substantively modifying a section of an existing Protocol Manual** | Report the manual changes and direct file link | Modify and commit the canonical **manual** |

**Rules of interpretation:**

- **Initial creation:** Start the file-creation invocation with **B&P**, **except ROM MCM**, which starts with **BUILD**. A separate instruction to save to GitHub is **redundant** for either command.
- **BUILD is not B&P:** It includes GitHub persistence **without** displaying the complete MCM in the ChatGPT window.
- **UPDATE is not a rebuild:** Retrieve the current record and manual, identify out-of-date structures and bring the **record** up to date while preserving its evidence and established substance, except for changes genuinely required by protocol compliance.
- **REVISE IN GITHUB is manual maintenance:** In this project's prompt vocabulary, reserve it for rewriting the **Protocol Manual**. The canonical cross-project GitHub workflow remains authoritative for the underlying GitHub mechanics and its broader document-maintenance operation.
- **Reconciliation is its own audit task:** Source-grounded changes to multiple already-created records are authorised by the explicit Step 7 reconciliation prompt. They must not be mislabeled as rewriting the SROMX manual.
- **Authorisation:** A request to discuss, inspect or audit a record is read-only unless a recognised command or explicit instruction authorises creation or modification.

**Examples:**

```text
BUILD ROM MCM: [BOOK], WHOLE BOOK
B&P ROM CSRM: [BOOK], WHOLE BOOK
B&P SROMX: [BOOK], FULL BOOK, POV [CHARACTER]
UPDATE SROMX: [BOOK], POV [CHARACTER]
REVISE IN GITHUB: ROM SROMX
```

<p align="right"><a href="#asoiaf-workflow-toc" title="Return to Table of Contents"><kbd>↑</kbd></a></p>

---

<a id="workflow-09"></a>
## 9. Source Boundaries, Navigation and Quality Gates

### Source and spoiler authority

1. The uploaded **complete primary EPUB** is the first authority for events, appearances, chronology and dramatic developments. RTE maps the source; MCM, CSRM and SROMX must remain consistent with it.
2. **One book at a time:** A whole-book reference for the active book ends at that book's final authorised narrative unit. Do not introduce later-book knowledge or television material as evidence.
3. Full-book **MCM and CSRM** are deliberate preparatory foresight records. Keep their spoiler status explicit and separate from reader-bounded discussion.
4. An SROMX must declare its **actual POV source chapters**, keep them in the proper reading order and preserve the appropriate POV-local spoiler boundary.
5. Do not require or automatically alter a live MLRP. The project's reread progression is carried by its RTE schedule and the user's actual reading.

### Canonical hierarchy

- **This file:** Defines ASOIAF project stages, sequencing, invocations and completion gates.
- **[RTE manual](https://github.com/dz480/CG-Protocols/blob/main/RTE/RTE.md):** Source counting, reading-time calculations and RTE formatting.
- **[MCM](https://github.com/dz480/CG-Protocols/blob/main/ROM/CHARACTERS/ROM_MASTER_CHARACTER_MAP.md), [CSRM](https://github.com/dz480/CG-Protocols/blob/main/ROM/RECAPS/ROM_CSRM.md), [SROMX](https://github.com/dz480/CG-Protocols/blob/main/ROM/RECAPS/SROMX.md) and [MNT](https://github.com/dz480/CG-Protocols/blob/main/ROM/ANALYSIS/ROM_MNT.md) manuals:** Specialist record content, structure and evidence.
- **[ROM NAVIGATION](https://github.com/dz480/CG-Protocols/blob/main/ROM/CORE/ROM_NAVIGATION.md):** Universal contextual links, spoiler-aware navigation and repository-level graph integrity.
- **[ChatGPT ↔ GitHub Workflow](https://github.com/dz480/CG-GitHub/blob/main/CHATGPT_GITHUB_WORKFLOW.md):** GitHub persistence, verification, maintenance and Markdown navigation presentation.

Where requirements conflict, apply the governing **specialist manual** to the record's substance and the canonical cross-project workflow to GitHub mechanics. The user-agreed BUILD/B&P/UPDATE/REVISE invocation vocabulary in Section 8 governs how the ASOIAF workflow is requested.

### Repository integrity

- Preserve stable filenames, source chapter IDs and already-valid anchors; publish absent nodes only when authorised.
- Maintain links **only to documents that exist**; a future book's planned file is not a working navigation destination.
- Distinguish full-book spoilers from a POV's narrower last-chapter boundary, and do not conflate POV groupings with contiguous Sequences.
- Make GitHub edits conservatively: preserve unaffected content, verify the resulting committed file, update directly dependent index entries and retain source-grounded uncertainty.
- After every book, perform an **end-to-end audit**, including manual content checks and any actual local/CI automated validation.

**Quality gate:** A record is not deemed verified merely because it was generated or a GitHub write returned success; its required contents, source coverage, cross-references and relevant checks must be confirmed.

<p align="right"><a href="#asoiaf-workflow-toc" title="Return to Table of Contents"><kbd>↑</kbd></a></p>

---

<a id="workflow-10"></a>
## 10. Book Transition and Reuse

After a book passes **Step 9**, begin the next novel at **Phase I**, taking its complete EPUB and repeating the same nine-step process.

- Update `[BOOK]` to the next novel's recognised book identifier, such as **COK** for *A Clash of Kings*.
- Build the next book's RTE, MCM and CSRM **before** continuing that reread.
- Determine the next book's **actual** chapter and POV inventory from its source. Do not reuse GOT's nine narrators, 73-unit schedule, character counts or narrative-thread ranking.
- If a POV has no further chapter until late in the book, leave its SROMX incomplete until that last chapter is read; other completed POV records can be built and published in parallel with the ongoing read.
- After the readthrough, conduct the same cross-record reconciliation, final whole-book MNT synthesis and final repository audit.
- Keep previous books' published records intact; add the new book's links under the appropriate spoiler-labelled index section.

**Reusable end-to-end command sequence:**

```text
RTE SCAN: [BOOK]
B&P RTE: [BOOK], WHOLE BOOK

BUILD ROM MCM: [BOOK], WHOLE BOOK
B&P ROM CSRM: [BOOK], WHOLE BOOK

[READ IN RTE ORDER]
B&P SROMX: [BOOK], FULL BOOK, POV [CHARACTER]
[REPEAT SROMX FOR EACH POV AS ITS FINAL CHAPTER IS READ]

[RECONCILE ALL FINISHED POV SROMX USING STEP 7]

B&P ROM MNT: [BOOK], WHOLE BOOK
APPLY ROM NAVIGATION: dz480/ASOIAF
```

**Terminal state for each novel:** A complete and mutually consistent book dossier, with every POV accounted for, a final ranked MNT and verified GitHub access. The repository as a whole remains an **expanding series record**, not a finished one-book archive.

<p align="right"><a href="#asoiaf-workflow-toc" title="Return to Table of Contents"><kbd>↑</kbd></a></p>

---

<a id="workflow-notes"></a>
## Appendix: Document Notes

> **Formalisation basis — Applies to: Entire document:** Initial publication formalises the GOT reread workflow agreed in the current project: source acquisition; RTE scan/schedule; pre-read MCM and CSRM; concurrent reading and SROMX; nine-POV-style reconciliation where applicable; whole-book MNT; and final navigation verification. The first GOT book required nine POV SROMX records, including Will's Prologue; that count is evidence for GOT only, not a fixed series-wide rule.

> **GOT completed records — Applies to: Sections 1, 2 and 10:** The first completed exemplar consists of [ROM MCM](ROM_MCM_AGOT.md), [ROM CSRM](ROM_CSRM_AGOT.md), nine [POV SROMX reports](README.md#sromx--pov-selected-narrative-reconstructions) and [ROM MNT](ROM_MNT_AGOT.md), indexed in the [README](README.md). The previously supplied GOT RTE schedule is an external project source asset, not currently a published root-level file in this repository. Future B&P RTE operations follow Section 3's creation convention.

> **Command scope — Applies to: Section 8:** The BUILD/B&P/UPDATE/REVISE definitions preserve the user's project-level invocation rules. The canonical GitHub workflow has a broader general-purpose meaning for REVISE IN GITHUB, but the narrower ASOIAF usage should control interpretation within this project's reread prompts.

> **Manual precedence — Applies to: Sections 4, 8 and 9:** The manual-specific mandatory MCM creation gate remains applicable even though this workflow requires a concise BUILD output. Any later manual changes take effect on subsequent records and structural UPDATEs; this file sets the sequence, not a frozen copy of manual output schemas.

