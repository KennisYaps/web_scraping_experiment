import requests
from bs4 import BeautifulSoup
import pandas as pd

weather_page = requests.get(
    "https://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168")
soup = BeautifulSoup(weather_page.content, 'html.parser')
# print(soup.prettify())
seven_day_forecast = soup.find(id="seven-day-forecast")
forecast_items = seven_day_forecast.find_all(class_="tombstone-container")
# [print(item.prettify()) for item in forecast_items]

# To extract the "title" attribute from the `img` tag, Just treat the BeautifulSoup object like a dictionary, and pass in the attribute we want as a key:
# [print(item.find("img")['title']+"\n")for item in forecast_items]

# getting period_name

periods = [period.get_text() for period in seven_day_forecast.select(
    ".tombstone-container .period-name")]

# getting short_description
short_descs = [sd.get_text() for sd in seven_day_forecast.select(
    ".tombstone-container .short-desc")]

# getting temperature
temps = [t.get_text()
         for t in seven_day_forecast.select(".tombstone-container .temp")]

# getting title attribute
descs = [d['title']
         for d in seven_day_forecast.select(".tombstone-container img")]

weather = pd.DataFrame({
    "period": periods,
    "short_desc": short_descs,
    "temp": temps,
    "desc": descs
})

print(weather)
