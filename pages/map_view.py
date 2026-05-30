import streamlit as st
import pandas as pd
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from database import init_db, get_all_reports

st.set_page_config(page_title="SpotIt Safety Map", page_icon="🗺️", layout="wide")

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
    "Gachibowli":    (17.4401, 78.3489),
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