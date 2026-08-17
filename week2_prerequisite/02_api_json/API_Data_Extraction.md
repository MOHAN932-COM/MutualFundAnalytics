# REST API & JSON Data Extraction

## 1. Objective

The objective of this assignment is to understand how REST APIs provide financial data in JSON format and how the extracted data can be converted into a CSV file for analysis.

This assignment is directly related to the MutualFundAnalytics project because mutual fund NAV data is an important part of the project.

## 2. API Used

A public Mutual Fund API was used to retrieve historical NAV data.

**API Endpoint:**

`https://api.mfapi.in/mf/125497`

The API provides mutual fund scheme information and historical NAV data.

## 3. HTTP Method

The API was accessed using the HTTP GET method.

GET is used when the client wants to retrieve information from a server.

The Python `requests` library was used:

```python
response = requests.get(API_URL, timeout=30)