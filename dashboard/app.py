import streamlit as st
import sqlite3
import pandas as pd
import plotly.express as px

# ---------------------------------------------------
# Page Configuration
# ---------------------------------------------------
st.set_page_config(
    page_title="Mutual Fund Analytics Dashboard",
    page_icon="📊",
    layout="wide"
)

# ---------------------------------------------------
# Load Data
# ---------------------------------------------------
@st.cache_data
def load_data():
    conn = sqlite3.connect("../bluestock_mf.db")
    df = pd.read_sql("SELECT * FROM fund_master", conn)
    conn.close()
    return df

df = load_data()

# ---------------------------------------------------
# Sidebar
# ---------------------------------------------------
st.sidebar.title("📌 Dashboard Filters")

category = st.sidebar.selectbox(
    "Select Category",
    ["All"] + sorted(df["category"].unique().tolist())
)

if category != "All":
    df = df[df["category"] == category]

fund_house = st.sidebar.selectbox(
    "Select Fund House",
    ["All"] + sorted(df["fund_house"].unique().tolist())
)

if fund_house != "All":
    df = df[df["fund_house"] == fund_house]

risk = st.sidebar.selectbox(
    "Select Risk Category",
    ["All"] + sorted(df["risk_category"].unique().tolist())
)

if risk != "All":
    df = df[df["risk_category"] == risk]

# ---------------------------------------------------
# Title
# ---------------------------------------------------
st.title("📊 Mutual Fund Analytics Dashboard")
st.markdown("### Interactive Dashboard using SQLite + Streamlit")

st.divider()

# ---------------------------------------------------
# KPI Cards
# ---------------------------------------------------
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Schemes", len(df))

with col2:
    st.metric("Fund Houses", df["fund_house"].nunique())

with col3:
    st.metric("Categories", df["category"].nunique())

with col4:
    st.metric(
        "Avg Expense Ratio",
        f"{df['expense_ratio_pct'].mean():.2f}%"
    )

st.divider()

# ---------------------------------------------------
# Charts
# ---------------------------------------------------
left, right = st.columns(2)

with left:

    st.subheader("Category Distribution")

    fig = px.bar(
        df["category"].value_counts().reset_index(),
        x="category",
        y="count",
        color="category",
        title="Funds by Category"
    )

    st.plotly_chart(fig, use_container_width=True)

with right:

    st.subheader("Risk Category")

    fig = px.pie(
        df,
        names="risk_category",
        title="Risk Category Distribution"
    )

    st.plotly_chart(fig, use_container_width=True)

# ---------------------------------------------------
# Fund House Distribution
# ---------------------------------------------------
st.subheader("Top Fund Houses")

fund_df = (
    df["fund_house"]
    .value_counts()
    .reset_index()
)

fund_df.columns = ["Fund House", "Schemes"]

fig = px.bar(
    fund_df,
    x="Fund House",
    y="Schemes",
    color="Schemes",
    title="Schemes by Fund House"
)

st.plotly_chart(fig, use_container_width=True)

# ---------------------------------------------------
# Expense Ratio
# ---------------------------------------------------
st.subheader("Expense Ratio Distribution")

fig = px.histogram(
    df,
    x="expense_ratio_pct",
    nbins=20,
    color_discrete_sequence=["green"]
)

st.plotly_chart(fig, use_container_width=True)

# ---------------------------------------------------
# Launch Year
# ---------------------------------------------------
st.subheader("Fund Launch Timeline")

launch = df.copy()

launch["launch_date"] = pd.to_datetime(
    launch["launch_date"]
)

launch["Year"] = launch["launch_date"].dt.year

year_df = (
    launch["Year"]
    .value_counts()
    .sort_index()
    .reset_index()
)

year_df.columns = ["Year", "Funds"]

fig = px.line(
    year_df,
    x="Year",
    y="Funds",
    markers=True
)

st.plotly_chart(fig, use_container_width=True)

# ---------------------------------------------------
# Search
# ---------------------------------------------------
st.subheader("🔍 Search Mutual Fund")

search = st.text_input("Enter Scheme Name")

if search:

    result = df[
        df["scheme_name"]
        .str.contains(search, case=False)
    ]

    st.dataframe(result)

# ---------------------------------------------------
# Dataset
# ---------------------------------------------------
st.subheader("Dataset Preview")

st.dataframe(
    df[
        [
            "scheme_name",
            "fund_house",
            "category",
            "sub_category",
            "expense_ratio_pct",
            "risk_category",
            "launch_date"
        ]
    ],
    use_container_width=True
)

# ---------------------------------------------------
# Download
# ---------------------------------------------------
csv = df.to_csv(index=False).encode("utf-8")

st.download_button(
    "⬇ Download CSV",
    csv,
    "fund_master.csv",
    "text/csv"
)

st.divider()

st.caption("Bluestock Internship Project | Mutual Fund Analytics Dashboard")