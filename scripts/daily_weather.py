import requests, urllib

from bs4 import BeautifulSoup
import pandas as pd
import json


# =============================================================================
# weather = requests.get('https://m.kma.go.kr/m/nation/forecast.jsp?ampm=0')
# soup = BeautifulSoup(weather.content, 'html.parser')
# predictions = soup.find_all('div', {'class':'nation_map posi2', 'id':'weather'})
# print(predictions)
# temps = (predictions[0].find_all('span'))
# 
# =============================================================================

location = []
status = []
temp = []
rain = []
snow = []
humidity = []
wind_direction = []
wind_speed = []


mid_wea = requests.get('http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108')
midterm = BeautifulSoup(mid_wea.content, 'xml')
print("midterm\n", midterm)

cities = []

curr_wea = requests.get('http://www.weather.go.kr/weather/observation/currentweather.jsp')
current = BeautifulSoup(curr_wea.content, 'html.parser')
table = current.find_all("tbody")
print(len(table))
entries = table[0].find_all("tr")
print(len(entries))

for e in entries:
    data = e.find_all("td")
    print()
    print("\n\n\n\n")
    
    
    
    
    
    
print(data)
valid_columns = [1, 5, 7, 8, 9, 10, 11]
cleaned_data = [data[idx].text if data[idx].text !='\xa0' else None for idx in valid_columns]
print(cleaned_data)    
    
    
    
    
    
