import streamlit as st
import pandas as pd
from database import init_db, get_all_reports

st.set_page_config(
    page_title="Dashboard | SpotIt",
    page_icon="📊",
    layout="wide"
)


st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #070716 0%, #111132 50%, #1b1550 100%);
    color: white;
}
.main-title {
    font-size: 42px;
    font-weight: 800;
    color: white;
    text-align: center;
}
.subtitle {
    text-align: center;
    color: #c7c7e8;
    font-size: 18px;
    margin-bottom: 35px;
}
.metric-card {
    background: rgba(255,255,255,0.08);
    padding: 24px;
    border-radius: 22px;
    border: 1px solid rgba(255,255,255,0.15);
    box-shadow: 0px 0px 25px rgba(108,99,255,0.25);
    text-align: center;
}
.metric-number {
    font-size: 36px;
    font-weight: 800;
    color: #7c5cff;
}
.metric-label {
    color: #d8d8ff;
    font-size: 14px;
}
.section-card {
    background: rgba(255,255,255,0.08);
    padding: 26px;
    border-radius: 22px;
    border: 1px solid rgba(255,255,255,0.15);
    box-shadow: 0px 0px 25px rgba(108,99,255,0.18);
    margin-top: 25px;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<h1 class="main-title">📊 Community Safety Dashboard</h1>
<p class="subtitle">Real reports submitted by users will appear here.</p>
""", unsafe_allow_html=True)

init_db()
reports = get_all_reports()

if not reports:
    df = pd.DataFrame()
else:
    df = pd.DataFrame(reports)

total_reports = len(df)

if not df.empty and "status" in df.columns:
    verified_reports = len(df[df["status"] == "Verified"])
    open_reports = len(df[df["status"].isin(["Submitted", "Under Review", "In Progress"])])
    resolved_reports = len(df[df["status"] == "Resolved"])
else:
    verified_reports = 0
    open_reports = total_reports
    resolved_reports = 0

col1, col2, col3, col4 = st.columns(4)

metrics = [
    ("Total Reports", total_reports),
    ("Verified Reports", verified_reports),
    ("Open Reports", open_reports),
    ("Resolved Reports", resolved_reports),
]

for col, (label, value) in zip([col1, col2, col3, col4], metrics):
    with col:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-number">{value}</div>
            <div class="metric-label">{label}</div>
        </div>
        """, unsafe_allow_html=True)

st.markdown('<div class="section-card">', unsafe_allow_html=True)
st.subheader("🚨 Reports by Category")

if not df.empty and "category" in df.columns:
    category_count = df["category"].value_counts()
    st.bar_chart(category_count)
else:
    st.info("No reports submitted yet.")

st.markdown("</div>", unsafe_allow_html=True)

st.markdown('<div class="section-card">', unsafe_allow_html=True)
st.subheader("📝 Recent Reports")

if not df.empty:
    st.dataframe(df, use_container_width=True, hide_index=True)
else:
    st.info("No recent reports available. Submit a report first.")

st.markdown("</div>", unsafe_allow_html=True)