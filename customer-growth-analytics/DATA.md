# Data and methodology

## Provenance
- Creator: Daqing Chen. Citation: Chen, D. (2015), Online Retail, UCI Machine Learning Repository, https://doi.org/10.24432/C5BW33.
- [Dataset page](https://archive.ics.uci.edu/dataset/352/online+retail).
- [Original archive](https://archive.ics.uci.edu/static/public/352/online+retail.zip).
- License: [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/). Attribution and transformations are recorded here. This license applies to the source dataset, not automatically to other repository material.
- Original workbook SHA256: `43465a06f2ccf7c8b5bd2892bc7defb52f97487934fe93b16ae4c3936424676d`.
- Source: 541,909 invoice lines from a UK-based non-store retailer, December 2010–December 2011. Many customers are wholesalers, according to UCI.

The original workbook and customer-level exports are not committed. Download from the cited source. Published outputs contain aggregate statistics only. No employer or client data is used.

## Sequential eligibility rules
1. Remove exact duplicate rows (5,268); this is an assumption, not proven duplication. See retained-duplicate sensitivity.
2. Exclude missing customer IDs (135,037 after deduplication). This makes the population known customers, not all transactions.
3. Exclude cancellation invoices whose number starts with C (8,872 remaining lines).
4. Exclude quantity or price ≤0 (40 remaining lines).
5. Exclude invalid dates (0).
6. Keep 2010-12-01 inclusive to 2011-12-01 exclusive (17,026 lines outside).

Final population: 375,666 lines, 4,297 customers, 17,754 invoices. Exclusions are sequential; raw diagnostics overlap. Removing cancellation invoices and negative quantities prevents any claim of net revenue. Valid positive-priced stock/adjustment codes are retained in v0.1; product-code review is a next increment.

## Definitions
- Positive purchase value: quantity × unit price, GBP, after eligibility rules. No costs, margin, tax reconciliation or refund matching.
- Order: distinct InvoiceNo. Frequency counts invoices, not lines.
- Recency: whole calendar days since last included purchase as of 2011-12-01.
- Monetary: sum of eligible positive purchase value. Not profit or lifetime value.
- RFM scores: average-tie percentile ranks mapped to 1–5, with low recency favorable. Equal values receive equal scores, so bins need not have equal counts.
- Action segments: ordered rules defined in the notebook. They use explicit recency/frequency and monetary thresholds rather than a clustering algorithm.
- Cohort: first observed purchase month. It is not necessarily customer acquisition month because earlier history is absent.
- Repeat rate: share of a cohort observed purchasing in a later calendar month. Blank cells mean future periods not observed, not zero.
- Temporal holdout: segment customers using only transactions before 2011-09-01, observe their purchases in September–November. Future-only customers do not enter historical segment denominators. Thresholds are fit on the pre-cutoff population only.

## Analytical choices and limitations
The full December 2010–November 2011 window avoids the incomplete final month, but left-censoring remains. Seasonality and unequal cohort ages complicate comparisons. The data cannot identify paid-campaign exposure, inactivity reasons, acquisition costs or unit margins. Extreme and wholesale orders may dominate amounts. No winsorization is applied; interpret concentration accordingly.

Action labels and cutoffs are analyst choices. Sensitivity explores alternatives. Descriptive temporal differences are not uplift estimates or accuracy scores. A causal commercial recommendation requires a designed experiment and contribution economics.

## Reproducibility record
Local execution: 2026-10-14 (America/Mexico_City). Python 3.12.14, pandas 3.0.1, NumPy 2.3.5, matplotlib 3.11.2. Exact source checksum and aggregate run metrics are in [run-metrics.json](output/run-metrics.json). The notebook stores real outputs from sequential local execution, not a Kaggle run. Prepared with AI assistance.

[Project home](README.md)
