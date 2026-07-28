import pandas as pd
import os

folder_path = "data/raw"

files = os.listdir(folder_path)

for file in files:

    if file.endswith(".csv"):

        path = os.path.join(folder_path, file)

        df = pd.read_csv(path)

        print("=" * 60)
        print("Dataset:", file)
        print("=" * 60)

        print("\nShape:")
        print(df.shape)

        print("\nColumns:")
        print(df.columns)

        print("\nData Types:")
        print(df.dtypes)

        print("\nFirst 5 Rows:")
        print(df.head())

        print("\nMissing Values:")
        print(df.isnull().sum())

        print("\nDuplicate Rows:")
        print(df.duplicated().sum())

        print("\n")