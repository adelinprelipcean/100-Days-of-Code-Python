import requests
from datetime import datetime, timezone
import time
import smtplib

my_email = '' # Your Email
my_password = '' # Your Password

MY_LAT = 0 # Your latitude
MY_LONG = 0 # Your longitude

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

while True:
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    
    if abs(MY_LAT - iss_latitude) <= 5 and abs(MY_LONG - iss_longitude) <= 5 and (datetime.now(timezone.utc).hour >= sunset or datetime.now(timezone.utc).hour <= sunrise):
        with smtplib.SMTP('smtp.gmail.com', 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(from_addr=my_email, to_addrs='', msg='Subject: Watch the sky!\n\nLook at the ISS!')
    time.sleep(3600)

