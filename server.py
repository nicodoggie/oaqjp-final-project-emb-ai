from operator import itemgetter
from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/emotionDetector')
def get_emotion_detector():
    text_to_analyze = request.args.get('textToAnalyze', '')
    
    result = emotion_detector(text_to_analyze)
    anger, disgust, fear, sadness, dominant_emotion = itemgetter(
        'anger', 'disgust', 'fear', 'sadness', 'dominant_emotion'
    )(result)

    if dominant_emotion is None:
        return "invalit text! Please try again!"

    return f"For the given statement, " \
        + f"the system response is "\
        + f"'anger': {anger}, 'disgust': {disgust}. "\
        + f"'fear': {fear}, 'sadness': {sadness}. " \
        + f"The dominant emotion is {dominant_emotion}/"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)