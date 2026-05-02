import streamlit as st
import joblib
import numpy as np

# Page Configuration
st.set_page_config(page_title="Cloud Cover Predictor", page_icon="☁️", layout="centered")

# Custom CSS for styling
st.markdown("""
    <style>
    .main { background: linear-gradient(to right, #dfe9f3, #ffffff); }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border-radius: 10px;
        height: 3em;
        width: 100%;
        font-size: 18px;
    }
    .stNumberInput input { border-radius: 8px; }
    </style>
    """, unsafe_allow_html=True)

# Model Loading Function
@st.cache_resource 
def load_model(): 
    try:
        return joblib.load("Cloud_cover.pkl")
    except Exception as e:
        st.error(f"Error loading model: {e}")
        return None

model = load_model()

# UI Header
st.title("☁️ Cloud Cover Predictor")
st.caption("Advanced ML App | By Raunak")
st.markdown("---")

# Sidebar
st.sidebar.header("ℹ️ About")
st.sidebar.write("This app predicts cloud cover based on weather conditions using a trained ML model.")

# Input Section
st.subheader("Enter Weather Details")
col1, col2 = st.columns(2)

with col1:
    temperature = st.number_input("🌡️ Temperature (°C)", value=16.0, step=0.1)
    humidity = st.slider("💧 Humidity (%)", 0, 100, 60)

with col2:
    wind_speed = st.number_input("🌬️ Wind Speed (km/h)", value=1.5, step=0.1)
    visibility = st.number_input("👁️ Visibility (km)", value=1.0, step=0.1)

st.markdown("---")

# Prediction Logic
if st.button("🔮 Predict Cloud Cover"):
    if model is None:
        st.warning("Model file 'Cloud_cover.pkl' not found. Please ensure the file is in the same folder.")
    else:
        try:
            # Prepare data and predict
            sample = np.array([[temperature, humidity, wind_speed, visibility]])
            prediction = model.predict(sample)[0]

            # Display Result
            st.success(f"☁️ Predicted Cloud Cover: {prediction:.2f}%")
            
            # Progress bar (clamped between 0-100)
            progress_val = min(max(int(prediction), 0), 100)
            st.progress(progress_val)

            # Weather Category
            if prediction < 30:
                st.info("Clear Sky 🌤️")
            elif prediction < 70:
                st.warning("Partly Cloudy ⛅")
            else:
                st.error("Highly Cloudy ☁️☁️")

        except Exception as e:
            st.error(f"Prediction error: {e}")

st.markdown("---")
st.caption("Made with ❤️ using Streamlit")
