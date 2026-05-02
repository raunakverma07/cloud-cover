import streamlit as st
import joblib
import numpy as np

# Page Configuration
st.set_page_config(page_title="Cloud Predictor Pro", page_icon="☁️", layout="centered")

# Custom CSS for a modern, sleek interface
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    div.stButton > button:first-child {
        background: linear-gradient(to right, #4facfe 0%, #00f2fe 100%);
        color: white;
        border: none;
        padding: 10px 20px;
        border-radius: 10px;
        font-weight: bold;
        width: 100%;
    }
    .stNumberInput, .stSlider {
        background-color: #161b22;
        border-radius: 10px;
        padding: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# Model Loading
@st.cache_resource 
def load_model(): 
    try:
        return joblib.load("Cloud_cover.pkl")
    except Exception as e:
        return None

model = load_model()

# UI Header
st.title("☁️ Cloud Cover Predictor")
st.markdown("Enter the meteorological parameters below to estimate cloud density.")

# Sidebar
with st.sidebar:
    st.header("📊 System Info")
    st.write("Model: Random Forest / Gradient Boosting")
    st.write("Author: Raunak")
    if model:
        st.success("Model Loaded Successfully")
    else:
        st.error("Model 'Cloud_cover.pkl' not found!")

# Input Section in a nice Container
with st.container():
    col1, col2 = st.columns(2)
    with col1:
        temp = st.number_input("🌡️ Temperature (°C)", value=25.0)
        hum = st.slider("💧 Humidity (%)", 0, 100, 50)
    with col2:
        wind = st.number_input("🌬️ Wind Speed (km/h)", value=10.0)
        vis = st.number_input("👁️ Visibility (km)", value=10.0)

st.markdown("---")

# Prediction Logic
if st.button("🔮 ANALYSE WEATHER"):
    if model is None:
        st.error("Model file missing. Please upload 'Cloud_cover.pkl'.")
    else:
        try:
            # Reshape input for prediction
            input_data = np.array([[temp, hum, wind, vis]])
            raw_prediction = model.predict(input_data)[0]

            # Logic to handle both numeric and string predictions
            try:
                # Try converting to float for numeric models
                val = float(raw_prediction)
                st.metric(label="Predicted Cloud Cover", value=f"{val:.2f}%")
                
                # Progress visual
                progress = min(max(int(val), 0), 100)
                st.progress(progress)

                if val < 30:
                    st.info("Status: Clear Sky 🌤️")
                elif val < 70:
                    st.warning("Status: Partly Cloudy ⛅")
                else:
                    st.error("Status: Heavy Overcast ☁️")
            
            except (ValueError, TypeError):
                # If model returns a string category instead of a number
                st.success(f"☁️ Predicted Condition: **{raw_prediction}**")

        except Exception as e:
            st.error(f"Processing Error: {e}")

st.markdown("<br><hr><center>Made with ❤️ using Streamlit</center>", unsafe_allow_html=True)
        
