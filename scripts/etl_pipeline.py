from pathlib import Path
import subprocess
import sys
import sqlite3


# ============================================================
# PROJECT PATH
# ============================================================

PROJECT_DIR = Path(__file__).resolve().parent.parent

CLEAN_SCRIPT = PROJECT_DIR / "clean_data.py"
LOAD_SCRIPT = PROJECT_DIR / "load_sqlite.py"
DB_PATH = PROJECT_DIR / "data" / "db" / "bluestock_mf.db"


# ============================================================
# HELPER FUNCTION
# ============================================================

def run_script(script_path):
    """Run a Python script and stop the pipeline if it fails."""

    print("\n" + "=" * 70)
    print(f"RUNNING: {script_path.name}")
    print("=" * 70)

    if not script_path.exists():
        raise FileNotFoundError(
            f"Required script not found: {script_path}"
        )

    result = subprocess.run(
        [sys.executable, str(script_path)],
        cwd=PROJECT_DIR,
        check=False
    )

    if result.returncode != 0:
        raise RuntimeError(
            f"{script_path.name} failed with exit code "
            f"{result.returncode}"
        )

    print(f"\n✓ {script_path.name} completed successfully.")


# ============================================================
# DATABASE VALIDATION
# ============================================================

def validate_database():

    print("\n" + "=" * 70)
    print("DATABASE VALIDATION")
    print("=" * 70)

    if not DB_PATH.exists():
        raise FileNotFoundError(
            f"Database was not created: {DB_PATH}"
        )

    if DB_PATH.stat().st_size == 0:
        raise RuntimeError(
            "Database exists but is empty."
        )

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
        "benchmark_indices",
    ]

    conn = sqlite3.connect(DB_PATH)

    try:
        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT name
            FROM sqlite_master
            WHERE type='table'
            """
        )

        existing_tables = {
            row[0] for row in cursor.fetchall()
        }

        missing_tables = [
            table for table in tables
            if table not in existing_tables
        ]

        if missing_tables:
            raise RuntimeError(
                f"Missing database tables: {missing_tables}"
            )

        print("\nTABLE ROW COUNTS\n")

        for table in tables:

            cursor.execute(
                f"SELECT COUNT(*) FROM {table}"
            )

            count = cursor.fetchone()[0]

            print(
                f"{table:<30} {count:>10,}"
            )

        print("\n✓ All required tables verified.")

    finally:
        conn.close()


# ============================================================
# MAIN ETL PIPELINE
# ============================================================

def main():

    print("\n" + "#" * 70)
    print("# BLUESTOCK MUTUAL FUND ETL PIPELINE")
    print("#" * 70)

    try:

        # Step 1: Clean raw data
        run_script(CLEAN_SCRIPT)

        # Step 2: Load processed data into SQLite
        run_script(LOAD_SCRIPT)

        # Step 3: Validate database
        validate_database()

        print("\n" + "#" * 70)
        print("# ETL PIPELINE COMPLETED SUCCESSFULLY")
        print("#" * 70)

        print(
            f"\nDatabase: {DB_PATH.resolve()}"
        )

    except Exception as error:

        print("\n" + "!" * 70)
        print("ETL PIPELINE FAILED")
        print("!" * 70)

        print(f"\nError: {error}")

        sys.exit(1)


if __name__ == "__main__":
    main()