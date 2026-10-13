# A Song of Ice and Fire | ROM Reading Index

## Repository Operating Manual

**[ASOIAF READTHROUGH PROJECT WORKFLOW (ASOIAF RPW)](ASOIAF_READTHROUGH_PROJECT_WORKFLOW.md)** — The series-specific Type C overview-led implementation of the [universal ROM RPW](https://github.com/dz480/CG-Protocols/blob/main/ROM/CORE/ROM_READTHROUGH_PROJECT_WORKFLOW.md): six-phase parent lifecycle, nine local practical steps, POV SROMX concurrency, reconciliation, spoiler boundaries and incremental plus final navigation validation. **Start here when beginning a new book.**


**Repository:** [dz480/ASOIAF](https://github.com/dz480/ASOIAF)  
**Published coverage:** *A Game of Thrones* (GOT), Book 1.  
**Purpose:** Spoiler-neutral directory of published ROM-family reading records, organised by book, report type and declared source scope.

> **Spoiler guidance:** All reports currently published here are complete-book or completed-POV references. Opening them can reveal later chapters, character outcomes and major narrative events. Chapter coordinates in this directory describe report coverage, not a live reading position.

## Book 1: A Game of Thrones (GOT)

### Complete-book references

- [ROM CSRM | Prologue + Ch. 1–72](ROM_CSRM_AGOT.md) · Complete-book chapter chronology and recap index. **Full-book spoilers.**
- [ROM MCM | Whole book](ROM_MCM_AGOT.md) · Master character map and appearance register. **Full-book spoilers.**
- [ROM MNT | Whole book](ROM_MNT_AGOT.md) · Final ranked synthesis of all nine POV-local narrative thread assessments, including a cross-thread flow chart. **Full-book spoilers.**

### SROMX | POV-selected narrative reconstructions

The nine completed full-book POV records are listed in order of their first narrated appearance, including Will's Prologue. Source chapters follow publication order, not reconstructed historical chronology.

- [SROMX | Will | Full Book](SROMX_GOT_POV_WILL.md) · Prologue (1 POV unit). **Spoilers through Prologue**.
- [SROMX | Bran Stark | Full Book](SROMX_GOT_POV_BRAN.md) · 7 POV chapters; GOT Ch. 1, 8, 17, 24, 37, 53, 66. **Spoilers through Ch. 66**.
- [SROMX | Catelyn Stark | Full Book](SROMX_GOT_POV_CATELYN.md) · 11 POV chapters; GOT Ch. 2, 6, 14, 18, 28, 34, 40, 55, 59, 63, 71. **Spoilers through Ch. 71**.
- [SROMX | Daenerys Targaryen | Full Book](SROMX_GOT_POV_DAENERYS.md) · 10 POV chapters; GOT Ch. 3, 11, 23, 36, 46, 54, 61, 64, 68, 72. **Spoilers through Ch. 72**.
- [SROMX | Eddard Stark | Full Book](SROMX_GOT_POV_EDDARD.md) · 15 POV chapters; GOT Ch. 4, 12, 16, 20, 25, 27, 30, 33, 35, 39, 43, 45, 47, 49, 58. **Spoilers through Ch. 58**.
- [SROMX | Jon Snow | Full Book](SROMX_GOT_POV_JON.md) · 9 POV chapters; GOT Ch. 5, 10, 19, 26, 41, 48, 52, 60, 70. **Spoilers through Ch. 70**.
- [SROMX | Arya Stark | Full Book](SROMX_GOT_POV_ARYA.md) · 5 POV chapters; GOT Ch. 7, 22, 32, 50, 65. **Spoilers through Ch. 65**.
- [SROMX | Tyrion Lannister | Full Book](SROMX_GOT_POV_TYRION.md) · 9 POV chapters; GOT Ch. 9, 13, 21, 31, 38, 42, 56, 62, 69. **Spoilers through Ch. 69**.
- [SROMX | Sansa Stark | Full Book](SROMX_GOT_POV_SANSA.md) · 6 POV chapters; GOT Ch. 15, 29, 44, 51, 57, 67. **Spoilers through Ch. 67**.

## Repository navigation conventions

- Every CSRM source unit has a permanent book-specific anchor, including [Prologue](ROM_CSRM_AGOT.md#agot-prologue) and [GOT Ch. 1](ROM_CSRM_AGOT.md#agot-ch-1). All 73 source units link to the applicable completed POV SROMX.
- Each POV report links to the **first selected CSRM unit** beneath Timeline and to **every constituent chapter or Prologue** beneath Narrative Overview.
- No SNR, CM, CRM or reader-bounded snapshot has been published in this repository. These destinations will be added when actual files exist.
- Current Reading Point / MLRP is not tracked or changed by repository navigation.

**Canonical navigation rules:** [ROM NAVIGATION](https://github.com/dz480/CG-Protocols/blob/main/ROM/CORE/ROM_NAVIGATION.md).

**Local validation:** Run `python3 scripts/validate_rom_navigation.py`. The [GitHub Actions workflow](.github/workflows/rom-navigation.yml) checks future changes when Actions is enabled.
