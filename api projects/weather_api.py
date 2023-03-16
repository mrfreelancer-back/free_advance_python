import requests
import sqlite3
import mysql.connector

def select_data(data):
    return {"city": data['address'], "date": data['days'][0]['datetime'], "max_temp": data['days'][0]['tempmax'], "min_temp": data['days'][0]['tempmin'], "humidity": data['days'][0]['humidity'], "pressure": data['days'][0]['pressure']}

def weather_api(city='isfahan', key='KHYDNYXMPWSE6G4NBXKNTG8Y8'):
    r = requests.get(f'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city}?unitGroup=metric&key={key}&contentType=json')
    return select_data(r.json())

def insert_sqlite3_data(data):
    cnct = sqlite3.connect("weather_api.bd")
    crsr = cnct.cursor()
    crsr.execute("INSERT INTO weather VALUES(?,?,?,?,?,?)", tuple([value for key, value in data.items()]))
    cnct.commit()
    cnct.close()
    print(f"Added values in sqlite3: {[v for k, v in data.items()]}")
    
def insert_mariadb_data(data):
    cnct = mysql.connector.connect(user='root', password='',
    host='127.0.0.1', database='weather_api')
    crsr = cnct.cursor()
    crsr.execute("INSERT INTO data VALUES(\"%s\", \"%s\", \"%s\", \"%s\", \"%s\", \"%s\")" %(data['city'], data['date'], data['max_temp'],data['min_temp'], data['humidity'], data['pressure']))
    cnct.commit()
    cnct.close()
    print(f"Added values in mariaDB: {[v for k, v in data.items()]}")

insert_mariadb_data(weather_api())