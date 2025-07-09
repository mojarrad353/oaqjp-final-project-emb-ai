from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_detctor():
    #retrieve the text to analyze
    text_to_analyze = request.args.get('textToAnalyze')

    #retrieve the emotion from the emotion_detector
    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] == None:
        return "Invalid text! Please try again!."

    else:
        #retrieving the dominant emotion
        dominant = response["dominant_emotion"]

        #prepare a list of emotion strings
        emotion_strs = []
        for key in ["anger", "disgust", "fear", "joy", "sadness"]:
            emotion_strs.append(f"'{key}': {response[key]}")

        #join with commas, add 'and' before the last item
        response = ", ".join(emotion_strs[:-1]) + " and " + emotion_strs[-1]

        #showing the desired output
        return f"For the given statement, the system response is {response}. The dominant emotion is <b>{dominant}</b>."

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)