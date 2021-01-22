import requests
from common import resource


class Tmdb:
    def __init__(self):
        self.api_key = resource.get_resource_key("tmdb")['api_key']

    def get_movie_list(self, movie_name: str):
        URL = f'https://api.themoviedb.org/3/search/movie?api_key={self.api_key}&language=en-US&query={movie_name}'
        response = requests.get(URL)
        response.raise_for_status()
        data = response.json()['results']
        # print(data)
        movie_list = [{"id": movie['id'], "title": movie['title'], "release_date": movie['release_date']} for movie in response.json()['results']]
        #for movie in data:
        #    print(movie['id'], movie['title'], movie['release_date'])
        return movie_list

    def get_movie_details(self, movie_id: int):
        image_server_path = 'https://image.tmdb.org/t/p/w500'
        details_url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={self.api_key}&language=en-US"
        response = requests.get(details_url)
        response.raise_for_status()
        movie = response.json()
        return {"id": movie['id'],
                "title": movie['title'],
                "release_date": movie['release_date'],
                "description": movie['overview'],
                "img_url": f'{image_server_path}{movie["poster_path"]}'}



# movie = Tmdb()
# print(movie.get_movie_list('godfather'))
# print('........')
# print(movie.get_movie_details(238))
