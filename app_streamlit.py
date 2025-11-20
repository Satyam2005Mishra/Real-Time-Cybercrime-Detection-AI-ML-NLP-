import streamlit as st
import pandas as pd
import sys
import os
import re
import base64
from io import BytesIO

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BACKEND = os.path.join(BASE_DIR, "backend")
sys.path.insert(0, BACKEND)

from engine import analyze_text, detect_phishing
from advice import advice_map

st.set_page_config(page_title="Cybercrime AI", layout="wide", page_icon="🛡")

# -------------------- HEADER --------------------
st.markdown("""
    <h1 style='text-align:center; color:#00c9ff;'>🛡 Real-Time Cybercrime Detection AI</h1>
    <p style='text-align:center; font-size:18px;'>Analyze messages instantly, detect threats, scan URLs, and get safety guidance.</p>
""", unsafe_allow_html=True)

# -------------------- TEXT INPUT --------------------
input_text = st.text_area("Enter your message:", height=150)

# URL detection
url_pattern = r"(http[s]?://\S+)"
found_urls = re.findall(url_pattern, input_text)

# -------------------- ANALYZE BUTTON --------------------
if st.button("Analyze"):
    category, risk = analyze_text(input_text)

    color = "#00CC66" if category == "Safe" else "#FF4444"

    # -------------------- RESULT CARD --------------------
    st.markdown(
        f"""
        <div style='padding:20px; border-radius:12px; 
        background:{color}; color:white; font-size:18px; margin-bottom:20px;'>
            <b>Prediction:</b> {category}<br>
            <b>Risk Level:</b> {risk}
        </div>
        """,
        unsafe_allow_html=True
    )

    # -------------------- KEYWORD HIGHLIGHTING --------------------
    st.subheader("🔍 Keyword Highlighting")

    highlighted = input_text
    danger_words = ["kill", "kyc", "click", "lottery", "leak", "money", "prize", "reward",
                    "idiot", "stupid", "useless", "hate", "die", "slap", "hurt"]

    for word in danger_words:
        highlighted = re.sub(
            rf"(?i)({word})",
            r"<span style='color:red; font-weight:bold;'>\1</span>",
            highlighted
        )

    st.markdown(
        f"<div style='padding:12px; border:1px solid #ccc; border-radius:8px;'>{highlighted}</div>",
        unsafe_allow_html=True
    )

    # -------------------- URL INSPECTOR --------------------
    st.subheader("🔗 URL Safety Check")

    if found_urls:
        for url in found_urls:
            if any(bad in url.lower() for bad in ["kyc", "verify", "login", "bank", "update", "secure"]):
                st.error(f"⚠️ Suspicious URL detected: {url}")
            else:
                st.success(f"✔️ URL looks safe: {url}")
    else:
        st.info("No URLs found in the message.")

    # -------------------- SAFETY ADVICE --------------------
    st.subheader("🛡 How to Stay Safe:")
    for step in advice_map[category]["avoid"]:
        st.markdown(f"- {step}")

    st.subheader("🛠 What to Do Next:")
    for step in advice_map[category]["steps"]:
        st.markdown(f"- {step}")

    # -------------------- RADAR CHART (RISK PROFILE) --------------------
    st.subheader("📡 Risk Radar Chart")

    radar_df = pd.DataFrame({
        "RiskType": ["Phishing", "Scam", "Extortion", "Threat", "Abuse", "Bullying", "Toxicity"],
        "Score": [20, 18, 15, 12, 10, 10, 8]
    })

    st.line_chart(radar_df.set_index("RiskType"))

    # -------------------- PIE CHART --------------------
    st.subheader("📊 Cybercrime Category Distribution")

    pie_df = pd.DataFrame({
        "Category": ["Phishing", "Scam", "Extortion", "Threat", "Abuse", "Bullying", "Toxicity", "Safe"],
        "Weight": [20, 18, 15, 10, 10, 10, 10, 7]
    })

    st.plotly_chart({
        "data": [{
            "values": pie_df["Weight"],
            "labels": pie_df["Category"],
            "type": "pie"
        }]
    })

    # -------------------- GENERATE PDF REPORT --------------------
    st.subheader("📄 Download Full Cyber Report")

    def generate_pdf(text, category, risk):
        content = f"""
Cybercrime Detection Report

Message:
{text}

Prediction:
{category}

Risk Level:
{risk}

Advice:
{advice_map[category]["avoid"]}

Next Steps:
{advice_map[category]["steps"]}
        """

        pdf_bytes = content.encode("utf-8")
        return pdf_bytes

    pdf_data = generate_pdf(input_text, category, risk)

    st.download_button(
        label="📥 Download Report",
        data=pdf_data,
        file_name="cyber_report.txt",
        mime="text/plain"
    )
