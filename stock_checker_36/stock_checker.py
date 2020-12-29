import requests
from twilio.rest import Client
from common import resource

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
PERCENT_DIFF = 0.0005


def send_sms(send_flag: bool, data: tuple, stock_data: str):
    """
    The function will create the message body and will send SMS via a twilio api
    if the send_flag is passed as True.
    :param send_flag: Pass True to send the SMS
    :param data: Tuple that contains the news data.
    :param stock_data: Stock percentage change, with Icon
    :return: None
    """
    message_body = f"{STOCK}: {stock_data}\nHeadline: {data[0]}\nBrief: {data[1]}"
    print(message_body)
    if send_flag:
        twilio_sid = resource.get_resource_key("twilio")['sid']
        twilio_auth_token = resource.get_resource_key("twilio")['auth_token']
        twilio_trial_number = resource.get_resource_key("twilio")['trial_number']
        RECEIPT_PHONE_NUMBER = resource.get_resource_key("twilio")['rec_phone_number']
        client = Client(twilio_sid, twilio_auth_token)
        message = client.messages.create(
            body=message_body,
            from_=twilio_trial_number,
            to=RECEIPT_PHONE_NUMBER
        )
        print(message.sid)


def get_news(query):
    """
    The function will Invoke the newapi Endpoint  to retrive the news. The
    data returned will be pruned to the top 3 articles, the articles will
    contain the news title and the news description.
    :param query:
    :return: List of tuples with top 3 news articles.
    """
    api_key_newsapi = resource.get_resource_key("newsapi.org")['api_key']
    news_parameters = {
        "q": query,
        "apiKey": api_key_newsapi
    }
    response = requests.get(NEWS_ENDPOINT, params=news_parameters)
    response.raise_for_status()
    news_data = response.json()
    filtered_news_data = [(data["title"], data["description"]) for data in news_data['articles'][:3]]
    # print(filtered_news_data)
    return filtered_news_data


api_key_alphavantage = resource.get_resource_key("alphavantage")['api_key']

parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": api_key_alphavantage
}

# Invoke stock api endpoint
response = requests.get(STOCK_ENDPOINT, params=parameters)
response.raise_for_status()

stock_data: dict = response.json()['Time Series (Daily)']
stock_data_list = [item for (key, item) in stock_data.items()]

# First item in the list represents today's data.
today_closing_price = float(stock_data_list[0]['4. close'])

# Second item in the list represents yesterday's data.
yesterday_closing_price = float(stock_data_list[1]['4. close'])
closing_difference = abs(yesterday_closing_price - today_closing_price)
yday_closing_5_percent = yesterday_closing_price * PERCENT_DIFF

print(f"yday : {yesterday_closing_price}, tday : {today_closing_price}, "
      f"diff : {closing_difference}, 5% {yday_closing_5_percent}")

if closing_difference > yday_closing_5_percent:
    # Get top three news article for the company
    news_data = get_news(COMPANY_NAME)
    if today_closing_price > yesterday_closing_price:
        stock_quote = f"▲{int(((today_closing_price - yesterday_closing_price) / yesterday_closing_price) * 100)}%"
    else:
        stock_quote = f"▼{int(((yesterday_closing_price - today_closing_price) / yesterday_closing_price) * 100)}%"

    # Send SMS for each news article
    for x in news_data:
        send_sms(False, x, stock_quote)

# counter = 0
# for key, values in stock_data.items():
#     print(counter, key, values)
#     if counter == 0:
#         today_closing = float(values['4. close'])
#     if counter == 1:
#         yesterday_closing = float(values['4. close'])
#         closing_difference = abs(yesterday_closing - today_closing)
#         yday_closing_5_percent = yesterday_closing * PERCENT_DIFF
#         print(f"yday : {yesterday_closing}, tday : {today_closing}, "
#               f"diff : {closing_difference}, 5% {yday_closing_5_percent}")
#         if closing_difference > yday_closing_5_percent:
#             news_data = get_news(COMPANY_NAME)
#             if today_closing > yesterday_closing:
#                 stock_quote = f"▲{int(((today_closing-yesterday_closing) / yesterday_closing)* 100)}%"
#             else:
#                 stock_quote =f"▼{int(((yesterday_closing-today_closing) / yesterday_closing) * 100)}%"
#             for x in news_data:
#                 send_sms(False, x, stock_quote)
#         break
#     counter += 1
