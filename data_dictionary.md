# Data Dictionary

## fund_master

| Column | Type | Description |
|---------|------|-------------|
| amfi_code | INTEGER | Unique AMFI Code |
| fund_house | TEXT | Mutual Fund House |
| scheme_name | TEXT | Name of Scheme |
| category | TEXT | Fund Category |
| sub_category | TEXT | Fund Sub Category |
| plan | TEXT | Regular/Direct Plan |
| launch_date | DATE | Launch Date |
| benchmark | TEXT | Benchmark Index |
| expense_ratio_pct | REAL | Expense Ratio |
| exit_load_pct | REAL | Exit Load |
| min_sip_amount | REAL | Minimum SIP |
| min_lumpsum_amount | REAL | Minimum Lumpsum |
| fund_manager | TEXT | Fund Manager |
| risk_category | TEXT | Risk Level |
| sebi_category_code | TEXT | SEBI Category Code |

---

## nav_history

| Column | Type | Description |
|---------|------|-------------|
| amfi_code | INTEGER | Fund Code |
| date | DATE | NAV Date |
| nav | REAL | Net Asset Value |

---

## aum_by_fund_house

| Column | Type | Description |
|---------|------|-------------|
| fund_house | TEXT | Fund House |
| date | DATE | Date |
| aum_crore | REAL | Assets Under Management |

---

## monthly_sip_inflows

| Column | Type | Description |
|---------|------|-------------|
| month | DATE | Month |
| sip_collections_crore | REAL | SIP Collections |
| sip_accounts_lakh | REAL | SIP Accounts |
| yoy_growth_pct | REAL | YoY Growth |

---

## category_inflows

| Column | Type | Description |
|---------|------|-------------|
| month | DATE | Month |
| category | TEXT | Fund Category |
| inflow_crore | REAL | Net Inflow |

---

## industry_folio_count

| Column | Type | Description |
|---------|------|-------------|
| month | DATE | Month |
| folio_count | REAL | Number of Folios |

---

## scheme_performance

| Column | Type | Description |
|---------|------|-------------|
| amfi_code | INTEGER | Fund Code |
| one_year_return | REAL | 1 Year Return |
| three_year_return | REAL | 3 Year Return |
| five_year_return | REAL | 5 Year Return |
| expense_ratio_pct | REAL | Expense Ratio |

---

## investor_transactions

| Column | Type | Description |
|---------|------|-------------|
| transaction_id | INTEGER | Transaction ID |
| amfi_code | INTEGER | Fund Code |
| investor_id | INTEGER | Investor ID |
| transaction_type | TEXT | SIP/Lumpsum/Redemption |
| amount_inr | REAL | Transaction Amount |
| transaction_date | DATE | Transaction Date |
| state | TEXT | Investor State |
| kyc_status | TEXT | KYC Status |

---

## portfolio_holdings

| Column | Type | Description |
|---------|------|-------------|
| amfi_code | INTEGER | Fund Code |
| portfolio_date | DATE | Portfolio Date |
| company_name | TEXT | Company Name |
| sector | TEXT | Sector |
| weight_pct | REAL | Holding Weight |

---

## benchmark_indices

| Column | Type | Description |
|---------|------|-------------|
| date | DATE | Date |
| benchmark_name | TEXT | Benchmark Name |
| close_value | REAL | Closing Value |