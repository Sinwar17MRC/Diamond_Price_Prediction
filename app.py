from flask import Flask, render_template, request, jsonify
import joblib
import pandas as pd
import numpy as np
from scipy.special import inv_boxcox

app = Flask(__name__)

scaler = joblib.load('scaler.joblib')
model = joblib.load('model_Optimal.joblib')

columns = ['cut', 'color', 'clarity']
encoders = {col: joblib.load(f"{col}_encoder.joblib") for col in columns}
Lamda = joblib.load('Lamda_bc.joblib')


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict-page')
def predict_page():
    return render_template('predict.html')



expected_columns = ['carat', 'cut', 'color', 'clarity', 'depth', 'table', 'x', 'y', 'z']
@app.route('/predict', methods=['POST'])
def predict():
    # Get JSON data from the request
    input_data = request.json

    # Convert input data to DataFrame
    input_df = pd.DataFrame([input_data])

    # Reorder columns to match the model's expected input format
    input_df = input_df[expected_columns]

    # Encode categorical columns using the loaded encoders
    for col in ['cut', 'color', 'clarity']:
        if col in input_df.columns:
            input_df[col] = encoders[col].transform(input_df[col])

    # Scale the input data
    input_df = scaler.transform(input_df)

    # Make the prediction
    prediction = model.predict(input_df)
    output = prediction[0]

    # Reverse the Box-Cox transformation
    original_prediction = inv_boxcox(output, Lamda)

    # Prepare the response in a structured format
    response = {
        "predicted_value": round(original_prediction, 2)  # Round for better readability
    }

    # Return the prediction as a JSON response
    return jsonify(response)



@app.route('/status', methods=['GET'])
def status():
    return jsonify({"status": "online"})


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080,debug=True)