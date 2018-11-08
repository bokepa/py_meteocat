# -*- coding: utf-8 -*-
import datetime
import time
import sys


from bs4 import BeautifulSoup
import requests


class Station:
        def __init__(self, name, code, lat, lon, alt, createdate, closedate, state, mun, com):
                self.name = name
                self.code = code
                

list_stations_url ="http://www.meteo.cat/observacions/llistat-xema"
list_stations_table_id ="llistaEstacions"

station_picture ="http://static-m.meteo.cat/content/xema/fotos/{station_id}.jpg"
station_url = "http://www.meteo.cat/observacions/xema/dades?codi={station_id}&dia={year}-{month}-{day}T00:00Z"
station_temperature_div_id = "dades-periode"
station_daily_summary_div_id = "resum-diari"

# Some literals used by the web
mean_temp = "Temperatura mitjana"
max_temp  = "Temperatura màxima"
min_temp  = "Temperatura mínima"
mean_hum  = "Humitat relativa mitjana"
rain_acc  = "Precipitació acumulada"
snow_height = "Gruix de neu màxim"
wind_max  = "Ratxa màxima del vent (10m)"
mean_pres = "Pressió atmosfèrica mitjana"
irradiation = "Irradiació solar global"

# Periodes
periods = {"00:00 - 00:30", "00:30 - 01:00", "01:00 - 01:30", "01:30 - 02:00"}



list_temperature_station_url =""

# given a datetime, return its meteocat nearest hour
# by example:
#   - given datetime = '13:24' -> Return 13:00 - 13:30'

def get_period_normalized(hour):{
    

}

# get all meteocat stations
def list_stations():
        url = list_stations_url
        response = requests.get(url)

        if response.status_code != 200:
            print("An error occurred while getting stations from Meteocat.cat")
            sys.exit(1)
    
        print "Connecting to Metocat to get Stations..."
        html = response.content
        soup = BeautifulSoup(html)
        table = soup.find(id=list_stations_table_id)
        i = 0
        for tr in table.find_all('tr')[1:]:
           
            tds = tr.find_all('td')
            st_comarca = tds[0].text
            st_municipi = tds[1].text
            st_estacio  = tds[2].text
            st_lat      = tds[3].text
            st_lon      = tds[4].text
            st_height   = tds[5].text
            st_created  = tds[6].text
            st_deleted  = tds[7].text
            st_status   = tds[8].text
            st_code     = st_estacio[st_estacio.index('['):st_estacio.index(']')+1]
            # ToDo: create station objects and put them into array to return
            print "STATION " , st_comarca, st_estacio, st_lat, st_lon, st_status, st_code

            i = i + 1
            print i
        print i

# Call nearest module to get the closest one        
def get_nearest_station(lat,lon, stations):
    return 1

#
def parseStationsList(html):
        table = soup.find(id=list_stations_table_id)
        tbody = tabl


if len(sys.argv) < 2:
        print("You need to provide a date in the format YYYY-MM-DD")
        sys.exit(1)

start_date = datetime.date(*time.strptime(sys.argv[1], '%Y-%m-%d')[:3])

if len(sys.argv) > 2:
        end_date = datetime.date(*time.strptime(sys.argv[2], '%Y-%m-%d')[:3])
        station_id = sys.argv[3]
else:
        end_date = datetime.date.today() - datetime.timedelta(1)

date = start_date
print ("Dates")
print (start_date)
print (end_date)

while date <= end_date:
    year, month, day = date.timetuple()[:3]

    base_url = "http://www.meteo.cat/observacions/xema/dades?codi={station_id}&dia={year}-{month}-{day}T00:00Z"

    url = base_url.format(year=year, month=month, day=day, station_id=station_id)

    response = requests.get(url)

    if response.status_code != 200:
        print("An error occurred while getting data for {day}/{month}/{year}".format(year=year, month=month, day=day))
        sys.exit(1)
    #else:
    html = response.content

    soup = BeautifulSoup(html)
    div = soup.find(id="dades-periode")
    print ("Station: ", station_id)
    print ("Dia: ")
    print (year)
    print (month)
    print (day)
    i=0
    for tr in div.find_all('tr')[2:]:
        #print (tr.text)
        ths = tr.find_all('th')
        hora = ths[0].text
        tds = tr.find_all('td')
        tm = tds[0].text
        tx = tds[1].text
        tn = tds[2].text
        htm = tds[3].text
        print "FRANJA:", hora.strip(), tm, tx, tn, htm
      
        i = i + 1
#        print (tds[0].text)
 
#      table = soup.find_all(attrs={'id': 'historyTable'})[0]
  #      mean_temp = int(table.tbody('tr')[1]('span')[2].text)

  #      sys.stdout.write("{}-{}-{},{}\n".format(year, month, day, mean_temp))
  #      sys.stdout.flush()
#    print (div.text)
#sys.stdout.write(div.text)
        #sys.stdout.flush()

    date = date + datetime.timedelta(1)
#list_stations()
s = Station("Barcelona Zoo", "X2", 41.38943, 2.18847, 7, "22.09.2006", "", "Online","Barcelones", "Barcelona")
print "Estacion:" , s.name
print "Fecha y hora: "
fecha = str(datetime.datetime.now().time())
print fecha[:5]