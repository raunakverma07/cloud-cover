import streamlit as st
import joblib

# Load model
model = joblib.load("Cloud_cover.pkl")

# Title
st.title("☁️ Cloud Cover Predictor")
st.write("By Raunak")

st.write("---")

# Inputs
temperature = st.number_input("Temperature", value=16.0)
humidity = st.number_input("Humidity", value=60)
wind_speed = st.number_input("Wind Speed", value=1.5)
visibility = st.number_input("Visibility", value=1.0)

# Button
if st.button("Predict"):
    sample = [[temperature, humidity, wind_speed, visibility]]
    
    prediction = model.predict(sample)
    
    st.success(f"Cloud Cover: {prediction[0]}")
