import os
import sys
from flask import Flask, request, render_template
from flask_cors import CORS, cross_origin
from text_to_speech.logging import logger
from text_to_speech.exception import TTSException
from text_to_speech.components.textToSpeech import TTSapplication
from text_to_speech.components.get_accent import get_accent_tld, get_accent_message

app = Flask(__name__)
CORS(app)


@app.route("/", methods=['GET'])
@cross_origin()
def home():
    """
    To load the web application

    Returns: Renders index.html from templates
    """
    try:
        accent_list = get_accent_message()
        return render_template('index.html', accent_list=accent_list)
    except Exception as e:
        raise TTSException(e, sys)from e


@app.route("/predict", methods=['POST', 'GET'])
@cross_origin()
def predict():
    try:
        if request.method == 'POST':
            data = request.json['data']
            accent_input = request.json['accent']
            accent = get_accent_tld(accent_input)
            result = TTSapplication().text2Speech(data, accent)
            return {"data": result.decode("utf-8")}
    except Exception as e:
        raise TTSException(e, sys)from e
        flash('Check your input', e)


@app.route("/predict", methods=["POST"])
def predict_json_endpoint():
    """
    Prediction API endpoint
    """
    try:
        record = request.get_json()
        accent = record.get("accent")
        data = record.get("message")
        result = TTSapplication().text2Speech(data, accent)
        return jsonify({"your converted mp3 is saved in Artifact folder"})
    except Exception as e:
        message = get_accent_message()
        return jsonify({"Check your input": message})

def main():
    data = "hello world"
    accent = get_accent_tld('American')
    result = TTSapplication().text2Speech(data, accent)
    return

if __name__ == "__main__":
    app.run(debug=True, port=int(os.getenv("PORT", 5000)))
