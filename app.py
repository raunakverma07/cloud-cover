import streamlit as st
import joblib

# Load model
model = joblib.load("Cloud_cover.pkl")

st.set_page_config(page_title="Raunak Cloud AI", page_icon="☁️", layout="centered")

# 🎨 Advanced CSS
st.markdown("""
<style>

body {
    background: linear-gradient(120deg, #1e293b, #0f172a);
    color: white;
}

/* Title */
.title {
    text-align: center;
    font-size: 45px;
    font-weight: 800;
    color: #38bdf8;
}

.name {
    text-align: center;
    font-size: 20px;
    color: #94a3b8;
}

/* Intro box */
.intro {
    background: rgba(255,255,255,0.05);
    padding: 20px;
    border-radius: 15px;
    margin-top: 15px;
    line-height: 1.6;
}

/* Card with hover */
.card {
    background: rgba(255,255,255,0.08);
    padding: 20px;
    border-radius: 15px;
    transition: 0.3s;
}

.card:hover {
    transform: scale(1.03);
    box-shadow: 0 0 20px rgba(56,189,248,0.4);
}

/* Button */
.stButton>button {
    width: 100%;
    background: linear-gradient(90deg, #38bdf8, #6366f1);
    color: white;
    font-size: 18px;
    border-radius: 10px;
    padding: 10px;
}

/* Result */
.result {
    text-align:center;
    padding:20px;
    border-radius:15px;
    font-size:24px;
    font-weight:bold;
    margin-top:20px;
}

</style>
""", unsafe_allow_html=True)

# 🏷️ Heading
st.markdown('<div class="title">☁️ Cloud Prediction System</div>', unsafe_allow_html=True)
st.markdown('<div class="name">Developed by Raunak</div>', unsafe_allow_html=True)

# 📖 Intro Paragraph
st.markdown("""
<div class="intro">
This intelligent cloud prediction system uses a Machine Learning model to estimate cloud coverage based on real-time weather conditions. 
By analyzing key parameters like temperature, humidity, wind speed, and visibility, the model provides quick and reliable predictions. 
This project demonstrates how data-driven approaches can be used to understand and forecast environmental patterns effectively.
</div>
""", unsafe_allow_html=True)

st.write("")

# 📦 Input Card
st.markdown('<div class="card">', unsafe_allow_html=True)

st.subheader("📊 Enter Weather Details")

col1, col2 = st.columns(2)

with col1:
    temperature = st.slider("🌡️ Temperature", -10.0, 50.0, 16.0, 4.0)
    humidity = st.slider("💧 Humidity", 0, 100, 60, 5)

with col2:
    wind_speed = st.slider("🌬️ Wind Speed", 0.0, 20.0, 1.5, 0.5)
    visibility = st.slider("👁️ Visibility", 0.0, 10.0, 1.0, 1.0)

st.markdown('</div>', unsafe_allow_html=True)

# 🚀 Prediction
if st.button("🔍 Predict Cloud"):
    sample = [[temperature, humidity, wind_speed, visibility]]
    prediction = model.predict(sample)[0]

    if prediction < 3:
        text = "☀️ Low Cloud"
        color = "#22c55e"
    elif prediction < 6:
        text = "⛅ Medium Cloud"
        color = "#facc15"
    else:
        text = "☁️ High Cloud"
        color = "#38bdf8"

    st.markdown(f"""
    <div class="result" style="background:{color}; color:black;">
        {text}
    </div>
    """, unsafe_allow_html=True)

# Footer
st.write("---")
st.markdown("<center>🚀 Machine Learning Project | Streamlit App</center>", unsafe_allow_html=True)
