import streamlit as st
import requests
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="Smart Public Bus — Demo", layout="centered")

st.title("Smart Public Bus — Minimal Frontend")

api_base = st.sidebar.text_input("API base URL", value="http://localhost:8000")
st.sidebar.markdown("Use the backend started with: `uvicorn app.main:app --reload`")

st.sidebar.header("Quick actions")
if st.sidebar.button("Health check"):
    try:
        r = requests.get(f"{api_base}/health", timeout=3)
        st.sidebar.success(r.json())
    except Exception as e:
        st.sidebar.error(f"Error: {e}")

st.header("Report GPS / Crowd (POST /gps)")
with st.form("gps_form"):
    bus_id = st.number_input("Bus ID", min_value=1, value=1, step=1)
    lat = st.number_input("Latitude", format="%.6f", value=28.6139)
    lon = st.number_input("Longitude", format="%.6f", value=77.2090)
    speed = st.number_input("Speed (km/h)", min_value=0.0, value=15.0)
    crowd_level = st.slider("Crowd level (0-100)", 0, 100, 30)
    ts = st.text_input("Timestamp (ISO, optional)", value="")
    submit = st.form_submit_button("Send GPS")

    if submit:
        payload = {
            "bus_id": int(bus_id),
            "lat": float(lat),
            "lon": float(lon),
            "speed": float(speed) if speed is not None else None,
            "crowd_level": int(crowd_level),
        }
        if ts:
            payload["timestamp"] = ts
        try:
            r = requests.post(f"{api_base}/gps", json=payload, timeout=5)
            r.raise_for_status()
            st.success("GPS saved")
            st.json(r.json())
        except Exception as e:
            st.error(f"Failed to POST /gps: {e}")

st.markdown("---")
st.header("Live bus / ETA / Crowd lookups")

col1, col2 = st.columns(2)
with col1:
    q_bus_id = st.number_input("Query Bus ID", min_value=1, value=1, step=1, key="qbus")
    if st.button("Get live location"):
        try:
            r = requests.get(f"{api_base}/buses/{int(q_bus_id)}/live", timeout=4)
            r.raise_for_status()
            data = r.json()
            st.json(data)
            # show on map
            df = pd.DataFrame([{"lat": data["lat"], "lon": data["lon"]}])
            st.map(df)
        except requests.HTTPError as he:
            st.error(f"HTTP error: {he.response.status_code} - {he.response.text}")
        except Exception as e:
            st.error(f"Error: {e}")

with col2:
    q_stop_id = st.number_input("Query Stop ID", min_value=1, value=1, step=1, key="qstop")
    if st.button("Get ETA"):
        try:
            params = {"bus_id": int(q_bus_id), "stop_id": int(q_stop_id)}
            r = requests.get(f"{api_base}/eta", params=params, timeout=4)
            r.raise_for_status()
            st.json(r.json())
        except requests.HTTPError as he:
            st.error(f"HTTP error: {he.response.status_code} - {he.response.text}")
        except Exception as e:
            st.error(f"Error: {e}")

st.markdown("---")
st.header("Crowd classification")
c_bus = st.number_input("Bus ID for crowd", min_value=1, value=1, step=1, key="crowdbus")
if st.button("Get crowd level"):
    try:
        r = requests.get(f"{api_base}/crowd/{int(c_bus)}", timeout=4)
        r.raise_for_status()
        st.json(r.json())
    except requests.HTTPError as he:
        st.error(f"HTTP error: {he.response.status_code} - {he.response.text}")
    except Exception as e:
        st.error(f"Error: {e}")

st.markdown("---")
st.caption("Minimal demo frontend. Adjust API base URL in the sidebar if backend runs")