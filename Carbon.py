import requests
import json
from sqlalchemy.orm import sessionmaker
from database_setup import engine, Carbon

Session = sessionmaker(bind=engine)
session = Session()

#getting the data
url_current = "https://k1nehbcl85.execute-api.eu-west-2.amazonaws.com/v1/intensity/date"
url = "https://k1nehbcl85.execute-api.eu-west-2.amazonaws.com/v1/intensity/date/2017-10-6"


# Updating DB function.
def update():
    info = requests.get(url_current)

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

# Pull and store updated data. 
update()

