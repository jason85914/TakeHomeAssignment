from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base

# 建立資料庫連線
engine = create_engine('sqlite:///financial_data.db', echo=True)

# 建立 Base 類別
Base = declarative_base()

# 定義資料表結構
class FinancialData(Base):
    __tablename__ = 'financial_data'
    id = Column(Integer, primary_key=True)
    symbol = Column(String)
    date = Column(Date)
    open_price = Column(Integer)
    high_price = Column(Integer)
    low_price = Column(Integer)
    close_price = Column(Integer)
    volume = Column(Integer)

    def __getitem__(self, key):
        if key == 'symbol':
            return self.symbol
        elif key == 'date':
            return self.date
        elif key == 'open_price':
            return self.open_price
        elif key == 'high_price':
            return self.high_price
        elif key == 'low_price':
            return self.low_price
        elif key == 'close_price':
            return self.close_price
        elif key == 'volume':
            return self.volume
        else:
            raise KeyError(f'Invalid key: {key}')

# 建立資料表
Base.metadata.create_all(engine)