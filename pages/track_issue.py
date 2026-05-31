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
[data-testid="stAppViewContainer"] {
    background: radial-gradient(circle at top left, rgba(124,58,237,0.22), transparent 35%),
                radial-gradient(circle at top right, rgba(37,99,235,0.18), transparent 30%),
                #080914;
}
.main-title { font-size: 42px; font-weight: 900; color: #fff; text-align: center; }
.subtitle { text-align: center; color: rgba(255,255,255,0.72); font-size: 18px; margin-bottom: 30px; }
.search-card, .detail-card, .status-card {
    background: rgba(255,255,255,0.08);
    border: 1px solid rgba(167,139,250,0.25);
    border-radius: 22px;
    box-shadow: 0 20px 60px rgba(0,0,0,0.35);
    backdrop-filter: blur(16px);
    animation: fadeIn 0.7s ease both;
}
.search-card { padding: 28px; }
.detail-card { padding: 24px; margin-top: 20px; color: rgba(255,255,255,0.85); }
.status-card { padding: 24px; text-align: center; transition: 0.25s; }
.status-card:hover { transform: translateY(-4px); box-shadow: 0 0 35px rgba(124,58,237,0.35); }
.status-title { font-size: 15px; color: rgba(255,255,255,0.62); }
.status-value { font-size: 26px; font-weight: 900; color: #A78BFA; }
.timeline-item {
    background: rgba(124,58,237,0.12);
    border-left: 5px solid #7C3AED;
    border-radius: 14px;
    padding: 16px;
    margin-bottom: 12px;
    color: rgba(255,255,255,0.84);
}
.stTextInput label { color: rgba(255,255,255,0.88) !important; font-weight: 700 !important; }
.stTextInput input {
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
}
.stButton > button:hover { transform: translateY(-2px) scale(1.01); box-shadow: 0 0 35px rgba(124,58,237,0.55); }
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