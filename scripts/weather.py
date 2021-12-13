import requests
import os
from time import sleep

# api.openweathermap.org/data/2.5/weather?q=Nairobi&appid=3381f087470b25177a64a1ca8d93f331
apikey = '3381f087470b25177a64a1ca8d93f331'
city = 'Machakos'
prevWeather = None
c = None
try:
    c = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={apikey}&units=metric')
except Exception as e:
	if prevWeather is not None:
		print(prevWeather)
	else:
		print("Offline")
	exit()

temp = str(c.json().get('main')).split(',')[0].replace("{'temp':", "")

weather = str(c.json().get('weather')).split(',')[1].replace("'main': ", "").replace("'","")


print(f" {temp}⁰C {weather}")
prevWeather = f" {temp}⁰C {weather}"
#sleep(1000*60*15)



