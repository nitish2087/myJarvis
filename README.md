# voice-to-text-recognition
Build in python,a voice-to-text recognition system to tanslate speech/voice, recorded using microphone into text at screen. And searching web for single best result of that query. Useful for English and Hindi voice languages.
Required packages:
> pip
> SpeechRecognition
> PyAudio
> beautifulsoup4
> google

Searching query: 
search(query, tld='com', lang='en', num=10, start=0, stop=None, pause=2.0), where,
query : query string that we want to search for.
tld : tld stands for top level domain which means we want to search our result on google.com or google.in or some other domain.
lang : lang stands for language.
num : Number of results we want.
start : First result to retrieve.
stop : Last result to retrieve. Use None to keep searching forever.
pause : Lapse to wait between HTTP requests. Lapse too short may cause Google to block your IP. Keeping significant lapse will make your program slow but its safe and better option.
Return : Generator (iterator) that yields found URLs. If the stop parameter is None the iterator will loop forever.

