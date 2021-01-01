import datetime

tomorrow = datetime.datetime.now() + datetime.timedelta(days=1)
end_date = datetime.datetime.now() + datetime.timedelta(days=180)
print(tomorrow.strftime("%d/%m/%Y"))