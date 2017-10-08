# Imports
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

# Configuring DB Conx
engine = create_engine("postgresql://@localhost/carbon_data")
Base = declarative_base()


# Setting up DB Schema
class Carbon(Base):
    __tablename__ = 'carbon_table'
    
    id = Column(Integer, primary_key=True)
    time_start = Column(String)
    time_end = Column(String)
    forecasted_carbon = Column(Integer)
    actual_carbon = Column(Integer)
    carbon_index = Column(String)

    def __repr__(self):
        return "<Carbon(time_start='%s', time_end='%s', forecasted_carbon='%s', actual_carbon='%s', carbon_index='%s')>" % (self.time_start, \
            self.time_end, self.forecasted_carbon, self.actual_carbon, self.carbon_index)

# Instantiating the DB
Base.metadata.create_all(engine)
