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

SELECT * FROM aum_by_fund_house;

SELECT fund_house, aum_crore
FROM aum_by_fund_house
WHERE fund_house = 'SBI Mutual Fund';

SELECT fund_house, aum_crore
FROM aum_by_fund_house
WHERE aum_crore > 500000;

SELECT fund_house, aum_crore
FROM aum_by_fund_house
ORDER BY aum_crore DESC;

SELECT fund_house, aum_crore
FROM aum_by_fund_house
ORDER BY aum_crore ASC;

SELECT COUNT(*) AS total_records
FROM aum_by_fund_house;

SELECT SUM(aum_crore) AS total_aum
FROM aum_by_fund_house;

SELECT AVG(aum_crore) AS average_aum
FROM aum_by_fund_house;

SELECT MAX(aum_crore) AS highest_aum
FROM aum_by_fund_house;

SELECT MIN(aum_crore) AS lowest_aum
FROM aum_by_fund_house;

SELECT fund_house,
       SUM(aum_crore) AS total_aum
FROM aum_by_fund_house
GROUP BY fund_house;

SELECT fund_house,
       SUM(aum_crore) AS total_aum
FROM aum_by_fund_house
GROUP BY fund_house
ORDER BY total_aum DESC;

SELECT fund_house,
       SUM(aum_crore) AS total_aum
FROM aum_by_fund_house
GROUP BY fund_house
HAVING total_aum > 3000000;

SELECT fund_house,
       SUM(aum_crore) AS total_aum
FROM aum_by_fund_house
GROUP BY fund_house
ORDER BY total_aum DESC
LIMIT 5;

SELECT
    fund_house,
    aum_crore,
    RANK() OVER (ORDER BY aum_crore DESC) AS ranking
FROM aum_by_fund_house;

-- 11. Fund Houses with Total AUM greater than 30 lakh crore
SELECT fund_house,
       SUM(aum_crore) AS total_aum
FROM aum_by_fund_house
GROUP BY fund_house
HAVING total_aum > 3000000;

-- 12. Fund Name with Latest NAV
SELECT
    f.amfi_code,
    f.scheme_name,
    n.nav
FROM fund_master f
JOIN nav_history n
ON f.amfi_code = n.amfi_code
LIMIT 10;

-- 13. Fund House and Scheme Names
SELECT
    f.fund_house,
    f.scheme_name,
    a.aum_crore
FROM fund_master f
JOIN aum_by_fund_house a
ON f.fund_house = a.fund_house
LIMIT 10;

-- 14. Funds with Expense Ratio Above Average
SELECT
    scheme_name,
    expense_ratio_pct
FROM fund_master
WHERE expense_ratio_pct >
(
    SELECT AVG(expense_ratio_pct)
    FROM fund_master
);
-- 15. Rank Fund Houses by AUM
SELECT
    fund_house,
    aum_crore,
    RANK() OVER (ORDER BY aum_crore DESC) AS fund_rank
FROM aum_by_fund_house;