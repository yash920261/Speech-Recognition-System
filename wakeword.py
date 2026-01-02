from vosk import Model, KaldiRecognizer, SetLogLevel
import pyaudio
import json

# Suppress Vosk warnings (0=errors only, -1=suppress all)
SetLogLevel(-1)

model = Model("model")
recognizer = KaldiRecognizer(model, 16000, '["jarvis", "[unk]"]')

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16,
                channels=1,
                rate=16000,
                input=True,
                frames_per_buffer=8000)

stream.start_stream()

def wait_for_wakeword():
    print("Listening for wake word: jarvis")

    while True:
        data = stream.read(4000, False)

        if recognizer.AcceptWaveform(data):
            result = json.loads(recognizer.Result())

            if "jarvis" in result.get("text", ""):
                print("Wake word detected!")
                return


# -------- RUN FUNCTION --------
if __name__ == "__main__":
    wait_for_wakeword()
