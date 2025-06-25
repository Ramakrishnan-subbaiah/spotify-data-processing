import re
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pymysql

#setup spotify credentials
#use your client id & Client secret
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id='327b0e9c322b47a790c66f48f1d113b2',
    client_secret='1a17a4717e8c416cac6ab46cc25d91e4'
))

#MySQL DB Connection
connection = pymysql.connect(
    host="localhost",
    user='root',
    password='root',
    database='test',
    cursorclass=pymysql.cursors.DictCursor
)

cursor = connection.cursor()

with open("tracksURL", 'r') as file:
    trackURL = file.readlines()

for trackURL in trackURL:
    trackURL = trackURL.strip()
    try:
        trackID = re.search(r'track/([a-zA-Z0-9]+)', trackURL).group(1)

        track = sp.track(trackID)

        trackData = {
            'Track Name': track['name'],
            'Artist': track['artists'][0]['name'],
            'Album': track['album']['name'],
            'Popularity': track['popularity'],
            'Duration (minutes)': track['duration_ms'] / 60000
        }

        insert_query = "INSERT INTO spotify_tracks (track_name, artist, album, popularity, duration_minutes) VALUES (%s, %s, %s, %s, %s);"

        cursor.execute(insert_query,(
                       trackData['Track Name'],
                       trackData['Artist'],
                       trackData['Album'],
                       trackData['Popularity'],
                       trackData['Duration (minutes)'],
                       ))

        connection.commit()

        print(f"Track {trackData['Track Name']} by {trackData['Artist']} inserted into the database")
    except Exception as e:
        print(f"Error Processing URL: {trackURL}, Error: {e}")

cursor.close()
connection.close()