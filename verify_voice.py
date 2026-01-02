import os
from speechbrain.pretrained import SpeakerRecognition

recog = SpeakerRecognition.from_hparams(
    source="speechbrain/spkrec-ecapa-voxceleb"
)

REFERENCE = os.path.join(os.path.dirname(__file__), "me.wav")

THRESHOLD = 0.08   # adjust as needed
MAX_THRESHOLD = 0.25  # Maximum acceptable threshold for more tolerance

def is_me(file):
    if not os.path.exists(REFERENCE):
        print(f"Error: Reference file '{REFERENCE}' not found.")
        print("Please run record_ref.py first to create your voice sample.")
        return False
    
    if not os.path.exists(file):
        print(f"Error: Audio file '{file}' not found.")
        return False
    
    try:
        score, _ = recog.verify_files(REFERENCE, file)
        score = float(score)
        print(f"Similarity score: {score:.4f} (Threshold: {THRESHOLD:.4f})")
        
        # More forgiving verification logic
        if score >= THRESHOLD:
            print("✔ Voice match: HIGH confidence")
            return True
        elif score >= THRESHOLD * 0.7:  # 70% of threshold
            print("⚠ Voice match: MEDIUM confidence (accepting)")
            return True
        else:
            print("❌ Voice match: LOW confidence (rejecting)")
            return False
            
    except Exception as e:
        print(f"Error during voice verification: {e}")
        return False
