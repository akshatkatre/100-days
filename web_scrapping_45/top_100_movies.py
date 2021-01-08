from bs4 import BeautifulSoup
import requests

URL = "https://www.empireonline.com/movies/features/best-movies-2/"

contents = requests.get(URL).text
soup = BeautifulSoup(contents, "html.parser")

top_100_movies = [title.getText() for title in soup.find_all(name="h3", class_="title")]
# movie_title_list = [title.getText() for title in soup.select(".title")]
# top_100_movies = movie_title_list[len(movie_title_list)-100:]

rank = 1

with open('top_movies_list.txt', 'a') as file_handle:
    for i in range(len(top_100_movies)-1, -1, -1):
        if ")" in top_100_movies[i]:
            row = f"{top_100_movies[i]}\n"
        else:
            row = f"{rank}) {top_100_movies[i]}\n"
        rank += 1
        # print(row)
        file_handle.write(row)


