from flask import Flask
from routes.company_info import company_info_bp
from routes.stock_data import stock_data_bp
from routes.historical_data import historical_data_bp
from routes.analytics import analytics_bp
import os

app = Flask(__name__)


app.register_blueprint(company_info_bp,url_prefix='/company-info')
app.register_blueprint(stock_data_bp,url_prefix='/stock-market-data')
app.register_blueprint(historical_data_bp,url_prefix='/historical-data')
app.register_blueprint(analytics_bp,url_prefix='/analytics')

if __name__=='__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)