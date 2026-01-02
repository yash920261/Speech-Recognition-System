from audio_utils import listen
import speech_recognition as sr

r = sr.Recognizer()

audio = listen()
text = r.recognize_google(audio)

print("YOU SAID:", text)
