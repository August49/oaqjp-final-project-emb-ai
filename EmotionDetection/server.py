"""
This module provides a Flask server for emotion detection.
"""

from flask import Flask, render_template, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/")
def index():
    """Render the index page."""
    return render_template("index.html")

@app.route("/emotionDetector", methods=["POST"])
def emotion_detector_route():
    """
    Handle POST requests to the /emotionDetector route.
    Analyze the emotion of the provided text and return the result.
    """
    if request.method == "POST":
        data = request.get_json()
        statement = data.get("statement")
        result = emotion_detector(statement)

        if result.get("dominant_emotion") is None:
            return jsonify({"message": "Invalid text! Please try again!"}), 400

        return jsonify(result)

    return None

if __name__ == "__main__":
    app.run(host="localhost", port=5000)
