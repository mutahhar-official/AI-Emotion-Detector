"""Flask web application for emotion detection."""

from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask(__name__)


@app.route("/")
def render_index():
    """Render the home page."""
    return render_template("index.html")


@app.route("/emotionDetector")
def emotion_detector_route():
    """Analyze text submitted by the user."""
    text_to_analyze = request.args.get("textToAnalyze")

    response = emotion_detector(text_to_analyze)

    if response["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    return (
    "Emotion Scores<br><br>"
    f"Anger = {response['anger']}<br>"
    f"Disgust = {response['disgust']}<br>"
    f"Fear = {response['fear']}<br>"
    f"Joy = {response['joy']}<br>"
    f"Sadness = {response['sadness']}<br><br>"
    f"<strong>Dominant emotion: {response['dominant_emotion'].upper()}</strong>"
)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
