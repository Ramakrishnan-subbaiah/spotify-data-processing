import pandas as pd
import re
import matplotlib.pyplot as plt
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


#setup spotify credentials
#use your client id & Client secret
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id='327b0e9c322b47a790c66f48f1d113b2',
    client_secret='1a17a4717e8c416cac6ab46cc25d91e4'
))

trackURL = "https://api.spotify.com/v1/tracks/3n3Ppam7vgaVa1iaRUc9Lp"

trackID = re.search(r'tracks/([a-zA-Z0-9]+)', trackURL).group(1)

track = sp.track(trackID)

trackData ={
    'Track Name' : track['name'],
    'Artist' : track['artists'][0]['name'],
    'Album' : track['album']['name'],
    'Popularity' : track['popularity'],
    'Duration (minutes)' : track['duration_ms'] / 60000
}

df = pd.DataFrame([trackData])

print(df)

df.to_csv("spotify_track_data.csv", index=False)

feature = ['Popularity', 'Duration (minutes)']
values = [trackData['Popularity'], trackData['Duration (minutes)']]

plt.figure(figsize=(8,5))
plt.bar(feature,values, color='blue', edgecolor='black')
plt.title(f"Track Meta data for '{trackData['Track Name']}' ")
plt.ylabel("value")
plt.show()
