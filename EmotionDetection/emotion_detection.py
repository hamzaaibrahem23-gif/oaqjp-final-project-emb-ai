import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    request_object = {
        "raw_document": {"text": text_to_analyze}
    }
    response = requests.post(url, json=request_object, headers=headers)

    if response.status_code == 200:
        formatted_response = json.loads(response.text)
        emotions = formatted_response["emotionPredictions"][0]["emotion"]
        dominant_emotion = max(emotions, key=emotions.get)
        result = {**emotions, 'dominant_emotion': dominant_emotion}

    elif response.status_code == 500:
        label = None
        score = None
    
    else:
        label = None
        score = None

    return result
