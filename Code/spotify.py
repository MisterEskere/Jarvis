import spotipy
import subprocess
from spotipy.oauth2 import SpotifyOAuth

# Percorso del file eseguibile di spotify
spotify = "C:\\Users\\User\\AppData\\Roaming\\Spotify\\Spotify.exe"

# Credenziali dell'applicazione Spotify
client_id = "b256096db716426f9fdf6e8a917e0645"
client_secret = "762a3b2d45db4c1dbb862d661393d8a0"
redirect_uri = 'http://localhost:8080/'

scope = 'user-modify-playback-state'
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope=scope))


def apri_spotify():
    # Esegui il file eseguibile di spotify
    subprocess.call(spotify, creationflags=subprocess.CREATE_NO_WINDOW)

def metti_in_pausa():
    try:
        sp.pause_playback()
    except:
        return False

def rimetti_musica():
    try:
        sp.start_playback()
    except:
        return False

def canzone_successiva():
    try:
        sp.next_track()
    except:
        return False

def canzone_precedente():
    try:
        sp.previous_track()
    except:
        return False
    
def metti_volume(volume):
    try:
        sp.volume(volume)
    except:
        return False

def riproduci_brano(brano):
    try:
        sp.start_playback(uris=brano)
    except:
        return False

def riproduci_album(album):
    try:
        sp.start_playback(context_uri=album)
    except:
        return False

def riproduci_artista(artista):
    try:
        sp.start_playback(context_uri=artista)
    except:
        return False

def riproduci_playlist(playlist):
    try:
        sp.start_playback(context_uri=playlist)
    except:
        return False