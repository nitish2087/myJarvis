import speech_recognition as sr
import pyaudio
r=sr.Recognizer()
with sr.Microphone() as source:
    print("Speak: ")
    audio=r.listen(source)
    print("Okay, stop now")

try:
    print("TEXT: "+ r.recognize_google(audio))
except:
    pass