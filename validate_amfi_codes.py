import pandas as pd

# Read datasets
fund_master = pd.read_csv("data/raw/01_fund_master.csv")
nav_history = pd.read_csv("data/raw/02_nav_history.csv")

# Extract unique AMFI codes
fund_codes = set(fund_master["amfi_code"])
nav_codes = set(nav_history["amfi_code"])

# Find missing codes
missing_codes = fund_codes - nav_codes

print("=" * 60)
print("AMFI CODE VALIDATION")
print("=" * 60)

print("\nTotal Fund Master Codes:", len(fund_codes))
print("Total NAV History Codes:", len(nav_codes))
print("Missing Codes:", len(missing_codes))

if len(missing_codes) == 0:
    print("\n✅ All AMFI codes are present in nav_history.")
else:
    print("\n❌ Missing AMFI Codes:")
    for code in sorted(missing_codes):
        print(code)