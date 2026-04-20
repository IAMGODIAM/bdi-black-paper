# DATA PROVENANCE
## The Measure of the Wound — Source Architecture

**DAG:** bdi-black-paper-provenance-2026-0420

---

## THE THREE-LAYER DATA ARCHITECTURE

### Layer 1 — Raw Evidence Vault (`bdi-raw-data-vault`)
**Scale: ~14,811 verified data points**

| File | Records | Years | Source Agency | API/Endpoint |
|------|---------|-------|--------------|-------------|
| `economic/bls_unemployment_by_race_1972-2025_FULL_RAW.json` | 54 | 1972–2025 | Bureau of Labor Statistics | LNS14000006/3 |
| `economic/census_acs_homeownership_income_RAW.json` | 17 | 2005–2022 | Census Bureau | ACS B25003/B19013 |
| `economic/census_acs_poverty_RAW.json` | 17 | 2005–2022 | Census Bureau | ACS B17001 |
| `economic/fed_reserve_scf_wealth_usda_land_RAW.json` | 26 | 1910–2022 | Federal Reserve / USDA | SCF + NASS |
| `economic/tier1_state_economics_ACS_2010-2022_RAW.json` | 260 | 2010–2022 | Census Bureau | ACS — all states |
| `economic/tier1_state_bls_unemployment_2010-2024_RAW.json` | 32 | 2010–2024 | Bureau of Labor Statistics | LAUS |
| `economic/tier2_metro_msa_economics_ACS_2015-2022_RAW.json` | 1,550 | 2015–2022 | Census Bureau | ACS — 516+ MSAs |
| `economic/tier3_county_economics_ACS5Y_2015-2022_RAW.json` | 12,382 | 2015–2022 | Census Bureau | ACS 5-year — 3,222 counties |
| `health/nchs_life_expectancy_maternal_mortality_RAW.json` | — | 1999–2021 | NCHS / CDC | WONDER |
| `criminal_justice/bjs_incarceration_mpv_killings_RAW.json` | — | 1991–2023 | BJS / Mapping Police Violence | DOJ/BJS + MPV |
| `education/tier1_naep_score_gaps_national_1992-2022_RAW.json` | — | 1992–2022 | NCES | NAEP |
| `education/tier1_state_education_attainment_2022_RAW.json` | — | 2022 | Census Bureau | ACS B15002 |
| `housing/census_decennial_homeownership_1940-2010_RAW.json` | — | 1940–2010 | Census Bureau | Decennial |
| `housing/hmda_mortgage_denial_eviction_RAW.json` | — | 1995–2022 | CFPB / FFIEC | HMDA |
| `historical/slavevoyages_1514-1866_aggregate_RAW.json` | 42 | 1514–1866 | SlaveVoyages.org | Voyages Database |
| `demographics/tier3_county_black_population_pct_2022_RAW.json` | — | 2022 | Census Bureau | ACS B02001 |

**Tier breakdown:**
- Tier 1 National/State: 479 observations
- Tier 1 State series: 358 observations
- Tier 2 Metro/MSA: 1,550 observations (516+ MSAs)
- Tier 3 County: 12,382 observations (3,222 counties)
- Historical (1514–1866): 42 observations
- **Grand total: ~14,811 verified data points**

All files committed to GitHub **unmodified** before any analysis. This is the ground truth layer.

---

### Layer 2 — BDI Sovereign Dataset (`bdi-sovereign-dataset`)
**Scale: 1,574 verified empirical observations**

8-pillar synthesis drawn from Layer 1. Every observation dual-source verified.  
Sealed on Base Mainnet blockchain: ExodusV4 Contract `0x8582684C53912D496Df60C5B1B9Bb44D3d2f9B44`, Token #2.  
DAG: `bdi-sovereign-dataset-v1-sealed-2026-0417`

**Count note:** The original claim of 1,855 was incorrect — metadata keys were counted as data points. Corrected to 1,574 per explicit counting rule in `BDI_QUANT_SPEC.md §3`. The correction is documented in the dataset JSON (`total_data_points_original_claim: 1855`, `count_correction_note`).

---

### Layer 3 — FarmBlock Application (`farmblock-data`)
**Scale: 15,578 census tracts**

6-dimension structural distress scoring applied to census tracts across 50 priority cities in 17 states.  
Source: `farmblock-data/processed/farmblock_fdi_v2.csv` (row count verified).

---

## BLOCKCHAIN SEALS

| Asset | Contract | Token | Network |
|-------|----------|-------|---------|
| BDI Sovereign Dataset | ExodusV4: `0x8582684C53912D496Df60C5B1B9Bb44D3d2f9B44` | #2 | Base Mainnet |

---

*CC0 1.0 Universal — Public Domain*  
*E5 Enclave Incorporated · EIN 99-3822441*
