from flask import Blueprint, request, jsonify
import yfinance as yf

analytics_bp = Blueprint('analytics_bp', __name__)

@analytics_bp.route('/', methods=['GET'])
def get_analytics():
    ticker = request.args.get('ticker')
    period = request.args.get('period', '1mo')
    interval = request.args.get('interval', '1d')

    if not ticker:
        return jsonify({"error": "Missing ticker parameter"}), 400

    try:
        stock = yf.Ticker(ticker)
        hist = stock.history(period=period, interval=interval)

        if hist.empty:
            return jsonify({"error": f"No historical data found for ticker {ticker}"}), 404

        close_prices = hist['Close']
        percentage_change = (close_prices.iloc[-1] - close_prices.iloc[0]) / close_prices.iloc[0] * 100

        analytics = {
            "ticker": ticker.upper(),
            "average_close": round(close_prices.mean(), 2),
            "max_close": round(close_prices.max(), 2),
            "min_close": round(close_prices.min(), 2),
            "volatility": round(close_prices.std(), 2),
            "percentage_change": round(percentage_change, 2)
        }

        return jsonify(analytics)

    except Exception as e:
        return jsonify({"error": str(e)}), 500
