import argparse
import sys
import os
import random
import math
from spotipy.oauth2 import SpotifyClientCredentials

import spotipy
import spotipy.util as util

SCOPE = 'user-library-read playlist-modify-private playlist-modify-public'

# remember to set this uri in spotify devportal aswell.
REDIRECT_URI='http://localhost:8888/callback/'

parser = argparse.ArgumentParser(description='create disarray in a playlist')
parser.add_argument('client_secret', type=str)
parser.add_argument('client_id', type=str)
parser.add_argument('username', type=str)
parser.add_argument('playlist_name', type=str)

args = parser.parse_args()

client_secret = args.client_secret
CLIENT_ID=args.client_id
username = args.username
playlist_name = args.playlist_name

token = util.prompt_for_user_token(username, SCOPE,CLIENT_ID,client_secret,REDIRECT_URI)

if token:
    sp = spotipy.Spotify(auth=token)
else:
    sys.exit('Bad token')

playlist_id_to_modify = ''

lists = sp.user_playlists(username)
for i in lists['items']:
    if i['name'] == playlist_name:
        playlist_id_to_modify = i['uri']

# load the first 100 songs
tracks = []
result = sp.playlist_tracks(playlist_id_to_modify, fields='items.track.id, next', additional_types=['track'])
tracks.extend(result['items'])

# if playlist is larger than 100 songs, continue loading it until end
while result['next']:
    result = sp.next(result)
    tracks.extend(result['items'])

#print(tracks)

t = []
for track in tracks:
    s = str(track)
    t.append(s[18:40])

#print(t)

# shuffle the tracks, randomly
random.shuffle(t)

nr_tracks = len(t)
hunds = math.floor(nr_tracks / 100)
overflow = nr_tracks - (hunds * 100)
hunds_c = hunds


i = 0
# remove all tracks for playlist
while hunds_c >= 1:
    sp.user_playlist_remove_all_occurrences_of_tracks(username, playlist_id_to_modify, t[i:i+99])
    hunds_c -= 1
    i += 100

sp.user_playlist_remove_all_occurrences_of_tracks(username, playlist_id_to_modify, t[hunds*100:hunds*100+overflow])

i = 0
hunds_c = hunds
# add the disarrayed tracks to the playlist
while hunds_c >= 1:
    sp.user_playlist_add_tracks(username, playlist_id_to_modify, t[i:i+99])
    hunds_c -= 1
    i += 100

sp.user_playlist_add_tracks(username, playlist_id_to_modify, t[hunds*100:hunds*100+overflow])

print("num tracks shuffled " + str(nr_tracks))
