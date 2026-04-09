import streamlit as st
import joblib

Load model

model = joblib.load("Cloud_cover.pkl")

Page config

st.set_page_config(page_title="Cloud AI", page_icon="☁️", layout="centered")

Custom CSS (Modern UI)

st.markdown("""

<style>  
body {  
    background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);  
    color: white;  
}  
  
.main {  
    background: transparent;  
}  
  
.title {  
    text-align: center;  
    font-size: 42px;  
    font-weight: bold;  
    background: linear-gradient(to right, #38bdf8, #22c55e);  
    -webkit-background-clip: text;  
    -webkit-text-fill-color: transparent;  
}  
  
.card {  
    background: rgba(255,255,255,0.08);  
    padding: 20px;  
    border-radius: 15px;  
    backdrop-filter: blur(10px);  
}  
  
.stButton>button {  
    width: 100%;  
    background: linear-gradient(90deg, #38bdf8, #22c55e);  
    color: black;  
    font-size: 18px;  
    font-weight: bold;  
    border-radius: 10px;  
    padding: 10px;  
}  
</style>  """, unsafe_allow_html=True)

Title

st.markdown('<div class="title">☁️ Cloud Cover AI</div>', unsafe_allow_html=True)
st.write("### Predict cloud coverage using weather conditions")

st.write("---")

Card UI

st.markdown('<div class="card">', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
temperature = st.slider("🌡️ Temperature (°C)", -10.0, 50.0, 16.0, 4.0)
humidity = st.slider("💧 Humidity (%)", 0, 100, 60, 5)

with col2:
wind_speed = st.slider("🌬️ Wind Speed", 0.0, 20.0, 1.5, 0.5)
visibility = st.slider("👁️ Visibility (km)", 0.0, 10.0, 1.0, 1.0)

st.markdown('</div>', unsafe_allow_html=True)

st.write("")

Prediction

if st.button("🚀 Predict Now"):
sample = [[temperature, humidity, wind_speed, visibility]]
prediction = model.predict(sample)[0]

# Smart Output Category  
if prediction < 3:  
    result = "☀️ Low Cloud"  
    color = "#22c55e"  
elif prediction < 6:  
    result = "⛅ Medium Cloud"  
    color = "#facc15"  
else:  
    result = "☁️ High Cloud"  
    color = "#38bdf8"  

st.markdown(f"""  
<div style="  
    text-align:center;  
    padding:20px;  
    border-radius:15px;  
    background:{color};  
    color:black;  
    font-size:24px;  
    font-weight:bold;">  
    {result}  
</div>  
""", unsafe_allow_html=True)

Footer

st.write("---")
st.markdown("<center>⚡ Built by Raunak</center>", unsafe_allow_html=True)

Ye d
