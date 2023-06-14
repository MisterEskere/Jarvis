import pyttsx3
import speech_recognition as sr
import spotify as sp

# Create a speech recognition object
r = sr.Recognizer()

# Initialize the text-to-speech engine
voice = pyttsx3.init()
voice.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_IT-IT_ELSA_11.0')

while True:

    # Voice recognition
    with sr.Microphone() as source: # Use the microphone
        try:
            audio = r.listen(source, 3, 5) # Listen to the microphone
            text = r.recognize_google(audio, language="it-IT") # Recognize the text
        except:
            audio = None
            text = ''
            continue

    text = text.lower() # Convert all text to lowercase
    print(text) # Print the recognized text

    # Command recognition
    if "jarvis apri spotify" in text:
        sp.open_spotify()

    elif "jarvis metti in pausa" in text:
        sp.pause_music()

    elif "jarvis rimetti la musica" in text:
        sp.resume_music()

    elif "jarvis prossima canzone" in text:
        sp.play_next_song()

    elif "jarvis canzone successiva" in text:
        sp.play_previous_song()

    elif "jarvis volume a" in text:
        position = text.find("jarvis volume a ")
        volume = text[position + len("jarvis volume a"):]

        sp.set_volume(int(volume))

    elif "jarvis riproduci traccia" in text:
        posizione = text.find("jarvis riproduci traccia ")
        traccia = text[posizione + len("jarvis riproduci traccia "):]

        sp.riproduci_brano(traccia)

    elif "jarvis riproduci album" in text:
        posizione = text.find("jarvis riproduci album ")
        album = text[posizione + len("jarvis riproduci album "):]

        sp.riproduci_album(album)

    elif "jarvis riproduci artista" in text:
        posizione = text.find("jarvis riproduci artista ")
        artista = text[posizione + len("jarvis riproduci artista"):]

        sp.riproduci_artista(artista) 

    elif "jarvis riproduci playlist" in text:
        posizione = text.find("jarvis riproduci playlist ")
        playlist = text[posizione + len("jarvis riproduci playlist "):]

        sp.riproduci_playlist(playlist)
