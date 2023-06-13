import subprocess
import time

import pyttsx3
import speech_recognition as sr
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Creo oggetto per riconoscimento vocale
r = sr.Recognizer()

# Inizializzazione del motore di sintesi vocale
voice = pyttsx3.init()
voice.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_IT-IT_ELSA_11.0')

# Percorso del file eseguibile di spotify
spotify = "C:\\Users\\User\\AppData\\Roaming\\Spotify\\Spotify.exe"

# Credenziali dell'applicazione Spotify
client_id = "b256096db716426f9fdf6e8a917e0645"
client_secret = "762a3b2d45db4c1dbb862d661393d8a0"
redirect_uri = 'http://localhost:8080/'

scope = 'user-modify-playback-state'
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope=scope))

while True:
    
    text = ''

    # Riconoscimento vocale
    with sr.Microphone() as source: # Utilizzo del microfono

        audio = r.listen(source) # Ascolto del microfono

    try:
        text = r.recognize_google(audio, language="it-IT") # Riconoscimento del testo
        print(text) 
    except sr.UnknownValueError: # Se non riesce a capire cosa hai detto
        print("Non sono riuscito a capire cosa hai detto.")
        continue

    text = text.lower() # Trasformo tutto il testo in minuscolo

    # Riconoscimento comandi
    if "jarvis apri spotify" in text:
        # Esegui il file eseguibile di spotify
        subprocess.call(spotify, creationflags=subprocess.CREATE_NO_WINDOW)
        voice.say("Fatto")
        voice.runAndWait()
        continue  

    if "jarvis metti in pausa" in text:
        try:
            sp.pause_playback()
        except:
            # Ignora l'eccezione e continua l'esecuzione
            pass
        continue  

    if "jarvis rimetti la musica" in text:
        try:
            sp.start_playback()
        except:
            # Ignora l'eccezione e continua l'esecuzione
            pass
        continue  

    if "jarvis canzone successiva" in text:
        try:
            sp.next_track()
        except:
            # Ignora l'eccezione e continua l'esecuzione
            pass
        continue
    
    if "jarvis canzone precedente" in text:
        try:
            sp.previous_track()
        except:
            # Ignora l'eccezione e continua l'esecuzione
            pass
        continue  

    if "jarvis metti il volume a" in text:
        volume_position = text.find("jarvis metti il volume a ")
        volume = text[volume_position + len("jarvis metti il volume a "):]

        try:
            sp.volume(int(volume))
        except:
            # Ignora l'eccezione e continua l'esecuzione
            pass
        continue  

    if "jarvis metti la canzone" in text:
        song_position = text.find("jarvis metti la canzone ")
        song = text[song_position + len("jarvis metti la canzone"):]

        try:
            results = sp.search(q=song, type='track', limit=1)
            track_id = results['tracks']['items'][0]['id']
            sp.start_playback(uris=['spotify:track:' + track_id])
        except:
            # Ignora l'eccezione e continua l'esecuzione
            pass
        continue

    if "jarvis metti la playlist" in text:
        playlist_position = text.find("jarvis metti la playlist ")
        playlist = text[playlist_position + len("jarvis metti la playlist "):]

        try:
            results = sp.search(q=playlist, type='playlist', limit=1)
            playlist_id = results['playlists']['items'][0]['id']
            sp.start_playback(context_uri='spotify:playlist:' + playlist_id)
        except:
            # Ignora l'eccezione e continua l'esecuzione
            pass
        continue

    if "jarvis metti l'album" in text:
        album_position = text.find("jarvis metti l'album ")
        album = text[album_position + len("jarvis metti l'album "):]

        try:
            results = sp.search(q=album, type='album', limit=1)
            album_id = results['albums']['items'][0]['id']
            sp.start_playback(context_uri='spotify:album:' + album_id)
        except:
            # Ignora l'eccezione e continua l'esecuzione
            pass
        continue

    if "jarvis chiudi spotify" in text:
        try:
            sp.pause_playback()
        except:
            # Ignora l'eccezione e continua l'esecuzione
            pass

        # Chiudi il file eseguibile di spotify
        subprocess.call("taskkill /IM Spotify.exe /F", creationflags=subprocess.CREATE_NO_WINDOW)
        voice.say("Fatto")
        voice.runAndWait()
        continue

    if "jarvis spegni il pc" in text:
        voice.say("Spegnimento in corso")
        voice.runAndWait()
        subprocess.call("shutdown /s /t 1", creationflags=subprocess.CREATE_NO_WINDOW)
        continue

    if "jarvis riavvia il pc" in text:
        voice.say("Riavvio in corso")
        voice.runAndWait()
        subprocess.call("shutdown /r /t 1", creationflags=subprocess.CREATE_NO_WINDOW)
        continue

    if "jarvis esci" in text:
        voice.say("Arrivederci")
        voice.runAndWait()
        break
