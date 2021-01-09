from bs4 import BeautifulSoup
import requests
from price_bot_47.emailer import send_email


ITEM_SHORT_DESC = "Instant Pot Multi Use Programmable Pressure"
URL = "https://www.amazon.com/Instant-Pot-Multi-Use-Programmable-Pressure/dp/B00FLYWNYQ/ref=sr_1_4?dchild=1&keywords=instant+pot&qid=1610190322&sr=8-4"
headers = {
    "User-Agent" : "en-US,en;q=0.5",
    "Accept-Language" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:84.0) Gecko/20100101 Firefox/84.0"
}
html_contents = requests.get(url=URL, headers=headers).text
# print(html_contents)

soup = BeautifulSoup(html_contents, "lxml")
# print(soup.prettify())
price = soup.find(id="priceblock_ourprice").getText()
print(price, type(price))
price_numeric = float(price.split("$")[1])
if price_numeric < 80.0:
    message_body = f"There is a price drop on {ITEM_SHORT_DESC} " \
                   f"the current price is {price}.\n" \
                   f"{URL}"
    print("Sending email...")
    send_email(message_body)
    print("Email sent...")


