import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder, StandardScaler

# --- DATA PROCESSING ---
@st.cache_resource
def get_model():
    df = pd.read_csv('Cardetails.csv')
    # Cleaning
    df = df.drop(columns=['torque'], errors='ignore').dropna().drop_duplicates()
    # Extracting numbers (Mileage, Engine, Power)
    for col in ['mileage', 'engine', 'max_power']:
        df[col] = df[col].str.extract(r'(\d+\.?\d*)').astype(float)
    df = df.dropna()
    # Category Encoding
    encoders = {}
    for col in ['fuel', 'seller_type', 'transmission', 'owner']:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col])
        encoders[col] = le
    # Features and Target
    X = df[['year', 'km_driven', 'fuel', 'seller_type', 'transmission', 'owner', 'mileage', 'engine', 'max_power', 'seats']]
    y = df['selling_price']
    # Model Training
    model = RandomForestRegressor(n_estimators=50) # Fast training
    model.fit(X, y)
    return model, encoders
model, encoders = get_model()
st.title("🚗 Car Price Prediction")
# User Inputs
year = st.slider("Manufacturing Year", 2000, 2024, 2015)
km = st.number_input("Kilometers Driven", value=50000)
fuel = st.selectbox("Fuel", encoders['fuel'].classes_)
trans = st.selectbox("Transmission", encoders['transmission'].classes_)
mileage = st.number_input("Mileage (kmpl)", value=18.0)
engine = st.number_input("Engine (CC)", value=1200)
power = st.number_input("Max Power (bhp)", value=75.0)
seats = st.radio("Seats", [4, 5, 7, 8], horizontal=True)
# PREDICTION
if st.button("Check Price"):
    # Input data ko model ke format mein convert karna
    input_data = pd.DataFrame([[
        year, km, 
        encoders['fuel'].transform([fuel])[0],
        encoders['seller_type'].transform(['Individual'])[0], # Default value
        encoders['transmission'].transform([trans])[0],
        encoders['owner'].transform(['First Owner'])[0],     # Default value
        mileage, engine, power, seats
    ]], columns=['year', 'km_driven', 'fuel', 'seller_type', 'transmission', 'owner', 'mileage', 'engine', 'max_power', 'seats'])  
    res = model.predict(input_data)
    st.success(f"Car ki estimated price hai: ₹{int(res[0]):,}")