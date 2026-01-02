import sounddevice as sd
import soundfile as sf

fs = 16000
duration = 4

print("Get ready… then speak clearly:")
print(">>>  This is my voice sample for verification  <<<")

sd.wait()
audio = sd.rec(int(duration * fs), samplerate=fs, channels=1)
sd.wait()

sf.write("me.wav", audio, fs)
print("Saved new me.wav")
