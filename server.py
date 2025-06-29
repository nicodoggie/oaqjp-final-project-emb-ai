from operator import itemgetter
from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/emotionDetector')
def get_emotion_detector():
    text_to_analyze = request.args.get('textToAnalyze')
    
    if text_to_analyze is None or text_to_analyze.strip() == '':
        return "You must enter text to analyze", 422

    result = emotion_detector(text_to_analyze)
    anger, disgust, fear, sadness, dominant_emotion = itemgetter(
        'anger', 'disgust', 'fear', 'sadness', 'dominant_emotion'
    )(result)emotion_detector}, 'sadness': {sadness}. " \
        + f"The dominant emotion is {dominant_emotion}/"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)