from pathlib import Path
import sqlite3
import pandas as pd
from sqlalchemy import create_engine


# ============================================================
# PROJECT PATHS
# ============================================================

BASE_DIR = Path(__file__).resolve().parent

# load_sqlite.py is currently in the project root.
# Therefore BASE_DIR is the project root.
PROJECT_DIR = BASE_DIR

PROCESSED_DIR = PROJECT_DIR / "data" / "processed"
DB_DIR = PROJECT_DIR / "data" / "db"
DB_PATH = DB_DIR / "bluestock_mf.db"

DB_DIR.mkdir(parents=True, exist_ok=True)


# ============================================================
# DATABASE CONNECTION
# ============================================================

engine = create_engine(
    f"sqlite:///{DB_PATH.as_posix()}"
)


# ============================================================
# PROCESSED CSV FILES
# ============================================================

files = {
    "fund_master": "01_fund_master.csv",
    "nav_history": "02_nav_history.csv",
    "aum_by_fund_house": "03_aum_by_fund_house.csv",
    "monthly_sip_inflows": "04_monthly_sip_inflows.csv",
    "category_inflows": "05_category_inflows.csv",
    "industry_folio_count": "06_industry_folio_count.csv",
    "scheme_performance": "07_scheme_performance.csv",
    "investor_transactions": "08_investor_transactions.csv",
    "portfolio_holdings": "09_portfolio_holdings.csv",
    "benchmark_indices": "10_benchmark_indices.csv",
}


# ============================================================
# LOAD CSV FILES INTO SQLITE
# ============================================================

print("=" * 60)
print("LOADING PROCESSED DATA INTO SQLITE")
print("=" * 60)

for table_name, filename in files.items():

    csv_path = PROCESSED_DIR / filename

    if not csv_path.exists():
        raise FileNotFoundError(
            f"Processed file not found: {csv_path}"
        )

    df = pd.read_csv(csv_path)

    df.to_sql(
        table_name,
        engine,
        if_exists="replace",
        index=False
    )

    print(
        f"✓ {table_name:<30} "
        f"{len(df):>8} rows"
    )


print("\nAll tables loaded successfully!")


# ============================================================
# DATABASE VERIFICATION
# ============================================================

print("\n" + "=" * 60)
print("DATABASE ROW COUNT VERIFICATION")
print("=" * 60)

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

for table_name in files.keys():

    cursor.execute(
        f"SELECT COUNT(*) FROM {table_name}"
    )

    count = cursor.fetchone()[0]

    print(
        f"{table_name:<30} {count:>8}"
    )

conn.close()


# ============================================================
# FINAL STATUS
# ============================================================

print("\n" + "=" * 60)
print("DATABASE INFORMATION")
print("=" * 60)

print(f"Database path : {DB_PATH.resolve()}")
print(f"Database size : {DB_PATH.stat().st_size:,} bytes")

print("\n✓ Database verification completed successfully!")