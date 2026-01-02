import speech_recognition as sr
import pyttsx3
import wave
import tempfile
import os

r = sr.Recognizer()
# Optimize recognition parameters
r.energy_threshold = 4000  # Adjust based on your environment (higher = less sensitive to noise)
r.dynamic_energy_threshold = True  # Automatically adjust to ambient noise
r.pause_threshold = 0.8  # Seconds of silence before phrase is considered complete
r.phrase_threshold = 0.3  # Minimum seconds of speaking audio before considering it a phrase
r.non_speaking_duration = 0.5  # Seconds of non-speaking audio to keep on both sides

tts = pyttsx3.init()

def speak(text):
    tts.say(text)
    tts.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Adjusting for ambient noise... Please wait")
        r.adjust_for_ambient_noise(source, duration=1)
        print("Listening... Speak now!")
        try:
            audio = r.listen(source, timeout=10, phrase_time_limit=10)
            return audio
        except sr.WaitTimeoutError:
            print("No speech detected within timeout period")
            return None

def save_temp(audio):
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as f:
        name = f.name
    w = wave.open(name, "wb")
    w.setnchannels(1)
    w.setsampwidth(2)
    w.setframerate(16000)
    w.writeframes(audio.get_raw_data())
    w.close()
    return name

def cleanup_temp(filepath):
    """Delete temporary audio file"""
    try:
        if os.path.exists(filepath):
            os.remove(filepath)
    except Exception as e:
        print(f"Warning: Could not delete temp file {filepath}: {e}")
