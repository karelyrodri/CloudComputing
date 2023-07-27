#!/usr/bin/env python3
# Author: Karely Rodriguez 
# CS4287-5287: Principles of Cloud Computing, Vanderbilt University

import time # for sleep
from kafka import KafkaProducer  # producer of events
import json
import requests
import sys
#global variables 
lat = 47.177046
lon = -122.186506

def getWeatherData():
    apiKey = ""
    url = "https://api.openweathermap.org/data/2.5/weather?lat=%s&lon=%s&appid=%s&units=imperial" % (lat, lon, apiKey)
    return requests.get(url).text


def getAirQualityData():
    url = "https://air-quality-by-api-ninjas.p.rapidapi.com/v1/airquality"
    querystring = {"lat":lat,"lon":lon}
    headers = {
	"X-RapidAPI-Key": "",
	"X-RapidAPI-Host": "air-quality-by-api-ninjas.p.rapidapi.com"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    return response.content
    

def getCovidData():
    url = "https://geocovid-19.p.rapidapi.com/geocovid"
    coords = str(lat) + "," + str(lon)
    querystring = {"coordinates":coords}
    headers = {
	"X-RapidAPI-Key": "",
	"X-RapidAPI-Host": "geocovid-19.p.rapidapi.com"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    return response.content 


def shell(shellNum):
    if shellNum == '1':
        data = getWeatherData()
        topic = "OpenWeatherMap"
    elif shellNum == '2':
        data = getAirQualityData()
        topic = "AirQuality"
    else: 
        data = getCovidData()
        topic = "Covid-19"
    return topic, json.loads(data)


sampleCoords = [{"lat":36.1745,"lon":-86.768},{"lat":47.177046,"lon":-122.186506},
                {"lat":33.4484,"lon":-112.074036},{"lat":25.7617,"lon":-80.191788},
                {"lat":37.335480,"lon":-121.893028}]   

#print("1 Weather Data\n2 Air quality Data\n3 Covid-19 Data")
#shellNum = input("Input the number associated with the topic you want to produce(1/2/3): ")
shellNum = sys.argv[1] #129.114.26.14:9092
producer = KafkaProducer (bootstrap_servers="129.114.26.14:30001") # acquire the producer
for i in range (len(sampleCoords)):  
    lat = sampleCoords[i]["lat"]
    lon = sampleCoords[i]["lon"]
    topic, data = shell(shellNum)
    timestamp = time.strftime("%I:%M:%S%p %Z")
    contents =  {
                "timestamp": timestamp,
                "content": data,
                }
    producer.send (topic, json.dumps(contents).encode("utf-8")) 
    producer.flush ()   # try to empty the sending buffer
    print("-Message sent to topic:", topic , "   ", timestamp)
    # sleep a second
    time.sleep (7)
producer.close ()

