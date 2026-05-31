import base64
import os
import streamlit as st

from database import init_db, get_report_stats


def get_logo_base64(logo_path: str = "assets/logo.png") -> str:
    if os.path.exists(logo_path):
        with open(logo_path, "rb") as file:
            return base64.b64encode(file.read()).decode()
    return ""


LOGO_B64 = get_logo_base64()

LOGO_SMALL = (
    f'<img src="data:image/png;base64,{LOGO_B64}" '
    f'style="height:118px; width:145px; object-fit:contain; display:block;" alt="SpotIt">'
    if LOGO_B64
    else '<span style="font-size:72px;">📍</span>'
)


SIDEBAR_CSS = """
<style>
/* Hide Streamlit default page list */
[data-testid="stSidebarNav"] {
    display: none !important;
    visibility: hidden !important;
    height: 0 !important;
    overflow: hidden !important;
}

section[data-testid="stSidebar"] nav {
    display: none !important;
}

/* Hide keyboard_double / sidebar collapse text */
[data-testid="stSidebarCollapseButton"],
[data-testid="stSidebarCollapseButton"] *,
button[title="Close sidebar"],
button[title="Open sidebar"] {
    display: none !important;
    visibility: hidden !important;
}

/* Sidebar background */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #1A0738 0%, #28105B 45%, #321775 100%) !important;
    border-right: 1px solid rgba(167,139,250,0.18) !important;
}

section[data-testid="stSidebar"] > div:first-child {
    padding-top: 0rem !important;
}

/* Sidebar inner padding */
[data-testid="stSidebar"] [data-testid="stVerticalBlock"] {
    gap: 0rem !important;
}

/* Logo block */
.sidebar-logo-block {
    padding: 28px 0px 18px 0px;
    margin: 0px 14px 16px 14px;
    border-bottom: 1px solid rgba(167,139,250,0.25);
}

.sidebar-logo-img {
    animation: none !important;
    transform: none !important;
    margin-bottom: 10px;
}

.brand-name {
    font-family: Georgia, serif !important;
    font-size: 25px;
    font-weight: 900;
    color: #FFFFFF !important;
    margin-top: 4px;
    line-height: 1.1;
}

.brand-tagline {
    font-size: 10px;
    font-weight: 600;
    color: rgba(196,181,253,0.85) !important;
    text-transform: uppercase;
    letter-spacing: 2.2px;
    margin-top: 2px;
}

/* Section labels */
.sidebar-nav-label {
    font-size: 10px;
    color: rgba(196,181,253,0.62) !important;
    text-transform: uppercase;
    letter-spacing: 2px;
    font-weight: 700;
    margin: 18px 14px 9px 14px;
}

/* Page link wrapper */
[data-testid="stSidebar"] [data-testid="stPageLink"] {
    margin: 0px 14px 9px 14px !important;
}

/* Page link buttons */
[data-testid="stSidebar"] [data-testid="stPageLink"] a {
    background: rgba(124,58,237,0.22) !important;
    border: 1px solid rgba(167,139,250,0.20) !important;
    border-radius: 9px !important;
    color: rgba(237,233,254,0.95) !important;
    padding: 12px 13px !important;
    font-size: 14px !important;
    font-weight: 700 !important;
    text-decoration: none !important;
    transition: 0.2s ease !important;
}

[data-testid="stSidebar"] [data-testid="stPageLink"] a:hover {
    background: rgba(167,139,250,0.28) !important;
    border-color: rgba(196,181,253,0.55) !important;
    color: #FFFFFF !important;
    transform: translateX(2px);
}

/* Divider */
.sidebar-divider {
    border: none;
    border-top: 1px solid rgba(167,139,250,0.25);
    margin: 18px 14px;
}

/* Stats */
.sidebar-stat {
    margin: 0px 14px 9px 14px;
    background: rgba(124,58,237,0.25);
    border: 1px solid rgba(167,139,250,0.24);
    border-radius: 13px;
    padding: 12px 14px;
    display: flex;
    align-items: center;
    gap: 12px;
}

.s-icon {
    font-size: 20px;
}

.s-val {
    color: #FFFFFF !important;
    font-size: 18px;
    font-weight: 900;
    line-height: 1.1;
}

.s-lbl {
    color: rgba(221,214,254,0.74) !important;
    font-size: 11px;
    margin-top: 2px;
}

/* Footer */
.sidebar-footer {
    color: rgba(221,214,254,0.58) !important;
    font-size: 10px;
    line-height: 1.7;
    text-align: center;
    padding: 8px 4px 20px 4px;
}

.live-dot {
    width: 8px;
    height: 8px;
    background: #22C55E;
    border-radius: 50%;
    display: inline-block;
    margin-right: 6px;
}
</style>
"""


def render_sidebar() -> None:
    st.markdown(SIDEBAR_CSS, unsafe_allow_html=True)

    with st.sidebar:
        st.markdown(
            f"""
            <div class="sidebar-logo-block">
                <div class="sidebar-logo-img">
                    {LOGO_SMALL}
                </div>
                <div class="brand-name">SpotIt</div>
                <div class="brand-tagline">Community Safety Platform</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown('<div class="sidebar-nav-label">Navigation</div>', unsafe_allow_html=True)

        st.page_link("app.py", label="🏠 Home", use_container_width=True)
        st.page_link("pages/report_issue.py", label="🚨 Report Incident", use_container_width=True)
        st.page_link("pages/track_issue.py", label="🔍 Track Incident", use_container_width=True)
        st.page_link("pages/dashboard.py", label="📊 Community Dashboard", use_container_width=True)
        st.page_link("pages/map_view.py", label="🗺️ Safety Map", use_container_width=True)

        st.markdown('<hr class="sidebar-divider">', unsafe_allow_html=True)

        st.markdown('<div class="sidebar-nav-label">Live Overview</div>', unsafe_allow_html=True)

        try:
            init_db()
            stats = get_report_stats()
            sidebar_stats = [
                ("🚨", str(stats.get("total_reports", 0)), "Total Reports"),
                ("✅", str(stats.get("resolved_reports", 0)), "Resolved"),
                ("⏳", str(stats.get("under_review_reports", 0)), "Under Review"),
            ]
        except Exception:
            sidebar_stats = [
                ("🚨", "0", "Total Reports"),
                ("✅", "0", "Resolved"),
                ("⏳", "0", "Under Review"),
            ]

        for icon, value, label in sidebar_stats:
            st.markdown(
                f"""
                <div class="sidebar-stat">
                    <span class="s-icon">{icon}</span>
                    <div>
                        <div class="s-val">{value}</div>
                        <div class="s-lbl">{label}</div>
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

        st.markdown('<hr class="sidebar-divider">', unsafe_allow_html=True)

        st.markdown(
            """
            <div class="sidebar-footer">
                <span class="live-dot"></span> Platform Live<br>
                🔒 Anonymous &amp; Secure<br>
                🏆 CivicTech Hackathon 2026<br>
                v1.0.0
            </div>
            """,
            unsafe_allow_html=True,
        )