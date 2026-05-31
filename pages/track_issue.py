import os
import sys


import streamlit as st

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from database import get_report, init_db

st.set_page_config(
    page_title="Track Report | SpotIt",
    page_icon="🔍",
    layout="wide",
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=Fraunces:ital,opsz,wght@0,9..144,300;0,9..144,700;0,9..144,900;1,9..144,400&display=swap');
:root {
    --p200: #DDD6FE;
    --p300: #C4B5FD;
    --p500: #7C3AED;
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
.stMarkdown p, .stTextInput label {
    font-family: 'Plus Jakarta Sans', sans-serif !important;
}
.main-title { font-family: 'Fraunces', serif; font-size: 42px; font-weight: 900; color: #000000; text-align: center; }
.subtitle { text-align: center; color: #000000; font-size: 18px; margin-bottom: 30px; }
.search-card, .detail-card, .status-card {
    background: rgba(255,255,255,0.88);
    border: 1px solid rgba(167,139,250,0.20);
    border-radius: 22px;
    box-shadow: var(--shadow-card);
    backdrop-filter: blur(16px);
    animation: fadeIn 0.7s ease both;
}
.search-card { padding: 28px; }
.detail-card { padding: 24px; margin-top: 20px; color: var(--gray-600); }
.status-card { padding: 24px; text-align: center; transition: 0.25s; }
.status-card:hover { transform: translateY(-4px); box-shadow: 0 12px 40px rgba(124,58,237,0.20); }
.status-title { font-size: 15px; color: var(--gray-600); }
.status-value { font-size: 26px; font-weight: 900; color: var(--p500); }
.timeline-item {
    background: rgba(124,58,237,0.08);
    border-left: 5px solid var(--p500);
    border-radius: 14px;
    padding: 16px;
    margin-bottom: 12px;
    color: var(--gray-800);
}
.stTextInput label { color: var(--gray-800) !important; font-weight: 700 !important; }
.stTextInput input {
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
}
.stButton > button:hover { transform: translateY(-2px) scale(1.01); box-shadow: 0 8px 32px rgba(124,58,237,0.45); }
@keyframes fadeIn { from { opacity: 0; transform: translateY(18px); } to { opacity: 1; transform: translateY(0); } }
</style>
""", unsafe_allow_html=True)

init_db()

st.markdown("""
<h1 class="main-title">🔍 Track Your Report</h1>
<p class="subtitle">Enter your SpotIt Report ID to check the current status of your anonymous report.</p>
""", unsafe_allow_html=True)

st.markdown('<div class="search-card">', unsafe_allow_html=True)
report_id = st.text_input("Report ID", placeholder="Example: SPOT20260530123045")
track_button = st.button("Track Report")
st.markdown('</div>', unsafe_allow_html=True)

if track_button:
    if not report_id.strip():
        st.error("Please enter a valid Report ID.")
    else:
        report = get_report(report_id.strip())

        if not report:
            st.error("❌ No report found with that ID.")
        else:
            st.success(f"✅ Report found: {report['report_id']}")

            col1, col2, col3 = st.columns(3)
            with col1:
                st.markdown(f"""
                <div class="status-card">
                    <div class="status-title">Current Status</div>
                    <div class="status-value">{report['status']}</div>
                </div>
                """, unsafe_allow_html=True)
            with col2:
                st.markdown(f"""
                <div class="status-card">
                    <div class="status-title">Category</div>
                    <div class="status-value">{report['category']}</div>
                </div>
                """, unsafe_allow_html=True)
            with col3:
                st.markdown("""
                <div class="status-card">
                    <div class="status-title">Privacy</div>
                    <div class="status-value">Anonymous</div>
                </div>
                """, unsafe_allow_html=True)

            st.markdown('<div class="detail-card">', unsafe_allow_html=True)
            st.subheader("📄 Report Details")
            st.write("**Report ID:**", report["report_id"])
            st.write("**Incident Category:**", report["category"])
            st.write("**Location:**", report["location"])
            st.write("**Date:**", report.get("date", ""))
            st.write("**Time:**", report.get("time", ""))
            st.write("**Submitted On:**", report["created_at"])
            st.write("**Description:**", report["description"])

            if report.get("image_path") and os.path.exists(report["image_path"]):
                st.image(report["image_path"], caption="Uploaded Evidence", use_container_width=True)

            st.markdown('</div>', unsafe_allow_html=True)

            st.markdown('<div class="detail-card">', unsafe_allow_html=True)
            st.subheader("📌 Status Timeline")
            statuses = ["Submitted", "Under Review", "Verified", "Resolved"]
            current_index = statuses.index(report["status"]) if report["status"] in statuses else 0
            for index, status in enumerate(statuses):
                marker = "✅" if index <= current_index else "⏳"
                st.markdown(f"""
                <div class="timeline-item">
                    <strong>{marker} {status}</strong><br>
                    {'Completed' if index <= current_index else 'Pending'}
                </div>
                """, unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

st.info("🔒 SpotIt uses only your Report ID for tracking. Your identity remains anonymous.")
