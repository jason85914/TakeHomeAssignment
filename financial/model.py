from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base

# connect to database
engine = create_engine('sqlite:///financial_data.db', echo=True)

# create Base class
Base = declarative_base()

# define table structure
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

    _column_map = {
        'symbol': 'symbol',
        'date': 'date',
        'open_price': 'open_price',
        'high_price': 'high_price',
        'low_price': 'low_price',
        'close_price': 'close_price',
        'volume': 'volume'
    }

    def __getitem__(self, key):
        if key in self._column_map:
            return getattr(self, self._column_map[key])
        else:
            raise KeyError(f'Invalid key: {key}')

# create table
Base.metadata.create_all(engine)