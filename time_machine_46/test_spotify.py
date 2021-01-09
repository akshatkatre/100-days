import spotipy
from spotipy.oauth2 import SpotifyOAuth
import common

spotify_client_id = common.resource.get_resource_key("spotify")['client_id']
spotify_client_secret = common.resource.get_resource_key("spotify")['client_secret']

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

print(sp.current_user())
user_id = sp.current_user()["id"]


