import os
from twilio.rest import Client
import requests
from common import resource


api_key = os.environ.get("OWM_API_KEY")
twilio_sid = os.environ.get("TW_SID")
twilio_auth_token = os.environ.get("TW_AUTH_TOKEN")
twilio_trial_number = os.environ.get("TW_TRAIL_NO")
RECEIPT_PHONE_NUMBER = os.environ.get("TW_REC_PHONE_NUM")
# api_key = resource.get_resource_key("openweathermap.org")['api_key']
# twilio_sid = resource.get_resource_key("twilio")['sid']
# twilio_auth_token = resource.get_resource_key("twilio")['auth_token']
# twilio_trial_number = resource.get_resource_key("twilio")['trial_number']
# RECEIPT_PHONE_NUMBER = resource.get_resource_key("twilio")['rec_phone_number']


PUNE_LAT = 18.5204
PUN_LON = 73.8567

parameters = {
    "lat": PUNE_LAT,
    "lon": PUN_LON,
    "appid": api_key,
    "exclude": 'current,minutely,daily'
}

ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"

response = requests.get(ENDPOINT, params=parameters)
response.raise_for_status()
data = response.json()

bring_umbrella = False
for counter, hour_data in enumerate(data['hourly'][:12]):
    print(counter, hour_data['weather'], hour_data['weather'][0]['id'])
    if hour_data['weather'][0]['id'] < 700:
        bring_umbrella = True
        break
if bring_umbrella:
    print(f"Carry umbrella: {bring_umbrella}")
    client = Client(twilio_sid, twilio_auth_token)
    message = client.messages.create(
        body="Please carry an umbrella it is going to rain today.",
        from_=twilio_trial_number,
        to=RECEIPT_PHONE_NUMBER
    )
    print(message.sid)



