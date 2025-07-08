import requests  #import the requests library to handle HTTP requests
import json # import json for cnverting the reponse text into a dictionary

def emotion_detector(text_to_analyze): # define the function with string argument
    # URL of the service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # headers for the API requests 
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"} 

    # create a dictionary of the input text
    obj = { "raw_document": { "text": text_to_analyze } } 

    # send the post request to the API
    response = requests.post(url, json = obj, headers = header)  

    # get the response in a dictionary by json
    formatted_response = json.loads(response.text)

    # get access to the emotions and their corresponding scores
    emotion_response = formatted_response['emotionPredictions'][0]['emotion']

    # finding the dominant emotion which has the maximum score
    dominant_emotion = max(emotion_response, key = emotion_response.get)

    # adding the dominant_emotion
    emotion_response['dominant_emotion'] = dominant_emotion

    return emotion_response # return the response text from the API
