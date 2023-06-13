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
    with sr.Microphone() as source:
        # Regolazione del rumore di fondo per eliminare i suoni indesiderati
        #r.adjust_for_ambient_noise(source)

        # Acquisizione dell'audio dal microfono
        audio = r.listen(source)
        time.sleep(3)

    try:
        # Utilizzo del riconoscimento vocale di Google per convertire l'audio in testo
        text = r.recognize_google(audio, language="it-IT")

        # Restituzione del testo riconosciuto
        text = text.lower() 
        print(text)
        
    except sr.UnknownValueError:
        print("Non sono riuscito a capire cosa hai detto.")
    except sr.RequestError:
        print("La richiesta al servizio di riconoscimento vocale è fallita.")

    # Riconoscimento comandi

    if "jarvis apri spotify" in text:
        # Esegui il fil
        subprocess.call(spotify, creationflags=subprocess.CREATE_NO_WINDOW)
        voice.say("Fatto")
        voice.runAndWait()

    if "jarvis metti in pausa" in text:
        try:
            sp.pause_playback()
        except:
            # Ignora l'eccezione e continua l'esecuzione
            pass

    if "jarvis rimetti la musica" in text:
        try:
            sp.start_playback()
        except:
            # Ignora l'eccezione e continua l'esecuzione
            pass

    if "jarvis prossima canzone" in text:
        try:
            sp.next_track()
        except:
            # Ignora l'eccezione e continua l'esecuzione
            pass
    
    if "jarvis metti canzone precedente" in text:
        try:
            sp.previous_track()
        except:
            # Ignora l'eccezione e continua l'esecuzione
            pass

    if "jarvis metti il volume a" in text:
        volume_position = text.find("jarvis metti il volume a ")
        volume = text[volume_position + len("jarvis metti il volume a "):]

        try:
            sp.volume(int(volume))
        except:
            # Ignora l'eccezione e continua l'esecuzione
            pass


    if "jarvis metti" in text:
        song_position = text.find("jarvis metti ")
        song = text[song_position + len("jarvis metti "):]

        try:
            results = sp.search(q=song, type='track', limit=1)
            track_id = results['tracks']['items'][0]['id']
            sp.start_playback(uris=['spotify:track:' + track_id])
        except:
            # Ignora l'eccezione e continua l'esecuzione
            pass


    # if "jarvis DIOCANEEEE" in text:
  #       song_position = text.find("jarvis metti ")  # Trova la canzone di "jarvis metti"

  #       song = text[song_position + len("jarvis metti"):]
 #
    #     print(song)

    # #     results = sp.search(q=song, type='track', limit=1)
     #    track_id = results['tracks']['items'][0]['id']
     #    print("ID della traccia:", track_id)