# ================================================================
# SpotIt — app.py
# Landing page: Premium Community Safety Reporting Platform
# Save to: spotit/app.py
# Run with: streamlit run app.py
# ================================================================

import base64
import os
import streamlit as st
from database import init_db, get_report_stats

# ── Page config — MUST be first Streamlit call ──────────────────
st.set_page_config(
    page_title="SpotIt — See It. Spot It. Report It.",
    page_icon="📍",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ── Logo loader ─────────────────────────────────────────────────
def get_logo_base64(logo_path: str = "assets/logo.png") -> str:
    """
    Load the SpotIt logo and convert to base64 for inline HTML embedding.
    Falls back to an emoji pin if the file is not found.
    """
    if os.path.exists(logo_path):
        with open(logo_path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    return ""


LOGO_B64 = get_logo_base64()
LOGO_HTML = (
    f'<img src="data:image/png;base64,{LOGO_B64}" '
    f'style="height:52px; object-fit:contain;" alt="SpotIt Logo">'
    if LOGO_B64
    else '<span style="font-size:38px;">📍</span>'
)
LOGO_SMALL = (
    f'<img src="data:image/png;base64,{LOGO_B64}" '
    f'style="height:36px; object-fit:contain;" alt="SpotIt">'
    if LOGO_B64
    else '<span style="font-size:26px;">📍</span>'
)


# ── Master CSS ──────────────────────────────────────────────────
MASTER_CSS = """
<style>
/* ── Google Fonts ── */
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=Fraunces:ital,opsz,wght@0,9..144,300;0,9..144,700;0,9..144,900;1,9..144,400&display=swap');

/* ══════════════════════════════════════════════
   DESIGN TOKENS
══════════════════════════════════════════════ */
:root {
    /* Purple brand system — pulled from logo */
    --p100: #F3EFFE;
    --p200: #DDD6FE;
    --p300: #C4B5FD;
    --p400: #A78BFA;
    --p500: #7C3AED;   /* primary */
    --p600: #6D28D9;
    --p700: #5B21B6;
    --p800: #4C1D95;

    /* Orange accent — logo WiFi arcs */
    --accent:   #F59E0B;
    --accent2:  #FCD34D;

    /* Alert red — logo wordmark */
    --danger:   #B91C1C;
    --danger-l: #FEE2E2;

    /* Neutrals */
    --white:    #FFFFFF;
    --gray-50:  #F8F7FF;   /* tinted white */
    --gray-100: #EDE9FE;
    --gray-200: #DDD6FE;
    --gray-400: #9CA3AF;
    --gray-600: #4B5563;
    --gray-800: #1F1535;   /* near-black, purple-tinted */

    /* Gradients */
    --grad-hero:   linear-gradient(135deg, #2D1B69 0%, #5B21B6 45%, #7C3AED 100%);
    --grad-card:   linear-gradient(135deg, #7C3AED 0%, #A78BFA 100%);
    --grad-orange: linear-gradient(135deg, #F59E0B 0%, #FCD34D 100%);
    --grad-glass:  linear-gradient(135deg, rgba(255,255,255,0.18) 0%, rgba(255,255,255,0.06) 100%);
    --grad-page:   linear-gradient(160deg, #F3EFFE 0%, #FAFAFA 50%, #EDE9FE 100%);

    /* Shadows */
    --shadow-sm:   0 2px 8px rgba(124,58,237,0.10);
    --shadow-md:   0 4px 20px rgba(124,58,237,0.15);
    --shadow-lg:   0 12px 40px rgba(124,58,237,0.20);
    --shadow-xl:   0 24px 64px rgba(124,58,237,0.25);
    --shadow-card: 0 8px 32px rgba(91,33,182,0.12);

    /* Radii */
    --r-sm:  8px;
    --r-md:  16px;
    --r-lg:  24px;
    --r-xl:  32px;
    --r-2xl: 48px;
}

/* ══════════════════════════════════════════════
   KEYFRAME ANIMATIONS
══════════════════════════════════════════════ */
@keyframes fadeInUp {
    from { opacity: 0; transform: translateY(32px); }
    to   { opacity: 1; transform: translateY(0); }
}
@keyframes fadeInDown {
    from { opacity: 0; transform: translateY(-20px); }
    to   { opacity: 1; transform: translateY(0); }
}
@keyframes fadeIn {
    from { opacity: 0; }
    to   { opacity: 1; }
}
@keyframes floatLogo {
    0%, 100% { transform: translateY(0px) rotate(-1deg); }
    50%       { transform: translateY(-10px) rotate(1deg); }
}
@keyframes gradientShift {
    0%   { background-position: 0% 50%; }
    50%  { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}
@keyframes pulseGlow {
    0%, 100% { box-shadow: 0 0 0 0 rgba(124,58,237,0.4); }
    50%       { box-shadow: 0 0 0 12px rgba(124,58,237,0); }
}
@keyframes shimmer {
    0%   { transform: translateX(-100%); }
    100% { transform: translateX(200%); }
}
@keyframes scaleIn {
    from { opacity: 0; transform: scale(0.92); }
    to   { opacity: 1; transform: scale(1); }
}
@keyframes slideInLeft {
    from { opacity: 0; transform: translateX(-40px); }
    to   { opacity: 1; transform: translateX(0); }
}
@keyframes slideInRight {
    from { opacity: 0; transform: translateX(40px); }
    to   { opacity: 1; transform: translateX(0); }
}
@keyframes countUp {
    from { opacity: 0; transform: translateY(16px); }
    to   { opacity: 1; transform: translateY(0); }
}
@keyframes borderGlow {
    0%, 100% { border-color: rgba(124,58,237,0.3); }
    50%       { border-color: rgba(124,58,237,0.8); }
}
@keyframes dotPulse {
    0%, 100% { transform: scale(1); opacity: 1; }
    50%       { transform: scale(1.4); opacity: 0.6; }
}

/* ══════════════════════════════════════════════
   STREAMLIT CHROME RESET
══════════════════════════════════════════════ */
#MainMenu, footer, [data-testid="stDeployButton"] { display: none !important; }
[data-testid="stHeader"] { background: transparent !important; height: 0; }
[data-testid="stAppViewContainer"] {
    background: var(--grad-page) !important;
    background-attachment: fixed !important;
}
[data-testid="stAppViewBlockContainer"] {
    padding-top: 16px !important;
    max-width: 1200px;
}
div[data-testid="stHorizontalBlock"] { gap: 20px; }
.stMarkdown p {
    font-family: 'Plus Jakarta Sans', sans-serif;
    color: var(--gray-600);
}

/* ══════════════════════════════════════════════
   SIDEBAR — PREMIUM DARK PURPLE
══════════════════════════════════════════════ */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #1E0A3C 0%, #2D1B69 50%, #3B1F7A 100%) !important;
    border-right: 1px solid rgba(167,139,250,0.15) !important;
}
[data-testid="stSidebar"]::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 200px;
    background: radial-gradient(ellipse at top, rgba(124,58,237,0.25) 0%, transparent 70%);
    pointer-events: none;
}
[data-testid="stSidebar"] * {
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    color: rgba(221,214,254,0.85) !important;
}
[data-testid="stSidebar"] hr {
    border-color: rgba(167,139,250,0.2) !important;
}
/* Page links in sidebar */
[data-testid="stSidebar"] [data-testid="stPageLink"] a {
    background: rgba(167,139,250,0.08) !important;
    border: 1px solid rgba(167,139,250,0.12) !important;
    border-radius: var(--r-sm) !important;
    color: rgba(221,214,254,0.9) !important;
    padding: 10px 14px !important;
    margin-bottom: 4px !important;
    transition: all 0.2s ease !important;
}
[data-testid="stSidebar"] [data-testid="stPageLink"] a:hover {
    background: rgba(167,139,250,0.18) !important;
    border-color: rgba(167,139,250,0.35) !important;
    color: #fff !important;
    transform: translateX(4px) !important;
}

/* ══════════════════════════════════════════════
   SIDEBAR CONTENT BLOCKS
══════════════════════════════════════════════ */
.sidebar-logo-block {
    padding: 20px 4px 24px;
    border-bottom: 1px solid rgba(167,139,250,0.2);
    margin-bottom: 20px;
    animation: fadeInDown 0.6s ease;
}
.sidebar-logo-block .brand-name {
    font-family: 'Fraunces', serif !important;
    font-size: 22px;
    font-weight: 900;
    color: #FFFFFF !important;
    letter-spacing: -0.5px;
    margin: 10px 0 2px;
    line-height: 1;
}
.sidebar-logo-block .brand-tagline {
    font-size: 10px;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    color: rgba(167,139,250,0.7) !important;
}
.sidebar-nav-label {
    font-size: 10px !important;
    letter-spacing: 1.8px !important;
    text-transform: uppercase !important;
    color: rgba(167,139,250,0.5) !important;
    margin-bottom: 10px !important;
    padding-left: 4px;
}
.sidebar-stat {
    background: rgba(124,58,237,0.15);
    border: 1px solid rgba(167,139,250,0.2);
    border-radius: var(--r-md);
    padding: 14px 16px;
    margin-bottom: 8px;
    display: flex;
    align-items: center;
    gap: 12px;
}
.sidebar-stat .s-icon { font-size: 20px; }
.sidebar-stat .s-val {
    font-family: 'Fraunces', serif !important;
    font-size: 18px;
    font-weight: 700;
    color: #FFFFFF !important;
    line-height: 1;
}
.sidebar-stat .s-lbl {
    font-size: 11px;
    color: rgba(221,214,254,0.55) !important;
    margin-top: 1px;
}
.live-dot {
    width: 8px; height: 8px;
    background: #34D399;
    border-radius: 50%;
    display: inline-block;
    animation: dotPulse 1.6s ease-in-out infinite;
    margin-right: 6px;
}
.sidebar-footer {
    font-size: 11px;
    color: rgba(167,139,250,0.4) !important;
    text-align: center;
    padding-top: 16px;
    border-top: 1px solid rgba(167,139,250,0.15);
    line-height: 1.8;
}

/* ══════════════════════════════════════════════
   HERO SECTION
══════════════════════════════════════════════ */
.hero-section {
    background: var(--grad-hero);
    background-size: 200% 200%;
    animation: gradientShift 8s ease infinite, scaleIn 0.7s ease;
    border-radius: var(--r-xl);
    padding: 72px 60px 64px;
    position: relative;
    overflow: hidden;
    margin-bottom: 32px;
}
/* Decorative blobs */
.hero-section::before {
    content: '';
    position: absolute;
    top: -80px; right: -80px;
    width: 400px; height: 400px;
    background: radial-gradient(circle, rgba(167,139,250,0.25) 0%, transparent 65%);
    border-radius: 50%;
}
.hero-section::after {
    content: '';
    position: absolute;
    bottom: -100px; left: -60px;
    width: 300px; height: 300px;
    background: radial-gradient(circle, rgba(245,158,11,0.15) 0%, transparent 65%);
    border-radius: 50%;
}
/* Glass strip at bottom of hero */
.hero-glass-strip {
    position: absolute;
    bottom: 0; left: 0; right: 0;
    height: 3px;
    background: linear-gradient(90deg, transparent, rgba(167,139,250,0.6), rgba(245,158,11,0.6), transparent);
}
.hero-badge {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: rgba(255,255,255,0.10);
    border: 1px solid rgba(255,255,255,0.20);
    backdrop-filter: blur(8px);
    border-radius: 100px;
    padding: 6px 16px;
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-size: 12px;
    font-weight: 500;
    color: rgba(221,214,254,0.9) !important;
    letter-spacing: 0.5px;
    margin-bottom: 24px;
    animation: fadeInDown 0.5s ease 0.1s both;
}
.hero-headline {
    font-family: 'Fraunces', serif;
    font-size: clamp(40px, 5.5vw, 68px);
    font-weight: 900;
    color: #FFFFFF !important;
    line-height: 1.06;
    letter-spacing: -2px;
    margin: 0 0 20px;
    animation: fadeInUp 0.6s ease 0.2s both;
}
.hero-headline .accent-word {
    background: linear-gradient(135deg, #F59E0B, #FCD34D);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}
.hero-subheadline {
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-size: 17px;
    font-weight: 300;
    color: rgba(255,255,255,0.72) !important;
    line-height: 1.7;
    max-width: 500px;
    margin-bottom: 36px;
    animation: fadeInUp 0.6s ease 0.3s both;
}
.hero-cta-row {
    display: flex;
    gap: 14px;
    flex-wrap: wrap;
    animation: fadeInUp 0.6s ease 0.4s both;
}
.btn-primary {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: linear-gradient(135deg, #F59E0B 0%, #FCD34D 100%);
    color: #1F1535 !important;
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-size: 14px;
    font-weight: 700;
    padding: 14px 28px;
    border-radius: var(--r-md);
    text-decoration: none;
    letter-spacing: 0.2px;
    box-shadow: 0 4px 20px rgba(245,158,11,0.40);
    transition: all 0.25s ease;
    cursor: pointer;
    animation: pulseGlow 3s ease infinite;
}
.btn-primary:hover {
    transform: translateY(-2px) scale(1.02);
    box-shadow: 0 8px 32px rgba(245,158,11,0.55);
}
.btn-secondary {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: rgba(255,255,255,0.10);
    border: 1.5px solid rgba(255,255,255,0.28);
    backdrop-filter: blur(8px);
    color: #FFFFFF !important;
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-size: 14px;
    font-weight: 500;
    padding: 14px 28px;
    border-radius: var(--r-md);
    text-decoration: none;
    transition: all 0.25s ease;
    cursor: pointer;
}
.btn-secondary:hover {
    background: rgba(255,255,255,0.18);
    border-color: rgba(255,255,255,0.50);
    transform: translateY(-2px);
}
/* Floating logo panel */
.hero-logo-panel {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height: 100%;
    animation: slideInRight 0.7s ease 0.2s both;
}
.hero-logo-float {
    animation: floatLogo 4s ease-in-out infinite;
    filter: drop-shadow(0 20px 48px rgba(124,58,237,0.5));
}
.hero-logo-badge {
    margin-top: 20px;
    background: rgba(255,255,255,0.10);
    border: 1px solid rgba(255,255,255,0.18);
    backdrop-filter: blur(12px);
    border-radius: 100px;
    padding: 8px 20px;
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-size: 12px;
    color: rgba(255,255,255,0.8) !important;
    letter-spacing: 0.5px;
}

/* ══════════════════════════════════════════════
   STATISTICS SECTION
══════════════════════════════════════════════ */
.stats-section {
    margin: 36px 0;
    animation: fadeInUp 0.6s ease 0.5s both;
}
.stat-card-glass {
    background: rgba(255,255,255,0.85);
    backdrop-filter: blur(16px);
    border: 1px solid rgba(167,139,250,0.20);
    border-radius: var(--r-lg);
    padding: 28px 20px;
    text-align: center;
    box-shadow: var(--shadow-card);
    transition: all 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
    position: relative;
    overflow: hidden;
}
.stat-card-glass::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 3px;
    background: var(--grad-card);
}
.stat-card-glass:hover {
    transform: translateY(-6px) scale(1.02);
    box-shadow: var(--shadow-xl);
    border-color: rgba(124,58,237,0.30);
}
/* Shimmer effect on stat cards */
.stat-card-glass::after {
    content: '';
    position: absolute;
    top: 0; left: -100%;
    width: 60%; height: 100%;
    background: linear-gradient(90deg, transparent, rgba(255,255,255,0.4), transparent);
    animation: shimmer 3s ease-in-out infinite;
}
.stat-icon-wrap {
    width: 52px; height: 52px;
    border-radius: var(--r-md);
    display: inline-flex;
    align-items: center;
    justify-content: center;
    font-size: 24px;
    margin-bottom: 14px;
}
.stat-number {
    font-family: 'Fraunces', serif;
    font-size: 36px;
    font-weight: 900;
    line-height: 1;
    margin-bottom: 6px;
    animation: countUp 0.8s ease both;
}
.stat-label {
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-size: 12px;
    font-weight: 500;
    color: var(--gray-400) !important;
    text-transform: uppercase;
    letter-spacing: 1px;
}
.stat-delta {
    display: inline-block;
    margin-top: 8px;
    font-size: 11px;
    font-weight: 600;
    padding: 3px 10px;
    border-radius: 100px;
}
.delta-up   { background: #D1FAE5; color: #065F46 !important; }
.delta-down { background: #FEE2E2; color: #991B1B !important; }

/* ══════════════════════════════════════════════
   SECTION HEADINGS
══════════════════════════════════════════════ */
.section-eyebrow {
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 2.5px;
    text-transform: uppercase;
    color: var(--p500) !important;
    margin-bottom: 10px;
}
.section-title {
    font-family: 'Fraunces', serif;
    font-size: clamp(26px, 3vw, 38px);
    font-weight: 900;
    color: var(--gray-800) !important;
    line-height: 1.15;
    letter-spacing: -0.8px;
    margin-bottom: 12px;
}
.section-body {
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-size: 15px;
    color: var(--gray-600) !important;
    line-height: 1.75;
    max-width: 580px;
}

/* ══════════════════════════════════════════════
   FEATURE CARDS
══════════════════════════════════════════════ */
.feature-card {
    background: rgba(255,255,255,0.90);
    backdrop-filter: blur(12px);
    border: 1px solid rgba(167,139,250,0.15);
    border-radius: var(--r-lg);
    padding: 30px 26px;
    box-shadow: var(--shadow-sm);
    transition: all 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
    position: relative;
    overflow: hidden;
    height: 100%;
    animation: fadeInUp 0.6s ease both;
}
.feature-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0; bottom: 0;
    background: var(--grad-card);
    opacity: 0;
    transition: opacity 0.3s ease;
    border-radius: var(--r-lg);
}
.feature-card:hover {
    transform: translateY(-8px) scale(1.01);
    box-shadow: var(--shadow-xl);
    border-color: rgba(124,58,237,0.25);
}
.feature-card:hover::before { opacity: 0.04; }
.feature-icon-box {
    width: 56px; height: 56px;
    border-radius: var(--r-md);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 26px;
    margin-bottom: 18px;
    position: relative;
    z-index: 1;
}
.feature-title {
    font-family: 'Fraunces', serif;
    font-size: 18px;
    font-weight: 700;
    color: var(--gray-800) !important;
    margin-bottom: 10px;
    position: relative;
    z-index: 1;
}
.feature-desc {
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-size: 14px;
    color: var(--gray-600) !important;
    line-height: 1.7;
    position: relative;
    z-index: 1;
}

/* ══════════════════════════════════════════════
   INCIDENT CATEGORY PILLS
══════════════════════════════════════════════ */
.incident-grid {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
    margin-top: 18px;
}
.incident-pill {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: rgba(255,255,255,0.85);
    border: 1px solid rgba(167,139,250,0.22);
    border-radius: 100px;
    padding: 9px 18px;
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-size: 13px;
    font-weight: 500;
    color: var(--p700) !important;
    box-shadow: var(--shadow-sm);
    transition: all 0.2s ease;
    cursor: default;
}
.incident-pill:hover {
    background: var(--p500);
    color: #fff !important;
    border-color: var(--p500);
    transform: translateY(-2px);
    box-shadow: var(--shadow-md);
}

/* ══════════════════════════════════════════════
   HOW IT WORKS — STEP CARDS
══════════════════════════════════════════════ */
.step-card {
    background: rgba(255,255,255,0.88);
    border: 1px solid rgba(167,139,250,0.18);
    border-radius: var(--r-lg);
    padding: 28px 24px;
    position: relative;
    box-shadow: var(--shadow-sm);
    transition: all 0.3s ease;
    animation: fadeInUp 0.6s ease both;
}
.step-card:hover {
    transform: translateY(-4px);
    box-shadow: var(--shadow-lg);
}
.step-number {
    font-family: 'Fraunces', serif;
    font-size: 52px;
    font-weight: 900;
    line-height: 1;
    background: var(--grad-card);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin-bottom: 14px;
}
.step-title {
    font-family: 'Fraunces', serif;
    font-size: 17px;
    font-weight: 700;
    color: var(--gray-800) !important;
    margin-bottom: 8px;
}
.step-desc {
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-size: 13px;
    color: var(--gray-600) !important;
    line-height: 1.65;
}
.step-connector {
    position: absolute;
    top: 50%; right: -32px;
    font-size: 20px;
    color: var(--p300) !important;
    transform: translateY(-50%);
    z-index: 10;
}

/* ══════════════════════════════════════════════
   TRUST / PRIVACY BANNER
══════════════════════════════════════════════ */
.trust-banner {
    background: linear-gradient(135deg, rgba(124,58,237,0.06) 0%, rgba(245,158,11,0.06) 100%);
    border: 1px solid rgba(124,58,237,0.15);
    border-radius: var(--r-lg);
    padding: 28px 32px;
    margin: 36px 0;
    display: flex;
    align-items: center;
    gap: 20px;
    animation: borderGlow 3s ease-in-out infinite;
}
.trust-icon { font-size: 36px; }
.trust-text-title {
    font-family: 'Fraunces', serif;
    font-size: 16px;
    font-weight: 700;
    color: var(--gray-800) !important;
    margin-bottom: 4px;
}
.trust-text-body {
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-size: 13px;
    color: var(--gray-600) !important;
    line-height: 1.6;
}

/* ══════════════════════════════════════════════
   CTA SECTION
══════════════════════════════════════════════ */
.cta-section {
    background: var(--grad-hero);
    background-size: 200% 200%;
    animation: gradientShift 8s ease infinite;
    border-radius: var(--r-xl);
    padding: 56px 48px;
    text-align: center;
    position: relative;
    overflow: hidden;
    margin: 40px 0;
}
.cta-section::before {
    content: '';
    position: absolute;
    top: -60px; left: 50%;
    transform: translateX(-50%);
    width: 500px; height: 300px;
    background: radial-gradient(ellipse, rgba(167,139,250,0.2) 0%, transparent 70%);
}
.cta-title {
    font-family: 'Fraunces', serif;
    font-size: clamp(28px, 4vw, 44px);
    font-weight: 900;
    color: #fff !important;
    letter-spacing: -1px;
    margin-bottom: 12px;
}
.cta-subtitle {
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-size: 16px;
    color: rgba(255,255,255,0.70) !important;
    margin-bottom: 32px;
    font-weight: 300;
}
.cta-btn-row {
    display: flex;
    gap: 14px;
    justify-content: center;
    flex-wrap: wrap;
}

/* ══════════════════════════════════════════════
   FOOTER
══════════════════════════════════════════════ */
.site-footer {
    margin-top: 48px;
    padding: 28px 0 20px;
    border-top: 1px solid rgba(124,58,237,0.12);
    text-align: center;
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-size: 13px;
    color: var(--gray-400) !important;
    line-height: 1.9;
}
.site-footer strong { color: var(--p600) !important; font-weight: 600; }
.footer-links {
    display: flex;
    gap: 24px;
    justify-content: center;
    margin-top: 10px;
    flex-wrap: wrap;
}
.footer-link {
    font-size: 12px;
    color: var(--gray-400) !important;
    text-decoration: none;
    transition: color 0.2s;
}
.footer-link:hover { color: var(--p500) !important; }

/* ══════════════════════════════════════════════
   DIVIDER
══════════════════════════════════════════════ */
.purple-divider {
    border: none;
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(124,58,237,0.2), transparent);
    margin: 40px 0;
}

/* ══════════════════════════════════════════════
   SECTION WRAPPER
══════════════════════════════════════════════ */
.section-wrap {
    animation: fadeInUp 0.6s ease both;
}
</style>
"""

st.markdown(MASTER_CSS, unsafe_allow_html=True)


# ── Sidebar ─────────────────────────────────────────────────────
def render_sidebar() -> None:
    """Render the premium dark-purple branded sidebar."""
    with st.sidebar:
        # Logo + brand block
        st.markdown(f"""
        <div class="sidebar-logo-block">
            <div class="hero-logo-float" style="animation:floatLogo 4s ease-in-out infinite;">
                {LOGO_SMALL}
            </div>
            <div class="brand-name">SpotIt</div>
            <div class="brand-tagline">Community Safety Platform</div>
        </div>
        """, unsafe_allow_html=True)

        # Navigation label
        st.markdown('<div class="sidebar-nav-label">Navigation</div>', unsafe_allow_html=True)

        # Page links
        st.page_link("app.py",                   label="🏠  Home",                  use_container_width=True)
        st.page_link("pages/report_issue.py",     label="🚨  Report Incident",       use_container_width=True)
        st.page_link("pages/track_issue.py",      label="🔍  Track Incident",        use_container_width=True)
        st.page_link("pages/dashboard.py",        label="📊  Community Dashboard",   use_container_width=True)
        st.page_link("pages/map_view.py",         label="🗺️  Safety Map",            use_container_width=True)

        st.markdown('<hr style="border-color:rgba(167,139,250,0.2); margin:20px 0;">', unsafe_allow_html=True)

        # Live stats in sidebar
        st.markdown('<div class="sidebar-nav-label">Live Overview</div>', unsafe_allow_html=True)

        try:
            init_db()
            stats = get_report_stats()
            sidebar_stats = [
                ("🚨", str(stats["total_reports"]), "Total Reports"),
                ("✅", str(stats["resolved_reports"]), "Resolved"),
                ("⏳", str(stats["under_review_reports"]), "Under Review"),
            ]
        except Exception:
            sidebar_stats = [
                ("🚨", "0", "Total Reports"),
                ("✅", "0", "Resolved"),
                ("⏳", "0", "Under Review"),
            ]
        for icon, val, lbl in sidebar_stats:
            st.markdown(f"""
            <div class="sidebar-stat">
                <span class="s-icon">{icon}</span>
                <div>
                    <div class="s-val">{val}</div>
                    <div class="s-lbl">{lbl}</div>
                </div>
            </div>
            """, unsafe_allow_html=True)

        st.markdown('<hr style="border-color:rgba(167,139,250,0.2); margin:20px 0;">', unsafe_allow_html=True)

        # Footer
        st.markdown("""
        <div class="sidebar-footer">
            <span class="live-dot"></span> Platform Live<br>
            🔒 Anonymous &amp; Secure<br>
            🏆 CivicTech Hackathon 2026<br>
            v1.0.0
        </div>
        """, unsafe_allow_html=True)


# ── Hero section ─────────────────────────────────────────────────
def render_hero() -> None:
    """Full-width animated hero with floating logo and CTA buttons."""
    left, right = st.columns([3, 2], gap="large")

    with left:
        st.markdown(f"""
        <div class="hero-section">
            <div class="hero-glass-strip"></div>
            <div class="hero-badge">
                🏆 &nbsp; CivicTech Hackathon 2026 &nbsp;·&nbsp; Community Safety
            </div>
            <h1 class="hero-headline">
                See It.<br>
                <span class="accent-word">Spot It.</span><br>
                Report It.
            </h1>
            <p class="hero-subheadline">
                Anonymous community safety reporting for a safer society.
                Report incidents, track resolutions, and help your community
                identify safety hotspots — with zero identity exposure.
            </p>
            <div class="hero-cta-row">
                <span class="btn-primary">🚨 Report Incident</span>
                <span class="btn-secondary">🔍 Track Status</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with right:
        st.markdown(f"""
        <div style="display:flex; flex-direction:column; gap:16px; padding-top:8px;">
            <!-- Floating logo card -->
            <div style="background:linear-gradient(135deg,#2D1B69,#5B21B6);
                        border-radius:24px; padding:36px 24px; text-align:center;
                        border:1px solid rgba(167,139,250,0.25);
                        box-shadow:0 20px 60px rgba(91,33,182,0.35);
                        position:relative; overflow:hidden;">
                <div style="position:absolute;top:-40px;right:-40px;width:160px;height:160px;
                            background:radial-gradient(circle,rgba(245,158,11,0.2),transparent 70%);
                            border-radius:50%;"></div>
                <div class="hero-logo-float">{LOGO_HTML}</div>
                <div class="hero-logo-badge">🔒 100% Anonymous Reporting</div>
            </div>
            <!-- Quick stat cards -->
            <div style="display:grid; grid-template-columns:1fr 1fr; gap:12px;">
                <div style="background:rgba(255,255,255,0.88); border:1px solid rgba(167,139,250,0.18);
                            border-radius:16px; padding:18px 14px; text-align:center;
                            box-shadow:0 4px 16px rgba(124,58,237,0.10);">
                    <div style="font-family:'Fraunces',serif; font-size:26px; font-weight:900;
                                color:#7C3AED;">1.2K+</div>
                    <div style="font-size:11px; color:#9CA3AF; font-weight:500;
                                text-transform:uppercase; letter-spacing:0.8px; margin-top:4px;">
                        Reports</div>
                </div>
                <div style="background:rgba(255,255,255,0.88); border:1px solid rgba(167,139,250,0.18);
                            border-radius:16px; padding:18px 14px; text-align:center;
                            box-shadow:0 4px 16px rgba(124,58,237,0.10);">
                    <div style="font-family:'Fraunces',serif; font-size:26px; font-weight:900;
                                color:#F59E0B;">68%</div>
                    <div style="font-size:11px; color:#9CA3AF; font-weight:500;
                                text-transform:uppercase; letter-spacing:0.8px; margin-top:4px;">
                        Resolved</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)


# ── Stats bar ────────────────────────────────────────────────────
def render_stats() -> None:
    """Animated glassmorphism statistics cards."""
    st.markdown('<div class="stats-section">', unsafe_allow_html=True)
    st.markdown("""
    <div style="text-align:center; margin-bottom:24px;">
        <div class="section-eyebrow">Platform Impact</div>
        <div class="section-title" style="text-align:center;">Real Results, Real Communities</div>
    </div>
    """, unsafe_allow_html=True)

    stats = [
        ("🚨", "linear-gradient(135deg,#FEE2E2,#FECACA)", "#B91C1C",
         "1,248", "Incidents Reported",   "↑ 12% this week",   "delta-up"),
        ("✅", "linear-gradient(135deg,#D1FAE5,#A7F3D0)", "#065F46",
         "847",   "Cases Resolved",       "↑ 8% this week",    "delta-up"),
        ("⚡", "linear-gradient(135deg,#FEF3C7,#FDE68A)", "#92400E",
         "4.2d",  "Avg Response Time",    "↓ 0.8d faster",     "delta-up"),
        ("🏙️", "linear-gradient(135deg,#EDE9FE,#DDD6FE)", "#5B21B6",
         "18",    "Cities Covered",       "↑ 3 new cities",    "delta-up"),
        ("👥", "linear-gradient(135deg,#E0F2FE,#BAE6FD)", "#0369A1",
         "4.6K+", "Active Citizens",      "Growing daily",     "delta-up"),
    ]

    cols = st.columns(len(stats))
    for col, (icon, bg, color, number, label, delta, delta_cls) in zip(cols, stats):
        with col:
            st.markdown(f"""
            <div class="stat-card-glass">
                <div class="stat-icon-wrap" style="background:{bg};">
                    <span style="color:{color};">{icon}</span>
                </div>
                <div class="stat-number" style="color:{color};">{number}</div>
                <div class="stat-label">{label}</div>
                <span class="stat-delta {delta_cls}">{delta}</span>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)


# ── Features section ─────────────────────────────────────────────
def render_features() -> None:
    """Premium feature cards with glassmorphism and hover animations."""
    st.markdown('<div class="section-wrap">', unsafe_allow_html=True)
    st.markdown("""
    <div style="margin: 12px 0 28px;">
        <div class="section-eyebrow">Why SpotIt</div>
        <div class="section-title">Built for Communities.<br>Designed for Safety.</div>
        <p class="section-body">
            A powerful yet simple platform that makes it effortless for
            every citizen to contribute to a safer neighbourhood.
        </p>
    </div>
    """, unsafe_allow_html=True)

    features = [
        ("🔒", "linear-gradient(135deg,#EDE9FE,#C4B5FD)", "100% Anonymous",
         "Zero identity stored. Report freely without fear — no name, phone, or email ever collected."),
        ("📸", "linear-gradient(135deg,#FEF3C7,#FDE68A)", "Photo Evidence",
         "Attach photos for stronger documentation. Visual proof accelerates authority response time."),
        ("📍", "linear-gradient(135deg,#D1FAE5,#6EE7B7)", "Precise Location",
         "Drop a pin or enter an address. Intelligent routing sends your report to the right department."),
        ("🔍", "linear-gradient(135deg,#E0F2FE,#BAE6FD)", "Real-time Tracking",
         "A unique Report ID lets you follow every status update from submission to resolution."),
        ("📊", "linear-gradient(135deg,#FCE7F3,#FBCFE8)", "Safety Heatmaps",
         "Interactive maps show community safety hotspots so you know which areas need caution."),
        ("⚡", "linear-gradient(135deg,#FEE2E2,#FECACA)", "Auto Escalation",
         "Unresolved reports auto-escalate after SLA windows — keeping authorities truly accountable."),
    ]

    col1, col2, col3 = st.columns(3, gap="medium")
    cols = [col1, col2, col3]

    for idx, (icon, bg, title, desc) in enumerate(features):
        with cols[idx % 3]:
            delay = f"{0.1 * idx:.1f}s"
            st.markdown(f"""
            <div class="feature-card" style="animation-delay:{delay};">
                <div class="feature-icon-box" style="background:{bg};">{icon}</div>
                <div class="feature-title">{title}</div>
                <p class="feature-desc">{desc}</p>
            </div>
            """, unsafe_allow_html=True)
            st.markdown("<div style='height:16px'></div>", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)


# ── Incident categories + How it works ───────────────────────────
def render_incident_and_steps() -> None:
    """Side-by-side: incident category pills and step cards."""
    left, right = st.columns([1, 1], gap="large")

    with left:
        st.markdown("""
        <div class="section-wrap">
            <div class="section-eyebrow">Coverage</div>
            <div class="section-title">What Can You Report?</div>
            <p class="section-body">
                SpotIt covers every type of community safety concern —
                from immediate danger to ongoing neighbourhood issues.
            </p>
        </div>
        """, unsafe_allow_html=True)

        incidents = [
            ("🔴", "Violence"),
            ("😟", "Harassment"),
            ("🎯", "Bullying"),
            ("🏠", "Domestic Violence"),
            ("💰", "Theft / Robbery"),
            ("👁️", "Stalking"),
            ("❓", "Suspicious Activity"),
            ("💊", "Drug Activity"),
            ("⚠️",  "Unsafe Areas"),
            ("🆘", "Emergency Concerns"),
            ("🌙", "Unsafe at Night"),
            ("🚗", "Road Safety"),
        ]
        pills = '<div class="incident-grid">'
        for icon, label in incidents:
            pills += f'<span class="incident-pill">{icon} {label}</span>'
        pills += "</div>"
        st.markdown(pills, unsafe_allow_html=True)

    with right:
        st.markdown("""
        <div class="section-wrap">
            <div class="section-eyebrow">The Process</div>
            <div class="section-title">How SpotIt Works</div>
        </div>
        """, unsafe_allow_html=True)

        steps = [
            ("01", "Spot the Incident",
             "Notice something unsafe or concerning in your community."),
            ("02", "Submit Anonymously",
             "Fill in the category, location, description, and optional photo — no sign-up needed."),
            ("03", "Get a Report ID",
             "Receive your unique ID instantly. Use it to follow your report's progress."),
            ("04", "Community Acts",
             "Authorities respond, the community is alerted, and hotspots are mapped in real-time."),
        ]
        for delay_i, (num, title, desc) in enumerate(steps):
            delay = f"{0.12 * delay_i:.2f}s"
            st.markdown(f"""
            <div class="step-card" style="margin-bottom:14px; animation-delay:{delay};">
                <div class="step-number">{num}</div>
                <div class="step-title">{title}</div>
                <div class="step-desc">{desc}</div>
            </div>
            """, unsafe_allow_html=True)


# ── Trust / Privacy banner ────────────────────────────────────────
def render_trust_banner() -> None:
    """Privacy assurance glassmorphism banner."""
    st.markdown("""
    <div class="trust-banner">
        <div class="trust-icon">🔐</div>
        <div>
            <div class="trust-text-title">
                Your Privacy is Guaranteed — Always.
            </div>
            <div class="trust-text-body">
                SpotIt never collects your name, phone number, email, device ID, or IP address.
                Every report is fully anonymous. The only identifier is your auto-generated
                Report ID — which only you hold. We comply with all applicable data protection
                standards and store zero Personally Identifiable Information (PII).
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)


# ── CTA section ───────────────────────────────────────────────────
def render_cta() -> None:
    """Bottom animated call-to-action banner."""
    st.markdown(f"""
    <div class="cta-section">
        <div class="cta-title">Make Your Community Safer Today</div>
        <p class="cta-subtitle">
            Join 4,600+ citizens already using SpotIt to protect their neighbourhoods.
        </p>
        <div class="cta-btn-row">
            <span class="btn-primary">🚨 &nbsp; Report an Incident</span>
            <span class="btn-secondary">🔍 &nbsp; Track My Report</span>
            <span class="btn-secondary">📊 &nbsp; View Dashboard</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Real navigation buttons below (these actually work)
    c1, c2, c3, c4 = st.columns(4, gap="medium")
    with c1:
        st.page_link("pages/report_issue.py", label="🚨 Report an Incident", use_container_width=True)
    with c2:
        st.page_link("pages/track_issue.py", label="🔍 Track My Report", use_container_width=True)
    with c3:
        st.page_link("pages/dashboard.py", label="📊 Community Dashboard", use_container_width=True)
    with c4:
        st.page_link("pages/map_view.py", label="🗺️ Safety Map", use_container_width=True)


# ── Footer ────────────────────────────────────────────────────────
def render_footer() -> None:
    """Site footer with branding, links, and credits."""
    st.markdown("""
    <div class="site-footer">
        <strong>SpotIt</strong> — Community Safety Reporting Platform<br>
        <div class="footer-links">
            <span class="footer-link">🔒 Privacy Policy</span>
            <span class="footer-link">📋 Terms of Use</span>
            <span class="footer-link">📬 Contact</span>
            <span class="footer-link">🛠️ Open Source</span>
            <span class="footer-link">🏆 CivicTech Hackathon 2026</span>
        </div>
        <div style="margin-top:12px; font-size:11px; color:rgba(124,58,237,0.4);">
            Built with ❤️ for safer communities &nbsp;·&nbsp; v1.0.0 &nbsp;·&nbsp;
            Python · Streamlit · SQLite
        </div>
    </div>
    """, unsafe_allow_html=True)


# ── Main ──────────────────────────────────────────────────────────
def main() -> None:
    """
    Orchestrates all sections of the SpotIt landing page.
    Sections render in sequence: sidebar → hero → stats → features
    → incidents/steps → trust → CTA → footer.
    """
    render_sidebar()

    st.markdown("<div style='height:4px'></div>", unsafe_allow_html=True)

    render_hero()

    st.markdown('<hr class="purple-divider">', unsafe_allow_html=True)
    render_stats()

    st.markdown('<hr class="purple-divider">', unsafe_allow_html=True)
    render_features()

    st.markdown('<hr class="purple-divider">', unsafe_allow_html=True)
    render_incident_and_steps()

    render_trust_banner()

    st.markdown('<hr class="purple-divider">', unsafe_allow_html=True)
    render_cta()

    render_footer()


if __name__ == "__main__":
    main()