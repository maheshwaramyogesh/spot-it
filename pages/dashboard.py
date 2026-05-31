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
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=Fraunces:ital,opsz,wght@0,9..144,300;0,9..144,700;0,9..144,900;1,9..144,400&display=swap');
:root {
    --p300: #C4B5FD;
    --p500: #7C3AED;
    --gray-600: #4B5563;
    --gray-800: #1F1535;
    --grad-page: linear-gradient(160deg, #F3EFFE 0%, #FAFAFA 50%, #EDE9FE 100%);
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
.stApp {
    font-family: 'Plus Jakarta Sans', sans-serif;
    color: var(--gray-800);
}
.main-title {
    font-family: 'Fraunces', serif;
    font-size: 42px;
    font-weight: 800;
    color: var(--gray-800);
    text-align: center;
}
.subtitle {
    text-align: center;
    color: var(--gray-600);
    font-size: 18px;
    margin-bottom: 35px;
}
.metric-card {
    background: rgba(255,255,255,0.88);
    padding: 24px;
    border-radius: 22px;
    border: 1px solid rgba(167,139,250,0.20);
    box-shadow: var(--shadow-card);
    text-align: center;
}
.metric-number {
    font-size: 36px;
    font-weight: 800;
    color: var(--p500);
}
.metric-label {
    color: var(--gray-600);
    font-size: 14px;
}
.section-card {
    background: rgba(255,255,255,0.88);
    padding: 26px;
    border-radius: 22px;
    border: 1px solid rgba(167,139,250,0.20);
    box-shadow: var(--shadow-card);
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
