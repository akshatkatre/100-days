import requests
from bs4 import BeautifulSoup


date = input("Which year do you want to travel to? Type date in YYYY-MM-DD format: ")

URL = f"https://www.billboard.com/charts/hot-100/{date}"

print(URL)
contents = requests.get(URL).text
soup = BeautifulSoup(contents, "html.parser")

print(soup.find_all(name="span", class_="chart-element__information__song"))
billboard_100_song_titles = [title.getText()
                             for title in
                             soup.find_all(name="span", class_="chart-element__information__song")]

for song_title in billboard_100_song_titles:
    print(song_title)

