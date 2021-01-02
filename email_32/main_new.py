import smtplib
import time
import datetime as dt
import random

tic = time.perf_counter()


def send_email(email_quote):
    my_email = ""

    with smtplib.SMTP("outlook.office365.com") as connection:
        connection.starttls()
        connection.login()
        connection.sendmail(
            from_addr=my_email,
            to_addrs="",
            msg=f"subject:Friday Motivation\n\n{email_quote}".
        )


SEND_EMAIL_DAY_OF_WEEK = 4
now = dt.datetime.now()
if now.weekday() == SEND_EMAIL_DAY_OF_WEEK:
    with open("quotes.txt") as file_handle:
        quotes = file_handle.readlines()
        quote = random.choice(quotes)
        send_email(quote)

toc = time.perf_counter()
print(f"total time taken {toc - tic} seconds")
