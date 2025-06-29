import requests
import json
from operator import itemgetter

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    data = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(url, json=data, headers=headers)

    if response:
        if response.status_code == 200:
            text_response = response.text
            json_response = json.loads(text_response)
            # let's extract the first prediction only
            prediction = json_response["emotionPredictions"][0]["emotion"]
            emotion_obj = {}
            dominant_emotion = ''
            dominant_score = 0
            for emotion, score in prediction.items():
                score = float(score)
                emotion_obj[emotion] = score
                if score >= dominant_score:
                    dominant_emotion = emotion
                    dominant_score = score

            emotion_obj['dominant_emotion'] = dominant_emotion
            return emotion_obj
        else:
            return f"received error code {response.status_code} with text {response.text}"
    else:
        raise Exception(f'Failed to retrieve emotion data')