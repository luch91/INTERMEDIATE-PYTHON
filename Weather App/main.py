import requests
from twilio.rest import Client

OpenW_Endpoint = "https://api.openweathermap.org/data/2.5/weather"
api_key = "f7a569ce55670b80135f52a84e5ce50b"
account_sid = "AC3df5e458e412fb3b5fd43cf0627ef4bd"
auth_token = "59553c72a42c2ac2ec410312a6ccd414"

weather_params = {
    "lat": 51.507351,
    "lon": -0.127758,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(OpenW_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
  body="It's going to rain today, get an umbrella",
  from_="+18317099732",
  to="+2349077815953"
)




# (weather_data["hourly"][0]["weather"][0]["id"])
