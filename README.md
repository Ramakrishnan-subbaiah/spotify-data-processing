# spotify-data-processing
Extracted data from API provided by Spotify and processed data to MySQL DB &amp; built analytics on top of that.

## Setup spotify developer account
https://developer.spotify.com/dashboard

Create your own spotify API credentials with the above link

## spotify.py

In this file we have written the code to read the data from API and filtered the data for some specific columns then performed the write operation to write the ouput in a CSV file (spotify_track_data.csv).

Also creaed a bar chart using matplotlib library to visualize the data.

## spotify-MSQL.py

In this file we have written the code to read the data from API and filtered the data for some specific columns and loaded into the MySql DB for further analysis.
