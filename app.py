from flask import Flask, render_template, request, jsonify
import joblib
import pandas as pd
import numpy as np
from scipy.special import inv_boxcox

app = Flask(__name__)

model = joblib.load('/model_Optimal.joblib')
scaler = joblib.load('/scaler.joblib')
columns = ['cut', 'color', 'clarity']
encoders = {col: joblib.load(f"{col}_encoder.joblib") for col in columns}
Lamda = joblib.load('/Lamda bc.joblib')


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict-page')
def predict_page():
    return render_template('predict.html')

@app.route('/predict', methods=['POST'])
def predict():
    input_data = request.form.to_dict()
    input_df = pd.DataFrame([input_data])

    # Encode categorical columns using the loaded encoders
    for col in columns:
        if col in input_df.columns:
            input_df[col] = encoders[col].transform(input_df[col])
    
    input_df = scaler.transform(input_df)

    # Make the prediction
    prediction = model.predict(input_df)
    output = prediction[0]

    original_prediction = inv_boxcox(output, Lamda)

    # Return the prediction as a JSON response
    return jsonify(prediction=original_prediction)




@app.route('/status', methods=['GET'])
def status():
    return jsonify({"status": "online"})


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080)