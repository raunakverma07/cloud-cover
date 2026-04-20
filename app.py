import streamlit as st import joblib

st.set_page_config(page_title="Cloud Cover Predictor", page_icon="☁️", layout="centered")

st.markdown(""" <style> .main { background: linear-gradient(to right, #dfe9f3, #ffffff); } .stButton>button { background-color: #4CAF50; color: white; border-radius: 10px; height: 3em; width: 100%; font-size: 18px; } .stNumberInput input { border-radius: 8px; } </style> """, unsafe_allow_html=True)

@st.cache_resource def load_model(): try: return joblib.load("Cloud_cover.pkl") except Exception as e: st.error(f"Error loading model: {e}") return None

model = load_model()

st.title("☁️ Cloud Cover Predictor") st.caption("Advanced ML App | By Raunak")

st.markdown("---")

st.sidebar.header("ℹ️ About") st.sidebar.write("This app predicts cloud cover based on weather conditions using a trained ML model.")

st.subheader("Enter Weather Details")

col1, col2 = st.columns(2)

with col1: temperature = st.number_input("🌡️ Temperature (°C)", value=16.0, step=0.1) humidity = st.slider("💧 Humidity (%)", 0, 100, 60)

with col2: wind_speed = st.number_input("🌬️ Wind Speed (km/h)", value=1.5, step=0.1) visibility = st.number_input("👁️ Visibility (km)", value=1.0, step=0.1)

st.markdown("---")

if st.button("🔮 Predict Cloud Cover"): if model is None: st.warning("Model not loaded properly.") else: try: sample = [[temperature, humidity, wind_speed, visibility]] prediction = model.predict(sample)

st.success(f"☁️ Predicted Cloud Cover: {prediction[0]}")

        st.progress(min(max(int(prediction[0]), 0), 100))

        if prediction[0] < 30:
            st.info("Clear Sky 🌤️")
        elif prediction[0] < 70:
            st.warning("Partly Cloudy ⛅")
        else:
            st.error("Highly Cloudy ☁️☁️")

    except Exception as e:
        st.error(f"Prediction error: {e}")

st.markdown("---") st.caption("Made with ❤️ using Streamlit")
