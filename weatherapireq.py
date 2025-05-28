import json
import requests

city_name=input('enter city name:')
api_key= 'eafd3d3b0f0584bcc1afc19370d2e5da'
# api_url=f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric'
api_url=f'http://127.0.0.1:8000/'

get_server_info = requests.get(api_url)
# print(get_server_info)
data=get_server_info.json()
print(data)
# pretty_data=json.dumps(data, indent=4)
# print(pretty_data)
# weather_data= data["weather"][0]['description']
# print(weather_data)
# temp_data=data["main"]["temp"]
# print(temp_data)
# timezone_data=data["timezone"]
# print(timezone_data)