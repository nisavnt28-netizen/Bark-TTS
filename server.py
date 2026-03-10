from flask import Flask, request, send_file
from TTS.api import TTS
import uuid

app = Flask(__name__)

tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2")

@app.route("/tts")
def tts_generate():
    text = request.args.get("text")

    file = f"{uuid.uuid4()}.wav"

    tts.tts_to_file(
        text=text,
        file_path=file,
        speaker_wav="voice.wav",
        language="en"
    )

    return send_file(file)

app.run(host="0.0.0.0", port=10000)
