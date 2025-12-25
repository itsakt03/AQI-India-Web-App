import streamlit as st
import pandas as pd
import numpy as np
import datetime

# --- ERROR HANDLING FOR ASSETS ---
try:
    # 1. PAGE SETUP
    st.set_page_config(
        page_title="AQI Tracker | Aryan Kumar Thakur",
        page_icon="🍃",
        layout="wide"
    )

    # 2. STYLING (The Human-Touch UI)
    st.markdown("""
        <style>
        .main { background-color: #f8fafc; }
        .stMetric { background-color: white; padding: 15px; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
        .dev-box {
            background: #1e293b;
            color: white;
            padding: 20px;
            border-radius: 15px;
            text-align: center;
            margin-bottom: 20px;
        }
        .advice-card {
            background: #fff;
            padding: 20px;
            border-radius: 12px;
            border-left: 5px solid #3b82f6;
            margin: 10px 0;
        }
        </style>
        """, unsafe_allow_html=True)

    # 3. SIDEBAR (Developer Profile: Aryan Kumar Thakur)
    with st.sidebar:
        st.markdown(f"""
            <div class="dev-box">
                <div style="font-size: 2rem;">👨‍💻</div>
                <h3 style="margin:0; color: #60a5fa;">Aryan Kumar Thakur</h3>
                <p style="font-size: 0.8rem; opacity: 0.7;">Python Developer</p>
            </div>
        """, unsafe_allow_html=True)
        
        st.write("### 📍 Location Settings")
        selected_city = st.selectbox(
            "Select City",
            ["New Delhi", "Mumbai", "Bangalore", "Kolkata", "Chennai", "Hyderabad", "Pune"]
        )
        
        st.markdown("---")
        st.write("### 🛠️ Tech Used")
        st.code("Python\nStreamlit\nPandas\nNumPy")

    # 4. DATA LOGIC
    def get_data(city):
        np.random.seed(sum(ord(c) for c in city))
        base_aqi = {"New Delhi": 320, "Mumbai": 140, "Bangalore": 60, "Kolkata": 210}.get(city, 100)
        val = int(base_aqi + np.random.randint(-30, 30))
        return {
            "aqi": val,
            "pm25": int(val * 0.6),
            "temp": np.random.randint(20, 35),
            "humidity": np.random.randint(40, 80)
        }

    def get_status(aqi):
        if aqi <= 50: return "Excellent", "#10b981", "Perfect for a walk! Aryan recommends going outside."
        if aqi <= 100: return "Good", "#22c55e", "Good air quality. Have a great day!"
        if aqi <= 200: return "Moderate", "#f59e0b", "A bit hazy. Sensitive people should be careful."
        if aqi <= 300: return "Poor", "#ef4444", "I'd suggest wearing a mask today. - Aryan"
        return "Severe", "#7f1d1d", "Hazardous! Stay indoors and keep the purifier on."

    # 5. UI CONTENT
    data = get_data(selected_city)
    label, color, note = get_status(data['aqi'])

    st.title(f"🌬️ {selected_city} Air Quality")
    st.markdown(f"**Built by Aryan Kumar Thakur** | {datetime.datetime.now().strftime('%H:%M %p')}")

    col1, col2, col3 = st.columns([2, 1, 1])

    with col1:
        st.markdown(f"""
            <div style="background:{color}; padding:40px; border-radius:20px; color:white;">
                <h1 style="font-size: 5rem; margin:0;">{data['aqi']}</h1>
                <h2 style="margin:0;">{label}</h2>
            </div>
            <div class="advice-card">
                <strong>💡 Aryan's Perspective:</strong><br>{note}
            </div>
        """, unsafe_allow_html=True)

    with col2:
        st.metric("Temperature", f"{data['temp']}°C")
        st.metric("PM 2.5", f"{data['pm25']} µg/m³")

    with col3:
        st.metric("Humidity", f"{data['humidity']}%")
        st.metric("Pollutant", "PM2.5", delta="Primary")

    # 6. GRAPH
    st.write("### 📈 24-Hour Trend")
    chart_data = pd.DataFrame(
        np.random.randn(24, 1) * 10 + data['aqi'],
        columns=['AQI']
    )
    st.area_chart(chart_data, color=color)

    # 7. FOOTER
    st.markdown(f"<div style='text-align:center; margin-top:50px; color:#94a3b8;'>Made with ❤️ by Aryan Kumar Thakur</div>", unsafe_allow_html=True)

except Exception as e:
    st.error(f"An error occurred: {e}")
    st.info("Try running: pip install streamlit pandas numpy")