# Companion script for official CSV analysis
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

YEARS=["2020-21","2021-22","2022-23","2023-24","2024-25"]
CSV_PATH="health_insurance_claim_settlement.csv"
OUT=Path("outputs"); OUT.mkdir(exist_ok=True)
df=pd.read_csv(CSV_PATH)
required=["fiscal_year","state_name","business_type","insurance_type","settlement_type","no_of_claims","amount_paid","unit"]
missing=[c for c in required if c not in df.columns]
if missing: raise ValueError(f"Missing columns: {missing}")
df["no_of_claims"]=pd.to_numeric(df["no_of_claims"],errors="coerce")
df["amount_paid"]=pd.to_numeric(df["amount_paid"],errors="coerce")
tn=df[df.state_name.astype(str).str.strip().str.casefold().isin(["tamil nadu","tamilnadu"])].copy()
if tn.empty: raise ValueError("No Tamil Nadu rows found.")
if tn.insurance_type.astype(str).str.casefold().eq("total").any(): tn=tn[tn.insurance_type.astype(str).str.casefold().eq("total")]
if tn.business_type.astype(str).str.casefold().eq("total").any(): tn=tn[tn.business_type.astype(str).str.casefold().eq("total")]
tn=tn[tn.fiscal_year.astype(str).isin(YEARS)]
tn.to_csv(OUT/"tamil_nadu_claim_settlement_cleaned.csv",index=False)
summary=tn.groupby("fiscal_year",as_index=False).agg(total_claims=("no_of_claims","sum"),amount_paid=("amount_paid","sum"))
summary.to_csv(OUT/"yearly_summary.csv",index=False)
fig,ax=plt.subplots(figsize=(9,5)); ax.plot(summary.fiscal_year,summary.total_claims,marker="o")
ax.set_title("Tamil Nadu: claims by financial year"); ax.set_xlabel("Financial year"); ax.set_ylabel("Claims")
fig.tight_layout(); fig.savefig(OUT/"yearly_claims.png",dpi=160); plt.show()
