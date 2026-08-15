import os
import pandas as pd


# ============================================================
# SIMPLE MUTUAL FUND RECOMMENDER
# ============================================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

REPORT_DIR = os.path.join(BASE_DIR, "reports")

RISK_FILE = os.path.join(
    REPORT_DIR,
    "risk_adjusted_fund_ranking.csv"
)


# ------------------------------------------------------------
# Risk appetite mapping
# ------------------------------------------------------------

RISK_MAPPING = {
    "low": "Low",
    "moderate": "Moderate",
    "medium": "Moderate",
    "high": "High"
}


# ------------------------------------------------------------
# Load fund data
# ------------------------------------------------------------

def load_fund_data():

    if not os.path.exists(RISK_FILE):
        raise FileNotFoundError(
            f"Required file not found: {RISK_FILE}"
        )

    df = pd.read_csv(RISK_FILE)

    return df


# ------------------------------------------------------------
# Recommend top 3 funds
# ------------------------------------------------------------

def recommend_funds(risk_appetite):

    risk_appetite = risk_appetite.strip().lower()

    if risk_appetite not in RISK_MAPPING:
        print(
            "Invalid risk appetite. "
            "Please choose Low, Moderate, or High."
        )
        return pd.DataFrame()

    target_risk = RISK_MAPPING[risk_appetite]

    df = load_fund_data()

    # Filter matching risk grade
    recommendations = df[
        df["risk_grade"].astype(str).str.strip().str.lower()
        == target_risk.lower()
    ].copy()

    if recommendations.empty:

        print(
            f"No funds found for {target_risk} risk."
        )

        return pd.DataFrame()

    # Sort by Sharpe ratio
    recommendations = recommendations.sort_values(
        by="sharpe_ratio",
        ascending=False
    )

    # Select top 3 funds
    recommendations = recommendations.head(3)

    return recommendations


# ------------------------------------------------------------
# Display recommendations
# ------------------------------------------------------------

def display_recommendations(risk_appetite):

    recommendations = recommend_funds(risk_appetite)

    if recommendations.empty:
        return

    print("\n" + "=" * 70)
    print("MUTUAL FUND RECOMMENDATIONS")
    print("=" * 70)

    print(f"Risk Appetite: {risk_appetite.title()}")

    print("\nTop 3 Recommended Funds:")
    print("-" * 70)

    display_columns = [
        column
        for column in [
            "scheme_name",
            "fund_house",
            "category",
            "risk_grade",
            "sharpe_ratio"
        ]
        if column in recommendations.columns
    ]

    print(
        recommendations[display_columns].to_string(
            index=False
        )
    )

    print("-" * 70)


# ------------------------------------------------------------
# Main program
# ------------------------------------------------------------

if __name__ == "__main__":

    print("=" * 70)
    print("MUTUAL FUND SIMPLE RECOMMENDER")
    print("=" * 70)

    print("\nRisk Appetite Options:")
    print("1. Low")
    print("2. Moderate")
    print("3. High")

    risk_input = input(
        "\nEnter your risk appetite: "
    )

    display_recommendations(risk_input)