from flask import Flask, render_template, request, jsonify
import joblib
import pandas as pd
import numpy as np
import os
app = Flask(__name__)

model = joblib.load('/model_Optimal.joblib')
scaler = joblib.load('/scaler.joblib')
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict')
def predict_page():
    return render_template('predict.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json

    # Extract and validate features to ensure values are between 1 and 10
    variables = [
        data.get('Clump Thickness', 0),
        data.get('Uniformity of Cell Size', 0),
        data.get('Uniformity of Cell Shape', 0),
        data.get('Marginal Adhesion', 0),
        data.get('Single Epithelial Cell Size', 0),
        data.get('Bare Nuclei', 0),
        data.get('Bland Chromatin', 0),
        data.get('Normal Nucleoli', 0),
        data.get('Mitoses', 0)
    ]

    # Convert features to a DataFrame
    variables_df = pd.DataFrame([variables], columns=[
        'Clump Thickness',
        'Uniformity of Cell Size',
        'Uniformity of Cell Shape',
        'Marginal Adhesion',
        'Single Epithelial Cell Size',
        'Bare Nuclei',
        'Bland Chromatin',
        'Normal Nucleoli',
        'Mitoses'
    ])

    # Scale the features using the loaded scaler
    features_scaled = scaler.transform(features_df)

    # Get the prediction from the regressor
    prediction = model.predict(features_scaled)[0]

    # Calculate probabilities based on the prediction
    if prediction <= 2:
        benign_prob = 100
        malignant_prob = 0
    elif prediction >= 4:
        benign_prob = 0
        malignant_prob = 100
    else:
        benign_prob = ((4 - prediction) / 2) * 100  # Scale from 2 to 4
        malignant_prob = ((prediction - 2) / 2) * 100  # Scale from 2 to 4

    # Map prediction to text
    prediction_text = 'Benign' if prediction < 3 else 'Malignant'

    # Create a response with probabilities
    response = {
        "prediction": prediction_text,
        "predicted_value": round(prediction, 4),
        "probabilities": {
            "Benign": round(benign_prob, 3),
            "Malignant": round(malignant_prob, 3)
        }
    }

    return jsonify(response)


@app.route('/status')
def status_page():
    return render_template('status.html')

@app.route('/status', methods=['GET'])
def status():
    return jsonify({"status": "online"})


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080)