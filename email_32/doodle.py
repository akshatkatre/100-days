import datetime as dt
import random

# date_of_birth = dt.datetime(year=1978, month=8, day=15)
# print(date_of_birth)

now = dt.datetime.now()
# print(now.year)
# print(now.weekday())
valid_day_of_the_week = 4

if now.weekday() == valid_day_of_the_week:
    with open("quotes.txt") as file_handle:
        quotes = file_handle.readlines()
        quote = random.choice(quotes)
        print(quote)