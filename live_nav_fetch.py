import requests
import pandas as pd

# API URL
url = "https://api.mfapi.in/mf/125497"

# Send request
response = requests.get(url)

# Check if request was successful
if response.status_code == 200:

    # Convert JSON to Python dictionary
    data = response.json()

    # Extract NAV records
    nav_data = data["data"]

    # Convert to DataFrame
    df = pd.DataFrame(nav_data)

    # Save to CSV
    df.to_csv("data/raw/live_nav.csv", index=False)

    print("Live NAV data saved successfully!")

    print("\nFirst 5 Rows:")
    print(df.head())

else:
    print("Failed to fetch data.")
    print("Status Code:", response.status_code)