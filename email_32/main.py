import pandas as pd
import datetime as dt
import random
import smtplib

SENDER_EMAIL = ""
PASSWORD = ""


def send_email(message_body, to_email_address):
    with smtplib.SMTP("outlook.office365.com") as connection:
        connection.starttls()
        connection.login(user=SENDER_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=SENDER_EMAIL,
            to_addrs=to_email_address,
            msg=f"subject:Happy Birthday!\n\n{message_body}"
        )


LETTER_TEMPLATES = ['letter_templates/letter_1.txt',
                    'letter_templates/letter_2.txt',
                    'letter_templates/letter_3.txt']

now = dt.datetime.now()
print(now.year, now.month, now.day)
df = pd.read_csv('birthdays.csv')
for index, row in df.iterrows():
    if now.month == row.month and now.day == row.day:
        print(row['name'])
        with open(random.choice(LETTER_TEMPLATES)) as file_handle:
            letter_template = "".join(file_handle.readlines())
        birth_day_message = letter_template.replace('[NAME]', row['name'])
        print(birth_day_message)
        print(row['email'])
        send_email(birth_day_message, row['email'])

