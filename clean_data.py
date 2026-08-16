from pathlib import Path
import pandas as pd


# ============================================================
# PROJECT PATHS
# ============================================================

PROJECT_DIR = Path(__file__).resolve().parent

RAW_DIR = PROJECT_DIR / "data" / "raw"
PROCESSED_DIR = PROJECT_DIR / "data" / "processed"

PROCESSED_DIR.mkdir(parents=True, exist_ok=True)


# ============================================================
# HELPER FUNCTION
# ============================================================

def read_csv(filename):
    """Read a CSV file from the raw data directory."""
    file_path = RAW_DIR / filename

    if not file_path.exists():
        raise FileNotFoundError(
            f"Raw data file not found: {file_path}"
        )

    return pd.read_csv(file_path)


# ============================================================
# READ RAW CSV FILES
# ============================================================

print("=" * 60)
print("READING RAW DATA")
print("=" * 60)

fund_master = read_csv("01_fund_master.csv")
nav_history = read_csv("02_nav_history.csv")
aum = read_csv("03_aum_by_fund_house.csv")
sip = read_csv("04_monthly_sip_inflows.csv")
category = read_csv("05_category_inflows.csv")
folio = read_csv("06_industry_folio_count.csv")
performance = read_csv("07_scheme_performance.csv")
transactions = read_csv("08_investor_transactions.csv")
portfolio = read_csv("09_portfolio_holdings.csv")
benchmark = read_csv("10_benchmark_indices.csv")


# ============================================================
# 01 FUND MASTER
# ============================================================

fund_master = fund_master.drop_duplicates()

fund_master["launch_date"] = pd.to_datetime(
    fund_master["launch_date"],
    errors="coerce"
)

fund_master.to_csv(
    PROCESSED_DIR / "01_fund_master.csv",
    index=False
)

print("✓ 01_fund_master cleaned")


# ============================================================
# 02 NAV HISTORY
# ============================================================

nav_history = nav_history.drop_duplicates(
    subset=["amfi_code", "date"]
)

nav_history["date"] = pd.to_datetime(
    nav_history["date"],
    errors="coerce"
)

nav_history["nav"] = pd.to_numeric(
    nav_history["nav"],
    errors="coerce"
)

nav_history = nav_history.dropna(
    subset=["amfi_code", "date"]
)

nav_history = nav_history.sort_values(
    ["amfi_code", "date"]
)


# Create a complete daily date range for every fund
# and forward-fill NAV for weekends and holidays.

completed_groups = []

for amfi_code, group in nav_history.groupby("amfi_code"):

    group = group.sort_values("date").copy()

    start_date = group["date"].min()
    end_date = group["date"].max()

    full_dates = pd.date_range(
        start=start_date,
        end=end_date,
        freq="D"
    )

    group = (
        group
        .set_index("date")
        .reindex(full_dates)
    )

    group.index.name = "date"

    # Restore AMFI code after reindexing
    group["amfi_code"] = amfi_code

    # Forward-fill NAV across weekends and holidays
    group["nav"] = group["nav"].ffill()

    completed_groups.append(
        group.reset_index()
    )


nav_history = pd.concat(
    completed_groups,
    ignore_index=True
)

nav_history = nav_history[
    nav_history["nav"] > 0
]

nav_history = nav_history.sort_values(
    ["amfi_code", "date"]
)

nav_history.to_csv(
    PROCESSED_DIR / "02_nav_history.csv",
    index=False
)

print("✓ 02_nav_history cleaned")

print(
    f"  NAV rows after complete date handling: "
    f"{len(nav_history):,}"
)

# ============================================================
# 03 AUM BY FUND HOUSE
# ============================================================

aum = aum.drop_duplicates()

aum["date"] = pd.to_datetime(
    aum["date"],
    errors="coerce"
)

aum["aum_crore"] = pd.to_numeric(
    aum["aum_crore"],
    errors="coerce"
)

aum = aum[
    aum["aum_crore"] > 0
]

aum.to_csv(
    PROCESSED_DIR / "03_aum_by_fund_house.csv",
    index=False
)

print("✓ 03_aum_by_fund_house cleaned")


# ============================================================
# 04 MONTHLY SIP INFLOWS
# ============================================================

sip = sip.drop_duplicates()

sip["month"] = pd.to_datetime(
    sip["month"],
    errors="coerce"
)

sip["yoy_growth_pct"] = pd.to_numeric(
    sip["yoy_growth_pct"],
    errors="coerce"
).fillna(0)

sip.to_csv(
    PROCESSED_DIR / "04_monthly_sip_inflows.csv",
    index=False
)

print("✓ 04_monthly_sip_inflows cleaned")


# ============================================================
# 05 CATEGORY INFLOWS
# ============================================================

category = category.drop_duplicates()

category["month"] = pd.to_datetime(
    category["month"],
    errors="coerce"
)

category["category"] = (
    category["category"]
    .astype(str)
    .str.strip()
)

category.to_csv(
    PROCESSED_DIR / "05_category_inflows.csv",
    index=False
)

print("✓ 05_category_inflows cleaned")


# ============================================================
# 06 INDUSTRY FOLIO COUNT
# ============================================================

folio = folio.drop_duplicates()

folio["month"] = pd.to_datetime(
    folio["month"],
    errors="coerce"
)

folio.to_csv(
    PROCESSED_DIR / "06_industry_folio_count.csv",
    index=False
)

print("✓ 06_industry_folio_count cleaned")


# ============================================================
# 07 SCHEME PERFORMANCE
# ============================================================

performance = performance.drop_duplicates()

performance["expense_ratio_pct"] = pd.to_numeric(
    performance["expense_ratio_pct"],
    errors="coerce"
)

performance = performance[
    (performance["expense_ratio_pct"] >= 0)
    &
    (performance["expense_ratio_pct"] <= 2.5)
]

performance.to_csv(
    PROCESSED_DIR / "07_scheme_performance.csv",
    index=False
)

print("✓ 07_scheme_performance cleaned")


# ============================================================
# 08 INVESTOR TRANSACTIONS
# ============================================================

transactions = transactions.drop_duplicates()

transactions["transaction_date"] = pd.to_datetime(
    transactions["transaction_date"],
    errors="coerce"
)

transactions["transaction_type"] = (
    transactions["transaction_type"]
    .astype(str)
    .str.upper()
    .str.strip()
)

transactions["kyc_status"] = (
    transactions["kyc_status"]
    .astype(str)
    .str.upper()
    .str.strip()
)

transactions["amount_inr"] = pd.to_numeric(
    transactions["amount_inr"],
    errors="coerce"
)

transactions = transactions[
    transactions["amount_inr"] > 0
]

transactions.to_csv(
    PROCESSED_DIR / "08_investor_transactions.csv",
    index=False
)

print("✓ 08_investor_transactions cleaned")


# ============================================================
# 09 PORTFOLIO HOLDINGS
# ============================================================

portfolio = portfolio.drop_duplicates()

portfolio["portfolio_date"] = pd.to_datetime(
    portfolio["portfolio_date"],
    errors="coerce"
)

portfolio["weight_pct"] = pd.to_numeric(
    portfolio["weight_pct"],
    errors="coerce"
)

portfolio = portfolio[
    portfolio["weight_pct"] >= 0
]

portfolio.to_csv(
    PROCESSED_DIR / "09_portfolio_holdings.csv",
    index=False
)

print("✓ 09_portfolio_holdings cleaned")


# ============================================================
# 10 BENCHMARK INDICES
# ============================================================

benchmark = benchmark.drop_duplicates()

benchmark["date"] = pd.to_datetime(
    benchmark["date"],
    errors="coerce"
)

benchmark["close_value"] = pd.to_numeric(
    benchmark["close_value"],
    errors="coerce"
)

benchmark = benchmark[
    benchmark["close_value"] > 0
]

benchmark.to_csv(
    PROCESSED_DIR / "10_benchmark_indices.csv",
    index=False
)

print("✓ 10_benchmark_indices cleaned")


# ============================================================
# FINAL STATUS
# ============================================================

print("\n" + "=" * 60)
print("ALL DATASETS CLEANED SUCCESSFULLY")
print("=" * 60)

print(f"Raw data directory       : {RAW_DIR.resolve()}")
print(f"Processed data directory : {PROCESSED_DIR.resolve()}")