from flask import Flask, jsonify, request
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import pandas as pd
from model import FinancialData, engine
from datetime import datetime

app = Flask(__name__)
engine = create_engine('sqlite:///financial_data.db')
Session = sessionmaker(bind=engine)

@app.route('/api/financial_data')
def get_financial_data():
    try:
        # 從 URL 參數中獲取 start_date、end_date、symbol、limit 和 page 等參數
        start_date = request.args.get('start_date')
        end_date = request.args.get('end_date')
        symbol = request.args.get('symbol')
        limit = int(request.args.get('limit', 5))
        page = int(request.args.get('page', 1))

        # 使用 SQLAlchemy 從資料庫中獲取財務數據
        session = Session()
        query = session.query(FinancialData).filter(FinancialData.symbol == symbol)
        if start_date:
            try:
                start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
                query = query.filter(FinancialData.date >= start_date)
            except ValueError:
                return jsonify({
                    'data': {},
                    'info': {
                        'error': 'Invalid start_date format. Please use YYYY-MM-DD.'
                    }
                })

        if end_date:
            try:
                end_date = datetime.strptime(end_date, '%Y-%m-%d').date()
                query = query.filter(FinancialData.date <= end_date)
            except ValueError:
                return jsonify({
                    'data': {},
                    'info': {
                        'error': 'Invalid end_date format. Please use YYYY-MM-DD.'
                    }
                })
        total_count = query.count()
        total_pages = (total_count + limit - 1) // limit
        data = query.offset((page - 1) * limit).limit(limit).all()
        session.close()

        # 將獲取的數據轉換為 JSON 格式並返回給客戶端
        result = {
            'data': [{
                'symbol': d.symbol,
                'date': d.date.strftime('%Y-%m-%d'),
                'open_price': str(d.open_price),
                'close_price': str(d.close_price),
                'volume': str(d.volume)
            } for d in data],
            'pagination': {
                'count': total_count,
                'page': page,
                'limit': limit,
                'pages': total_pages
            },
            'info': {'error': ''}
        }
        return jsonify(result)
    except ValueError as e:
        return jsonify({
            'data': {},
            'info': {
                'error': str(e)
            }
        })
    except Exception as e:
        return jsonify({
            'data': {},
            'info': {
                'error': str(e)
            }
        })

@app.route('/api/statistics')
def get_statistics():
    try:
        start_date = request.args.get('start_date')
        end_date = request.args.get('end_date')
        symbol = request.args.get('symbol')

        # Create session
        session = Session()

        # Query data
        if not symbol:
            return jsonify({
                'data': {},
                'info': {
                    'error': 'symbol is required'
                }
            })

        query = session.query(FinancialData).filter(FinancialData.symbol == symbol)
        if start_date:
            try:
                start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
                query = query.filter(FinancialData.date >= start_date)
            except ValueError:
                return jsonify({
                    'data': {},
                    'info': {
                        'error': 'Invalid start_date format. Please use YYYY-MM-DD.'
                    }
                })

        if end_date:
            try:
                end_date = datetime.strptime(end_date, '%Y-%m-%d').date()
                query = query.filter(FinancialData.date <= end_date)
            except ValueError:
                return jsonify({
                    'data': {},
                    'info': {
                        'error': 'Invalid end_date format. Please use YYYY-MM-DD.'
                    }
                })

        data = query.all()

        # Calculate statistics
        if data:
            total_open_price = 0
            total_close_price = 0
            total_volume = 0
            for row in data:
                total_open_price += int(row.open_price)
                total_close_price += int(row.close_price)
                total_volume += int(row.volume)

            average_daily_open_price = round(total_open_price / len(data), 2) if data else 0.0
            average_daily_close_price = round(total_close_price / len(data), 2)
            average_daily_volume = round(total_volume / len(data), 2)
        else:
            average_daily_open_price = 0
            average_daily_close_price = 0
            average_daily_volume = 0

        # Create avg_result
        avg_result = {
            'data': {
                'start_date': start_date,
                'end_date': end_date,
                'symbol': symbol,
                'average_daily_open_price': average_daily_open_price,
                'average_daily_close_price': average_daily_close_price,
                'average_daily_volume': average_daily_volume
            },
            'info': {
                'error': ''
            }
        }

        # Close session
        session.close()

        return jsonify(avg_result)
    except Exception as e:
        return jsonify({
            'data': {},
            'info': {
                'error': str(e)
            }
        })
    
    
if __name__ == '__main__':
    app.run()