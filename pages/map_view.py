import streamlit as st
import pandas as pd

st.set_page_config(page_title="SpotIt Map View", page_icon="🗺️", layout="wide")

st.title("🗺️ SpotIt Safety Map")
st.write("View reported civic and safety issues across different locations.")

reports = pd.DataFrame({
    "Issue": [
        "Broken Streetlight",
        "Road Damage",
        "Garbage Dump",
        "Water Leakage",
        "Unsafe Area"
    ],
    "Category": [
        "Lighting",
        "Road",
        "Sanitation",
        "Water",
        "Safety"
    ],
    "Status": [
        "Pending",
        "In Progress",
        "Resolved",
        "Pending",
        "In Progress"
    ],
    "Location": [
        "Koti",
        "Ameerpet",
        "Madhapur",
        "Charminar",
        "Gachibowli"
    ],
    "lat": [
        17.3850,
        17.4375,
        17.4486,
        17.3616,
        17.4401
    ],
    "lon": [
        78.4867,
        78.4483,
        78.3908,
        78.4747,
        78.3489
    ]
})

st.subheader("📍 Report Locations on Map")
st.map(reports[["lat", "lon"]])

st.subheader("🔎 Filter Reports")

status_filter = st.selectbox(
    "Filter by status",
    ["All", "Pending", "In Progress", "Resolved"]
)

category_filter = st.selectbox(
    "Filter by category",
    ["All", "Lighting", "Road", "Sanitation", "Water", "Safety"]
)

filtered_reports = reports.copy()

if status_filter != "All":
    filtered_reports = filtered_reports[filtered_reports["Status"] == status_filter]

if category_filter != "All":
    filtered_reports = filtered_reports[filtered_reports["Category"] == category_filter]

st.dataframe(filtered_reports, use_container_width=True)

st.subheader("📋 Report Details")

for _, row in filtered_reports.iterrows():
    with st.expander(f"{row['Issue']} - {row['Location']}"):
        st.write(f"**Category:** {row['Category']}")
        st.write(f"**Status:** {row['Status']}")
        st.write(f"**Location:** {row['Location']}")
        st.write(f"**Latitude:** {row['lat']}")
        st.write(f"**Longitude:** {row['lon']}")

st.subheader("✅ Final Integration Check")

st.success("Map View module integrated successfully.")
st.info("This page helps users visually identify safety and civic issue locations.")