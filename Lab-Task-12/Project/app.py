from flask import Flask, render_template, request, jsonify
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, PolynomialFeatures
from sklearn.linear_model import LinearRegression

app = Flask(__name__)

# --- Model Training Phase ---
def train_insurance_model():
    # Load your dataset
    df = pd.read_csv("medical_insurance.csv")
    
    # Pre-processing (as per your code)
    df['bmi'] = df['bmi'].fillna(df['bmi'].mean())
    df['children'] = df['children'].astype(int) 
    df['charges'] = df['charges'].astype(int) 
    df['bmi'] = df['bmi'].astype(int)
    
    X = df.drop('charges', axis=1)
    y = df['charges']

    # Encoding Categorical Data
    le_sex = LabelEncoder()
    le_smoker = LabelEncoder()
    le_region = LabelEncoder()
    
    X['sex'] = le_sex.fit_transform(X['sex'])
    X['smoker'] = le_smoker.fit_transform(X['smoker'])
    X['region'] = le_region.fit_transform(X['region'])
    
    # Polynomial Features (Degree 2 for better accuracy)
    poly = PolynomialFeatures(degree=2)
    X_poly = poly.fit_transform(X)
    
    # Train Linear Regression
    model = LinearRegression()
    model.fit(X_poly, y)
    
    return model, poly, le_sex, le_smoker, le_region

# Globally initialize the model
model, poly_feat, le_sex, le_smoker, le_region = train_insurance_model()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # User input se data lena
        data = [
            int(request.form['age']),
            le_sex.transform([request.form['sex']])[0],
            float(request.form['bmi']),
            int(request.form['children']),
            le_smoker.transform([request.form['smoker']])[0],
            le_region.transform([request.form['region']])[0]
        ]
        
        # Transformation
        input_data = np.array([data])
        input_poly = poly_feat.transform(input_data)
        
        # Prediction
        prediction = model.predict(input_poly)[0]
        
        # FIX: Agar prediction negative ho to usay positive (absolute) ya minimum 0 kar dena
        final_result = abs(round(prediction, 2))
        
        return jsonify({'result': final_result})
    
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)