import smtplib
import requests
from twilio.rest import Client
from common import resource

TWILIO_SID = resource.get_resource_key("twilio")['sid']
TWILIO_AUTH_TOKEN = resource.get_resource_key("twilio")['auth_token']
TWILIO_VIRTUAL_NUMBER = resource.get_resource_key("twilio")['trial_number']
TWILIO_VERIFIED_NUMBER = resource.get_resource_key("twilio")['to_number']
EMAIL_U = resource.get_resource_key("email")['user']
EMAIL_P = resource.get_resource_key("email")['pass']
SHEETY_USERS_ENDPOINT = resource.get_resource_key("sheety")['endpoint_users']
BEARER_TOKEN = resource.get_resource_key("sheety")['bearer_token']


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message, live=False):
        if live:
            message = self.client.messages.create(
                body=message,
                from_=TWILIO_VIRTUAL_NUMBER,
                to=TWILIO_VERIFIED_NUMBER,
            )
            # Prints if successfully sent.
            print(message.sid)
        else:
            print(
                f"***Dry run***\nfrom: {TWILIO_VIRTUAL_NUMBER}\nTo: {TWILIO_VERIFIED_NUMBER}\nMessage:\n{message}\n\n")

    def get_email_ids(self):
        print("Inside get_email_ids method")
        headers = {"Authorization": f"Bearer {BEARER_TOKEN}",
                   "Content-Type": "application/json"}
        response = requests.get(url=SHEETY_USERS_ENDPOINT, headers=headers)
        data = response.json()['users']
        print(data)
        return data

    def send_email(self, message, to_email, live=False):
        if live:
            with smtplib.SMTP("outlook.office365.com") as connection:
                connection.starttls()
                connection.login(user=EMAIL_U, password=EMAIL_P)
                connection.sendmail(
                    from_addr=EMAIL_U,
                    to_addrs=to_email,
                    msg=f"subject:Flight Price Alert!\n\n{message}".encode('utf-8')
                )
        else:
            print(f"to email: {to_email}")
            print(f"subject:Flight Price Alert!\n\n{message}")
