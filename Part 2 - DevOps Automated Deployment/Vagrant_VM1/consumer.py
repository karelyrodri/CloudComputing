# Author: Karely Rodriguez
# CS4287-5287: Principles of Cloud Computing, Vanderbilt University

import time # for sleep
from kafka import KafkaConsumer  # consumer of events
import json
import couchdb

def sendToCouchDB(dbName, entry):
    couch = couchdb.Server("http://vm2:kr@129.114.25.56:5984")
    couch[dbName].save(entry)


def weatherData(response):
    timestamp = response["timestamp"]
    content = response["content"]
    data = content["main"]
    temp = data["temp"]
    feelsLike = data["feels_like"]
    humidity = data["humidity"]
    description = content["weather"][0]["description"]
    city = content["name"]
    windSpeed = content["wind"]["speed"]
    return {"timestamp" : timestamp, "city" : city,
            "description" : description, 
            "temperature" : temp, "feels like" : feelsLike, 
            "humidity" : humidity, "wind speed" : windSpeed
            }

def airQualityData(response):
    timestamp = response["timestamp"]
    data = response["content"]
    aqi = data["overall_aqi"]
    no2 = data["NO2"]["concentration"]
    so2 = data["SO2"]["concentration"]
    co = data["CO"]["concentration"]
    o3 = data["O3"]["concentration"]
    return {"timestamp" : timestamp, "air quality index" : aqi,
             "Ozone" : o3, "nitrogen dioxide" : no2,
             "sulfur dioxide" : so2, "carbon monoxide" : co
            }

def covidData(response):
    timestamp = response["timestamp"]
    content = response["content"]
    data = content["response"]["data"]
    county = data["place_name"]
    cases = data["total_confirmed_cases"]
    deaths = data["total_deaths"]
    trend = data["last_7_days_trend"]
    sources = data["sources"][0]["source_name"]
    return {"timestamp" : timestamp, "county" : county, 
            "cases" : cases, "deaths" : deaths,
            "trend" : trend, "sources" : sources
            }

consumer = KafkaConsumer(bootstrap_servers="129.114.26.14:9092", group_id = "group1") # acquire the consumer
consumer.subscribe(topics=["OpenWeatherMap", "AirQuality", "Covid-19"]) # subscribes to topics

# we keep reading and printing
for msg in consumer: 
    time.sleep (1)
    # Otherwise we will need to demultiplex the incoming data according to the
    # topic coming in.
    contents = json.loads(msg.value)
    if msg.topic == "OpenWeatherMap":
        print("-WEATHER Message Recieved")
        sendToCouchDB("weather",weatherData(contents))
    elif msg.topic == "AirQuality":
        print("-AIR Message Recieved")
        sendToCouchDB("air_quality", airQualityData(contents))
    elif msg.topic ==  "Covid-19":
        print("-COVID Message Recieved")
        sendToCouchDB("covid", covidData(contents))
consumer.close ()
