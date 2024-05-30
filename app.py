import os

import ChatTTS
from flask import Flask, request, send_file, jsonify, Response
import io
import soundfile as sf

app = Flask(__name__)
chat = ChatTTS.Chat()
model_source = os.getenv('MODEL_SOURCE', "huggingface")
model_path = os.getenv('MODEL_PATH', "models")
chat.load_models(source=model_source, local_path=model_path)


@app.route('/')
def home():
    return send_file('tts.html')


@app.route('/tts', methods=['GET'])
def text_to_speech():
    text = request.args.get('text')
    if not text:
        return jsonify({"error": "No text provided"}), 400

    wavs = chat.infer([text], use_decoder=True)
    audio_buffer = io.BytesIO()
    sf.write(audio_buffer, wavs[0][0], 24000, format='WAV')
    audio_buffer.seek(0)
    return Response(audio_buffer, mimetype="audio/wav")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8889)
