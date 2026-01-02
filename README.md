# Speech Recognition Voice Assistant

A Python-based voice assistant with wake word detection, speaker verification, and conversational AI capabilities.

## Features

- 🎙️ **Wake Word Detection** - Activates on "Jarvis" using Vosk
- 🔐 **Speaker Verification** - Authenticates users by voice using SpeechBrain
- 🗣️ **Speech Recognition** - Converts speech to text using Google Speech Recognition
- 💬 **AIML Chatbot** - Responds to queries using AIML pattern matching
- 🔊 **Text-to-Speech** - Speaks responses using pyttsx3

## Prerequisites

- Python 3.7+
- Microphone
- Internet connection (for Google Speech Recognition)

## Installation

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd SPEECH_RECOGNITION_SYSTEM
   ```

2. **Install dependencies**
   ```bash
   pip install vosk pyaudio speechbrain speech_recognition pyttsx3 aiml sounddevice soundfile
   ```

3. **Download Vosk Model**
   - Download a Vosk model from [https://alphacephei.com/vosk/models](https://alphacephei.com/vosk/models)
   - Extract to the `model/` directory

## Setup

### 1. Record Your Voice Reference
Before using the assistant, record a voice sample for authentication:

```bash
python record_ref.py
```

This creates `me.wav` - your voice reference file for verification.

### 2. Test Individual Components

**Test Text-to-Speech:**
```bash
python test_tts.py
```

**Test Microphone:**
```bash
python test_mic.py
```

**Test Speaker Verification:**
```bash
python test_verify.py
```

**Test AIML Chatbot:**
```bash
python test_aiml.py
```

**Test Wake Word Detection:**
```bash
python wakeword.py
```

## Usage

### Run the Assistant

```bash
python assistant.py
```

### Interaction Flow

1. Wait for the prompt: `Listening for wake word: jarvis`
2. Say **"Jarvis"** to activate
3. The assistant responds: **"Yes?"**
4. Speak your question clearly
5. Voice verification occurs automatically
6. The assistant responds with speech

### Example Conversation

```
YOU: "Jarvis"
ASSISTANT: "Yes?"
YOU: "Hello"
ASSISTANT: "Hello! How can I help you?"
```

## Configuration

### Adjust Voice Verification Threshold

Edit `verify_voice.py`:
```python
THRESHOLD = 0.08  # Lower = stricter, Higher = more lenient
```

### Adjust Audio Recognition Settings

Edit `audio_utils.py`:
```python
r.energy_threshold = 4000  # Lower = more sensitive to quiet speech
```

### Add Custom Responses

Edit `chatbot.aiml` to add new conversation patterns:
```xml
<category>
  <pattern>YOUR QUESTION</pattern>
  <template>Your response here</template>
</category>
```

## Project Structure

```
SPEECH_RECOGNITION_SYSTEM/
├── assistant.py          # Main assistant application
├── wakeword.py          # Wake word detection module
├── audio_utils.py       # Audio capture and TTS utilities
├── verify_voice.py      # Speaker verification module
├── chatbot.aiml         # AIML conversation patterns
├── record_ref.py        # Voice reference recording script
├── test_*.py            # Test scripts for individual components
├── me.wav               # Your voice reference (created by record_ref.py)
└── model/               # Vosk speech recognition model
```

## Troubleshooting

### Voice Not Recognized
- Ensure `me.wav` exists (run `record_ref.py`)
- Check similarity scores in console output
- Adjust `THRESHOLD` in `verify_voice.py`
- Speak at similar volume as when recording reference

### Wake Word Not Detected
- Speak clearly and loudly
- Reduce background noise
- Check microphone is working (`python test_mic.py`)

### No Speech Output
- Check system volume
- Test TTS: `python test_tts.py`
- Verify speakers/headphones are connected

### Internet Connection Errors
- Google Speech Recognition requires internet
- Check your network connection

## Technologies Used

- **[Vosk](https://alphacephei.com/vosk/)** - Offline wake word detection
- **[SpeechBrain](https://speechbrain.github.io/)** - Speaker recognition
- **[SpeechRecognition](https://pypi.org/project/SpeechRecognition/)** - Speech-to-text
- **[pyttsx3](https://pyttsx3.readthedocs.io/)** - Text-to-speech
- **[PyAudio](https://people.csail.mit.edu/hubert/pyaudio/)** - Audio I/O
- **[AIML](https://pypi.org/project/python-aiml/)** - Conversational patterns

## License

This project is open source and available under the MIT License.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
