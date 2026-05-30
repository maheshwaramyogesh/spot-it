import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Dashboard | SpotIt",
    page_icon="📊",
    layout="wide"
)

st.markdown("""
<style>
.main-title {
    font-size: 40px;
    font-weight: 800;
    color: #5B4BDB;
    text-align: center;
}

.subtitle {
    text-align: center;
    color: #666;
    font-size: 18px;
    margin-bottom: 30px;
}

.metric-card {
    background: white;
    padding: 24px;
    border-radius: 20px;
    box-shadow: 0px 4px 20px rgba(0,0,0,0.08);
    text-align: center;
    transition: 0.3s;
}

.metric-card:hover {
    transform: translateY(-5px);
    box-shadow: 0px 8px 30px rgba(91,75,219,0.25);
}

.metric-number {
    font-size: 34px;
    font-weight: 800;
    color: #6C63FF;
}

.metric-label {
    color: #666;
    font-size: 14px;
}

.section-card {
    background: white;
    padding: 24px;
    border-radius: 20px;
    box-shadow: 0px 4px 20px rgba(0,0,0,0.08);
    margin-top: 20px;
    animation: fadeIn 0.8s ease-in;
}

@keyframes fadeIn {
    from {
        opacity: 0;
        transform: translateY(18px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

.badge {
    background: #EFEAFE;
    color: #5B4BDB;
    padding: 6px 12px;
    border-radius: 999px;
    font-size: 13px;
    font-weight: 600;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div>
    <h1 class="main-title">📊 Community Safety Dashboard</h1>
    <p class="subtitle">
        View safety reports, community trends, and incident hotspots.
    </p>
</div>
""", unsafe_allow_html=True)

reports = pd.DataFrame({
    "Report ID": ["SPOT1001", "SPOT1002", "SPOT1003", "SPOT1004", "SPOT1005"],
    "Category": ["Harassment", "Theft / Robbery", "Unsafe Area", "Suspicious Activity", "Bullying"],
    "Location": ["Ameerpet", "Madhapur", "Koti", "Secunderabad", "Hitech City"],
    "Status": ["Under Review", "Verified", "Submitted", "In Progress", "Resolved"],
    "Date": ["2026-05-30", "2026-05-30", "2026-05-29", "2026-05-29", "2026-05-28"]
})

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-number">128</div>
        <div class="metric-label">Total Reports</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-number">76</div>
        <div class="metric-label">Verified Reports</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-number">39</div>
        <div class="metric-label">Open Reports</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-number">13</div>
        <div class="metric-label">Resolved Reports</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="section-card">', unsafe_allow_html=True)
st.subheader("🚨 Reports by Category")

category_data = pd.DataFrame({
    "Category": [
        "Harassment",
        "Violence",
        "Theft / Robbery",
        "Unsafe Area",
        "Suspicious Activity",
        "Bullying",
        "Domestic Violence"
    ],
    "Reports": [28, 15, 22, 31, 18, 9, 5]
})

st.bar_chart(category_data.set_index("Category"))
st.markdown("</div>", unsafe_allow_html=True)

st.markdown('<div class="section-card">', unsafe_allow_html=True)
st.subheader("📍 Safety Hotspots")

hotspot_col1, hotspot_col2, hotspot_col3 = st.columns(3)

with hotspot_col1:
    st.markdown("### Ameerpet")
    st.markdown('<span class="badge">High Reports</span>', unsafe_allow_html=True)
    st.write("Most reported: Harassment")

with hotspot_col2:
    st.markdown("### Madhapur")
    st.markdown('<span class="badge">Medium Reports</span>', unsafe_allow_html=True)
    st.write("Most reported: Theft / Robbery")

with hotspot_col3:
    st.markdown("### Koti")
    st.markdown('<span class="badge">Watch Area</span>', unsafe_allow_html=True)
    st.write("Most reported: Unsafe Area")

st.markdown("</div>", unsafe_allow_html=True)

st.markdown('<div class="section-card">', unsafe_allow_html=True)
st.subheader("📝 Recent Reports")
st.dataframe(reports, use_container_width=True)
st.markdown("</div>", unsafe_allow_html=True)

st.markdown('<div class="section-card">', unsafe_allow_html=True)
st.subheader("💡 Community Insights")

st.write("""
- Harassment and unsafe area reports are the most common.
- Ameerpet currently has the highest number of reports.
- Most reports are submitted during evening hours.
- Community reporting can help identify repeated safety concerns.
""")

st.markdown("</div>", unsafe_allow_html=True)