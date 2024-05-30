import torch
import ChatTTS
from flask import Flask, request, jsonify, Response
import io
import soundfile as sf

app = Flask(__name__)
chat = ChatTTS.Chat()
chat.load_models()

@app.route('/tts', methods=['GET'])
def text_to_speech():
    text = request.args.get('text')
    if not text:
        return jsonify({"error": "No text provided"}), 400

    wavs = chat.infer([text], use_decoder=True)
    audio_buffer = io.BytesIO()
    sf.write(audio_buffer, wavs[0][0], 24000, format='WAV')
    audio_buffer.seek(0)
    return Response(audio_buffer,mimetype="audio/wav")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8889)
