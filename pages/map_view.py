import streamlit as st
import pandas as pd
import sys
import os


sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from database import init_db, get_all_reports
from sidebar_component import render_sidebar

st.set_page_config(page_title="SpotIt Safety Map", page_icon="🗺️", layout="wide")

st.markdown("""
<style>
            render_sidebar()
            /* Hide default Streamlit multipage navigation */
[data-testid="stSidebarNav"] {
    display: none !important;
}

/* Remove default sidebar spacing */
section[data-testid="stSidebar"] > div:first-child {
    padding-top: 0rem !important;
}
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
.stApp, .stMarkdown, .stMarkdown p, label {
    font-family: 'Plus Jakarta Sans', sans-serif !important;
}
h1, h2, h3 {
    font-family: 'Fraunces', serif !important;
    color: var(--gray-800) !important;
}
.stMarkdown, .stMarkdown p, .stCaptionContainer {
    color: var(--gray-600);
}
[data-testid="stMetric"],
.stExpander,
[data-testid="stSelectbox"] {
    background: rgba(255,255,255,0.88);
    border: 1px solid rgba(167,139,250,0.20);
    border-radius: 16px;
    box-shadow: var(--shadow-card);
}
[data-testid="stMetric"] {
    padding: 16px;
}
[data-testid="stMetricValue"] {
    color: var(--p500);
}
label, [data-testid="stSelectbox"] label {
    color: var(--gray-800) !important;
    font-weight: 700 !important;
}
</style>
""", unsafe_allow_html=True)

init_db()

st.title("🗺️ SpotIt Safety Map")
st.write("View reported safety incidents across Hyderabad.")

location_coords = {
    "Madhapur":      (17.4486, 78.3908),
    "Gachibowli":    (17.4401, 78.3489),
    "Kukatpally":    (17.4849, 78.3995),
    "Hitech City":   (17.4486, 78.3808),
    "Ameerpet":      (17.4375, 78.4483),
    "Begumpet":      (17.4432, 78.4671),
    "Banjara Hills": (17.4138, 78.4431),
    "Secunderabad":  (17.4399, 78.4983),
    "Jubilee Hills": (17.4229, 78.4082),
    "Kondapur":      (17.4600, 78.3615),
    "Miyapur":       (17.4957, 78.3565),
    "Dilsukhnagar":  (17.3686, 78.5247),
    "Koti":          (17.3850, 78.4867),
    "Charminar":     (17.3616, 78.4747),
}

all_reports = get_all_reports()

if all_reports:
    df = pd.DataFrame(all_reports)

    df["lat"] = df["location"].map(
        lambda x: location_coords.get(x, (17.3850, 78.4867))[0]
    )
    df["lon"] = df["location"].map(
        lambda x: location_coords.get(x, (17.3850, 78.4867))[1]
    )

    col1, col2 = st.columns(2)
    with col1:
        status_filter = st.selectbox(
            "Filter by Status",
            ["All", "Submitted", "Under Review", "Verified", "Resolved"]
        )
    with col2:
        category_filter = st.selectbox(
            "Filter by Category",
            ["All"] + list(df["category"].unique())
        )

    filtered = df.copy()
    if status_filter != "All":
        filtered = filtered[filtered["status"] == status_filter]
    if category_filter != "All":
        filtered = filtered[filtered["category"] == category_filter]

    st.subheader("📍 Incident Locations on Map")
    if not filtered.empty:
        st.map(filtered[["lat", "lon"]])
    else:
        st.warning("No reports match your filter.")

    st.subheader("📋 Report Details")
    for _, row in filtered.iterrows():
        with st.expander(f"🚨 {row['category']} — {row['location']}"):
            st.write(f"**Report ID:** {row['report_id']}")
            st.write(f"**Category:** {row['category']}")
            st.write(f"**Location:** {row['location']}")
            st.write(f"**Status:** {row['status']}")
            st.write(f"**Description:** {row['description']}")
            st.write(f"**Submitted:** {row['created_at']}")

    st.divider()
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Incidents", len(df))
    col2.metric("Filtered Results", len(filtered))
    col3.metric("Areas Covered", df["location"].nunique())

else:
    st.info("No reports yet. Submit a report to see it on the map!")
    empty_df = pd.DataFrame({
        "lat": [17.3850],
        "lon": [78.4867]
    })
    st.map(empty_df)

st.divider()
st.caption("SpotIt Safety Map • CivicTech Hackathon 2026 • Hyderabad")
