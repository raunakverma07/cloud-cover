# Prediction Logic (Updated)
if st.button("🔮 Predict Cloud Cover"):
    if model is None:
        st.warning("Model file 'Cloud_cover.pkl' not found.")
    else:
        try:
            # Data prepare karein
            sample = [[temperature, humidity, wind_speed, visibility]]
            prediction = model.predict(sample)

            # String ko float mein badlein (Error fix)
            pred_value = float(prediction[0])

            # Result dikhayein
            st.success(f"☁️ Predicted Cloud Cover: {pred_value:.2f}%")
            
            # Progress bar
            progress_val = min(max(int(pred_value), 0), 100)
            st.progress(progress_val)

            if pred_value < 30:
                st.info("Clear Sky 🌤️")
            elif pred_value < 70:
                st.warning("Partly Cloudy ⛅")
            else:
                st.error("Highly Cloudy ☁️☁️")

        except ValueError:
            st.error(f"Prediction result is not a number: {prediction[0]}")
        except Exception as e:
            st.error(f"Prediction error: {e}")
            
