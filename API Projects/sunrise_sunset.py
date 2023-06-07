import requests
from datetime import datetime

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
# data = response.json()

# longitude = data["iss_position"]["longitude"]
# latitude = data["iss-position"]["latitude"]
# iss_position = (longitude, latitude)
# print(iss_position)
LAT = 31.2638905
LONG = -98.5456116

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()

iss_longitude = float(data["iss_position"]["longitude"])
iss_latitude = float(data["iss-position"]["latitude"])

parameters = {
    "lat": LAT,
    "lng": LONG,
    "formatted": 0
}

sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
print(sunrise)

time_now = datetime.now()
