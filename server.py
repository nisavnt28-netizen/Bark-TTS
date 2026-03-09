from flask import Flask, request, send_file
from bark import generate_audio, preload_models
from scipy.io.wavfile import write
import uuid

app = Flask(__name__)

# preload bark model
preload_models()

@app.route("/tts")
def tts():
    text = request.args.get("text")

    audio = generate_audio(text)

    filename = f"{uuid.uuid4()}.wav"

    write(filename, 24000, audio)

    return send_file(filename, mimetype="audio/wav")

app.run(host="0.0.0.0", port=10000)
