import aiml
import speech_recognition as sr
import os

from wakeword import wait_for_wakeword
from audio_utils import speak, listen, save_temp, cleanup_temp
from verify_voice import is_me

# Load AIML bot
kernel = aiml.Kernel()

aiml_file = "chatbot.aiml"
if not os.path.exists(aiml_file):
    print(f"Error: {aiml_file} not found!")
    exit(1)

kernel.learn(aiml_file)

r = sr.Recognizer()

print("Assistant ready. Say 'jarvis' to wake me...")

while True:

    # 1. Wait for wake word
    wait_for_wakeword()
    speak("Yes?")

    # 2. Record voice
    audio = listen()
    
    # Check if audio was captured
    if audio is None:
        speak("I did not hear anything. Please try again.")
        continue
    
    wavfile = save_temp(audio)

    try:
        # 3. Verify speaker
        if not is_me(wavfile):
            print("❌ Voice not authorized")
            speak("Sorry. You are not authorized to talk to me.")
            continue

        print("✔ Voice verified")

        # 4. Convert to text
        max_retries = 2
        text = None
        
        for attempt in range(max_retries):
            try:
                print(f"Converting speech to text... (Attempt {attempt + 1}/{max_retries})")
                text = r.recognize_google(audio, language='en-US')
                break  # Success!
            except sr.UnknownValueError:
                if attempt < max_retries - 1:
                    print("Could not understand audio, retrying...")
                    continue
                else:
                    print("❌ Could not understand audio after retries")
                    speak("Sorry, I could not understand what you said. Please speak clearly.")
                    break
            except sr.RequestError as e:
                print(f"❌ Could not request results from Google Speech Recognition service; {e}")
                speak("Sorry, there was an error connecting to the speech service.")
                break
            except Exception as e:
                print(f"❌ Speech recognition error: {e}")
                speak("Sorry, I did not hear you clearly.")
                break
        
        if text is None:
            continue

        print("YOU:", text)

        # 5. Get AIML response
        clean = text.upper().replace("?", "").replace("'", "")
        reply = kernel.respond(clean)
        
        print(f"BOT (AIML): {reply}")

        if reply.strip() == "":
            reply = "Sorry. I do not understand."

        # 6. Speak reply
        print(f"Speaking: {reply}")
        speak(reply)
    
    finally:
        # Always cleanup temp file
        cleanup_temp(wavfile)
