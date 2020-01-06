import speech_recognition as sr
from googlesearch import search
import os
from flask import Flask,redirect
import pyaudio

app = Flask(__name__)

@app.route('/')
def hello(j):
   return redirect("j", code=302)

r=sr.Recognizer()
with sr.Microphone() as source:
    print("Speak: ")
    audio=r.listen(source)
    print("Okay, stop now")32

try:
    s= r.recognize_google(audio)
    print("TEXT: "+s)
    l=""
    for j in search(s, tld="co.in", num=10, stop=1, pause=2):
        l+=j
    print(l)
    hello(l)
except:
    pass

if __name__ == '__main__':
   port = int(os.environ.get('PORT', 5000))
   #app.run(host='127.0.0.1', port=port)
   app.run(host='0.0.0.0', port=port)










