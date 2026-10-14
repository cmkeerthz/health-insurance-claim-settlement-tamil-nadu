# Health Insurance Claim Settlement Patterns in Tamil Nadu

EDA for FY 2020–21 to FY 2024–25.

- The `.ipynb` contains code, explanatory notes, and embedded preview charts.
- The preview charts use **synthetic illustrative demo data**, not official IRDAI data.
- Do not publish demo charts as factual findings. To analyze real data, obtain the official IRDAI dataset “Year and State wise Claim Settlement Under Health Insurance Business”, place it as `health_insurance_claim_settlement.csv`, set `USE_DEMO_DATA = False`, and run the notebook.
- Expected columns: `fiscal_year`, `state_name`, `business_type`, `insurance_type`, `settlement_type`, `no_of_claims`, `amount_paid`, `unit`. Confirm units and definitions in the source.
