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
    "<div class='emotion-result'>"
    "<h3>Emotion Scores</h3>"

    f"<div class='emotion-row'><span>Anger</span>"
    f"<span>{response['anger']:.4f}</span></div>"

    f"<div class='emotion-row'><span>Disgust</span>"
    f"<span>{response['disgust']:.4f}</span></div>"

    f"<div class='emotion-row'><span>Fear</span>"
    f"<span>{response['fear']:.4f}</span></div>"

    f"<div class='emotion-row'><span>Joy</span>"
    f"<span>{response['joy']:.4f}</span></div>"

    f"<div class='emotion-row'><span>Sadness</span>"
    f"<span>{response['sadness']:.4f}</span></div>"

    f"<div class='dominant-emotion'>"
    f"Dominant emotion: "
    f"<strong>{response['dominant_emotion'].upper()}</strong>"
    "</div>"

    "</div>"
)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
