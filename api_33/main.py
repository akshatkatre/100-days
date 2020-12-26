import requests
from datetime import datetime
import smtplib
import time

PUNE_LAT:float = 18.5204
PUNE_LONG:float = 73.8567


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    data = response.json()
    iss_lat = float(data['iss_position']['latitude'])
    iss_lng = float(data['iss_position']['longitude'])
    print(f"iss lat: {iss_lat}, iss long: {iss_lng}")
    print(f"Pune lat: {PUNE_LAT}, Pune Long: {PUNE_LONG}")
    if abs(iss_lat - PUNE_LAT) < 6 and abs(iss_lng - PUNE_LONG) < 6:
        return True
    return False


def is_it_current_dark():
    parameters = {
        "lat": PUNE_LAT,
        "lng": PUNE_LONG,
        "formatted": 0
    }
    response = requests.get(url='https://api.sunrise-sunset.org/json', params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise: str = data['results']['sunrise']
    sunset: str = data['results']['sunset']
    print(sunrise, sunset)
    sunrise_hr = int(sunrise.split("T")[1][:2])
    sunset_hr = int(sunset.split("T")[1][:2])
    print(sunrise_hr, sunset_hr)
    current_hr = int(datetime.now().hour)
    print(current_hr)
    if not (sunrise_hr <= current_hr <= sunset_hr):
        return True
    return False


def send_iss_email(send_email: bool):
    my_email = ""
    if send_email:
        with smtplib.SMTP("outlook.office365.com") as connection:
            connection.starttls()
            connection.login()
            connection.sendmail(
                from_addr=my_email,
                to_addrs="",
                msg=f"subject:ISS Location\n\nISS is close by, go to the window and peer out!"
            )
    else:
        print("Internationl Space Station is close by... peer outside the window")


counter = 0
while True:
    tic = time.perf_counter()
    print('Invoking International Space Station api...')
    if is_iss_overhead() and is_it_current_dark():
        send_iss_email(False)
    print('Sleep for 60 seconds')
    time.sleep(60)
    counter += 1
    toc = time.perf_counter()
    print(f'waking up')
    if counter > 10:
        break


