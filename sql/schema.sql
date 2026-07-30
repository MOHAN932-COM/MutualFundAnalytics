CREATE TABLE fund_master (

    amfi_code INTEGER PRIMARY KEY,

    fund_house TEXT,

    scheme_name TEXT,

    category TEXT,

    sub_category TEXT,

    plan TEXT,

    launch_date DATE,

    benchmark TEXT,

    expense_ratio_pct REAL,

    exit_load_pct REAL,

    min_sip_amount REAL,

    min_lumpsum_amount REAL,

    fund_manager TEXT,

    risk_category TEXT,

    sebi_category_code TEXT

);
CREATE TABLE nav_history (

    amfi_code INTEGER,

    date DATE,

    nav REAL,

    FOREIGN KEY (amfi_code)
    REFERENCES fund_master(amfi_code)

);
CREATE TABLE aum_by_fund_house (

    fund_house TEXT,

    date DATE,

    aum_crore REAL

);
CREATE TABLE monthly_sip_inflows (

    month DATE,

    sip_collections_crore REAL,

    sip_accounts_lakh REAL,

    yoy_growth_pct REAL

);
CREATE TABLE category_inflows (

    month DATE,

    category TEXT,

    inflow_crore REAL

);
CREATE TABLE industry_folio_count (

    month DATE,

    folio_count REAL

);
CREATE TABLE scheme_performance (

    amfi_code INTEGER,

    one_year_return REAL,

    three_year_return REAL,

    five_year_return REAL,

    expense_ratio_pct REAL,

    FOREIGN KEY(amfi_code)
    REFERENCES fund_master(amfi_code)

);
CREATE TABLE investor_transactions (

    transaction_id INTEGER PRIMARY KEY,

    amfi_code INTEGER,

    investor_id INTEGER,

    transaction_type TEXT,

    amount_inr REAL,

    transaction_date DATE,

    state TEXT,

    kyc_status TEXT,

    FOREIGN KEY(amfi_code)
    REFERENCES fund_master(amfi_code)

);
CREATE TABLE portfolio_holdings (

    amfi_code INTEGER,

    portfolio_date DATE,

    company_name TEXT,

    sector TEXT,

    weight_pct REAL,

    FOREIGN KEY(amfi_code)
    REFERENCES fund_master(amfi_code)

);
CREATE TABLE benchmark_indices (

    date DATE,

    benchmark_name TEXT,

    close_value REAL

);