import pyttsx3

engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voices')

# Force Zira (usually clearer)
engine.setProperty('voice', voices[1].id)

engine.setProperty('rate', 170)

engine.say("Hello Yash. If you can hear this, your audio system is working correctly.")
engine.runAndWait()
