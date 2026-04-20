# Chapter 3 — THE STACK: How the Data Was Built
### Part Two — The Data Architecture

**Work:** The Measure of the Wound  
**Subtitle:** A Sovereign Empirical Record of Black American Structural Distress, 1991–2024  
**Publisher:** E5 Enclave Incorporated · EIN 99-3822441 · Liberty City, Miami, Florida  
**Filed:** April 20, 2026  
**DAG:** bdi-chapter3-v1-2026-0420  
**Status:** DRAFT v1.0

---

> *"Not everything that is faced can be changed, but nothing can be changed until it is faced."*
> — James Baldwin

---

## Opening

The credibility of this paper is inseparable from the architecture that produced it. Every number in every finding chapter is traceable — through a documented chain of custody — to a federal primary source file committed to a public GitHub repository before any analysis was performed. The chain does not break. It cannot break. That is not a rhetorical claim. It is a design specification.

This chapter describes that architecture. It is not optional reading. The findings in Chapters 5 through 7 are only as strong as the methodology described here. Readers who wish to contest any number in this paper are invited to begin here, with the counting rules and source files, and work forward.

---

## I. The Four-Layer Stack

The data infrastructure underlying this paper is organized into four distinct layers. Each layer has a specific role. They are not redundant. Citing the wrong layer for a given purpose is a methodological error.

**Layer 1 — The Raw Evidence Vault**  
Repository: `github.com/IAMGODIAM/bdi-raw-data-vault`

Seventeen files drawn directly from federal APIs and databases, committed to GitHub unmodified before any analysis was performed. This is the ground truth. If any number in this paper is contested, the verification path begins here. The files are named, the sources are documented, the pull dates are recorded. There is no intermediate step between the federal source and this repository. The vault contains approximately **14,811 verified data points** across four tiers of geographic resolution.

**Layer 2 — The Sovereign Dataset**  
Repository: `github.com/IAMGODIAM/bdi-sovereign-dataset`

The synthesized flagship instrument. **1,574 verified empirical observations** drawn from Layer 1, organized across eight structural pillars, covering a 33-year empirical window (1991–2024) with historical context extending to 1514. Every observation is dual-source verified — confirmed against at least two independent federal instruments. The dataset is sealed on the Base Mainnet blockchain (ExodusV4 Contract `0x8582684C53912D496Df60C5B1B9Bb44D3d2f9B44`, Token #2), making it immutable against political revision. Published CC0 — public domain, no license required.

**Layer 3 — The FarmBlock Application**  
Repository: `github.com/IAMGODIAM/farmblock-data`

The operational application of the data infrastructure to the census-tract level. **15,578 census tracts** scored across 50 priority cities in 17 states using the FarmBlock Distress Index (FDI) — a six-dimension composite measuring poverty, income deprivation, food access deficit, health burden, housing vacancy, and digital exclusion. Layer 3 is the bridge between the national structural record and the specific communities it describes.

**Layer 4 — This Paper**  
Repository: `github.com/IAMGODIAM/bdi-black-paper`

The interpretive and argumentative layer. This paper synthesizes the three data layers into a coherent account of Black American structural distress — its dimensions, its persistence, its geography, and what it demands. Every factual claim in Chapters 5 through 7 carries a traceable path back through Layer 2 to Layer 1.

---

## II. The Raw Evidence: What the Vault Contains

The 14,811 data points in the raw evidence vault are organized across four geographic tiers:

| Tier | Geography | Count | Source Files |
|------|-----------|-------|-------------|
| Tier 1 — National | National aggregates + DC/PR | 479 | BLS CPS, Census ACS, Fed Reserve SCF, USDA NASS |
| Tier 1 — State | All 50 states + DC | 358 | BLS LAUS, Census ACS state-level series |
| Tier 2 — Metro | 516+ MSAs | 1,550 | Census ACS 5-year MSA estimates |
| Tier 3 — County | 3,222 counties | 12,382 | Census ACS 5-year county estimates |
| Historical | 1514–1866 aggregate | 42 | SlaveVoyages Trans-Atlantic Database |
| **Total** | | **~14,811** | |

The county tier dominates the raw count — 12,382 of the 14,811 total data points — because the Census Bureau's ACS 5-year estimates cover 3,222 counties across multiple years and multiple variables. This is not a weakness; it is the geographic resolution that enables the FarmBlock application in Layer 3. The national and state-level series, while smaller in raw count, carry the most analytical weight for the longitudinal findings in Chapters 5 and 6.

### The 17 Source Files

Every file in the vault maps to a federal agency, a specific dataset, and an API endpoint or data access mechanism. The full source table appears in `data/SOURCES.md`. The key instruments are:

**Bureau of Labor Statistics:** The Current Population Survey racial unemployment series, 1972–2025 — the longest continuous race-disaggregated labor market dataset in American public records. Fifty-three years of the Black/white unemployment ratio. The LAUS state-level series extends this to all fifty states from 2010 through 2024.

**Census Bureau — American Community Survey:** The ACS provides the foundational economic architecture of the dataset — homeownership rates, household income, poverty rates — at national, state, MSA, and county levels. The 5-year estimates at the county level constitute the single largest block of data points in the vault (12,382 county-year observations).

**Federal Reserve Survey of Consumer Finances:** The SCF is the most rigorous instrument available for measuring the racial wealth gap. Conducted every three years since 1989, it provides median and mean wealth by race, enabling the longitudinal analysis of wealth divergence documented in Chapter 5.

**National Center for Health Statistics:** The NCHS vital statistics system provides the maternal mortality and life expectancy data that anchors the health findings in Chapter 6. These are not survey-based estimates. They are administrative records — birth certificates, death certificates, hospital discharge records — compiled into the most authoritative health dataset available to researchers.

**Bureau of Justice Statistics:** The BJS Prisoners series provides the incarceration rate by race, 1991–2023. This is the primary federal source for carceral data. It is supplemented by the Mapping Police Violence database for the police killing counts.

**SlaveVoyages Trans-Atlantic Slave Trade Database:** The historical anchor. Forty-two aggregate observations covering the period 1514–1866. The wound did not begin in 1991. The 33-year empirical window is chosen for data quality, not historical scope. The SlaveVoyages data provides the origin point from which the subsequent four centuries of structural conditions descend.

---

## III. The Sovereign Dataset: What Was Synthesized

Moving from 14,811 raw data points to 1,574 verified empirical observations required a synthesis methodology that is explicit, documented, and replicable. This section describes that methodology.

### The Counting Rule

A single empirical observation is defined as: **one row in a time series or one unique observation in a cross-sectional dataset, where the value represents a directly measured or reported quantity from a federal primary source.**

Metadata keys, derived fields, and structural JSON elements do not count as data points. The original claimed count of 1,855 violated this rule by including JSON metadata keys as observations. The corrected count of 1,574 applies this rule consistently. The correction is documented in the dataset JSON (`total_data_points_original_claim: 1855`, `count_correction_note`), the BDI_QUANT_SPEC.md, and in the stack truth table. This paper uses 1,574. All references to 1,855 are historical artifacts of the pre-correction state.

### The Eight Pillars

The synthesis organizes the 1,574 observations into eight structural pillars:

| Pillar | Weight in BDI Composite | Core Instruments |
|--------|------------------------|-----------------|
| Economic | 20% | BLS unemployment, Census income/poverty, Fed Reserve SCF wealth, USDA land |
| Health | 20% | NCHS maternal mortality, NCHS life expectancy, CDC PLACES |
| Criminal Justice | 20% | BJS incarceration, Mapping Police Violence |
| Education | 15% | NAEP score gaps, Census ACS attainment |
| Housing | 10% | HMDA mortgage denial, Census decennial homeownership, eviction data |
| Environmental | 10% | EPA facility proximity, Cancer Alley documentation |
| Political | 5% | Representation and voting access indicators |
| Historical | Context | SlaveVoyages 1514–1866 |

The weighting scheme is not arbitrary. Economic, health, and criminal justice receive equal highest weight (20% each) because these are the three dimensions where the data shows the most persistent, least-improving gaps over the 33-year empirical window. The historical pillar carries no composite weight because it serves as context for understanding the origin of the structural conditions documented in the other seven — not as a comparably measured dimension.

### The Dual-Source Verification Protocol

Every pillar in the sovereign dataset is confirmed against at least two independent federal instruments. Where sources conflict, the conflict is documented in `bdi-raw-data-vault/dual_source_log.json`, and the more conservative estimate is used. This is not a methodological weakness — it is an explicit design choice. A sovereign empirical record that makes the strongest possible claims using the most conservative defensible numbers is harder to dismiss than one that maximizes the apparent magnitude of the findings.

The data does not need maximizing. The findings, at their most conservative, are damning.

### The Blockchain Seal

The sovereign dataset is sealed on the Base Mainnet blockchain. This is not a technical flourish. It is a specific response to a specific historical pattern: federal datasets on Black American conditions have been revised, defunded, discontinued, and reclassified under political pressure. The annual Statistical Abstracts of the United States ceased publication in 2012. The Census Bureau's racial homeownership data has been subject to methodology changes that complicate longitudinal comparison. The Department of Justice's collection of police use-of-force data has been suspended and resumed multiple times since 2000.

A blockchain seal means the dataset as published cannot be altered. It can be extended. It can be contested. It cannot be revised under political pressure and republished as if the original never existed. The ExodusV4 contract on Base Mainnet records the dataset hash at a specific block. The record is permanent.

---

## IV. The FarmBlock Application: Bringing the Data to the Address

The third layer of the stack translates the national and state-level structural record into the geography of lived experience: the census tract.

Fifteen thousand, five hundred and seventy-eight census tracts. Fifty priority cities. Seventeen states. Six structural dimensions scored using the FarmBlock Distress Index formula:

```
FDI Score = (D1_poverty + D2_income_inv + D3_food_access + D4_health + D5_vacancy + D6_digital) / 6 × 100
```

Each dimension is min-max normalized (0–1) across all tracts in the dataset before scoring. This means the FDI is a relative measure — identifying the most distressed tracts relative to the universe of tracts studied — rather than an absolute threshold. A tract in the top quintile of FDI scores is experiencing structural conditions that place it among the most compromised 20% of urban census tracts in the 50-city priority universe.

The FarmBlock layer does not include race as a scoring variable. Racial composition data is stored in the vault but is not weighted in the FDI composite. This is intentional: the six dimensions measured — poverty, income deprivation, food access deficit, health burden, vacancy, digital exclusion — are structural conditions that independently generate distress regardless of the racial composition of the tract. The evidence, however, shows that in the 50-city priority universe, the highest-scoring tracts are disproportionately Black. The data does not need race as an input variable to arrive at a racially concentrated output. That is precisely the point.

---

## V. What the Stack Does Not Claim

A sovereign empirical record is bounded by what it measures. This paper does not claim:

**Causation where only correlation is demonstrated.** The wealth gap between Black and white Americans is documented. The mechanisms that produce and reproduce it — discriminatory lending, exclusionary zoning, carceral extraction, school funding inequities — are documented in the secondary literature and referenced here. But the dataset measures outcomes, not causal pathways. The causal argument is coherent and well-supported. It is not what the data itself proves.

**Completeness.** The 1,574 observations do not capture every dimension of Black American structural distress. Sub-county environmental data, mental health burden, intergenerational wealth transfer dynamics, and criminal legal debt are dimensions that warrant inclusion in BDI v2.0 but are not fully represented here. Where gaps exist, they are documented.

**Finality.** This is version one. The data architecture is designed for extension. CC0 licensing means any researcher can fork the dataset, add dimensions, extend the time series, or apply it to new geographies without permission. The architecture invites extension. The findings, at this level of evidence, are already sufficient to answer the question the paper asks.

---

## VI. The Transition to Findings

Layer 1 contains the evidence. Layer 2 synthesizes it. Layer 3 applies it. Layer 4 — this paper — interprets it.

Part Three begins with the economic findings: thirty-three years of the Federal Reserve's wealth data, the BLS unemployment series, the HMDA mortgage denial record. The numbers do not require interpretation to be understood. They require only to be read.

---

*CC0 1.0 Universal — Public Domain*  
*E5 Enclave Incorporated · EIN 99-3822441 · Liberty City, Miami, Florida*  
*DAG: bdi-chapter3-v1-2026-0420 · Nil satis nisi optimum*
