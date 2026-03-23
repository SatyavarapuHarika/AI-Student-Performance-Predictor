from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np

app = Flask(__name__)

# Load model
model = pickle.load(open("model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

# Home route
@app.route("/")
def home():
    return render_template("index.html")

# Prediction API
@app.route("/predict", methods=["POST"])
def predict():
    data = request.json

    hours = float(data["hours"])
    attendance = float(data["attendance"])

    features = np.array([[hours, attendance]])
    features_scaled = scaler.transform(features)

    prediction = model.predict(features_scaled)[0]

    return jsonify({"prediction": round(prediction, 2)})

if __name__ == "__main__":
    app.run(debug=True)