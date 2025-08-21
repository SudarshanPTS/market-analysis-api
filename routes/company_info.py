from flask import Blueprint, request, jsonify
import yfinance as yf

company_info_bp = Blueprint('company_info_bp', __name__)

@company_info_bp.route('/', methods=['GET'])
def get_company_info():
    ticker = request.args.get('ticker')
    if not ticker:
        return jsonify({"error": "Missing 'ticker' query parameter."}), 400
    try:
        stock = yf.Ticker(ticker)
        info = stock.info
        if not info or 'shortName' not in info:
            return jsonify({"error": f"No data found for ticker '{ticker}'."}), 404

        company_data = {
            "ticker": ticker.upper(),
            "name": info.get("shortName", "N/A"),
            "sector": info.get("sector", "N/A"),
            "industry": info.get("industry", "N/A"),
            "website": info.get("website", "N/A"),
            "summary": info.get("longBusinessSummary", "N/A"),
            "market_cap": info.get("marketCap", "N/A"),
            "current_price": info.get("currentPrice", "N/A"),
            "country": info.get("country", "N/A"),
        }
        return jsonify(company_data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
