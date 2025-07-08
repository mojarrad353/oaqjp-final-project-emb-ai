import requests  #import the requests library to handle HTTP requests

def emotion_detector(text_to_analyze): # define the function with string argument

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict' # URL of the service
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"} # headers for the API requests
    obj = { "raw_document": { "text": text_to_analyze } } # create a dictionary of the input text

    response = requests.post(url, json = obj, headers = header) # send the post request to the API 

    return response.text # return the response text from the API
