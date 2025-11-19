from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

model = pickle.load(open("model.pkl", "rb"))
stage_encoder = pickle.load(open("stage_encoder.pkl", "rb"))
disease_encoder = pickle.load(open("disease_encoder.pkl", "rb"))

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    crop_stage = request.form["crop_stage"]
    temperature = float(request.form["temperature"])
    humidity = float(request.form["humidity"])
    soil_moisture = float(request.form["soil_moisture"])
    rainfall = float(request.form["rainfall"])
    soil_pH = float(request.form["soil_pH"])

    # Encode crop stage
    crop_stage_enc = stage_encoder.transform([crop_stage])[0]

    # Feature array
    features = np.array([[crop_stage_enc, temperature, humidity, soil_moisture, rainfall, soil_pH]])

    prediction = model.predict(features)[0]
    final_output = disease_encoder.inverse_transform([prediction])[0]

    print("Prediction:", final_output)    # Shows in VS Code Terminal

    return render_template("index.html", prediction=f"Predicted Disease: {final_output}")

if __name__ == "__main__":
    app.run(debug=True)
