import pandas as pd
import os

# ===============================
# Paths
# ===============================
raw_path = "data/raw"
processed_path = "data/processed"

os.makedirs(processed_path, exist_ok=True)

# ===============================
# Read CSV Files
# ===============================
fund_master = pd.read_csv(f"{raw_path}/01_fund_master.csv")
nav_history = pd.read_csv(f"{raw_path}/02_nav_history.csv")
aum = pd.read_csv(f"{raw_path}/03_aum_by_fund_house.csv")
sip = pd.read_csv(f"{raw_path}/04_monthly_sip_inflows.csv")
category = pd.read_csv(f"{raw_path}/05_category_inflows.csv")
folio = pd.read_csv(f"{raw_path}/06_industry_folio_count.csv")
performance = pd.read_csv(f"{raw_path}/07_scheme_performance.csv")
transactions = pd.read_csv(f"{raw_path}/08_investor_transactions.csv")
portfolio = pd.read_csv(f"{raw_path}/09_portfolio_holdings.csv")
benchmark = pd.read_csv(f"{raw_path}/10_benchmark_indices.csv")

# =====================================================
# 01 FUND MASTER
# =====================================================

fund_master.drop_duplicates(inplace=True)

fund_master["launch_date"] = pd.to_datetime(fund_master["launch_date"])

fund_master.to_csv(
    f"{processed_path}/01_fund_master.csv",
    index=False
)

print("01_fund_master cleaned")

# =====================================================
# 02 NAV HISTORY
# =====================================================

nav_history.drop_duplicates(inplace=True)

nav_history["date"] = pd.to_datetime(nav_history["date"])

nav_history.sort_values(
    ["amfi_code", "date"],
    inplace=True
)

nav_history["nav"] = (
    nav_history.groupby("amfi_code")["nav"]
    .ffill()
)

nav_history = nav_history[nav_history["nav"] > 0]

nav_history.to_csv(
    f"{processed_path}/02_nav_history.csv",
    index=False
)

print("02_nav_history cleaned")

# =====================================================
# 03 AUM BY FUND HOUSE
# =====================================================

aum.drop_duplicates(inplace=True)

aum["date"] = pd.to_datetime(aum["date"])

aum = aum[aum["aum_crore"] > 0]

aum.to_csv(
    f"{processed_path}/03_aum_by_fund_house.csv",
    index=False
)

print("03_aum_by_fund_house cleaned")

# =====================================================
# 04 MONTHLY SIP INFLOWS
# =====================================================

sip.drop_duplicates(inplace=True)

sip["month"] = pd.to_datetime(sip["month"])

sip["yoy_growth_pct"] = sip["yoy_growth_pct"].fillna(0)

sip.to_csv(
    f"{processed_path}/04_monthly_sip_inflows.csv",
    index=False
)

print("04_monthly_sip_inflows cleaned")

# =====================================================
# 05 CATEGORY INFLOWS
# =====================================================

category.drop_duplicates(inplace=True)

category["month"] = pd.to_datetime(category["month"])

category["category"] = category["category"].str.strip()

category.to_csv(
    f"{processed_path}/05_category_inflows.csv",
    index=False
)

print("05_category_inflows cleaned")

# =====================================================
# 06 INDUSTRY FOLIO COUNT
# =====================================================

folio.drop_duplicates(inplace=True)

folio["month"] = pd.to_datetime(folio["month"])

folio.to_csv(
    f"{processed_path}/06_industry_folio_count.csv",
    index=False
)

print("06_industry_folio_count cleaned")

# =====================================================
# 07 SCHEME PERFORMANCE
# =====================================================

performance.drop_duplicates(inplace=True)

performance = performance[
    (performance["expense_ratio_pct"] >= 0)
    &
    (performance["expense_ratio_pct"] <= 2.5)
]

performance.to_csv(
    f"{processed_path}/07_scheme_performance.csv",
    index=False
)

print("07_scheme_performance cleaned")

# =====================================================
# 08 INVESTOR TRANSACTIONS
# =====================================================

transactions.drop_duplicates(inplace=True)

transactions["transaction_date"] = pd.to_datetime(
    transactions["transaction_date"]
)

transactions["transaction_type"] = (
    transactions["transaction_type"]
    .str.upper()
    .str.strip()
)

transactions["kyc_status"] = (
    transactions["kyc_status"]
    .str.upper()
    .str.strip()
)

transactions = transactions[
    transactions["amount_inr"] > 0
]

transactions.to_csv(
    f"{processed_path}/08_investor_transactions.csv",
    index=False
)

print("08_investor_transactions cleaned")

# =====================================================
# 09 PORTFOLIO HOLDINGS
# =====================================================

portfolio.drop_duplicates(inplace=True)

portfolio["portfolio_date"] = pd.to_datetime(
    portfolio["portfolio_date"]
)

portfolio = portfolio[
    portfolio["weight_pct"] >= 0
]

portfolio.to_csv(
    f"{processed_path}/09_portfolio_holdings.csv",
    index=False
)

print("09_portfolio_holdings cleaned")

# =====================================================
# 10 BENCHMARK INDICES
# =====================================================

benchmark.drop_duplicates(inplace=True)

benchmark["date"] = pd.to_datetime(
    benchmark["date"]
)

benchmark = benchmark[
    benchmark["close_value"] > 0
]

benchmark.to_csv(
    f"{processed_path}/10_benchmark_indices.csv",
    index=False
)

print("10_benchmark_indices cleaned")

print("\nAll datasets cleaned successfully!")