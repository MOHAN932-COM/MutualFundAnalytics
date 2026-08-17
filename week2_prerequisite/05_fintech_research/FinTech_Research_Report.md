# FinTech Business Understanding

## MutualFundAnalytics Project

## 1. Introduction

FinTech refers to the use of technology to provide financial services more efficiently.

Indian FinTech platforms use software, APIs, databases and data analytics to provide services such as stock trading, mutual fund investment, portfolio tracking and financial reporting.

This report studies Zerodha and its mutual fund platform, Coin, and explains how data analytics can improve customer experience and support financial decision-making.

---

## 2. About Zerodha

Zerodha is an Indian financial technology company that provides online investment and trading services.

Its platform allows users to access financial products such as stocks, mutual funds and other securities.

For mutual fund investing, Zerodha provides the Coin platform.

---

## 3. Zerodha Coin

Coin is Zerodha's mutual fund investment platform.

It provides access to direct mutual fund plans and allows investors to view and manage their mutual fund investments.

Coin also provides fund analysis features such as:

- NAV information
- Fund performance
- CAGR
- Expense ratio
- Exit load
- Assets Under Management
- Risk-o-meter
- Fund manager information
- Portfolio composition
- Sector allocation

These features help investors understand mutual fund schemes before making decisions.

---

## 4. Brokerage Platform

A brokerage platform acts as an interface between investors and financial markets.

Investors can use a brokerage platform to place orders for securities through a registered broker.

The general process is:

Investor
→ Brokerage Platform
→ Stock Exchange
→ Order Matching
→ Trade Execution
→ Clearing & Settlement

For mutual funds, platforms can also provide fund discovery, investment, portfolio tracking and performance information.

---

## 5. Demat Account

A Demat account is used to hold securities electronically.

Instead of holding physical certificates, securities are maintained in electronic form.

Investors generally need:

- Bank account
- Trading or broking account
- Demat account

SEBI explains that a Demat account is maintained with a SEBI-registered Depository Participant and is used to hold securities in electronic form.

---

## 6. Depositories: NSDL and CDSL

India has two major depositories:

### NSDL

NSDL stands for National Securities Depository Limited.

It provides electronic holding and transfer of securities.

### CDSL

CDSL stands for Central Depository Services (India) Limited.

It also provides electronic holding and settlement services.

Depositories help maintain securities electronically and support secure transfer and settlement.

The two main Indian depositories are NSDL and CDSL. :contentReference[oaicite:1]{index=1}

---

## 7. Role of SEBI

SEBI stands for Securities and Exchange Board of India.

SEBI is the regulator of India's securities market.

Its role includes protecting investors, promoting the development of the securities market and regulating market participants.

SEBI provides investor education covering areas such as:

- Mutual funds
- Stock markets
- Depositories
- Brokers
- Investment advisors
- Risk management
- KYC

SEBI also provides information about registered intermediaries and market infrastructure institutions.

---

## 8. Trading and Investment Lifecycle

A simplified securities-market lifecycle is:

Investor
→ Account Setup
→ Order / Investment
→ Platform / Broker
→ Exchange or Fund Platform
→ Trade / Transaction Processing
→ Clearing
→ Settlement
→ Securities / Units Reflected in Account

For a stock transaction, an investor places an order through a broker, the order is matched on the exchange, and clearing and settlement follow.

SEBI describes the process where an investor places an order through a broker, the exchange matches the order, the clearing corporation handles clearing, and the depository facilitates transfer of securities. :contentReference[oaicite:2]{index=2}

---

## 9. Settlement Process

Settlement is the process of completing a financial transaction after a trade has been executed.

For securities transactions, settlement involves transferring:

- Securities from the seller
- Funds from the buyer

Depositories support electronic transfer of securities during settlement.

This reduces the need for physical certificates and makes the process more efficient.

---

## 10. Market Participants

Important participants in the Indian financial market include:

### Investors

Individuals or institutions that invest in financial products.

### Stock Exchanges

Platforms where securities are traded.

Examples include NSE and BSE.

### Brokers

Intermediaries that provide trading access to investors.

### Depositories

NSDL and CDSL hold securities electronically.

### Depository Participants

They provide investors access to depository services.

### Clearing Corporations

They support clearing and settlement of trades.

### Asset Management Companies

AMCs manage mutual fund schemes and their investments.

### SEBI

SEBI regulates the securities market and protects investor interests.

---

## 11. How Zerodha Uses Data Analytics

Data analytics is important for a digital investment platform because large amounts of financial and customer data need to be processed and presented in a useful form.

Coin provides investors with analytical information about their mutual fund investments.

For example, Coin provides:

- Invested amount
- Current value
- Profit and loss
- P&L percentage
- XIRR
- Average NAV
- Current NAV
- Units held
- Transaction history

Coin also provides scheme-level information such as NAV changes, CAGR, expense ratio, AUM, risk-o-meter and portfolio composition. :contentReference[oaicite:3]{index=3}

### XIRR

XIRR is particularly useful when an investor makes multiple investments at different dates, such as through SIPs.

It considers the timing and amount of multiple cash flows to calculate an annualised return.

Therefore, XIRR provides a more useful performance measure than simply looking at total profit for investments with multiple transactions. :contentReference[oaicite:4]{index=4}

---

## 12. How Analytics Improves Customer Experience

Data analytics improves the customer experience by converting raw investment data into understandable information.

For example:

Raw Transactions
→ Calculations
→ Performance Metrics
→ Visual Information
→ Investor Insights

Instead of manually calculating returns, investors can view:

- Current portfolio value
- Profit or loss
- XIRR
- NAV
- Units
- Investment history

Coin also allows users to organise their portfolio based on parameters such as invested amount, current amount, P&L, P&L percentage and scheme type. :contentReference[oaicite:5]{index=5}

This makes portfolio monitoring easier and helps investors understand their investments.

---

## 13. Connection with MutualFundAnalytics

The Zerodha Coin example is closely related to the MutualFundAnalytics project.

The MutualFundAnalytics project follows a similar data-analysis concept:

Raw Mutual Fund Data
→ Data Ingestion
→ Data Cleaning
→ Data Transformation
→ SQLite Database
→ SQL / Python Analysis
→ Power BI Dashboard
→ Mutual Fund Insights

The project analyses mutual fund data such as NAV and other fund-related information.

The results can be used to calculate performance metrics and create dashboards for understanding fund behaviour.

Similarly, a FinTech platform processes investment data and presents meaningful metrics to its users.

---

## 14. MutualFundAnalytics Data Analytics Flow

The project can be represented as:

API / CSV Files
        ↓
Python Data Ingestion
        ↓
Data Cleaning
        ↓
Data Transformation
        ↓
SQLite Database
        ↓
SQL / Python Analysis
        ↓
Performance Metrics
        ↓
Power BI Dashboard
        ↓
User Insights

This demonstrates how raw financial data can be transformed into useful analytical information.

---

## 15. Comparison with Zerodha Coin

| Area | Zerodha Coin | MutualFundAnalytics |
|------|--------------|---------------------|
| Financial domain | Mutual funds | Mutual funds |
| Data | Investment and fund data | Mutual fund data |
| NAV | Used for fund tracking | Analysed in project |
| Performance | P&L, XIRR, CAGR | Performance analysis |
| Data processing | Platform-based processing | Python processing |
| Database | Platform infrastructure | SQLite |
| Analytics | Portfolio and fund analytics | SQL/Python analytics |
| Visualization | User-facing platform | Power BI dashboard |
| Main purpose | Investment management | Data analysis and insights |

---

## 16. Benefits of Data Analytics in FinTech

Data analytics can help FinTech platforms:

1. Track investment performance.
2. Calculate returns.
3. Monitor portfolio changes.
4. Present financial information clearly.
5. Compare investment products.
6. Identify trends in financial data.
7. Support business decisions.
8. Improve customer experience.

---

## 17. Conclusion

Zerodha Coin demonstrates how technology and data analytics can be used to improve the mutual fund investment experience.

The platform provides investors with information such as NAV, P&L, XIRR, CAGR, investment value, units and portfolio information.

The MutualFundAnalytics project applies similar data-analysis principles by collecting mutual fund data, cleaning and transforming it, storing it in SQLite, analysing it using SQL and Python, and presenting insights through Power BI.

Therefore, FinTech platforms and the MutualFundAnalytics project both demonstrate how financial data can be converted into meaningful information that supports better analysis and decision-making.

---

## 18. Sources

- Zerodha Coin - What is Coin
- Zerodha Support - Mutual Fund Portfolio Tracking
- Zerodha Support - XIRR on Coin
- Zerodha Support - Mutual Fund Scheme Details
- SEBI Investor - Understanding Depositories
- SEBI Investor - What You Need to Start Investing
- SEBI Investor - Market Infrastructure Institutions