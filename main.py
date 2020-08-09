import argparse
import sys
import os
import random
from spotipy.oauth2 import SpotifyClientCredentials

import spotipy
import spotipy.util as util

SCOPE = 'user-library-read playlist-modify-private playlist-modify-public'

REDIRECT_URI='http://localhost:8888/callback/'

parser = argparse.ArgumentParser(description='create disarray in a playlist')
parser.add_argument('username', type=str)
parser.add_argument('playlist_name', type=str)

args = parser.parse_args()

username = args.username
playlist_name = args.playlist_name

sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

playlist_id_to_modify = ''

lists = sp.user_playlists(username)
for i in lists['items']:
    if i['name'] == playlist_name:
        playlist_id_to_modify = i['uri']

# load the first 100 songs
tracks = []
result = sp.playlist_tracks(playlist_id_to_modify, additional_types=['track'])
tracks.extend(result['items'])


# if playlist is larger than 100 songs, continue loading it until end
while result['next']:
    result = sp.next(result)
    tracks.extend(result['items'])

# remove all local songs
i = 0  # just for counting how many tracks are local
for item in tracks:
    if item['is_local']:
        tracks.remove(item)
        i += 1


# print result
print("Playlist length: " + str(len(tracks)) + "\nExcluding: " + str(i))