import os
import requests
from datetime import datetime, timedelta
from sqlalchemy.orm import sessionmaker
from model import FinancialData, engine
from flask import Flask
Session = sessionmaker(bind=engine)

app = Flask(__name__)

# get raw data from API and save to database
@app.route('/')
def get_raw_data():
    symbols = ['IBM', 'AAPL']
    api_key = os.environ.get('ALPHA_VANTAGE_API_KEY')
   
    # get data from API
    base_url = 'https://www.alphavantage.co/query'
    data = []
    for symbol in symbols:
        params = {
            'function': 'TIME_SERIES_DAILY_ADJUSTED',
            'symbol': symbol,
            'apikey': api_key,
            'outputsize': 'compact'
        }
        try:
            response = requests.get(base_url, params=params)
            response.raise_for_status()
        except requests.exceptions.HTTPError as err:
            print(f'HTTP error occurred: {err}')
            continue
        except requests.exceptions.RequestException as err:
            print(f'Other error occurred: {err}')
            continue
        try:
            raw_data = response.json()['Time Series (Daily)']
        except KeyError:
            print(f'Error: Time Series (Daily) not found in response for symbol {symbol}')
            print(f'{response.json()}')
            print(f'{api_key}')
            continue
        for date, values in raw_data.items():
           
            # only store data for the last 14 days
            if datetime.strptime(date, '%Y-%m-%d').date() >= datetime.today().date() - timedelta(days=14):
                data.append(FinancialData(
                    symbol=symbol,
                    date=datetime.strptime(date, '%Y-%m-%d').date(),
                    open_price=int(float(values['1. open'])),
                    high_price=int(float(values['2. high'])),
                    low_price=int(float(values['3. low'])),
                    close_price=int(float(values['4. close'])),
                    volume=int(values['6. volume'])
                ))
    session = Session()
    
    # check if data exists in database
    for item in data:
        symbol = item['symbol']
        date = item['date']

        count = session.query(FinancialData).filter_by(symbol=symbol, date=date).count()

        if count == 0:
           
            # if data does not exist, add to database
            financial_data = item
            session.add(financial_data)
    
    # commit changes
    session.commit()
    session.close()
    return 'Data retrieved and stored successfully!'


if __name__ == '__main__':
    app.run()