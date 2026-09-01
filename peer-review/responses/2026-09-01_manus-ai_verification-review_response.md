# AUTHOR RESPONSE TO INDEPENDENT VERIFICATION REVIEW

**Paper:** *The Measure of the Wound: A Sovereign Empirical Record of Black American Structural Distress, 1991–2024*
**Review under response:** *Verification Report — The Measure of the Wound*, Manus AI, September 1, 2026
**Edition reviewed:** Corrected Print Edition v1.1 (80 pp.)
**This response accompanies:** Corrected Print Edition **v1.2** (86 pp.)
**Publisher:** E5 Enclave Incorporated · EIN 99-3822441 · CC0 1.0 Universal

---

## Summary of disposition

**Nine findings. Seven accepted and implemented. One accepted and left open with a stated reason. One had already been corrected before the review arrived.** No finding is rejected.

The review's determination — *partially verified*, with the correction process real but the package not fully reproducible — was correct on the materials it was given, and remains correct in one respect after this revision. We say so below rather than claiming more than we can support.

**The review found the most serious error in this paper.** We are recording that plainly, because the mechanism by which we missed it is itself a finding, and because a project that publishes an errata appendix and then treats an outside critique defensively has misunderstood its own argument.

---

## 1. The finding that mattered: the SCF wealth series (W-1)

**Accepted in full. The table has been rebuilt from scratch.**

The reviewer observed that Table 5.1 stated no price basis, that its 2022 endpoint matched the Federal Reserve's constant-2022-dollar race-specific medians while its 1989 endpoint did not, and that the resulting comparison could not support the paper's claims.

On verification the problem proved worse than a labelling defect.

| | Black median | White median | Gap |
|---|---|---|---|
| Old table, 1989 | $12,000 | $95,000 | $83,000 |
| Old table deflated to 2022 dollars (CPI-U factor 2.360) | $28,321 | $224,211 | — |
| **Federal Reserve, 1989, constant 2022 dollars** | **$9,200** | **$164,030** | **$154,830** |
| Old table, 2022 | $44,900 | $285,000 | $240,100 |
| **Federal Reserve, 2022** | **$44,890** | **$285,010** | **$240,120** |

The old 1989 figures reconcile with the Federal Reserve's published series under **neither** basis — off by $19,121 and $60,181 respectively. And the two series agree almost exactly at 2022. That agreement is the diagnostic: the table took the Fed's current real endpoint and extended it backward from an incompatible, undocumented source. It was a splice, and the trend it appeared to show was substantially an artifact of thirty-three years of inflation.

**What the corrected series shows.** Rebuilt from Federal Reserve FEDS Notes, *Greater Wealth, Greater Uncertainty*, October 18, 2023, Figure 2 — constant 2022 dollars, families, cited by title, date and figure number:

- Black median family wealth rose **388 percent**; white median rose **74 percent**. Black wealth grew more than five times faster in percentage terms.
- The ratio rose from **0.056 to 0.158** — it nearly tripled, a far larger improvement than the defective series implied.
- The absolute gap nonetheless widened, from **$154,830 to $240,120**: an increase of $85,290, a 1.55-fold expansion, and **the widest real gap in any wave of the survey**.

**Withdrawn:** "the gap nearly tripled" (2.89×), the 3.2-cent ratio gain, and the 868-year parity horizon.

We note that the corrected finding is stronger, not weaker. Faster proportional growth on a base one-eighteenth the size widening the absolute distance is a cleaner statement of the mechanism this paper documents than the inflation-contaminated version it replaces. The reviewer improved the paper's central economic argument by breaking it.

**On our reduced independence.** Table 5.1 now rests on the Federal Reserve's own published presentation rather than on an SCF microdata extraction performed by this project. That is better provenance and less independence. A microdata extraction with published code is owed, and it is listed as an open item.

---

## 2. Projections (W-2)

**Accepted. No wealth parity horizon is asserted in this edition.**

The reviewer was right that these figures were framed with insufficient warning, and right that a corrected single number would not fix it. Extrapolating the corrected series from different baselines in the same table gives:

| Baseline | Implied years to parity |
|---|---|
| 1989 | 274 |
| 1992 | 1,632 |
| 1995 | 1,511 |
| 2001 | **no convergence** — the 2022 ratio is below 2001's |
| 2007 | 366 |
| 2013 | 117 |

A factor-of-fourteen spread, with one plausible baseline yielding no convergence at all. The 1989 wave compounds the problem: the ratio rises 2.5-fold in the single step to 1992, a move no later wave approaches.

That table is now printed in §5.1 in place of a headline figure. The NAEP 144-year figure is retained, because the reviewer independently confirmed its arithmetic, but it is now explicitly labelled an arithmetic extension of two endpoints rather than a forecast.

---

## 3. Incarceration definition (W-3)

**Accepted. The paper's scope claim was overstated and has been narrowed.**

BJS publishes, for 2022, **1,196 per 100,000 Black adult U.S. residents and 229 per 100,000 white adult residents — a ratio of 5.22.** Our series shows 1,862 and 295, which correspond closely to BJS's *male* imprisonment rates (approximately 1,826 and 279). The vault does not record which denominator it used, and the Cahalan (1986) pre-1980 crosswalk is undocumented. The reviewer also correctly notes that BJS dates the series to 1926, not 1925.

Chapter 6 now prints both ratios, states that the basis is probably male rates, and stops writing "Black Americans" where the source may say "Black males."

The finding the chapter argues from — the *stability* of the ratio across ninety-seven years, moving 0.14 points — holds on either basis. But the paper was claiming a scope its source may not support, and that has stopped.

---

## 4. Pre-1933 maternal mortality (W-4)

**Accepted.** The 1915 and 1930 figures come from the birth-registration states only, which were not nationally representative, and the cross-era comparison is not strictly commensurable. The caveat is now in the text.

The 2022 figures are confirmed directly against NCHS: 49.5 and 19.0 per 100,000, ratio 2.605, rounding to 2.61 — the reviewer's arithmetic and ours agree. The chapter now also offers readers who reject the 1930 datum entirely the 2010→2022 rise from 2.24 to 2.61, which occurs wholly within a fully registered national system.

---

## 5. Unemployment aggregation (W-5)

**Accepted as a disclosure failure; the stored values were correct.**

The reviewer computed 5.5 ÷ 3.3 = 1.667 against our printed 1.683. The discrepancy arises because our ratios are computed from unrounded monthly data while the displayed component rates are rounded annual averages. Worked: 2023's twelve monthly values average 5.5167 and 3.2750, giving **1.685** — consistent with the stored 1.683 to rounding.

So the numbers were right and the method was invisible, which is a real defect in a paper that asks to be checked. The aggregation rule is now stated in §5.2 with that worked example and a vintage-revision note.

---

## 6. Farmland peak, NAEP precision (W-6, W-7)

**Both accepted.** The 15-million-acre peak's year and level carry acknowledged uncertainty in the literature; the 1997 figure of 1.5 million is well supported, and the 90 percent loss is now framed against a peak of uncertain exact year. On NAEP, both the accommodation change between 1992 and later administrations and the fact that our precision exceeds NCES's published rounded tables are now disclosed.

---

## 7. The bundle (W-8)

**Accepted without qualification. This was our error and it was avoidable.**

The bundle we supplied was created incrementally (`main..branch`) and declared a prerequisite commit the reviewer did not have. It was therefore useless for its stated purpose: a reviewer with no clone could not inspect the tree, the raw vault JSON, or the manifests. It made the paper's central procedural claim — that the record can be checked — untestable for the one reader who tried.

A complete-history bundle is supplied with this response: **`bdi-black-paper-v1.2-complete.bundle`**. `git bundle verify` reports *"The bundle records a complete history"* and it requires no prerequisite object.

For the record, the prerequisite the reviewer could not resolve, `91a9c756`, is the pre-existing tip of `main`; the v1.1 commit `ba509724` has since been merged to `origin/main`.

---

## 8. The finding we have not closed: FDI reproducibility

**Accepted and left open. The reviewer's characterisation is adopted verbatim in Appendix E.4a:**

> **The FDI outputs in this paper are not independently reproducible from the published package.**

What is public: the scored output CSVs, formulas, weights, normalization method, the Humphreys decomposition including its unreconciled 79.7-versus-87.25 discrepancy, and the eight enumerated imputation artifacts. What is not public: raw pre-scoring inputs with ACS table identifiers, release years and geography codes; the Phase 3 corpus supplying the normalization bounds; transformation code with a dependency lockfile; and a deterministic rebuild command.

A reader can therefore audit the FDI's *logic* and not its *arithmetic*. The 87.25 Humphreys score, the 15,507 tract scores and the 49 city rankings should be cited as this organization's published outputs, not as independently verified results. Producing the data package is the first deliverable of FDI v3.0.

We could have written a paragraph asserting that the data is public and checkable. The reviewer demonstrated that for this component it is not, and the paper now says so.

---

## 9. Already corrected before the review arrived (W-9)

The reviewer flagged the Introduction's "Five Compound Catastrophe Zones" heading as an apparent contradiction with the Chapter 7 ranking, and recommended relabelling the five as case studies.

This had been found and corrected on August 31, before the review was received; the reviewer necessarily worked from the superseded v1.1 PDF and its accompanying bundle. In v1.2 the Introduction names the instrument's actual top five — Humphreys, Claiborne, Sunflower, Amite and Alexander — and states the withdrawal explicitly, rather than relabelling the earlier list.

The convergence is worth noting: two independent audits, one internal and one external, flagged the same defect within hours of each other.

---

## Why our own audit missed W-1 and W-3

This is the part of the review we consider most useful, and it is now recorded in Appendix H.

Our recomputation pass rebuilt every derived statistic from the vault's stored series rather than carrying figures forward from prior drafts. It worked as designed: it caught ten errors, including an undercount of 481 deaths, a floor claim contradicted by seventeen years of its own series, and a parity projection wrong by a factor of 3.3.

It could not catch W-1 or W-3, because **it verified that our arithmetic followed from our data and never asked whether our data was coherent.** Every figure derived from the wealth table was correctly derived. The table was a splice. An internal consistency check is structurally incapable of detecting an incoherent input, and we mistook the completeness of one kind of audit for the completeness of auditing.

**The protocol is amended: primary-source reconciliation of every series endpoint is now a required pass, not an optional one.** Endpoint values must be traced to a named agency table with its price basis, universe, unit of observation and population restrictions recorded, before any derived statistic is computed from them.

---

## Open items carried forward

| # | Item | Status |
|---|---|---|
| 1 | SCF microdata extraction with published code and race coding, replacing dependence on the Fed's summary presentation | Open |
| 2 | FDI data package: raw inputs, normalization bounds, code, lockfile, deterministic rebuild command | Open — blocks any claim of FDI reproducibility |
| 3 | Incarceration series crosswalk: BJS table identifiers, numerator/denominator, sex and age restrictions, Cahalan-to-BJS mapping | Open |
| 4 | ACS table identifiers, vintages and geography codes for every Humphreys input | Open |
| 5 | Historical maternal mortality source tables and measure definition | Open |
| 6 | Exclude the 8 sentinel-artifact tracts; rebuild imputation to fail loudly rather than fill silently | Scheduled for FDI v3.0 |
| 7 | Generate the Stack Truth Table from row counts at build time rather than maintaining it by hand | Scheduled for v3.0 |

---

## Closing

The review's central judgment was that this paper should not yet be described as fully source-verified or fully reproducible. On the wealth series that judgment was correct and we have rebuilt the table. On FDI reproducibility it remains correct and we now say so in the paper itself.

What the review demonstrates is the thing the CC0 licence was chosen for. A reader with no access to our repositories, no relationship to this organization and no obligation to be kind found a defect that our own audit was structurally unable to find, and the paper is materially more defensible for it.

We would rather publish a corrected record than an unchallenged one. Our thanks to the reviewer, and the invitation stands: the data is public, the code is public, and the errata appendix has room in it.

---

*E5 Enclave Incorporated · Liberty City, Miami, Florida · CC0 1.0 Universal*
*By Grace, perfect ways.*
