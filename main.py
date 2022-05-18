import psycopg2
import os
import pandas as pd
from decouple import config

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pprint

def main():
	# con = psycopg2.connect(os.environ.get("POSTGRES_URI"))
    con = psycopg2.connect('postgres://hnewxezrserycc:fa7730d9660660f7dc0292e1282e327c0a93ff49d062cf25f270d30bc27747e3@ec2-3-209-61-239.compute-1.amazonaws.com:5432/d26q7d7nbt04qe')
    cur = con.cursor()
    select_all_query = """SELECT * FROM playlists"""
    # grabbing all items
    cur.execute(select_all_query)
    query_results = cur.fetchall()
    print(len(query_results))
    print(query_results[0])
    # def create_pandas_table(sql_query, database = con):
    #     table = pd.read_sql_query(sql_query, database)
    #     return table

    # playlist_table = create_pandas_table(select_all_query)
    # print(playlist_table)
    cur.close()
    con.close()

    client_credentials_manager = SpotifyClientCredentials(client_id=config('CLIENT_ID'), client_secret=config('CLIENT_SECRET'))
    sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)
    artist = 'Robert Pete Williams'
    track = 'On My Way From Texas'
    track_id_search = sp.search(q='artist:' + artist + ' track:' + track, type='track')
    track_id = track_id_search['tracks']['items'][0]['id']
    track_id = '2ZIaH69kaz55RM4Pjx6KXl'
    audio_features = sp.audio_features(track_id)[0]
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(audio_features)

if __name__=="__main__":
    main()