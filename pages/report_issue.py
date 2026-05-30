import streamlit as st
from datetime import datetime

st.set_page_config(
    page_title="Report Incident | SpotIt",
    page_icon="📍",
    layout="wide"
)

# -------------------------------
# Custom Styling
# -------------------------------

st.markdown("""
<style>

.main-title{
    font-size:40px;
    font-weight:700;
    color:#5B4BDB;
}

.subtitle{
    color:#666;
    font-size:18px;
    margin-bottom:20px;
}

.form-card{
    background:white;
    padding:25px;
    border-radius:20px;
    box-shadow:0px 4px 20px rgba(0,0,0,0.08);
}

.stButton > button{
    background:linear-gradient(90deg,#6C63FF,#8B5CF6);
    color:white;
    border:none;
    border-radius:10px;
    padding:12px 20px;
    font-weight:600;
    width:100%;
}

.stButton > button:hover{
    transform:scale(1.02);
    transition:0.3s;
}

.report-header{
    text-align:center;
    padding:10px;
    animation: fadeIn 1s ease-in;
}

@keyframes fadeIn{
    from{
        opacity:0;
        transform:translateY(20px);
    }
    to{
        opacity:1;
        transform:translateY(0px);
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

    location = st.text_input(
        "Location",
        placeholder="Enter incident location"
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

            report_id = (
                "SPOT" +
                datetime.now().strftime("%Y%m%d%H%M%S")
            )

            st.success("Report submitted successfully!")

            st.info(
                f"Your Report ID: **{report_id}**\n\n"
                "Save this ID to track your report."
            )


    st.markdown("</div>", unsafe_allow_html=True)

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