import streamlit as st
import pandas as pd
import numpy as np
import datetime

try:
    # 1. PAGE SETUP
    st.set_page_config(
        page_title="AQI Tracker | Aryan Kumar Thakur",
        page_icon="🍃",
        layout="wide"
    )

    # 2. STYLING
    st.markdown("""
        <style>
        .main { background-color: #f8fafc; }
        .stMetric { background-color: white; padding: 15px; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
        .dev-box {
            background: #1e293b; color: white; padding: 20px;
            border-radius: 15px; text-align: center; margin-bottom: 20px;
        }
        .advice-card {
            background: #fff; padding: 20px; border-radius: 12px;
            border-left: 5px solid #3b82f6; margin: 10px 0;
        }
        </style>
        """, unsafe_allow_html=True)

    # 3. SIDEBAR
    with st.sidebar:
        st.markdown(f"""
            <div class="dev-box">
                <div style="font-size: 2rem;">👨‍💻</div>
                <h3 style="margin:0; color: #60a5fa;">Aryan Kumar Thakur</h3>
                <p style="font-size: 0.8rem; opacity: 0.7;">Python Developer</p>
            </div>
        """, unsafe_allow_html=True)
        
        st.write("### 📍 Location Settings")
        
        # 28 States and their Capitals
        locations = {
            "Andhra Pradesh": "Amaravati", "Arunachal Pradesh": "Itanagar", "Assam": "Dispur",
            "Bihar": "Patna", "Chhattisgarh": "Raipur", "Goa": "Panaji", "Gujarat": "Gandhinagar",
            "Haryana": "Chandigarh", "Himachal Pradesh": "Shimla", "Jharkhand": "Ranchi",
            "Karnataka": "Bengaluru", "Kerala": "Thiruvananthapuram", "Madhya Pradesh": "Bhopal",
            "Maharashtra": "Mumbai", "Manipur": "Imphal", "Meghalaya": "Shillong",
            "Mizoram": "Aizawl", "Nagaland": "Kohima", "Odisha": "Bhubaneswar",
            "Punjab": "Chandigarh", "Rajasthan": "Jaipur", "Sikkim": "Gangtok",
            "Tamil Nadu": "Chennai", "Telangana": "Hyderabad", "Tripura": "Agartala",
            "Uttar Pradesh": "Lucknow", "Uttarakhand": "Dehradun", "West Bengal": "Kolkata"
        }

        selected_state = st.selectbox("Select State", sorted(locations.keys()))
        selected_city = locations[selected_state]
        
        st.info(f"Showing data for capital: **{selected_city}**")
        st.markdown("---")
        st.code("Python\nStreamlit\nPandas")

    # 4. DATA LOGIC (Region-based base AQI)
    def get_data(city):
        np.random.seed(sum(ord(c) for c in city))
        # Logic to simulate higher AQI for Northern/Industrial capitals
        high_aqi_cities = ["New Delhi", "Patna", "Lucknow", "Kolkata", "Chandigarh"]
        base_aqi = 250 if city in high_aqi_cities else 80
        
        val = int(base_aqi + np.random.randint(-40, 60))
        return {
            "aqi": max(10, val), # Ensure it's not negative
            "pm25": int(val * 0.65),
            "temp": np.random.randint(15, 38),
            "humidity": np.random.randint(30, 90)
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

    st.title(f"🌬️ {selected_city}, {selected_state}")
    st.markdown(f"**Developed by Aryan Kumar Thakur** | {datetime.datetime.now().strftime('%d %b %Y, %H:%M %p')}")

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
    st.write(f"### 📈 24-Hour AQI Trend for {selected_city}")
    chart_data = pd.DataFrame(np.random.randn(24, 1) * 15 + data['aqi'], columns=['AQI'])
    st.area_chart(chart_data, color=color)

    # 7. FOOTER
    st.markdown(f"<div style='text-align:center; margin-top:50px; color:#94a3b8;'>Made with ❤️ by Aryan Kumar Thakur</div>", unsafe_allow_html=True)

except Exception as e:
    st.error(f"Something went wrong: {e}")
