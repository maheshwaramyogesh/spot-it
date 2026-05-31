import os
import sys
from datetime import datetime

import streamlit as st

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from database import create_report, init_db
from image_utils import save_uploaded_image

st.set_page_config(
    page_title="Report Incident | SpotIt",
    page_icon="🚨",
    layout="wide",
)

st.markdown("""
<style>
[data-testid="stAppViewContainer"] {
    background: radial-gradient(circle at top left, rgba(124,58,237,0.22), transparent 35%),
                radial-gradient(circle at top right, rgba(37,99,235,0.18), transparent 30%),
                #080914;
}
.main-title {
    font-size: 42px;
    font-weight: 900;
    color: #ffffff;
    text-align: center;
    margin-bottom: 6px;
}
.subtitle {
    color: rgba(255,255,255,0.72);
    font-size: 18px;
    text-align: center;
    margin-bottom: 28px;
}
.form-card {
    background: rgba(255,255,255,0.08);
    border: 1px solid rgba(167,139,250,0.25);
    border-radius: 24px;
    padding: 28px;
    box-shadow: 0 20px 60px rgba(0,0,0,0.35);
    backdrop-filter: blur(16px);
    animation: slideUp 0.7s ease both;
}
.privacy-card {
    background: rgba(124,58,237,0.12);
    border: 1px solid rgba(167,139,250,0.25);
    border-radius: 18px;
    padding: 18px;
    color: rgba(255,255,255,0.78);
    margin-top: 24px;
}
.stTextInput label, .stTextArea label, .stSelectbox label, .stDateInput label, .stTimeInput label, .stFileUploader label {
    color: rgba(255,255,255,0.88) !important;
    font-weight: 700 !important;
}
.stTextInput input, .stTextArea textarea {
    background: rgba(255,255,255,0.08) !important;
    color: white !important;
    border-radius: 12px !important;
    border: 1px solid rgba(167,139,250,0.25) !important;
}
.stButton > button {
    background: linear-gradient(90deg, #7C3AED, #2563EB);
    color: white;
    border: none;
    border-radius: 14px;
    padding: 14px 22px;
    font-weight: 800;
    width: 100%;
    transition: 0.25s;
    box-shadow: 0 0 24px rgba(124,58,237,0.35);
}
.stButton > button:hover {
    transform: translateY(-2px) scale(1.01);
    box-shadow: 0 0 35px rgba(124,58,237,0.55);
}
@keyframes slideUp {
    from { opacity: 0; transform: translateY(22px); }
    to { opacity: 1; transform: translateY(0); }
}
</style>
""", unsafe_allow_html=True)

init_db()

st.markdown("""
<h1 class="main-title">🚨 Report a Safety Incident</h1>
<p class="subtitle">Submit an anonymous report to help your community identify safety concerns.</p>
""", unsafe_allow_html=True)

st.markdown('<div class="form-card">', unsafe_allow_html=True)

category = st.selectbox(
    "Incident Category",
    [
        "Violence",
        "Harassment",
        "Bullying",
        "Domestic Violence",
        "Theft / Robbery",
        "Stalking",
        "Suspicious Activity",
        "Drug Activity",
        "Unsafe Area",
        "Emergency Concern",
        "Other",
    ],
)

col1, col2 = st.columns(2)
with col1:
    incident_date = st.date_input("Incident Date", value=datetime.today())
with col2:
    incident_time = st.time_input("Incident Time")

location = st.text_input("Location", placeholder="Example: Ameerpet, Hyderabad")

description = st.text_area(
    "Description",
    placeholder="Briefly describe what happened. Do not include personal details unless necessary.",
    height=170,
)
st.caption(f"Characters: {len(description)}")

uploaded_file = st.file_uploader("Upload Evidence (Optional)", type=["jpg", "jpeg", "png"])
if uploaded_file is not None:
    st.image(uploaded_file, caption="Uploaded Evidence Preview", use_container_width=True)

submit = st.button("📤 Submit Anonymous Report")

if submit:
    if not location.strip():
        st.error("Please enter a location.")
    elif not description.strip():
        st.error("Please enter a description.")
    else:
        report_id = "SPOT" + datetime.now().strftime("%Y%m%d%H%M%S")
        image_path = ""

        if uploaded_file is not None:
            image_path = save_uploaded_image(uploaded_file)
            if image_path == "":
                st.error("Invalid image file. Please upload a JPG, JPEG, or PNG image.")
                st.stop()

        success = create_report(
            report_id=report_id,
            category=category,
            description=description,
            location=location.strip(),
            date=str(incident_date),
            time=str(incident_time),
            image_path=image_path,
        )

        if success:
            st.success("✅ Report submitted and saved successfully!")
            st.info(f"Your Report ID: **{report_id}**\n\nSave this ID to track your report later.")
            
        else:
            st.error("Something went wrong. The report was not saved. Please try again.")

st.markdown('</div>', unsafe_allow_html=True)

st.markdown("""
<div class="privacy-card">
🔒 <b>Privacy Notice:</b> SpotIt does not collect your name, email, or phone number. Reports are anonymous and tracked only by Report ID.
</div>
""", unsafe_allow_html=True)