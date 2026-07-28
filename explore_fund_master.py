import pandas as pd

# Read fund master dataset
df = pd.read_csv("data/raw/01_fund_master.csv")

print("=" * 60)
print("FUND MASTER EXPLORATION")
print("=" * 60)

print("\nColumns:")
print(df.columns)

print("\nUnique Fund Houses:")
print(df["fund_house"].unique())

print("\nNumber of Fund Houses:")
print(df["fund_house"].nunique())

print("\nCategories:")
print(df["category"].unique())

print("\nSub Categories:")
print(df["sub_category"].unique())

print("\nRisk Categories:")
print(df["risk_category"].unique())

print("\nAMFI Code and Scheme Name:")
print(df[["amfi_code", "scheme_name"]])