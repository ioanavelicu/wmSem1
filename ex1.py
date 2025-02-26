### **Exercise 1: Extracting and Cleaning Data from an API**
import requests
import pandas as pd

cities = ["New York", "London", "Tokyo", "Paris", "Berlin"]
infos = []

for city in cities:
    url = f"https://wttr.in/{city}?format=%C+%t"
    response = requests.get(url)
    data = response.text.strip()
    weatherData = data.rsplit(' ', 1)
    infos.append({
        "oras": city,
        "temperatura": weatherData[1],
        "conditie meteo": weatherData[0]
    })


df = pd.DataFrame(infos)
df.to_csv('weatherConditions.csv', index=False)
print(df)