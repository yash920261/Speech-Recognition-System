from speechbrain.pretrained import SpeakerRecognition

rec = SpeakerRecognition.from_hparams(
    source="speechbrain/spkrec-ecapa-voxceleb"
)

print("MODEL LOADED OK")
