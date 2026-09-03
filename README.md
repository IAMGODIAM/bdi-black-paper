# THE MEASURE OF THE WOUND
### A Sovereign Empirical Record of Black American Structural Distress, 1991–2024

**Publisher:** E5 Enclave Incorporated · EIN 99-3822441 · Liberty City, Miami, Florida  
**License:** CC0 1.0 Universal — Public Domain  
**Status:** CORRECTED PRINT EDITION — complete, reconciled, peer-review ready  
**Version:** Black Paper v1.4 — Submission Edition  
**DAG:** bdi-black-paper-genesis-2026-0420

---

## THE DATA

This paper is built on the largest unified open dataset documenting Black American structural conditions ever assembled by a Black-led organization.

| Layer | What It Is | Scale |
|-------|-----------|-------|
| **Raw Evidence Vault** | 17 unmodified federal API pulls (BLS, Census, NCHS, BJS, Fed Reserve, USDA, SlaveVoyages) | **~14,811 verified data points** |
| **Sovereign Dataset** | 8-pillar synthesized instrument, 33-year window (1991–2024), on-chain sealed | **1,574 empirical observations** |
| **FarmBlock Application** | Tract-level structural distress scoring across 49 cities in 17 states | **15,507 census tracts** |

**Geographic coverage:** 52 state-level geographies · 516+ metro areas · 3,222 counties · 49 cities · 15,507 census tracts  
**Temporal span:** 1514–2024 (empirical window: 1991–2024, 33 years)  
**Blockchain seal:** ExodusV4 Token #2, Base Mainnet

---

## THIS EDITION

**`final/The_Measure_of_the_Wound.pdf`** — 91-page Corrected Print Edition, Black Paper **v1.4 (Submission Edition)**. v1.4 states the FarmBlock reproducibility limit in Chapter 7 where the index is introduced, and rewrites the AI disclosure to describe the division of labor exactly rather than approximately. v1.3 added the abstract, author of record, AI-assistance disclosure, keywords/JEL codes and consolidated References; v1.2 carried the second-wave corrections from an independent verification review of v1.1 (Manus AI, September 1, 2026 — review and author response in `peer-review/`).

All chapters are complete. Every derived statistic was recomputed from the Layer-1 raw series rather than carried forward from prior drafts, and flagged figures were re-verified against live federal sources in August 2026.

| Reconciliation pass | Result |
|---|---|
| Claim Triage Matrix (27 claims) | 11 source-conflicted and 4 internally-derived claims resolved |
| Independent recomputation | **10 arithmetic/transcription errors** found in the drafts |
| Live federal-source verification | BLS and NAEP series re-pulled; NAEP confirmed the 24-point gap and ~144-year parity horizon |
| Governance-document audit | **3 canonical counts** in the Stack Truth Table found stale (15,578→15,507 tracts; 50→49 cities) |
| Published-index audit | **8 tracts** found carrying imputation artifacts, including the corpus's top-ranked tract |

Every correction is enumerated in [`metadata/CORRECTIONS_LEDGER.md`](metadata/CORRECTIONS_LEDGER.md) and printed as **Appendix H** of the paper, with the original claim and the verified value side by side.

Notable withdrawals: the unsourced "$4.5 billion Section 3 gap"; the "never below 2× unemployment" and "never below 5.7× incarceration" floor claims; the "five compound catastrophe zones" list that did not match the instrument's own ranking.

**Reproducing the PDF (deterministic):** `./build/rebuild.sh` (or `.\build\rebuild.ps1` on Windows) builds the pinned container in `build/Dockerfile` and regenerates `final/measure_of_the_wound.html` and `final/The_Measure_of_the_Wound.pdf`. Two runs on the same commit are byte-identical; compare against `final/The_Measure_of_the_Wound.pdf.sha256`. Procedure and rationale in [`build/REPRODUCING.md`](build/REPRODUCING.md). Without Docker: `python3 final/build.py` on any host with `markdown` and `weasyprint` (visually identical; hash may differ).

---

## REPO STRUCTURE

```
bdi-black-paper/
├── README.md                          ← You are here
├── OUTLINE.md                         ← Detailed chapter-by-chapter outline
│
├── drafts/                            ← Working drafts (living documents)
│   ├── 00_PREFACE.md
│   ├── 01_INTRODUCTION.md
│   ├── 02_CHAPTERS_1_2.md
│   ├── 03_CHAPTER_3_METHODOLOGY.md
│   ├── 04_CHAPTER_4_MEASURE.md
│   ├── 05_CHAPTER_5_ECONOMIC.md
│   ├── 06_CHAPTER_6_HEALTH_JUSTICE_EDUCATION.md
│   ├── 07_CHAPTER_7_COMPOUND.md
│   ├── 08_CHAPTER_8_POLICY.md
│   ├── 09_CONCLUSION.md
│   ├── 10_APPENDICES.md
│   └── 11_REFERENCES.md
│
├── final/                             ← Built edition (from drafts/ via build.py)
│   ├── build.py                       ← Deterministic HTML+PDF build
│   ├── print.css
│   ├── measure_of_the_wound.html
│   ├── The_Measure_of_the_Wound.pdf
│   └── The_Measure_of_the_Wound.pdf.sha256
│
├── build/                             ← Pinned container for byte-identical rebuilds
│   ├── Dockerfile
│   ├── requirements.txt
│   ├── rebuild.sh / rebuild.ps1
│   └── REPRODUCING.md
│
├── data/                              ← Wrangled data support files
│   ├── SOURCES.md                     ← Full source citation table
│   ├── pillar_summaries/              ← Per-pillar statistical extracts
│   └── figures/                       ← Charts, tables, visualizations
│
├── peer-review/                       ← Reviewer comments and responses
│   ├── REVIEW_GUIDE.md               ← Instructions for reviewers
│   └── responses/                     ← Author responses to reviewer comments
│
└── metadata/                          ← Provenance, DAGs, seals
    ├── DATA_PROVENANCE.md
    ├── COUNTING_METHODOLOGY.md
    └── BLOCKCHAIN_SEALS.md
```

---

## THE STACK (sibling repositories)

This paper draws from a four-layer public data stack. All repositories are CC0 licensed.

| Repo | Role | Link |
|------|------|------|
| `bdi-raw-data-vault` | Layer 1 — Raw federal evidence archive (~14,811 points) | [GitHub](https://github.com/IAMGODIAM/bdi-raw-data-vault) |
| `bdi-sovereign-dataset` | Product A — Synthesized 8-pillar instrument (1,574 observations) | [GitHub](https://github.com/IAMGODIAM/bdi-sovereign-dataset) |
| `farmblock-data` | Product B — Tract-level distress scoring (15,507 tracts, 49 cities) | [GitHub](https://github.com/IAMGODIAM/farmblock-data) |
| `farmblock-dataset` | Product B (county pilot) — Phase 2 county publication | [GitHub](https://github.com/IAMGODIAM/farmblock-dataset) |

---

## CITATION

> Armstead, Israel Lee. (2026). *The Measure of the Wound: A Sovereign Empirical Record of Black American Structural Distress, 1991–2024.* Corrected Print Edition v1.4. E5 Enclave Incorporated. CC0 1.0 Universal. GitHub: IAMGODIAM/bdi-black-paper · publication package: IAMGODIAM/measure-of-the-wound

---

## PROVENANCE

- **Organization:** E5 Enclave Incorporated, a 501(c)(3) public charity
- **Leadership:** Israel Lee Armstead, President & Chief Visionary
- **Physical base:** Liberty City, Miami, Florida
- **Intellectual tradition:** W.E.B. Du Bois (*The Philadelphia Negro*, 1899) · James Baldwin · Ralph McCartney (Overtown, Miami)
- **Standard:** *Nil satis nisi optimum* — Nothing but the best is good enough

---

*Dum spiro, spero — While I breathe, I hope.*
