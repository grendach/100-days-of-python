import os
import requests
import spotipy
from bs4 import BeautifulSoup
from spotipy.oauth2 import SpotifyOAuth

URL = "https://www.billboard.com/charts/hot-100/"
SP_CLIENT_ID = os.environ['SP_CLIENT_ID'] 
SP_CLIENT_SECRET = os.environ['SP_CLIENT_SECRET']

date = input("Which year do you want to travel to? Type the date in the format YYYY-MM-DD: ")

response = requests.get(URL + date)
website_html = response.text
soup = BeautifulSoup(website_html, "html.parser")

songs_list = soup.find_all("h3", class_="a-no-trucate")
song_names = [(song.getText().strip('\t\n')) for song in songs_list]
print(song_names)

#Spotify Authentication
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=SP_CLIENT_ID,
        client_secret=SP_CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]
print(user_id)
#Searching Spotify for songs by title
song_uris = []
year = date.split("-")[0]

for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
        print(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")


#Creating a new private playlist in Spotify
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)

#Adding songs found into the new playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
