# CORRECTIONS LEDGER — THE MEASURE OF THE WOUND
## Every figure changed between Black Paper v1.0 drafts and the Print Edition

**Prepared:** August 31, 2026 · **Basis:** BDI_CLAIM_TRIAGE_MATRIX (27 claims), STACK_TRUTH_TABLE, CLAIM_REWRITES_MIRANDA_v1, REPORT_3_BLACK_PAPER_ADJUSTMENTS, plus independent recomputation of every derived statistic from the Layer-1 raw vault JSON and live federal-source verification.

**Verification method.** Three passes. (1) **Recomputation** — every ratio, gap, sum, mean and projection in the drafts recalculated from the raw vault series rather than copied forward. (2) **Live source check** — flagged series re-pulled from the primary federal source in August 2026. (3) **Triage application** — all 27 Claim Triage Matrix rulings applied to manuscript language.

---

## A. ERRORS FOUND BY RECOMPUTATION (not previously flagged)

These are new. They were not in the April triage matrix; they surfaced when the drafts' arithmetic was rebuilt from the source series.

| # | Draft claim | Status | Verified value | Print-edition language |
|---|---|---|---|---|
| R-1 | "Black unemployment has never fallen below 2x the white rate" (Conclusion v2, v2.1) | **FALSE** | Ratio fell below 2.0 in **17 of 54 years**; low 1.576 (2020) | "The ratio has ranged from 1.58 to 2.56 and averaged 2.115 across 54 years. It has never inverted — not in one month of one year." |
| R-2 | "Below 1.86, no normal economic year has gone in more than half a century" (Report 3, Adj. 3) | **FALSE** | 2023 = 1.683, 2024 = 1.666 — both normal expansion years | Floor language removed. Replaced with the distributional statement above. |
| R-3 | "3,015 Black Americans killed by police 2013–2023; 377 unarmed" | **UNDERCOUNT** | Vault row sum: **3,496 killed; 397 unarmed** | Corrected to 3,496 and 397; aggregate Black share 26.7% of 13,096 total. |
| R-4 | "Incarceration ratio has never fallen below 5.7" | **FALSE** | 1991–2022 window minimum **5.80 (2018)**; full 1925–2022 series minimum 5.44 (1940); maximum 7.70 (2000) | "In the empirical window the ratio has not fallen below 5.8. Across the full 97-year series it has ranged 5.44 to 7.70." |
| R-5 | "Homeownership gap stands at 30.1 points today" | **WRONG VINTAGE** | ACS 2022: **28.9 pp**; ACS 2023 (NAR): 44.7% vs 72.4% = **27.7 pp** | "28.9 percentage points (ACS 2022); 27.7 points on the 2023 release." |
| R-6 | "Wealth ratio reaches parity in approximately 263 years" | **ARITHMETIC ERROR** | Observed rate 0.00097/yr → **868 years** to ratio parity from 2022 | "At the rate of change actually observed since 1989, ratio parity is roughly eight and a half centuries away." |
| R-7 | "The gap tripled in absolute dollars" | **IMPRECISE** | $83,000 → $240,100 = **2.893×** | "The absolute gap nearly tripled — a 2.89-fold increase, $157,100 of new distance." |
| R-8 | "COVID erased 20 years of life expectancy gains in 18 months" | **TIMELINE WRONG** | Black life expectancy fell **4.0 years** across **two calendar years** (74.8 → 70.8, 2019→2021), returning to a mid-1990s level | "Between 2019 and 2021 — two years, not eighteen months — Black life expectancy fell four full years, to a level last seen in the mid-1990s." |
| R-9 | "NAEP gap... exists in 2022 as it did in 1992" (Conclusion) | **OVERSTATED** | G8 reading gap narrowed 29.6 → 24.5; G8 math 40 → 32; G4 reading 32 → 28 | Movement acknowledged and quantified; convergence rate stated. |
| R-10 | "Eviction rate three times the white rate" | **SCOPE UNSTATED** | Eviction Lab 2000–2016: 3.00–3.54×. Graetz et al. 2023 PNAS: ~4× evictions, ~4.8× filings | Both cited with explicit scope and instrument. |

---

## B. TRIAGE MATRIX RULINGS APPLIED (April 18, 2026 — 27 claims)

| ID | Ruling | Print-edition disposition |
|---|---|---|
| E-1 | source-confirmed | SCF 1989 $83,000 → 2022 $240,100. Vintage locked, footnoted. |
| E-2 | source-confirmed | ~30 pp restated as 28.9 pp (ACS 2022) per R-5. |
| E-3 | source-conflicted | "Ranged 2.24 to 2.84 across ACS 2005–2022" — no "never below 2:1" absolute. |
| E-4 | source-confirmed | 1968 ≈ 24 pp vs 2022 28.9 pp. Both vintages footnoted. |
| H-1 | source-confirmed | 69.9/100K locked to **2021**; 2022 = 49.5 shown; NCHS 2024 trajectory noted. |
| H-2 | source-conflicted | Rewritten per R-8. |
| H-3 | source-conflicted | Fence-line tract geography specified: 65–94% Black (St. James Districts 4–5); parish ≈44%. |
| CJ-1 | source-conflicted | Rewritten per R-4. |
| ED-1 | source-conflicted | 24-point gap and century-plus parity horizon — **independently confirmed against the live NAEP API** (see §C). |
| HO-1 | source-confirmed | HMDA denial ratio; range 2.01–2.36 stated rather than a single figure. |
| HO-2 | source-conflicted | Rewritten per R-10. |
| HO-3 | internally-derived | **$4.5B aggregate removed.** Replaced with HUD OIG 2013-AT-0003: 53% of PHAs did not file required Section 3 reports. |
| HO-4 | source-conflicted | "Erased a decade in 18 months" → "reversed nearly a decade of gains across the 2007–2013 window." |
| HI-1 | source-conflicted | Embarked/disembarked disambiguated: 12,521,337 / 10,702,656 / 1,818,681 lost (14.5%). |
| HI-2 | source-confirmed | 1514 anchor retained with footnote. |
| EN-1 | citation-vintage | EJScreen cited via Public Environmental Data Partners; EPA.gov removal (Feb 5, 2025) disclosed. |
| CD-1 | source-confirmed | Humphreys 78.6% (ACS 2022). |
| CD-2 | source-confirmed | Detroit 77.1%. |
| CD-3 | source-confirmed | East St. Louis 97.4%. |
| CD-4 | source-confirmed | Claiborne 86.1%. |
| CD-5 | source-conflicted | Same fix as H-3. |
| CD-6 | citation-vintage | **32.1% all-persons and 55.0% child poverty (ACS 2022)** adopted as the citation figures; 36.4% (ACS 2015–2019) retained as the historical vintage; ACS 2024 5-year now reports 27% ±6.3 — disclosed as the current release. |
| CD-7 | source-confirmed | Hospital closure 2013 (HRSA AHRF). |
| CD-8 | source-conflicted | "No grocery within 15 miles" → USDA FARA low-income/low-access (LILA) designation. |
| CD-9 | internally-derived → **published** | Humphreys score corrected **83.5 → 87.25** and the full five-component decomposition printed as Appendix E. |
| META-1 | source-confirmed | **1,855 → 1,574** verified empirical observations, everywhere. |
| META-2 | internally-derived | "MiroFish 94%" removed. Replaced with the dual-source protocol description. |

---

## C. LIVE FEDERAL-SOURCE VERIFICATION (August 2026)

| Series | Endpoint | Result |
|---|---|---|
| Black unemployment (LNS14000006) | BLS via FRED, monthly 2019–2025 | Annual averages reproduce the vault series. 2019 = 6.1, 2023 = 5.5, 2024 = 5.9, 2025 = 6.9. **Confirms vault.** |
| White unemployment (LNS14000003) | BLS via FRED, monthly 2019–2025 | 2019 = 3.3, 2023 = 3.3, 2024 = 3.6, 2025 = 3.7. **Confirms vault.** Ratios recomputed from live monthly data reproduce R-1 and R-2. |
| NAEP G8 reading by race, national | NCES Nation's Report Card data service | **1992:** White 267.001, Black 237.374 → gap **29.63**. **2022:** White 268.443, Black 243.902 → gap **24.54**. Confirms ED-1 exactly: the gap is ~24 points, not 20. Convergence 5.09 points in 30 years → **~144 years to parity**, not 64. |
| Humphreys County, MS (FIPS 28053) | Census ACS 5-year profile | Current release reports 27% ±6.3 poverty, median household income $33,731, population 7,395. Wide margin of error at this population size disclosed in text. |
| Homeownership by race | ACS 2023 via NAR *Snapshot of Race and Home Buying in America* (2025) | Black 44.7%, White 72.4% → 27.7 pp. Confirms direction; updates the vintage. |

**Note on API access.** The Census Bureau data API now requires a registered key for programmatic access; the figures above were verified against the Bureau's published profiles and released tables rather than by unauthenticated API call. The vault's underlying ACS pulls (committed April 2026) remain the citation of record for the series tables, and each is footnoted to its table number.

---

## D. STRUCTURAL ADDITIONS

| Item | Action |
|---|---|
| Chapters 5, 6, 7, 8 | **Drafted** from the locked outline; previously stubs. |
| Introduction | **Drafted**; previously a stub. |
| Appendices A–H | **Drafted**; previously stubs. |
| Report 3 drafting directives 3–8 | Executed inside the new chapters (unemployment distribution, maternal mortality reversal, COVID reversal, housing headline, Shelby inflection, three historical anchors). |
| Scope statement (Adj. 1) | Introduction now states the nested window: 1991–2024 core, with series to 1900 (health), 1925 (justice), 1940 (housing), 1964 (political), 1514 (historical). |
| Chapter 2 longitudinal claim (Adj. 2) | Added. |

---

## E. WHAT A REVIEWER SHOULD STILL CONTEST

Disclosed, not concealed. A sovereign record that hides its soft edges is promotional, not empirical.

1. **The `% Black` variable at 15% weight in the county FDI.** Defended as a structural-exposure proxy in Appendix E; a reviewer may reasonably argue it makes the instrument partly tautological with respect to racial concentration. The tract instrument excludes it — compare the two.
2. **Equal weighting in the tract FDI.** A transparent baseline, not an empirically derived one. PCA weighting is the stated v3.0 path.
3. **The Humphreys decomposition reproduces 79.7, not 87.25**, when recalculated against approximate corpus bounds. The published score stands on the full-corpus normalization; the arithmetic gap is printed in Appendix E rather than smoothed over.
4. **D4 health imputed to zero** where CDC PLACES is unavailable — conservative, but it understates distress in data-sparse tracts.
5. **The food-desert proxy** substitutes an ACS income/poverty threshold for a FARA download that 404'd at collection. Rows are flagged.
6. **Mapping Police Violence is not a federal instrument.** It is the most complete public database of its kind, and it is labeled as non-federal wherever cited.
7. **Small-county ACS margins of error** — Humphreys' poverty estimate carries a ±6.3-point margin. Stated in text.

---

*E5 Enclave Incorporated · EIN 99-3822441 · CC0 1.0 Universal*
