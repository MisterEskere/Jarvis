import pyttsx3

engine = pyttsx3.init()

voices = engine.getProperty('voices')

for voice in voices:
    print("Nome:", voice.name)
    print("Lingua:", voice.languages)
    print("ID:", voice.id)
    print()

    engine.setProperty('voice', voice.id)

    engine.say("Prova")
    engine.runAndWait()