"""
Code Challenge
  Name: 
    JSON Parser
  Filename: 
    json.py
  Problem Statement:
    Get me the other details about the city
        Latitude and Longitude
        Weather Condition
        Wind Speed
        Sunset Rise and Set timing
"""
import requests
city = input("enter city")
url1 = "http://api.openweathermap.org/data/2.5/weather?q="
url2 =city
url3 = "&appid=e9185b28e9969fb7a300801eb026de9c"

url = url1 + url2 + url3
print (url)
response = requests.get(url)
response.content
jsondata = response.json()
print(jsondata["coord"]["lon"])
print(jsondata["coord"]["lat"])
print(jsondata["weather"])
print(jsondata["wind"]["speed"])
print(jsondata["sys"]["sunrise"])
print(jsondata["sys"]["sunset"])