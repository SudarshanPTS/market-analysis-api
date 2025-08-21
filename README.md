# Market Analysis API

A Flask-based API for real-time and historical stock data analysis. Fetches data from Yahoo Finance, provides analytics, and is suitable for business research, fintech prototypes, and developer learning.

---

## Features

- **Company Info**: Retrieve metadata for any listed company.
- **Stock Market Data**: Get current stock price, volume, day high/low, and more.
- **Historical Market Data**: Download historical prices with specified period/interval.
- **Analytics**: View average, max, min, volatility, and percentage change for a ticker.

---

## Tech Stack

- Python 3
- Flask
- yfinance
- pandas

---

## Setup & Installation

1. **Clone the repository**

    ```
    git clone https://github.com/your-username/market-analysis-api.git
    cd market-analysis-api
    ```

2. **Create and activate a virtual environment**

    ```
    python -m venv venv
    # On Windows PowerShell
    .\venv\Scripts\Activate.ps1
    # On macOS/Linux
    source venv/bin/activate
    ```

3. **Install dependencies**

    ```
    pip install -r requirements.txt
    ```

4. **Run the Flask app**

    ```
    python app.py
    ```

   By default, the API will run at: `http://127.0.0.1:5000/`

---

## API Endpoints

### 1. Company Info

- **GET /company-info/**
    - **Params**: `ticker` (e.g., AAPL)
    - **Example**:  
      `http://127.0.0.1:5000/company-info/?ticker=AAPL`

### 2. Stock Market Data

- **GET /stock-market-data/**
    - **Params**: `ticker` (e.g., GOOGL)
    - **Example**:  
      `http://127.0.0.1:5000/stock-market-data/?ticker=GOOGL`

### 3. Historical Market Data

- **GET /historical-data/**
    - **Params**: `ticker`, `period` (optional, e.g., 1mo), `interval` (optional, e.g., 1d)
    - **Example**:  
      `http://127.0.0.1:5000/historical-data/?ticker=MSFT&period=1mo&interval=1d`

### 4. Analytics

- **GET /analytics/**
    - **Params**: `ticker`, `period` (optional), `interval` (optional)
    - **Returns**: Average, maximum, minimum, volatility, percent change.
    - **Example**:  
      `http://127.0.0.1:5000/analytics/?ticker=TSLA&period=3mo&interval=1d`
---

## Example Response
{
"ticker": "TSLA",
"average_close": 212.34,
"max_close": 220.45,
"min_close": 199.11,
"volatility": 5.12,
"percentage_change": 3.37
}
