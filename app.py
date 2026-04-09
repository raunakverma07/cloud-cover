import streamlit as st
import joblib

# load model
model = joblib.load("Cloud_cover.pkl")

# 🎨 Page config
st.set_page_config(page_title="Raunak's Cloud Model", page_icon="☁️", layout="centered")

# 🎨 Custom CSS
st.markdown("""
    <style>
    .main {
        background-color: #0f172a;
        color: white;
    }
    .title {
        text-align: center;
        font-size: 40px;
        font-weight: bold;
        color: #38bdf8;
    }
    .subtitle {
        text-align: center;
        font-size: 18px;
        color: #cbd5f5;
    }
    .stButton>button {
        background-color: #38bdf8;
        color: black;
        font-weight: bold;
        border-radius: 10px;
        padding: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# 🏷️ Title
st.markdown('<div class="title">☁️ Raunak\'s Cloud Prediction Model</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Predict Cloud Cover using Weather Data</div>', unsafe_allow_html=True)

st.write("---")

# 🎯 Inputs (with default + steps)
col1, col2 = st.columns(2)

with col1:
    temperature = st.slider("🌡️ Temperature", min_value=-10.0, max_value=50.0, value=16.0, step=4.0)
    humidity = st.slider("💧 Humidity", min_value=0, max_value=100, value=60, step=5)

with col2:
    wind_speed = st.slider("🌬️ Wind Speed", min_value=0.0, max_value=20.0, value=1.5, step=0.5)
    visibility = st.slider("👁️ Visibility (km)", min_value=0.0, max_value=10.0, value=1.0, step=1.0)

st.write("---")

# 🚀 Prediction
if st.button("🔍 Predict Cloud Cover"):
    sample = [[temperature, humidity, wind_speed, visibility]]
    prediction = model.predict(sample)

    st.success(f"☁️ Predicted Cloud Cover: {prediction[0]}")

# 📌 Footer
st.write("---")
st.markdown("<center>Made by Raunak 🚀</center>", unsafe_allow_html=True)
