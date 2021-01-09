# NOTE - This code works when run from the Pycharm Terminal.
#        It does not work from Pycharm console

import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json
from bs4 import BeautifulSoup
import requests

PATH = '/Users/akshat/PycharmProjects/my_resources.json'


def get_resource_key(resource: str) -> str:
    with open(PATH) as file_handle:
        data = json.load(file_handle)
    return data[resource]


# date = input("Which year do you want to travel to? Type date in YYYY-MM-DD format: ")
date = "2020-01-01"
year = date[:4]

URL = f"https://www.billboard.com/charts/hot-100/{date}"

# print(URL)
contents = requests.get(URL).text
soup = BeautifulSoup(contents, "html.parser")

# print(soup.find_all(name="span", class_="chart-element__information__song"))
billboard_100_song_titles = [title.getText()
                             for title in
                             soup.find_all(name="span", class_="chart-element__information__song")]

print(f"Number of titles scraped from billboard 100 is: {len(billboard_100_song_titles)}")

# *********SPOTIFY

spotify_client_id = get_resource_key("spotify")['client_id']
spotify_client_secret = get_resource_key("spotify")['client_secret']

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=spotify_client_id,
        client_secret=spotify_client_secret,
        show_dialog=True,
        cache_path="token.txt"
    )
)

# print(sp.current_user())
user_id = sp.current_user()["id"]
# print(user_id)

print(sp.user_playlists(user=user_id))

playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100",
                                   public=False, description=f"{date} Billboard 100")
print(f"New playlist created : {playlist['name']}, id : {playlist['id']}")

print(sp.user_playlists(user=user_id))

tracks = []
# Loop through the billboard song title, search on spotify and add to tracks list
for song_title in billboard_100_song_titles:
    # print(song_title)
    query = "track:{'song_replace'}".replace('song_replace', song_title)
    # print(query)
    songs_output = sp.search(q=query, limit=1)
    try:
        print(songs_output['tracks']['items'][0]['uri'])
        tracks.append(songs_output['tracks']['items'][0]['uri'])
    except:
        print(f"--- Song not found {song_title}")

# Add tracks to playlist
sp.playlist_add_items(playlist_id=playlist['id'], items=tracks)

print("Playlist items : ")
print(f"Total items in playlist: {sp.playlist_items(playlist_id=playlist['id'])['total']}")
