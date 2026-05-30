import streamlit as st
import pandas as pd
import sys
import os

# ── Connect to database ──────────────────────────────────────────
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from database import init_db, get_report_stats, get_reports_by_category, get_all_reports

# ── Page config ──────────────────────────────────────────────────
st.set_page_config(
    page_title="Dashboard | SpotIt",
    page_icon="📊",
    layout="wide"
)

# ── Initialize database ──────────────────────────────────────────
init_db()

# ── Styling ──────────────────────────────────────────────────────
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
    from { opacity: 0; transform: translateY(18px); }
    to   { opacity: 1; transform: translateY(0); }
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

# ── Header ───────────────────────────────────────────────────────
st.markdown("""
<div>
    <h1 class="main-title">📊 Community Safety Dashboard</h1>
    <p class="subtitle">
        View safety reports, community trends, and incident hotspots.
    </p>
</div>
""", unsafe_allow_html=True)

# ── Load real data from database ─────────────────────────────────
stats        = get_report_stats()
all_reports  = get_all_reports()
cat_data     = get_reports_by_category()

total      = stats["total_reports"]
verified   = stats["verified_reports"]
open_rep   = stats["submitted_reports"] + stats["under_review_reports"]
resolved   = stats["resolved_reports"]

# ── Metric Cards ─────────────────────────────────────────────────
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-number">{total}</div>
        <div class="metric-label">Total Reports</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-number">{verified}</div>
        <div class="metric-label">Verified Reports</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-number">{open_rep}</div>
        <div class="metric-label">Open Reports</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-number">{resolved}</div>
        <div class="metric-label">Resolved Reports</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<div style='height:20px'></div>", unsafe_allow_html=True)

# ── Reports by Category Chart ─────────────────────────────────────
st.markdown('<div class="section-card">', unsafe_allow_html=True)
st.subheader("🚨 Reports by Category")

if cat_data:
    cat_df = pd.DataFrame(cat_data)
    st.bar_chart(cat_df.set_index("category")["count"])
else:
    st.info("No reports submitted yet. Category chart will appear here.")

st.markdown("</div>", unsafe_allow_html=True)

# ── Status Distribution ───────────────────────────────────────────
st.markdown('<div class="section-card">', unsafe_allow_html=True)
st.subheader("📈 Report Status Overview")

status_data = pd.DataFrame({
    "Status": ["Submitted", "Under Review", "Verified", "Resolved"],
    "Count": [
        stats["submitted_reports"],
        stats["under_review_reports"],
        stats["verified_reports"],
        stats["resolved_reports"]
    ]
})
st.bar_chart(status_data.set_index("Status"))

st.markdown("</div>", unsafe_allow_html=True)

# ── Safety Hotspots ───────────────────────────────────────────────
st.markdown('<div class="section-card">', unsafe_allow_html=True)
st.subheader("📍 Safety Hotspots")

if all_reports:
    df = pd.DataFrame(all_reports)
    if "location" in df.columns:
        hotspot_df = df["location"].value_counts().head(3).reset_index()
        hotspot_df.columns = ["Location", "Reports"]

        cols = st.columns(len(hotspot_df))
        for i, row in hotspot_df.iterrows():
            with cols[i]:
                st.markdown(f"### {row['Location']}")
                if row["Reports"] >= 5:
                    badge = "High Reports"
                elif row["Reports"] >= 3:
                    badge = "Medium Reports"
                else:
                    badge = "Watch Area"
                st.markdown(
                    f'<span class="badge">{badge}</span>',
                    unsafe_allow_html=True
                )
                st.write(f"Total reports: **{row['Reports']}**")
else:
    st.info("No hotspot data yet. Submit reports to see hotspots.")

st.markdown("</div>", unsafe_allow_html=True)

# ── Recent Reports Table ──────────────────────────────────────────
st.markdown('<div class="section-card">', unsafe_allow_html=True)
st.subheader("📝 Recent Reports")

if all_reports:
    df = pd.DataFrame(all_reports)
    display_cols = [c for c in
        ["report_id", "category", "location", "status", "created_at"]
        if c in df.columns]
    st.dataframe(
        df[display_cols].head(10),
        use_container_width=True,
        hide_index=True
    )
else:
    st.info("No reports yet. Reports will appear here once submitted.")

st.markdown("</div>", unsafe_allow_html=True)

# ── Community Insights ────────────────────────────────────────────
st.markdown('<div class="section-card">', unsafe_allow_html=True)
st.subheader("💡 Community Insights")

col1, col2, col3 = st.columns(3)

# Most reported category
if cat_data:
    top_category = pd.DataFrame(cat_data).iloc[0]["category"]
else:
    top_category = "No data yet"

# Most active location
if all_reports:
    df = pd.DataFrame(all_reports)
    top_location = df["location"].value_counts().idxmax() \
        if "location" in df.columns and not df.empty \
        else "No data yet"
else:
    top_location = "No data yet"

with col1:
    st.success(f"**Most Reported Category**\n\n{top_category}")

with col2:
    st.info(f"**Most Active Location**\n\n{top_location}")

with col3:
    st.warning(f"**Total Reports**\n\n{total} Reports")

st.markdown("</div>", unsafe_allow_html=True)

# ── Footer ────────────────────────────────────────────────────────
st.markdown("---")
st.caption(
    "SpotIt Dashboard • CivicTech Hackathon 2026 • Community Safety Analytics"
)