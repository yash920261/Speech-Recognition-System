from audio_utils import listen, save_temp, cleanup_temp
from verify_voice import is_me
import speech_recognition as sr

audio = listen()
wavfile = save_temp(audio)

try:
    if is_me(wavfile):
        print("✔ Same speaker - access granted")
    else:
        print("❌ Different speaker - access denied")
finally:
    cleanup_temp(wavfile)
