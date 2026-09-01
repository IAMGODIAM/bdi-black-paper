# APPENDICES

## APPENDIX A — SOURCE CITATION TABLE

Every series used in this paper, with the agency, instrument, coverage and vault location. All raw files were committed unmodified to `bdi-raw-data-vault` before any analysis was performed.

| # | Series | Agency &amp; instrument | Years | Vault file |
|---|---|---|---|---|
| 1 | Unemployment by race | Bureau of Labor Statistics<br/>CPS, series LNS14000006 / LNS14000003 | 1972–2025 | `economic/bls_unemployment_by_race_1972-2025_FULL_RAW.json` |
| 2 | State unemployment | Bureau of Labor Statistics<br/>LAUS | 2010–2024 | `economic/tier1_state_bls_unemployment_2010-2024_RAW.json` |
| 3 | Homeownership, income | Census Bureau<br/>ACS 1-year, B25003B/H, B19013B/H | 2005–2022 | `economic/census_acs_homeownership_income_RAW.json` |
| 4 | Poverty | Census Bureau<br/>ACS 1-year, B17001B/H | 2005–2022 | `economic/census_acs_poverty_RAW.json` |
| 5 | Family wealth | Federal Reserve Board<br/>Survey of Consumer Finances, triennial | 1989–2022 | `economic/fed_reserve_scf_wealth_usda_land_RAW.json` |
| 6 | Black farmland | USDA NASS<br/>Census of Agriculture | 1910–2022 | `economic/fed_reserve_scf_wealth_usda_land_RAW.json` |
| 7 | State economics | Census Bureau<br/>ACS 5-year, all states | 2010–2022 | `economic/tier1_state_economics_ACS_2010-2022_RAW.json` |
| 8 | Metro economics | Census Bureau<br/>ACS 5-year, 516+ MSAs | 2015–2022 | `economic/tier2_metro_msa_economics_ACS_2015-2022_RAW.json` |
| 9 | County economics | Census Bureau<br/>ACS 5-year, 3,222 counties | 2015–2022 | `economic/tier3_county_economics_ACS5Y_2015-2022_RAW.json` |
| 10 | Life expectancy, maternal mortality | NCHS<br/>National Vital Statistics Reports | 1900–2022 | `health/nchs_life_expectancy_maternal_mortality_RAW.json` |
| 11 | Imprisonment by race | Bureau of Justice Statistics<br/>Prisoners series; Cahalan 1986 for pre-1980 | 1925–2022 | `criminal_justice/bjs_incarceration_mpv_killings_RAW.json` |
| 12 | Police killings | Mapping Police Violence *(non-federal)*<br/>MPV public database | 2013–2023 | `criminal_justice/bjs_incarceration_mpv_killings_RAW.json` |
| 13 | NAEP score gaps | NCES<br/>Main Assessment, reading and mathematics | 1992–2022 | `education/tier1_naep_score_gaps_national_1992-2022_RAW.json` |
| 14 | Educational attainment | Census Bureau<br/>ACS B15002, all states | 2022 | `education/tier1_state_education_attainment_2022_RAW.json` |
| 15 | Historical homeownership; voter turnout | Census Bureau<br/>Census of Housing; CPS P20 November supplement | 1940–2010; 1964–2020 | `housing/census_decennial_homeownership_1940-2010_RAW.json` |
| 16 | Mortgage denial; eviction | CFPB / FFIEC; Princeton Eviction Lab<br/>HMDA; Eviction Lab national dataset | 1993–2022; 2000–2016 | `housing/hmda_mortgage_denial_eviction_RAW.json` |
| 17 | Transatlantic slave trade | Slave Voyages, Emory University<br/>Trans-Atlantic Slave Trade Database, 2023 edition | 1514–1866 | `historical/slavevoyages_1514-1866_aggregate_RAW.json` |
| 18 | County Black population share | Census Bureau<br/>ACS B02001 | 2022 | `demographics/tier3_county_black_population_pct_2022_RAW.json` |

**Supplementary sources cited in text:** HUD Office of Inspector General, *Audit of HUD's Section 3 Program*, 2013-AT-0003 (March 28, 2013); Graetz et al., *PNAS* (2023), eviction and filing rates by race; EPA EJScreen via Public Environmental Data Partners (removed from EPA.gov February 5, 2025); Tessum et al. (2021); Mikati et al. (2018); CDC PLACES 2023; USDA Food Access Research Atlas 2019; HRSA Area Health Resources File.

**Primary-source qualitative evidence:** McCartney, Ralph, oral history interview, August 14, 1997, Samuel Proctor Oral History Program, University of Florida / Black Archives of South Florida. Meek, Carrie P., Congressional Record, 103rd Congress, February 1, 1994, p. 723.

---

## APPENDIX B — COUNTING METHODOLOGY

**The rule.** One data point equals one row in a time series, or one unique observation record.

**Included:** each year of an annual series; each census decade in a decennial series; each year × race combination in a stratified series; each year × grade combination in NAEP.

**Excluded:** JSON metadata keys (`source`, `pillar`, `notes`, `verification_note`); text-only records carrying no numeric observation; duplicate series committed from the same source in more than one file.

**The correction of record.** The dataset was publicly described at one point as containing **1,855 data points**. That count included metadata keys as though they were observations. Applying the rule above yields **1,574 verified empirical observations**. The corrected figure is used in every public statement, is recorded in the dataset JSON itself (`total_data_points_original_claim: 1855`, with a correction note), and appears in this paper's Introduction rather than only in a methods note.

**Tier breakdown of the raw vault (~14,811 observations):**

| Tier | Scope | Observations |
|---|---|---|
| Tier 1 | National series | 479 |
| Tier 1 | State series | 358 |
| Tier 2 | Metro / MSA (516+ areas) | 1,550 |
| Tier 3 | County (3,222 counties) | 12,382 |
| Historical | 1514–1866 aggregates | 42 |

---

## APPENDIX C — PILLAR SUMMARY

| Pillar | Weight | Headline finding | Series span |
|---|---|---|---|
| Economic | 20% | Real wealth gap widened $154,830 → $240,120 (widest on record) while the ratio nearly tripled, 0.056 → 0.158 | 1972–2025 |
| Health | 20% | Maternal mortality ratio 1.48 (1930) → 2.61 (2022); Black life expectancy −4.0 years, 2019–2021 | 1900–2022 |
| Criminal justice | 20% | Imprisonment ratio 6.45 (1925) → 6.31 (2022); moved 0.14 points in 97 years | 1925–2023 |
| Education | 15% | Grade 8 reading gap 29.6 → 24.5 points; ~144 years to parity at observed rate | 1992–2022 |
| Housing | 10% | Homeownership gap 28.9 pp in 2022 vs ~24 pp when the Fair Housing Act passed | 1940–2023 |
| Environmental | 10% | Fence-line tracts, St. James Parish Districts 4–5: 65–94% Black vs ~44% parish-wide | 2015–2022 |
| Political | 5% | 2012 the only year Black turnout exceeded white (+2.5); −8.3 by 2020 | 1964–2020 |
| Historical | context only | 12,521,337 embarked; 1,818,681 lost; 13.5M acres of farmland lost 1910–1997 | 1514–1997 |

---

## APPENDIX D — THE RANKED COMPOUND DISTRESS COUNTIES

FarmBlock County Distress Index, Phase 2 published pilot, n = 24.

| Rank | County | FDI | Rank | County | FDI |
|---|---|---|---|---|---|
| 1 | Humphreys, MS | 87.25 | 13 | Acadia, LA | 55.28 |
| 2 | Claiborne, MS | 85.26 | 14 | Accomack, VA | 54.37 |
| 3 | Sunflower, MS | 78.34 | 15 | Benton, TN | 51.59 |
| 4 | Alexander, IL | 77.38 | 16 | Adams, WI | 50.89 |
| 5 | Amite, MS | 70.86 | 17 | Bronx, NY | 50.43 |
| 6 | East Carroll, LA | 70.02 | 18 | Adams, OH | 48.85 |
| 7 | Adams, MS | 68.31 | 19 | Tallapoosa, AL | 48.36 |
| 8 | Barbour, AL | 65.68 | 20 | Ashtabula, OH | 45.70 |
| 9 | Ashley, AR | 59.55 | 21 | Allegany, MD | 43.14 |
| 10 | Gadsden, FL | 57.98 | 22 | Essex (Newark), NJ | 42.83 |
| 11 | Wayne (Detroit), MI | 56.79 | 23 | Fresno, CA | 40.03 |
| 12 | St. Louis City, MO | 55.43 | 24 | Allen, IN | 34.47 |

*Earlier drafts named a "five compound catastrophe zones" list — Humphreys, Detroit, East St. Louis, Claiborne and Cancer Alley — that did not correspond to this ranking. Detroit ranks 11th. East St. Louis lies in St. Clair County, Illinois, which is not in this corpus. The list is withdrawn; the ranking above stands.*

---

## APPENDIX E — FARMBLOCK METHODOLOGY AND KNOWN DEFECTS

### E.1 Formulas

**County (Phase 2, n = 24):**
```
FDI_county = normalize(poverty_rate)                        × 0.25
           + normalize(mean(diabetes_pct, hypertension_pct)) × 0.25
           + normalize(pct_no_internet)                      × 0.20
           + normalize(vacancy_rate)                         × 0.15
           + normalize(pct_black)                            × 0.15
```

**Tract (v2.0, n = 15,507):**
```
FDI_tract = (D1_poverty + D2_income_deficit + D3_food_access
           + D4_health + D5_vacancy + D6_digital) / 6 × 100
```
where `normalize(x) = (x − corpus_min) / (corpus_max − corpus_min)`, and the tract formula contains **no racial composition variable**.

### E.2 The `% Black` variable, and the objection to it

The county formula includes Black population share at 15 percent weight as a structural-exposure proxy: the theoretical basis is that communities with higher Black population concentration have been subjected to greater documented disinvestment, redlining and exclusion, and that the variable therefore captures accumulated exposure to systemic risk rather than any intrinsic characteristic.

**The strongest objection is that this is partly circular.** An index that includes racial composition and is then used to demonstrate racial disparity in outcomes has assumed part of what it sets out to show. This objection is legitimate and is not dismissed here.

Two responses, offered as arguments rather than refutations. First, the tract instrument excludes the variable entirely and produces convergent results — the highest-distress tracts are overwhelmingly majority-Black without the formula being told to look for that. Second, the county weights were sensitivity-tested and alternative weight sets produce similar rank orderings among high-distress counties. Readers who find the objection dispositive should use the tract instrument, which was built partly for them.

### E.3 Humphreys County decomposition

| Component | Raw | Normalized | Weight | Contribution |
|---|---|---|---|---|
| Poverty | 35.0% | 1.000 | 0.25 | 0.250 |
| Health burden | 36.15% | 1.000 | 0.25 | 0.250 |
| Digital exclusion | 30.0% | 0.447 | 0.20 | 0.089 |
| Vacancy | 28.0% | 0.419 | 0.15 | 0.063 |
| Structural exposure | 80.0% | 0.964 | 0.15 | 0.145 |
| **Hand-calculated total** | | | | **0.797 → 79.7** |
| **Published score** | | | | **87.25** |

The published score normalizes against the full Phase 3 corpus; the hand calculation above uses approximate range endpoints, producing a 7.5-point difference. The published figure is the citation of record. The discrepancy is printed rather than reconciled away.

### E.4 Known defects in the published tract file

**Eight tracts carry imputation artifacts.** Each has `poverty_rate` filled to exactly 100.0 alongside `median_hh_income` filled to exactly $75,738.50 — the corpus median. Several also carry `pct_no_internet` at the corpus mean. These are rows where the Census returned suppressed or null values and the pipeline substituted a maximum for one field and a central-tendency fill for another.

| FIPS tract | City | Pop | FDI | Fills |
|---|---|---|---|---|
| 13215010606 | Columbus, GA | 1815 | 79.42 | poverty=100.0; income=corpus median; no_internet=100.0 |
| 36005031900 | Bronx, NY | 762 | 58.19 | poverty=100.0; income=corpus median; no_internet=100.0 |
| 06037980014 | Los Angeles, CA | 40 | 58.08 | poverty=100.0; income=corpus median |
| 45079010806 | Columbia, SC | 876 | 45.41 | poverty=100.0; income=corpus median; no_internet=corpus mean |
| 45079010408 | Columbia, SC | 4243 | 43.01 | poverty=100.0; income=corpus median; no_internet=corpus mean |
| 04013981000 | Phoenix, AZ | 696 | 42.22 | poverty=100.0; income=corpus median; no_internet=corpus mean |
| 12057010900 | Lakeland, FL | 7218 | 31.37 | poverty=100.0; income=corpus median |
| 12011980000 | Jacksonville, FL | 2 | 31.12 | poverty=100.0; income=corpus median; no_internet=corpus mean |

The first row is the highest-scoring tract in the entire published corpus. It reports 100 percent poverty, 100 percent without home internet, and a $75,738 median household income simultaneously — an impossible combination. It is a group-quarters tract on a military installation, and its score also sets the reported maximum for Columbus, Georgia in the published city rankings.

Because the tract instrument min–max normalizes across the corpus, an artificially maximal tract compresses every other tract's normalized position on the affected dimensions. These eight rows are flagged for exclusion in FDI v3.0, and the imputation logic will be rebuilt to fail loudly rather than fill silently.

**398 tracts (2.6 percent) have D4 health imputed to zero** where CDC PLACES data was unavailable. This is conservative in the wrong direction: it understates distress in precisely the data-sparse places most likely to be distressed.

**Food-desert proxy.** USDA FARA direct download returned HTTP 404 at collection time. The substitute is `food_desert_proxy = 1 WHERE poverty_rate ≥ 20% AND median_household_income ≤ $65,000`, approximating the USDA low-income/low-access standard. Every row carries a `food_desert_source` flag distinguishing proxy-assigned from FARA-confirmed designations.

### E.4a Reproducibility status

**The FDI outputs in this paper are not independently reproducible from the published package.** That is the finding of the September 2026 independent review and it is accepted here without qualification.

What exists publicly: the scored output CSVs, the formulas, the weights, the normalization method, the Humphreys decomposition and the enumerated defects. What does not yet exist publicly: the raw pre-scoring inputs with ACS table identifiers, release years and geography codes; the full Phase 3 corpus that supplies the normalization bounds; the transformation code with a dependency lockfile; and a deterministic command that rebuilds every published score from raw inputs.

Until that package is released, a reader can audit the *logic* of the FDI and cannot audit its *arithmetic*. The distinction matters and it is stated plainly: the 87.25 score for Humphreys County, the 15,507 tract scores and the 49 city rankings should be cited as this organization's published outputs, not as independently verified results. Producing that package is the first deliverable of FDI v3.0.

### E.5 Verified corpus counts

| Quantity | Value | Basis |
|---|---|---|
| Tracts scored | **15,507** | direct row count, `processed/farmblock_fdi_v2.csv` |
| Cities | **49** | direct row count, `processed/farmblock_city_rankings.csv` (48 distinct names; Columbus appears in GA and OH) |
| Counties, tract layer | 49 | pipeline manifest v2.1 |
| Counties, published county pilot | 24 | direct row count, `farmblock_fdi_phase2.csv` |

*These supersede the Stack Truth Table values of 15,578 and 50, which were locked April 18, 2026 and did not incorporate the version 2.1 removal of duplicated Selma, Alabama rows.*

---

## APPENDIX F — PROVENANCE AND SEALS

| Asset | Contract | Token | Network |
|---|---|---|---|
| BDI Sovereign Dataset v1.0 | ExodusV4 `0x8582684C53912D496Df60C5B1B9Bb44D3d2f9B44` | #2 | Base Mainnet |

**Repositories, all CC0 1.0 Universal:**

| Repo | Layer | Contents |
|---|---|---|
| `IAMGODIAM/bdi-raw-data-vault` | Layer 1 | 18 raw federal source files, ~14,811 observations; reports and triage records |
| `IAMGODIAM/bdi-sovereign-dataset` | Layer 2 | 1,574 verified observations, 8 pillars; quantitative specification |
| `IAMGODIAM/farmblock-data` | Layer 3, tract | 15,507 tracts, 49 cities |
| `IAMGODIAM/farmblock-dataset` | Layer 3, county | 24-county published pilot |
| `IAMGODIAM/bdi-black-paper` | Layer 4 | This manuscript, drafts, peer review |

**Related campaign record:** the DC Package — nine policy packets delivered to congressional leaders and to Justice Clarence Thomas in July 2026, comprising a 166-page shared evidentiary record per packet — is published at `dc.e5enclave.com`. This paper is the empirical instrument underlying that record.

---

## APPENDIX G — ACKNOWLEDGMENTS AND INTELLECTUAL LINEAGE

W.E.B. Du Bois · Ida B. Wells · Harriet Tubman · Frederick Douglass · Nat Turner · Ella Baker · Malcolm X · James Baldwin · Cornel West · Melina Abdullah · The Movement for Black Lives

Ralph McCartney, Overtown, Miami · Congresswoman Carrie Meek · The Black Archives of South Florida · The Samuel Proctor Oral History Program, University of Florida

*Nil satis nisi optimum.*

---

## APPENDIX H — CORRECTIONS LEDGER

## A. ERRORS FOUND BY RECOMPUTATION (not previously flagged)

These are new. They were not in the April triage matrix; they surfaced when the drafts' arithmetic was rebuilt from the source series.

| # | Draft claim | Status | Verified value | Print-edition language |
|---|---|---|---|---|
| R-1 | "Black unemployment has never fallen below 2x the white rate" (Conclusion v2, v2.1) | **FALSE** | Ratio fell below 2.0 in **17 of 54 years**; low 1.576 (2020) | "The ratio has ranged from 1.58 to 2.56 and averaged 2.115 across 54 years. It has never inverted — not in one month of one year." |
| R-2 | "Below 1.86, no normal economic year has gone in more than half a century" (Report 3, Adj. 3) | **FALSE** | 2023 = 1.683, 2024 = 1.666 — both normal expansion years | Floor language removed. Replaced with the distributional statement above. |
| R-3 | "3,015 Black Americans killed by police 2013–2023; 377 unarmed" | **UNDERCOUNT** | Vault row sum: **3,496 killed; 397 unarmed** | Corrected to 3,496 and 397; aggregate Black share 26.7% of 13,096 total. |
| R-4 | "Incarceration ratio has never fallen below 5.7" | **FALSE** | 1991–2022 window minimum **5.80 (2018)**; full 1925–2022 series minimum 5.44 (1940); maximum 7.70 (2000) | "In the empirical window the ratio has not fallen below 5.8. Across the full 97-year series it has ranged 5.44 to 7.70." |
| R-5 | "Homeownership gap stands at 30.1 points today" | **WRONG VINTAGE** | ACS 2022: **28.9 pp**; ACS 2023 (NAR): 44.7% vs 72.4% = **27.7 pp** | "28.9 percentage points (ACS 2022); 27.7 points on the 2023 release." |
| R-6 | "Wealth ratio reaches parity in approximately 263 years" | **ARITHMETIC ERROR**, then **WITHDRAWN ENTIRELY** (see W-1) | The 263-year figure was miscalculated; the recomputed 868-year figure rested on a defective series; the corrected series yields 274 years from 1989 but 1,632 from 1992 and no convergence from 2001 | No parity horizon is asserted. The sensitivity table is printed in §5.1 instead. |
| R-7 | "The gap tripled in absolute dollars" | **IMPRECISE**, then **SUPERSEDED** (see W-1) | Nominal 2.893×; in constant 2022 dollars **1.55×**, $154,830 → $240,120 | "The absolute gap widened by $85,290 in real terms and is the widest in the series." |
| R-8 | "COVID erased 20 years of life expectancy gains in 18 months" | **TIMELINE WRONG** | Black life expectancy fell **4.0 years** across **two calendar years** (74.8 → 70.8, 2019→2021), returning to a mid-1990s level | "Between 2019 and 2021 — two years, not eighteen months — Black life expectancy fell four full years, to a level last seen in the mid-1990s." |
| R-9 | "NAEP gap... exists in 2022 as it did in 1992" (Conclusion) | **OVERSTATED** | G8 reading gap narrowed 29.6 → 24.5; G8 math 40 → 32; G4 reading 32 → 28 | Movement acknowledged and quantified; convergence rate stated. |
| R-10 | "Eviction rate three times the white rate" | **SCOPE UNSTATED** | Eviction Lab 2000–2016: 3.00–3.54×. Graetz et al. 2023 PNAS: ~4× evictions, ~4.8× filings | Both cited with explicit scope and instrument. |

---

## B. TRIAGE MATRIX RULINGS APPLIED (April 18, 2026 — 27 claims)

| ID | Ruling | Print-edition disposition |
|---|---|---|
| E-1 | source-confirmed → **REVERSED** (see W-1) | The 1989 endpoint could not be reconciled to the Federal Reserve's published race-specific medians under either price basis. Table rebuilt from the Fed's constant-2022-dollar series. |
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

## B2. SECOND-WAVE CORRECTIONS — INDEPENDENT REVIEW (v1.2)

On September 1, 2026 an independent review of the v1.1 print edition was conducted by Manus AI, working only from the published PDF, the corrections ledger and the supplied git bundle — with no access to this project's repositories. It found problems the internal audit had missed, and its principal finding is the most material error yet identified in this paper. The findings are adopted below.

**Why the internal audit missed them.** The recomputation pass described in §A verified that every derived figure followed correctly from the vault's stored series. It did. What it never asked was whether a stored series was itself coherent, or whether it reconciled to the agency's published figures. An internal consistency check cannot detect an incoherent input. The audit protocol is amended: **primary-source reconciliation of every series endpoint is now a required pass.**

| # | Claim | Finding | Print-edition disposition |
|---|---|---|---|
| **W-1** | **Table 5.1, the SCF wealth series; the "$83,000 → $240,100" gap; "nearly tripled"; the 3.2-cent ratio gain; the 868-year parity horizon** | **CRITICAL — series defective.** The table stated no price basis. Its 1989 endpoint ($12k / $95k) was nominal while its 2022 endpoint ($44.9k / $285k) was the Fed's constant-2022-dollar figure — a real endpoint back-filled with nominal history, whose apparent trend was substantially an inflation artifact. Worse, deflating the old 1989 values to 2022 dollars yields $28,321 and $224,211 against the Fed's published $9,200 and $164,030 — so they reconcile under **neither** basis, and their provenance was undocumented. | **Table rebuilt in full** from Federal Reserve FEDS Notes (Oct 18, 2023), Figure 2, constant 2022 dollars, families. Corrected findings: real gap **$154,830 → $240,120** (1.55×, +$85,290, widest in the series); ratio **0.056 → 0.158** (nearly tripled); Black median wealth **+388%** vs white **+74%**. The "nearly tripled gap," the 3.2-cent gain and the 868-year horizon are all withdrawn. |
| **W-2** | Parity projections (wealth and NAEP) | Presented with insufficient warning that they are mechanical extrapolations. The wealth horizon proves extremely baseline-sensitive: 274 years from 1989, 1,632 from 1992, 1,511 from 1995, 366 from 2007, 117 from 2013, and **no convergence at all** from 2001. | **No wealth parity horizon is asserted.** The full sensitivity table is printed in §5.1. The NAEP 144-year figure is retained but explicitly labelled an arithmetic extension of two endpoints, not a forecast. |
| **W-3** | Incarceration ratios, and "Black Americans were imprisoned at 6.31 times the white rate" | **Definition unverified and probably overstated in scope.** BJS publishes, for 2022, **1,196 per 100,000 Black adult residents and 229 per 100,000 white adult residents — a ratio of 5.22.** The series' 1,862 and 295 correspond closely to BJS *male* rates (≈1,826 and 279). The vault does not record the denominator, and the Cahalan (1986) pre-1980 crosswalk is undocumented. BJS also dates its series to 1926, not 1925. | Chapter 6 now prints the BJS all-adults ratio of **5.22** alongside the series ratio of 6.31, states that the basis is probably male rates, and stops writing "Black Americans" where the source may say "Black males." The stability finding, which holds on either basis, carries the argument. |
| **W-4** | 1930 maternal mortality ratio of 1.48, and the 1.76-fold widening | The pre-1933 figures come from the birth-registration states only, which were not nationally representative. The cross-era comparison is not strictly commensurable. | Caveat added in full. The 2022 ratio is confirmed directly against NCHS (49.5 ÷ 19.0 = 2.605 → 2.61). The chapter now notes that the direction holds across every intermediate decade, and offers the 2010→2022 rise (2.24 → 2.61), entirely within a fully registered system, to readers who reject the 1930 datum. |
| **W-5** | Unemployment ratios shown beside rounded annual rates | 5.5 ÷ 3.3 = 1.667, not the 1.683 printed. The discrepancy arises because ratios are computed from unrounded monthly data while the displayed component rates are rounded annual averages. | Aggregation rule now stated explicitly in §5.2, with the worked 2023 example (5.5167 ÷ 3.2750 = 1.685) and a vintage-revision note. The stored values are correct; the method was undisclosed. |
| **W-6** | Black farmland "13.5 million acres lost, 1910–1997" | The 15-million-acre peak's year and level are contested; some compilations place the maximum nearer 1900. | Note added. The 1997 figure of 1.5 million is well supported; the 90 percent loss is now framed against a peak carrying acknowledged uncertainty in year and level. |
| **W-7** | NAEP endpoint precision and comparability | NCES publishes rounded scores (267/237, 268/244) and discloses that 1992 permitted no testing accommodations while later years did. | Both disclosed in §6.6. |
| **W-8** | The supplied git bundle | **Unusable for independent review.** It was created incrementally (`main..branch`) and declares a prerequisite commit the reviewer did not have, so the repository tree, raw vault JSON and manifests could not be inspected at all. | Replaced with a **complete-history bundle** requiring no prerequisite. This was the single largest obstacle to the review and it was an avoidable packaging error. |
| **W-9** | Introduction's "Five Compound Catastrophe Zones" heading | Flagged as an apparent contradiction with the Chapter 7 ranking. | **Already corrected before the review was received** — the reviewer worked from the superseded v1.1 PDF. The Introduction now names the instrument's actual top five and states the withdrawal. |

**Findings acknowledged and not yet closed.** The review's three "critical" reproducibility actions are only partly satisfied by this edition. The complete bundle (W-8) addresses repository access. It does **not** yet supply a full data package for the FDI computation — raw inputs, normalization bounds, transformation code and a deterministic rebuild command — nor ACS table identifiers and geography codes for every Humphreys input. Until those exist, the correct characterisation is the reviewer's: **the FDI outputs are not independently reproducible from the supplied package.** Appendix E says so.

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
8. **The incarceration series' denominator is not established** (W-3). It is probably male rates; BJS's all-adults 2022 ratio is 5.22 against the series' 6.31. Both are printed. The crosswalk is owed.
9. **The FDI computation is not independently reproducible** from the published package (see Appendix E.4a). The reviewer's characterisation is adopted verbatim.
10. **The pre-1933 maternal mortality figures** rest on the birth-registration states only and are not nationally representative (W-4).
11. **Table 5.1 now depends on a single secondary presentation** of the SCF — the Federal Reserve's own FEDS Note — rather than on an extraction from SCF microdata performed by this project. That is an improvement in provenance and a reduction in independence. A microdata extraction with published code is owed.

---

*E5 Enclave Incorporated · EIN 99-3822441 · CC0 1.0 Universal*
