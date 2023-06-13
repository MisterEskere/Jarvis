import pyttsx3
import speech_recognition as sr
import spotify as sp

# Creo oggetto per riconoscimento vocale
r = sr.Recognizer()

# Inizializzazione del motore di sintesi vocale
voice = pyttsx3.init()
voice.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_IT-IT_ELSA_11.0')

while True:

    # Riconoscimento vocale
    with sr.Microphone() as source: # Utilizzo del microfono
        try:
            audio = r.listen(source, 3, 5) # Ascolto del microfono
            text = r.recognize_google(audio, language="it-IT") # Riconoscimento del testo
        except:
            audio = None
            text = ''
            continue

    text = text.lower() # Trasformo tutto il testo in minuscolo
    print(text) # Stampo il testo riconosciuto 

    # Riconoscimento comandi
    if "jarvis apri spotify" in text:
        sp.apri_spotify()

    elif "jarvis metti in pausa" in text:
        sp.metti_in_pausa()

    elif "jarvis rimetti la musica" in text:
        sp.rimetti_musica()

    elif "jarvis canzone successiva" in text:
        sp.canzone_successiva()
    
    elif "jarvis canzone precedente" in text:
        sp.canzone_precedente()

    elif "jarvis metti il volume a" in text:
        sp.metti_volume(int(text[23:]))

    elif "jarvis metti la canzone" in text:
        sp.riproduci_brano(text[22:])

    elif "jarvis metti l'album" in text:
        sp.riproduci_album(text[21:])

    elif "jarvis metti l'artista" in text:
        sp.riproduci_artista(text[22:]) 

    elif "jarvis metti la playlist" in text:
        sp.riproduci_playlist(text[24:])