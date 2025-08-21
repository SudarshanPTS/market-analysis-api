import yfinance as yf

def fetch_company_info(ticker):
    stock = yf.Ticker(ticker)
    info = stock.info
    return info