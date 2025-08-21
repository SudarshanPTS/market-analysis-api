from flask import Blueprint, request, jsonify
import yfinance as yf

stock_data_bp = Blueprint('stock_data_bp', __name__)

@stock_data_bp.route('/', methods=['GET'])
def get_stock_data():
    ticker = request.args.get('ticker')
    if not ticker:
        return jsonify({"error": "Missing 'ticker' query parameter."}), 400
    
    try:
        stock = yf.Ticker(ticker)
        info = stock.info
        
        # If cannot find ticker or info missing
        if not info or 'regularMarketPrice' not in info:
            return jsonify({"error": f"No stock data found for ticker '{ticker}'."}), 404
        
        # Extract key real-time stock metrics
        stock_data = {
            "ticker": ticker.upper(),
            "current_price": info.get("regularMarketPrice", "N/A"),
            "day_high": info.get("dayHigh", "N/A"),
            "day_low": info.get("dayLow", "N/A"),
            "volume": info.get("volume", "N/A"),
            "previous_close": info.get("previousClose", "N/A"),
            "open": info.get("open", "N/A"),
            "currency": info.get("currency", "N/A"),
            "market_time": info.get("regularMarketTime", "N/A"),
        }
        return jsonify(stock_data)
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500
