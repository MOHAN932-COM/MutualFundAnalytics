import requests
import pandas as pd
import json
from pathlib import Path

# ============================================================
# MutualFundAnalytics - REST API & JSON Assignment
# ============================================================

# Public Mutual Fund API
AMFI_CODE = "125497"
API_URL = f"https://api.mfapi.in/mf/{AMFI_CODE}"

# Output directory
OUTPUT_DIR = Path(__file__).parent

JSON_FILE = OUTPUT_DIR / "api_response.json"
CSV_FILE = OUTPUT_DIR / "api_data.csv"

# ============================================================
# 1. Send GET request
# ============================================================

response = requests.get(API_URL, timeout=30)

print("HTTP Status Code:", response.status_code)

# Check API response
response.raise_for_status()

# ============================================================
# 2. Convert JSON response
# ============================================================

data = response.json()

# Save complete JSON response
with open(JSON_FILE, "w", encoding="utf-8") as file:
    json.dump(data, file, indent=4)

print("JSON response saved successfully.")

# ============================================================
# 3. Extract NAV data
# ============================================================

nav_data = data.get("data", [])

# Convert JSON records into DataFrame
df = pd.DataFrame(nav_data)

# ============================================================
# 4. Save JSON data as CSV
# ============================================================

df.to_csv(CSV_FILE, index=False)

print("CSV file saved successfully.")

# ============================================================
# 5. Display extracted data
# ============================================================

print("\nNumber of records:", len(df))

print("\nColumns:")
print(df.columns.tolist())

print("\nFirst 5 records:")
print(df.head())