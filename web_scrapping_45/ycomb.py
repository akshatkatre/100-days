from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
soup = BeautifulSoup(response.text, "html.parser")

# first_article = soup.select_one(".storylink")
# article_text = first_article.getText()
# article_link = first_article.get("href")
# article_upvote = soup.select_one(".score").getText()
# print(article_text, article_link, article_upvote)

storylinks = soup.select(".storylink")
article_text_list = [article.getText() for article in storylinks]
article_link_list = [article.get("href") for article in storylinks]
article_upvote_list = [int(article.getText().replace(' points','')) for article in soup.select(".score")]

print(article_text_list)
print(article_link_list)
print(article_upvote_list)
max_upvotes = max(article_upvote_list)
index_max_upvotes = article_upvote_list.index(max_upvotes)
print(index_max_upvotes)
print(article_text_list[index_max_upvotes])

