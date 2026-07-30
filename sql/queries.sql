-- 1. Top 5 Funds by Expense Ratio
SELECT scheme_name, expense_ratio_pct
FROM fund_master
ORDER BY expense_ratio_pct DESC
LIMIT 5;

-- 2. Average NAV per Fund
SELECT amfi_code, AVG(nav) AS average_nav
FROM nav_history
GROUP BY amfi_code;

-- 3. Top 5 Fund Houses by AUM
SELECT fund_house, SUM(aum_crore) AS total_aum
FROM aum_by_fund_house
GROUP BY fund_house
ORDER BY total_aum DESC
LIMIT 5;

-- 4. Monthly SIP Collections
SELECT month, sip_collections_crore
FROM monthly_sip_inflows
ORDER BY month;

-- 5. Category Wise Inflows
SELECT category, SUM(inflow_crore) AS total_inflow
FROM category_inflows
GROUP BY category;

-- 6. Industry Folio Count
SELECT month, folio_count
FROM industry_folio_count
ORDER BY month;

-- 7. Schemes with Expense Ratio below 1%
SELECT amfi_code, expense_ratio_pct
FROM scheme_performance
WHERE expense_ratio_pct < 1;

-- 8. Transactions by State
SELECT state, COUNT(*) AS total_transactions
FROM investor_transactions
GROUP BY state
ORDER BY total_transactions DESC;

-- 9. Top 10 Portfolio Holdings
SELECT company_name, weight_pct
FROM portfolio_holdings
ORDER BY weight_pct DESC
LIMIT 10;

-- 10. Average Benchmark Close Value
SELECT benchmark_name,
AVG(close_value) AS average_close
FROM benchmark_indices
GROUP BY benchmark_name;