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
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=Fraunces:ital,opsz,wght@0,9..144,300;0,9..144,700;0,9..144,900;1,9..144,400&display=swap');
:root {
    --p200: #DDD6FE;
    --p300: #C4B5FD;
    --p500: #7C3AED;
    --p600: #6D28D9;
    --p700: #5B21B6;
    --p400: #A78BFA;
    --white: #FFFFFF;
    --gray-600: #4B5563;
    --gray-800: #1F1535;
    --grad-page: linear-gradient(160deg, #F3EFFE 0%, #FAFAFA 50%, #EDE9FE 100%);
    --grad-card: linear-gradient(135deg, #7C3AED 0%, #A78BFA 100%);
    --shadow-card: 0 8px 32px rgba(91,33,182,0.12);
}
[data-testid="stAppViewContainer"] {
    background: var(--grad-page) !important;
    background-attachment: fixed !important;
}
#MainMenu, footer, [data-testid="stDeployButton"] { display: none !important; }
[data-testid="stHeader"] { background: transparent !important; height: 0; }
[data-testid="stAppViewBlockContainer"] {
    padding-top: 16px !important;
    max-width: 1200px;
}
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #1E0A3C 0%, #2D1B69 50%, #3B1F7A 100%) !important;
    border-right: 1px solid rgba(167,139,250,0.15) !important;
}
[data-testid="stSidebar"] * {
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    color: rgba(221,214,254,0.85) !important;
}
[data-testid="stSidebar"] [data-testid="stPageLink"] a {
    background: rgba(167,139,250,0.08) !important;
    border: 1px solid rgba(167,139,250,0.12) !important;
    border-radius: 8px !important;
    color: rgba(221,214,254,0.9) !important;
}
[data-testid="stSidebar"] [data-testid="stPageLink"] a:hover {
    background: rgba(167,139,250,0.18) !important;
    border-color: rgba(167,139,250,0.35) !important;
    color: #fff !important;
}
.stMarkdown p, .stTextInput label, .stTextArea label, .stSelectbox label, .stDateInput label, .stTimeInput label, .stFileUploader label {
    font-family: 'Plus Jakarta Sans', sans-serif !important;
}
.main-title {
    font-family: 'Fraunces', serif;
    font-size: 42px;
    font-weight: 900;
    color: #000000;
    text-align: center;
    margin-bottom: 6px;
}
.subtitle {
    color: #000000;
    font-size: 18px;
    text-align: center;
    margin-bottom: 28px;
}
.form-card {
    background: rgba(255,255,255,0.88);
    border: 1px solid rgba(167,139,250,0.20);
    border-radius: 24px;
    padding: 28px;
    box-shadow: var(--shadow-card);
    backdrop-filter: blur(16px);
    animation: slideUp 0.7s ease both;
}
.privacy-card {
    background: rgba(255,255,255,0.88);
    border: 1px solid rgba(167,139,250,0.20);
    border-radius: 18px;
    padding: 18px;
    color: var(--gray-600);
    margin-top: 24px;
    box-shadow: var(--shadow-card);
}
.stTextInput label, .stTextArea label, .stSelectbox label, .stDateInput label, .stTimeInput label, .stFileUploader label {
    color: var(--gray-800) !important;
    font-weight: 700 !important;
}
.stTextInput input, .stTextArea textarea {
    background: var(--white) !important;
    color: var(--gray-800) !important;
    border-radius: 12px !important;
    border: 1px solid rgba(167,139,250,0.35) !important;
}
.stButton > button {
    background: var(--grad-card);
    color: white;
    border: none;
    border-radius: 14px;
    padding: 14px 22px;
    font-weight: 800;
    width: 100%;
    transition: 0.25s;
    box-shadow: 0 4px 20px rgba(124,58,237,0.35);
}
.stButton > button:hover {
    transform: translateY(-2px) scale(1.01);
    box-shadow: 0 8px 32px rgba(124,58,237,0.45);
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
