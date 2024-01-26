import requests
from twilio.rest import Client


api_key = input("Enter your openweathermap.com api key: ")
lat = input("Enter the latitude of your location: ")
long = input("Enter the longitude of your location: ")
weather_api_endpoint = "https://api.openweathermap.org/data/2.5/forecast"
account_sid = input("Enter your twilio account sid number: ")
auth_token = input("Enter your twilio account auth token: ")
from_num = input("Enter the number which will send the sms(formatted as +countrycode...): ")
to_num = input("Enter the number which the sms will be sent(formatted as +countrycode...): ")

parameters = {
    "lat": lat,
    "lon" : long,
    "appid" : api_key,
    # to limit time stamps to near future
    "cnt": 4,
}

api_response = requests.get(weather_api_endpoint,params=parameters)
api_response.raise_for_status()
weather_data = api_response.json()
weather_data_id = api_response.json()["list"][0]["weather"][0]["id"]

will_rain = False
for hourly_data in weather_data["list"]:
    cond_code = hourly_data["weather"][0]["id"]
    if int(cond_code) < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid,auth_token)
    message = client.messages.create( from_=from_num, body= "Consider bringing an umbrella today it might rain.", to= to_num)
print(message.status)