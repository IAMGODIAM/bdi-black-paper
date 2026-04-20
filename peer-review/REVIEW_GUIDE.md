# PEER REVIEW GUIDE
## The Measure of the Wound — Black Paper v1.0

**Publisher:** E5 Enclave Incorporated  
**Reviewing:** `IAMGODIAM/bdi-black-paper`

---

## How to Review This Paper

This paper uses an open peer review model. All reviewer comments are public and responded to publicly in `peer-review/responses/`.

### What Reviewers Should Evaluate

1. **Data accuracy** — Are the cited statistics verifiable against the source files in `bdi-raw-data-vault`?
2. **Counting methodology** — Is the data point counting rule in `bdi-sovereign-dataset/BDI_QUANT_SPEC.md` correct and applied consistently?
3. **Causal claims** — Does the paper distinguish between correlation and causation appropriately?
4. **Missing evidence** — Are there Federal sources that should be included but are not?
5. **Framing and language** — Does the language accurately represent what the data shows without over- or under-stating?
6. **Appendix completeness** — Are all source citations complete and verifiable?

### What Reviewers Should NOT Do

- Request softening of findings that are directly supported by the data
- Request removal of historical context that is documented primary-source evidence
- Apply standards that are not applied to comparable academic scholarship
- Suggest the dataset's conclusions are invalid because they are uncomfortable

### How to Submit Comments

Open a GitHub Issue in this repository with:
- Label: `peer-review`
- Title: `[REVIEW] Chapter X — [brief description]`
- Body: Specific claim, specific concern, specific alternative evidence if applicable

Author responses will be filed in `peer-review/responses/`.

---

## Data Access

All underlying data is public and CC0:

| Layer | Repo | What to check |
|-------|------|---------------|
| Raw federal sources | `bdi-raw-data-vault` | Primary source files in `/economic`, `/health`, `/criminal_justice`, etc. |
| Synthesized dataset | `bdi-sovereign-dataset` | `bdi_sovereign_dataset_v1.json` + `BDI_QUANT_SPEC.md` |
| FarmBlock application | `farmblock-data` | `processed/farmblock_fdi_v2.csv` |
| Counting methodology | `bdi-sovereign-dataset` | `BDI_QUANT_SPEC.md` |

---

*Open peer review. CC0. The data is the argument.*
