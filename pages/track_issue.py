import streamlit as st

st.set_page_config(
    page_title="Track Report | SpotIt",
    page_icon="🔍",
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

.search-card {
    background: white;
    padding: 28px;
    border-radius: 20px;
    box-shadow: 0px 4px 20px rgba(0,0,0,0.08);
    animation: fadeIn 0.8s ease-in;
}

.status-card {
    background: white;
    padding: 24px;
    border-radius: 20px;
    box-shadow: 0px 4px 20px rgba(0,0,0,0.08);
    text-align: center;
    transition: 0.3s;
}

.status-card:hover {
    transform: translateY(-5px);
    box-shadow: 0px 8px 30px rgba(91,75,219,0.25);
}

.status-title {
    font-size: 16px;
    color: #666;
}

.status-value {
    font-size: 28px;
    font-weight: 800;
    color: #6C63FF;
}

.detail-card {
    background: white;
    padding: 24px;
    border-radius: 20px;
    box-shadow: 0px 4px 20px rgba(0,0,0,0.08);
    margin-top: 20px;
}

.timeline-item {
    background: #F6F3FF;
    padding: 16px;
    border-left: 5px solid #6C63FF;
    border-radius: 12px;
    margin-bottom: 12px;
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

.stButton > button {
    background: linear-gradient(90deg, #6C63FF, #8B5CF6);
    color: white;
    border: none;
    border-radius: 12px;
    padding: 12px 20px;
    font-weight: 700;
    width: 100%;
}

.stButton > button:hover {
    transform: scale(1.02);
    transition: 0.3s;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<h1 class="main-title">🔍 Track Your Report</h1>
<p class="subtitle">
Enter your SpotIt Report ID to check the current status of your safety report.
</p>
""", unsafe_allow_html=True)

st.markdown('<div class="search-card">', unsafe_allow_html=True)

report_id = st.text_input(
    "Report ID",
    placeholder="Example: SPOT20260530123045"
)

track_button = st.button("Track Report")

st.markdown("</div>", unsafe_allow_html=True)

if track_button:
    if not report_id.strip():
        st.error("Please enter a valid Report ID.")
    else:
        st.success(f"Report found: {report_id}")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.markdown("""
            <div class="status-card">
                <div class="status-title">Current Status</div>
                <div class="status-value">Under Review</div>
            </div>
            """, unsafe_allow_html=True)

        with col2:
            st.markdown("""
            <div class="status-card">
                <div class="status-title">Category</div>
                <div class="status-value">Harassment</div>
            </div>
            """, unsafe_allow_html=True)

        with col3:
            st.markdown("""
            <div class="status-card">
                <div class="status-title">Priority</div>
                <div class="status-value">High</div>
            </div>
            """, unsafe_allow_html=True)

        st.markdown('<div class="detail-card">', unsafe_allow_html=True)
        st.subheader("📄 Report Details")

        st.write("**Report ID:**", report_id)
        st.write("**Incident Category:** Harassment")
        st.write("**Location:** Ameerpet, Hyderabad")
        st.write("**Submitted On:** 30 May 2026")
        st.write("**Description:** Report submitted anonymously for community safety review.")

        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown('<div class="detail-card">', unsafe_allow_html=True)
        st.subheader("📌 Status Timeline")

        st.markdown("""
        <div class="timeline-item">
            <strong>Submitted</strong><br>
            Your report was submitted successfully.
        </div>

        <div class="timeline-item">
            <strong>Under Review</strong><br>
            The report is currently being reviewed.
        </div>

        <div class="timeline-item">
            <strong>Verified</strong><br>
            Pending verification.
        </div>

        <div class="timeline-item">
            <strong>Resolved</strong><br>
            Not resolved yet.
        </div>
        """, unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)

st.divider()

st.info(
    "🔒 SpotIt uses only your Report ID for tracking. "
    "Your identity remains anonymous."
)