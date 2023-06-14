import spotipy
import subprocess
from spotipy.oauth2 import SpotifyOAuth

# Path of the Spotify executable file
spotify = "C:\\Users\\User\\AppData\\Roaming\\Spotify\\Spotify.exe"

def read_file(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print("File not found.")
        return None

# Spotify application credentials
client_id = read_file('.../API/spotify_client.txt')
client_secret = read_file('.../API/spotify_secret.txt')
redirect_uri = 'http://localhost:8080/'

scope = 'user-modify-playback-state'
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope=scope))

def open_spotify():
    # Execute the Spotify executable file
    subprocess.call(spotify, creationflags=subprocess.CREATE_NO_WINDOW)

def pause_music():
    try:
        sp.pause_playback()
    except:
        return False

def resume_music():
    try:
        sp.start_playback()
    except:
        return False

def play_next_song():
    try:
        sp.next_track()
    except:
        return False

def play_previous_song():
    try:
        sp.previous_track()
    except:
        return False
    
def set_volume(volume):
    try:
        sp.volume(volume)
    except:
        return False

def play_track(song):
    try:
        results = sp.search(q=song, type='track', limit=1)
        track_id = results['tracks']['items'][0]['id']
        sp.start_playback(uris=['spotify:track:' + track_id])
    except:
        return False

def play_album(album):
    try:
        results = sp.search(q=album, type='album', limit=1)
        album_id = results['albums']['items'][0]['id']
        sp.start_playback(context_uri='spotify:album:' + album_id)
    except:
        return False

def play_artist(artist):
    try:
        results = sp.search(q=artist, type='artist', limit=1)
        artist_id = results['artists']['items'][0]['id']
        sp.start_playback(context_uri='spotify:artist:' + artist_id)
    except:
        return False

def play_playlist(playlist):
    try:
        results = sp.search(q=playlist, type='playlist', limit=1)
        playlist_id = results['playlists']['items'][0]['id']
        sp.start_playback(context_uri='spotify:playlist:' + playlist_id)
    except:
        return False