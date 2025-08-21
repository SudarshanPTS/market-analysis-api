from flask import Blueprint, request, jsonify
import yfinance as yf

historical_data_bp = Blueprint('historical_data_bp', __name__)

@historical_data_bp.route('/', methods=['GET'])
@historical_data_bp.route('', methods=['GET'])
def get_historical_data():
    ticker = request.args.get('ticker')
    period = request.args.get('period', default='1mo')  # Default to 1 month
    interval = request.args.get('interval', default='1d')  # Default to 1 day
    
    if not ticker:
        return jsonify({"error": "Missing 'ticker' query parameter."}), 400
    
    try:
        stock = yf.Ticker(ticker)
        hist = stock.history(period=period, interval=interval)
        
        if hist.empty:
            return jsonify({"error": f"No historical data found for ticker '{ticker}'."}), 404
        
        # Convert historical data to a list of dicts for JSON serialization
        data = []
        for date, row in hist.iterrows():
            data.append({
                "date": date.strftime('%Y-%m-%d'),
                "open": row['Open'],
                "high": row['High'],
                "low": row['Low'],
                "close": row['Close'],
                "volume": int(row['Volume'])
            })
        
        return jsonify({
            "ticker": ticker.upper(),
            "period": period,
            "interval": interval,
            "historical_data": data
        })
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500
