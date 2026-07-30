import pandas as pd
from sqlalchemy import create_engine

# Create SQLite database
engine = create_engine("sqlite:///bluestock_mf.db")

processed = "data/processed"

# Read cleaned CSVs
fund_master = pd.read_csv(f"{processed}/01_fund_master.csv")
nav_history = pd.read_csv(f"{processed}/02_nav_history.csv")
aum = pd.read_csv(f"{processed}/03_aum_by_fund_house.csv")
sip = pd.read_csv(f"{processed}/04_monthly_sip_inflows.csv")
category = pd.read_csv(f"{processed}/05_category_inflows.csv")
folio = pd.read_csv(f"{processed}/06_industry_folio_count.csv")
performance = pd.read_csv(f"{processed}/07_scheme_performance.csv")
transactions = pd.read_csv(f"{processed}/08_investor_transactions.csv")
portfolio = pd.read_csv(f"{processed}/09_portfolio_holdings.csv")
benchmark = pd.read_csv(f"{processed}/10_benchmark_indices.csv")

# Load into SQLite
fund_master.to_sql("fund_master", engine, if_exists="replace", index=False)
nav_history.to_sql("nav_history", engine, if_exists="replace", index=False)
aum.to_sql("aum_by_fund_house", engine, if_exists="replace", index=False)
sip.to_sql("monthly_sip_inflows", engine, if_exists="replace", index=False)
category.to_sql("category_inflows", engine, if_exists="replace", index=False)
folio.to_sql("industry_folio_count", engine, if_exists="replace", index=False)
performance.to_sql("scheme_performance", engine, if_exists="replace", index=False)
transactions.to_sql("investor_transactions", engine, if_exists="replace", index=False)
portfolio.to_sql("portfolio_holdings", engine, if_exists="replace", index=False)
benchmark.to_sql("benchmark_indices", engine, if_exists="replace", index=False)

print("fund_master loaded")
print("nav_history loaded")
print("aum_by_fund_house loaded")
print("monthly_sip_inflows loaded")
print("category_inflows loaded")
print("industry_folio_count loaded")
print("scheme_performance loaded")
print("investor_transactions loaded")
print("portfolio_holdings loaded")
print("benchmark_indices loaded")

print("\nAll tables loaded successfully!")
import sqlite3

conn = sqlite3.connect("bluestock_mf.db")
cursor = conn.cursor()

tables = [
    "fund_master",
    "nav_history",
    "aum_by_fund_house",
    "monthly_sip_inflows",
    "category_inflows",
    "industry_folio_count",
    "scheme_performance",
    "investor_transactions",
    "portfolio_holdings",
    "benchmark_indices"
]

print("\n========== ROW COUNT VERIFICATION ==========\n")

for table in tables:
    cursor.execute(f"SELECT COUNT(*) FROM {table}")
    count = cursor.fetchone()[0]
    print(f"{table:<30} {count}")

conn.close()

print("\nDatabase verification completed successfully!")