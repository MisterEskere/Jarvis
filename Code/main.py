import pyttsx3
import speech_recognition as sr
import spotify as sp
import utility as ut

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
        position = text.find("jarvis riproduci traccia ")
        track = text[position + len("jarvis riproduci traccia "):]

        sp.riproduci_brano(track)

    elif "jarvis riproduci album" in text:
        position = text.find("jarvis riproduci album ")
        album = text[position + len("jarvis riproduci album "):]

        sp.riproduci_album(album)

    elif "jarvis riproduci artista" in text:
        position = text.find("jarvis riproduci artista ")
        artist = text[position + len("jarvis riproduci artista"):]

        sp.riproduci_artista(artist) 

    elif "jarvis riproduci playlist" in text:
        position = text.find("jarvis riproduci playlist ")
        playlist = text[position + len("jarvis riproduci playlist "):]

        sp.riproduci_playlist(playlist)

    elif "jarvis che ore sono" in text:
        time = ut.current_time()
        voice.say("Sono le " + time)
        voice.runAndWait()

    elif "jarvis che giorno è" in text:
        date = ut.current_date()
        voice.say("Oggi è il " + date)
        voice.runAndWait()

    elif "jarvis che tempo fa a" in text:
        position = text.find("jarvis che tempo fa a ")
        city = text[position + len("jarvis che tempo fa a "):]

        weather = ut.weather(city)
        voice.say(weather)
        voice.runAndWait()
    