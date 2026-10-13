# A Song of Ice and Fire | ROM Reading Index

**Repository:** [dz480/ASOIAF](https://github.com/dz480/ASOIAF)  
**Published coverage:** *A Game of Thrones* (GOT), Book 1.  
**Purpose:** Spoiler-neutral directory of published ROM-family reading records, organised by book, report type and declared source scope.

> **Spoiler guidance:** All reports currently published here are complete-book or completed-POV references. Opening them can reveal later chapters, character outcomes and major narrative events. Chapter coordinates in this directory describe report coverage, not a live reading position.

## Book 1: A Game of Thrones (GOT)

### Complete-book references

- [ROM CSRM | Prologue + Ch. 1–72](ROM_CSRM_AGOT.md) · Complete-book chapter chronology and recap index. **Full-book spoilers.**
- [ROM MCM | Whole book](ROM_MCM_AGOT.md) · Master character map and appearance register. **Full-book spoilers.**

### SROMX | POV-selected narrative reconstructions

The following reports are arranged by each POV's first numbered chapter. Their source chapters are **non-consecutive** and follow the novel's published reading order, rather than a reconstructed chronological sequence.

- [SROMX | Bran Stark | Full Book](SROMX_GOT_POV_BRAN.md) · 7 POV chapters; GOT Ch. 1, 8, 17, 24, 37, 53, 66. **Spoilers through Ch. 66.**
- [SROMX | Catelyn Stark | Full Book](SROMX_GOT_POV_CATELYN.md) · 11 POV chapters; GOT Ch. 2, 6, 14, 18, 28, 34, 40, 55, 59, 63, 71. **Spoilers through Ch. 71.**
- [SROMX | Daenerys Targaryen | Full Book](SROMX_GOT_POV_DAENERYS.md) · 10 POV chapters; GOT Ch. 3, 11, 23, 36, 46, 54, 61, 64, 68, 72. **Spoilers through Ch. 72.**
- [SROMX | Eddard Stark | Full Book](SROMX_GOT_POV_EDDARD.md) · 15 POV chapters; GOT Ch. 4, 12, 16, 20, 25, 27, 30, 33, 35, 39, 43, 45, 47, 49, 58. **Spoilers through Ch. 58.**

## Repository navigation conventions

- Each CSRM chapter has a permanent book-specific deep-link anchor, such as [GOT Ch. 1](ROM_CSRM_AGOT.md#agot-ch-1). Chapters with a published POV reconstruction link back to that SROMX.
- Each POV report links to its **first included CSRM chapter** beneath Timeline and to **every included chapter** beneath Narrative Overview.
- No SNR, CM, CRM, MNT or reader-bounded snapshot has been published in this repository. These destinations will be added when actual files exist.
- Current Reading Point / MLRP is not tracked or changed by repository navigation.

**Canonical navigation rules:** [ROM NAVIGATION](https://github.com/dz480/CG-Protocols/blob/main/ROM/CORE/ROM_NAVIGATION.md).

**Local validation:** Run `python3 scripts/validate_rom_navigation.py`. The [GitHub Actions workflow](.github/workflows/rom-navigation.yml) checks future changes when Actions is enabled.
