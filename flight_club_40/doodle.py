import smtplib
import requests
from common import resource


EMAIL_U = resource.get_resource_key("email")['user']
EMAIL_P = resource.get_resource_key("email")['pass']
SHEETY_USERS_ENDPOINT = resource.get_resource_key("sheety")['endpoint_users']
BEARER_TOKEN = resource.get_resource_key("sheety")['bearer_token']


class NotificationManager:

    def __init__(self):
        pass

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
            print(f"subject:Flight Price Alert!\n\n{message}")

    def get_email_ids(self):
        print("Inside get_email_ids method")
        headers = {"Authorization": f"Bearer {BEARER_TOKEN}",
                   "Content-Type": "application/json"}
        response = requests.get(url=SHEETY_USERS_ENDPOINT, headers=headers)
        data = response.json()['users']
        print(data)
        return data


if __name__ == "__main__":
    nm = NotificationManager()
    users_list = nm.get_email_ids()
    for user in users_list:
        nm.send_email(message="Test email... £99.85", to_email=user['email'], live=True)
    # nm.send_email("Test email... £99.85")
