#Basic Weather App using Python

import requests

URL= "https://api.openweathermap.org/data/2.5/weather"
api_key = "e6bb055a2a39c71cf3ea281aa93d22d6"

query = {
         "q" : input("\n Enter the city name :"),
         "appid" : api_key
         }

X = requests.get(URL,params= query)

print("\n")

print("\nTemperature  in Celcius : " + str(X.json()["main"]["temp"] - 273.17 ))

print("\n About Weather Conditon: " + str(X.json()["weather"][0]["description"]))

print("\n pressure : " + str(X.json()["main"]["pressure"]))

print("\n Humidity % : " + str(X.json()["main"]["humidity"]))

print("\n Wind Speed in m/sec :" + str(X.json()["wind"]["speed"]))

