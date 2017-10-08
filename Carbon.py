import requests
import json

#setting up the database
from sqlalchemy import create_engine
engine = create_engine("postgresql://@localhost/carbon_data")

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

from sqlalchemy import Column, Integer, String

class Carbon(Base):
    __tablename__ = 'carbon_table'
    
    id = Column(Integer, primary_key=True)
    time_start = Column(String)
    time_end = Column(String)
    forecasted_carbon = Column(Integer)
    actual_carbon = Column(Integer)
    carbon_index = Column(String)

    def __repr__(self):
        return "<User(time_start='%s', time_end='%s', forecasted_carbon='%s', actual_carbon='%s', carbon_index='%s')>" % (self.time_start, \
            self.time_end, self.forecasted_carbon, self.actual_carbon, self.carbon_index)

Base.metadata.create_all(engine)

from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
Session.configure(bind=engine)
session = Session()

#getting the data
url_current = "https://k1nehbcl85.execute-api.eu-west-2.amazonaws.com/v1/intensity/date"
url = "https://k1nehbcl85.execute-api.eu-west-2.amazonaws.com/v1/intensity/date/2017-10-6"
    
info = requests.get(url)
#print (info.status_code)
#print (info.headers)
#print (info.encoding)s
#print (info.text)
#print (info.json())

#adding the data to the database
if(info.ok):
    data = info.json()['data']
    for n in range(len(data)):
        timeData = data[n]
        actualCarbon = timeData['intensity']['actual']
        forecastedCarbon = timeData['intensity']['forecast']
        carbonIndex = timeData['intensity']['index']
        timeStart = timeData['from']
        timeEnd = timeData['to']
        #print (forecasted_carbon, actual_carbon, carbon_index)

        row = Carbon(time_start=timeStart, time_end=timeEnd, forecasted_carbon=forecastedCarbon, \
                     actual_carbon=actualCarbon, carbon_index=carbonIndex)
        session.add(row)
        session.commit()
else:
    info.raise_for_status()

def update():
    info = requests.get(url_current)
    #print (info.status_code)
    #print (info.headers)
    #print (info.encoding)
    #print (info.text)
    #print (info.json())

    #adding the data to the database
    if(info.ok):
        data = info.json()['data']
        for n in range(len(data)):
            timeData = data[n]
            actualCarbon = timeData['intensity']['actual']
            forecastedCarbon = timeData['intensity']['forecast']
            carbonIndex = timeData['intensity']['index']
            timeStart = timeData['from']
            timeEnd = timeData['to']
            #print (forecasted_carbon, actual_carbon, carbon_index)

            row = Carbon(time_start=timeStart, time_end=timeEnd, forecasted_carbon=forecastedCarbon, \
                         actual_carbon=actualCarbon, carbon_index=carbonIndex)
            session.add(row)
            session.commit()
    else:
        info.raise_for_status()

