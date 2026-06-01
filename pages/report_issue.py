import streamlit as st
import sys
from pathlib import Path
from datetime import datetime

sys.path.append(str(Path(__file__).resolve().parents[1]))

from database import init_db, create_report
from image_utils import save_uploaded_image
from sidebar_component import render_sidebar


st.set_page_config(
    page_title="Report Incident | SpotIt",
    page_icon="📍",
    layout="wide"
)

render_sidebar()

init_db()

# -------------------------------
# Custom Styling
# -------------------------------
st.markdown("""
<style>
.main-title {
    font-size: 40px;
    font-weight: 700;
    color: #000000;
}

.subtitle {
    color: #000000;
    font-size: 18px;
    margin-bottom: 20px;
}

.form-card {
    background: white;
    padding: 25px;
    border-radius: 20px;
    box-shadow: 0px 4px 20px rgba(0,0,0,0.08);
}

.stButton > button {
    background: linear-gradient(90deg,#6C63FF,#8B5CF6);
    color: white;
    border: none;
    border-radius: 10px;
    padding: 12px 20px;
    font-weight: 600;
    width: 100%;
}

.stButton > button:hover {
    transform: scale(1.02);
    transition: 0.3s;
}

.report-header {
    text-align: center;
    padding: 10px;
    animation: fadeIn 1s ease-in;
}

@keyframes fadeIn {
    from {
        opacity: 0;
        transform: translateY(20px);
    }
    to {
        opacity: 1;
        transform: translateY(0px);
    }
}
</style>
""", unsafe_allow_html=True)



# -------------------------------
# Header
# -------------------------------
st.markdown(
    """
    <div class="report-header">
        <h1 class="main-title">🚨 Report a Safety Incident</h1>
        <p class="subtitle">
            Help create safer communities by anonymously reporting incidents.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

# -------------------------------
# Form
# -------------------------------
with st.container():

    
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
            "Other"
        ]
    )

    col1, col2 = st.columns(2)

    with col1:
        incident_date = st.date_input(
            "Incident Date",
            value=datetime.today()
        )

    with col2:
        incident_time = st.time_input(
            "Incident Time"
        )

    location = st.selectbox(
    "Location",
    sorted([
        "Madhapur",
        "Gachibowli",
        "Kukatpally",
        "Hitech City",
        "Ameerpet",
        "Begumpet",
        "Banjara Hills",
        "Secunderabad",
        "Jubilee Hills",
        "Kondapur",
        "Miyapur",
        "Dilsukhnagar",
        "Koti",
        "Charminar"
    ])
)

    description = st.text_area(
        "Description",
        placeholder="Describe what happened...",
        height=180
    )

    st.caption(f"Characters: {len(description)}")

    uploaded_file = st.file_uploader(
        "Upload Evidence (Optional)",
        type=["jpg", "jpeg", "png"]
    )

    if uploaded_file is not None:
        st.image(
            uploaded_file,
            caption="Uploaded Evidence",
            use_container_width=True
        )

    st.write("")

    submit = st.button("📤 Submit Report")

    if submit:

        if not location.strip():
            st.error("Please enter a location.")

        elif not description.strip():
            st.error("Please enter a description.")

        else:
            report_id = "SPOT" + datetime.now().strftime("%Y%m%d%H%M%S")

            image_path = ""

            if uploaded_file is not None:
                image_path = save_uploaded_image(uploaded_file, report_id)

            saved = create_report(
                report_id=report_id,
                category=category,
                description=description,
                location=location,
                date=str(incident_date),
                time=str(incident_time),
                image_path=image_path
            )

            if saved:
                st.success("Report submitted successfully!")

                st.info(
                    f"Your Report ID: **{report_id}**\n\n"
                    "Save this ID to track your report."
                )
            else:
                st.error("Something went wrong. The report was not saved. Please try again.")

   
# -------------------------------
# Privacy Notice
# -------------------------------
st.divider()

st.info(
    """
    🔒 SpotIt does not collect your name, email,
    or phone number.

    All reports are submitted anonymously.
    """
)