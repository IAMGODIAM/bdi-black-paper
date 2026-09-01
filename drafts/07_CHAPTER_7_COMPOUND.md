# CHAPTER 7 — THE COMPOUND CATASTROPHE

> *"They have their plans set decades and scores in advance... 50 to 60 years ago these plans were on the books and it's coming to pass every day."*
> — Ralph McCartney, Overtown, Miami, 1997

Eight pillars measured separately produce eight findings. Measured together, they produce something the separate measurements cannot see: places where every pillar has failed simultaneously, and where the failures feed each other faster than any single-pillar remedy can reach them.

A county with high poverty is a poor county. A county with high poverty, the highest hypertension prevalence in its comparison universe, no acute-care hospital, twenty-eight percent of its housing stock vacant and thirty percent of its residents without home internet is not a poor county. It is a county in which each condition forecloses the escape route from the others. No hospital means telehealth; no internet means no telehealth. Vacancy means no property tax base; no tax base means no hospital.

This chapter measures that interaction. It is also the chapter in which this paper's own instrument is subjected to the same scrutiny the instrument applies to everyone else.

---

## 7.1 The FarmBlock Distress Index

The FDI is a place-level composite operating at two resolutions.

**County layer** (24-county published pilot):

```
FDI_county = poverty(0.25) + health_burden(0.25) + digital_exclusion(0.20)
           + vacancy(0.15) + Black_pct_proxy(0.15)
```

**Tract layer** (15,507 tracts), which deliberately excludes racial composition entirely:

```
FDI_tract = (D1_poverty + D2_income_deficit + D3_food_access
           + D4_health + D5_vacancy + D6_digital) / 6 × 100
```

All dimensions are min–max normalized across the corpus before compositing. The two instruments are built differently on purpose: the county formula includes Black population share at 15 percent as a structural-exposure proxy; the tract formula uses structural dimensions only. Where the two agree, the agreement is not an artifact of the race variable, because one of them does not contain it.

The rationale for the county proxy is set out in full in Appendix E, along with the strongest objection to it — that including racial composition in an instrument used to demonstrate racial disparity risks circularity. The tract instrument exists partly as the answer to that objection.

---

## 7.2 The Ranked Counties

**Table 7.1 — FarmBlock County Distress Index, top 12 of 24 published**

| Rank | County | FDI | % Black | Poverty | Median income | No internet | Vacancy | Hypertension |
|---|---|---|---|---|---|---|---|---|
| 1 | **Humphreys, MS** | **87.25** | 80.0% | 35.0% | $24,000 | 30.0% | 28.0% | 51.7% |
| 2 | **Claiborne, MS** | **85.26** | 83.0% | 35.0% | $26,000 | 28.0% | 25.0% | 50.0% |
| 3 | **Sunflower, MS** | **78.34** | 72.0% | 32.0% | $28,000 | 26.0% | 24.0% | 48.0% |
| 4 | **Alexander, IL** | **77.38** | 33.2% | 21.4% | $40,365 | 38.2% | 42.4% | 47.9% |
| 5 | **Amite, MS** | **70.86** | 40.2% | 27.1% | $34,866 | 30.2% | 19.3% | 43.2% |
| 6 | East Carroll, LA | 70.02 | 67.0% | 40.3% | $30,856 | 29.7% | 28.3% | 49.6% |
| 7 | Adams, MS | 68.31 | 53.4% | 27.2% | $37,271 | 17.3% | 22.0% | 51.7% |
| 8 | Barbour, AL | 65.68 | 46.9% | 24.2% | $39,712 | 24.3% | 22.8% | 46.4% |
| 9 | Ashley, AR | 59.55 | 24.8% | 23.3% | $44,804 | 23.6% | 23.7% | 41.4% |
| 10 | Gadsden, FL | 57.98 | 55.0% | 22.0% | $45,000 | 18.0% | 14.0% | 40.0% |
| 11 | Wayne (Detroit), MI | 56.79 | 40.0% | 22.0% | $54,000 | 16.0% | 20.0% | 38.0% |
| 12 | St. Louis City, MO | 55.43 | 44.0% | 22.0% | $51,020 | 14.0% | 18.0% | 43.0% |

**A correction to this paper's own framing.** Earlier drafts named five "compound catastrophe zones": Humphreys County, Detroit, East St. Louis, Claiborne County, and the Louisiana petrochemical corridor. That list does not match the instrument's output and is withdrawn.

The instrument's actual top five are **Humphreys, Claiborne, Sunflower, Alexander and Amite** — four Mississippi Delta counties and one Illinois river county. Wayne County (Detroit) ranks eleventh at 56.79, thirty points below Humphreys. East St. Louis sits in St. Clair County, Illinois, which is not in the published corpus at all; Alexander County, Illinois — rank four — is Cairo, a different place with a different history.

The five originally named were selected for documentary depth, not by score. Detroit and Cancer Alley belong in this paper, and they appear below as case studies with their actual standing disclosed. But a composite index that names a top five must name the top five the composite produced. Substituting the more familiar cities would have been the exact failure this instrument exists to prevent.

---

## 7.3 Humphreys County, Mississippi

FIPS 28053. Population approximately 7,400 and falling. FDI 87.25 — the highest score in the corpus.

**Table 7.2 — Humphreys County score decomposition**

| Component | Raw value | Normalized | Weight | Contribution |
|---|---|---|---|---|
| Poverty | 35.0% | 1.000 | 0.25 | 0.250 |
| Health burden | 36.15% (mean of diabetes 20.6, hypertension 51.7) | 1.000 | 0.25 | 0.250 |
| Digital exclusion | 30.0% no internet | 0.447 | 0.20 | 0.089 |
| Vacancy | 28.0% | 0.419 | 0.15 | 0.063 |
| Structural exposure (% Black) | 80.0% | 0.964 | 0.15 | 0.145 |

Humphreys sits at the corpus ceiling on both of the highest-weighted components. **51.7 percent hypertension prevalence** — in a county where high blood pressure is the statistical majority condition, not the exception. The nearest acute-care hospital option disappeared when Humphreys County Medical Center closed in **2013**; thirteen years later, three in ten residents have no home internet, which means the telehealth substitute is unavailable to the same households.

The county qualifies as low-income, low-access under USDA Food Access Research Atlas criteria. *An earlier draft stated "no grocery store within fifteen miles." USDA FARA does not use a fifteen-mile threshold — its measures are 0.5, 1, 10 and 20 miles — and the claim is replaced with the designation the federal instrument actually issues.*

**On poverty, three figures and why all three appear.** ACS 2015–2019 recorded 36.4 percent all-persons poverty; ACS 2022 recorded 32.1 percent, with **55.0 percent of children** below the line; the most recent ACS five-year release reports approximately 27 percent, with a margin of error of ±6.3 points. Earlier drafts used "37 percent" without a vintage lock. All three vintages are printed here because in a county of 7,400 the survey margin is wide enough that a single figure asserted without its interval is not a finding — it is a rounding decision presented as one. The decline is also not straightforwardly good news: Humphreys has lost roughly a third of its population since 1980, and a poverty rate calculated on a shrinking denominator measures departure as much as improvement.

**On the score itself.** The published FDI is 87.25. Recomputing the five components by hand against approximate corpus bounds yields **79.7** — a gap of roughly 7.5 points, arising because the published score normalizes against the full Phase 3 corpus while a hand calculation uses approximate range endpoints. The published figure stands as the citation of record. The discrepancy is printed rather than smoothed because Humphreys is this paper's flagship example, and a flagship example that cannot be audited is a slogan.

---

## 7.4 The Cases the Index Ranks Lower

### Detroit — Wayne County, Michigan (rank 11, FDI 56.79)

Wayne County's composite is thirty points below Humphreys, and the reason is instructive rather than exculpatory. Detroit has infrastructure: hospitals, broadband, a tax base, transit. Its distress is concentrated and internal rather than county-wide. The tract layer shows this directly — across **587 Detroit tracts** the median FDI is 33.9 while the maximum reaches **68.8**. The county average conceals a distribution in which specific neighborhoods score in Delta territory while others do not.

This is the strongest argument for the tract instrument. County-level analysis of a large metropolitan county will systematically understate concentrated urban distress, because the affluent tracts and the abandoned tracts are averaged into a single unremarkable number. Detroit's problem is not that the county is uniformly distressed. It is that the distressed parts are as distressed as rural Mississippi and are politically invisible inside a county average.

### The Louisiana corridor

The petrochemical corridor does not appear as a single ranked unit because it is not a county — it spans several parishes along an 85-mile stretch, and the burden is concentrated in fence-line tracts rather than distributed across parish geography. East Carroll Parish, Louisiana ranks sixth at 70.02 with the highest poverty rate in the corpus (40.3 percent), but East Carroll is in the northeast Delta, not the industrial corridor.

The corridor's documentation is therefore tract-level and is presented in Chapter 6: fence-line census tracts in St. James Parish Districts 4 and 5 are 65 to 94 percent Black, against a parish-wide figure of approximately 44 percent. The instrument that captures this is the tract instrument, and the geography that matters is the tract geography.

---

## 7.5 The Tract Layer: 15,507 Tracts, 49 Cities

**Table 7.3 — Highest-distress cities by median tract FDI**

| City | Tracts | Median FDI | Max FDI | Median poverty | Median % Black |
|---|---|---|---|---|---|
| Albany, GA | 29 | 49.5 | 70.8 | 27.5% | 70.6% |
| Jackson, MS | 67 | 45.3 | 62.5 | 24.2% | 85.7% |
| Macon, GA | 48 | 41.9 | 74.1 | 26.8% | 51.5% |
| Shreveport, LA | 73 | 39.9 | 71.0 | 19.0% | 52.4% |
| Bronx, NY | 348 | 39.0 | 58.2 | 25.0% | 32.0% |
| St. Louis, MO | 104 | 38.6 | 67.2 | 21.0% | 44.3% |
| Augusta, GA | 56 | 37.6 | 62.0 | 19.7% | 60.7% |
| New Orleans, LA | 182 | 35.3 | 66.2 | 20.9% | 58.5% |
| Detroit, MI | 587 | 33.9 | 68.8 | 19.3% | 31.0% |
| Baltimore, MD | 199 | 33.4 | 65.8 | 19.7% | 71.7% |

The gap between median and maximum in every row is the finding. Macon's median tract scores 41.9 and its worst scores 74.1. Detroit's median is 33.9 and its worst is 68.8. **Distress is not distributed across these cities. It is concentrated inside them**, which is why place-based intervention has to be targeted below the city level to reach it.

### 7.5.1 Corrections to the published counts

Three canonical figures in this paper's own governance documents were found to be stale and are corrected here.

| Claim | Previously locked | **Verified** |
|---|---|---|
| Tracts scored | 15,578 | **15,507** |
| Cities | 50 | **49** (48 distinct names; Columbus appears in both GA and OH) |
| Counties, tract layer | — | 49 |

The Stack Truth Table of April 18, 2026 locked 15,578 tracts and 50 cities as "verified row counts," and explicitly instructed that the pipeline manifest's lower city figure be corrected upward to match. Direct row counts of the published files show the opposite: the manifest was right and the truth table was wrong. The manifest records the reason — **Selma, Alabama was removed at version 2.1 because its rows duplicated Montgomery County** — a deduplication performed after the truth table was written and never propagated to it.

Every downstream figure in this paper has been rebuilt on 15,507 and 49.

### 7.5.2 A defect in the published tract file

Eight of the 15,507 tracts carry an imputation artifact that inflates their scores, and one of them is the highest-scoring tract in the corpus.

All eight share a signature: `poverty_rate` set to exactly 100.0 alongside `median_hh_income` set to exactly $75,738.50 — the corpus median, a fill value. Several also carry `pct_no_internet` at 5.879292, likewise a corpus mean. These are tracts where the Census returned suppressed or null values, and the pipeline substituted a maximum for one field and a central-tendency fill for another.

The consequence is concrete. **Census Tract 106.06, Muscogee County, Georgia — the top-ranked tract in the entire dataset at FDI 79.42 — is one of these eight.** It records 100 percent poverty, 100 percent without internet, and a $75,738 median household income simultaneously, which is not a possible combination. It is a group-quarters tract on a military installation. Its inflated score also sets the reported maximum for Columbus, Georgia in the published city rankings.

Because the tract instrument min–max normalizes across the corpus, an artificially maximal tract compresses every other tract's normalized position on the affected dimensions. The eight rows are enumerated in Appendix E and flagged for exclusion in FDI v3.0.

A second, opposite-direction issue: **398 tracts — 2.6 percent of the corpus — have the D4 health dimension imputed to zero** where CDC PLACES data was unavailable. That choice is conservative and it understates distress in exactly the data-sparse places most likely to be distressed.

Neither defect changes the county rankings or any finding in Chapters 5 or 6. Both are disclosed because the alternative — publishing an index whose top-ranked unit is an artifact, and waiting to see whether anyone checks — is the practice this paper was built to refuse.

---

## 7.6 What Targeting Means

The FarmBlock instrument exists to answer an operational question: given finite capacity, where does intervention go first?

The answer the data gives is not the answer political attention gives. The highest-distress places in this corpus are small Delta counties with declining populations and no organized constituency — Humphreys, Claiborne, Sunflower, Amite — and one Illinois river county, Alexander, whose profile is driven by 42.4 percent housing vacancy and 38.2 percent digital exclusion rather than by poverty alone.

These places are not where cameras go. They are where the composite says the compound burden is heaviest.

That is the entire argument for building the instrument. A ranked, auditable, publicly available composite makes it possible to direct resources by measured burden rather than by visibility — and to be held accountable when the direction chosen does not match what the measurement says.

Chapter 8 turns to what the full record demands.
