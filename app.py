import streamlit as st
import joblib
import pandas as pd
import numpy as np

try:
    model = joblib.load('malaria_climate_model.pkl')
    feature_cols = joblib.load('model_features.pkl')
except:
    model = None
    feature_cols = None

st.set_page_config(page_title="Nigeria Malaria Predictor by State", layout="centered")

st.title("🦟 Nigeria Malaria Prevalence Predictor")
st.write("Select any state in Nigeria along with annual weather conditions to predict malaria prevalence rate using our Random Forest model.")

st.sidebar.header("Input Settings")

# 1. State Dropdown
selected_state = st.sidebar.selectbox(
    "Select State",
    options=['Abia', 'Adamawa', 'Akwa Ibom', 'Anambra', 'Bauchi', 'Bayelsa', 'Benue', 'Borno',
             'Cross River', 'Delta', 'Ebonyi', 'Edo', 'Ekiti', 'Enugu', 'FCT', 'Gombe', 'Imo',
             'Jigawa', 'Kaduna', 'Kano', 'Katsina', 'Kebbi', 'Kogi', 'Kwara', 'Lagos',
             'Nasarawa', 'Niger', 'Ogun', 'Ondo', 'Osun', 'Oyo', 'Plateau', 'Rivers',
             'Sokoto', 'Taraba', 'Yobe', 'Zamfara']
)

# 2. Climate Inputs
temp_input = st.sidebar.slider(
    "Annual Mean Temperature (°C)",
    min_value=20.0,
    max_value=35.0,
    value=26.5,
    step=0.1
)

rain_input = st.sidebar.slider(
    "Annual Total Precipitation (mm)",
    min_value=200.0,
    max_value=3500.0,
    value=1100.0,
    step=10.0
)

st.subheader(f"Prediction for {selected_state} State")

if model is not None and feature_cols is not None:
    input_row = {col: 0 for col in feature_cols}
    input_row['annual_mean_temp_c'] = temp_input
    input_row['annual_total_precipitation_mm'] = rain_input
    
    state_col = f'state_{selected_state}'
    if state_col in input_row:
        input_row[state_col] = 1
        
    input_df = pd.DataFrame([input_row])[feature_cols]
    prediction = model.predict(input_df)[0]
    
    st.metric(label="Predicted Malaria Prevalence (RDT %)", value=f"{prediction:.2f}%")
    
    if prediction < 20:
        st.success("🟢 Low Prevalence Risk")
    elif prediction < 45:
        st.warning("🟡 Moderate Prevalence Risk")
    else:
        st.error("🔴 High Prevalence Risk")
else:
    st.error("Model components missing! Please build the model locally inside Colab first.")
