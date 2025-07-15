from flask import Flask, render_template, request
import joblib
import pandas as pd
import json
import os

PREDICTIONS_FILE = 'predictions.json'

def load_predictions():
    if os.path.exists(PREDICTIONS_FILE):
        with open(PREDICTIONS_FILE, 'r') as f:
            return json.load(f)
    return {'High': 0, 'Medium': 0, 'Low': 0}

def save_predictions(data):
    with open(PREDICTIONS_FILE, 'w') as f:
        json.dump(data, f, indent=4)

app = Flask(__name__)

# Load the trained model
model = joblib.load('energy_prediction_model .pkl')

@app.route('/')
def home():
    prediction_counts = load_predictions()
    return render_template('index.html', prediction_counts=prediction_counts)

@app.route('/predict', methods=['POST'])
def predict():
    # Get data from form
    building_type = request.form['building_type']
    square_footage = int(request.form['square_footage'])
    occupancy = int(request.form['occupancy'])
    insulation_type = request.form['insulation_type']
    appliance_count = int(request.form['appliance_count'])
    avg_temperature = int(request.form['avg_temperature'])
    hvac_efficiency = int(request.form['hvac_efficiency'])
    energy_sources = request.form['energy_sources']
    peak_usage_hours = int(request.form['peak_usage_hours'])
    annual_energy_cost = int(request.form['annual_energy_cost'])

    # Prepare input data for the model
    input_data = pd.DataFrame({
        'Building_Type': [building_type],
        'Floor_Area': [square_footage],
        'Number_Of_Occupants': [occupancy],
        'Insulation_Type': [insulation_type],
        'Appliance_Count': [appliance_count],
        'Average_Temperature': [avg_temperature],
        'HVAC_Efficiency': [hvac_efficiency],
        'Energy_Sources': [energy_sources],
        'Peak_Usage_Hours': [peak_usage_hours],
        'Annual_Energy_Cost': [annual_energy_cost]
    })

    # Perform one-hot encoding on the input data
    input_data_encoded = pd.get_dummies(input_data)

    # Ensure input matches model's training columns
    missing_cols = set(model.feature_names_in_) - set(input_data_encoded.columns)
    for col in missing_cols:
        input_data_encoded[col] = 0
    input_data_encoded = input_data_encoded[model.feature_names_in_]
    
    # Make the prediction
    probabilities = model.predict_proba(input_data_encoded)
    prediction_index = probabilities.argmax()
    prediction = model.classes_[prediction_index]
    confidence_score = probabilities[0][prediction_index] * 100

    # Load, update, and save prediction counts
    prediction_counts = load_predictions()
    prediction_counts[prediction] += 1
    save_predictions(prediction_counts)

    return render_template('index.html', prediction=prediction, prediction_counts=prediction_counts)

if __name__ == '__main__':
    app.run(debug=True)
