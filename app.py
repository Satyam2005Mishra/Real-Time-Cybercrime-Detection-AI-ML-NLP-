from flask import Flask, request, jsonify
import joblib
from utils import clean_text

app = Flask(__name__)
pipe = joblib.load("cyber_pipeline.joblib")

@app.route("/api", methods=["POST"])
def predict():
    text = request.json.get("text", "")
    pred = pipe.predict([clean_text(text)])[0]
    return jsonify({"prediction": pred})

if __name__ == "__main__":
    app.run(debug=True)
