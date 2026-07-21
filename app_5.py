import streamlit as st
import sys
import os

# ── PATH FIX — works on local machine AND Streamlit Cloud ─────────────────────
ROOT = os.path.dirname(os.path.abspath(__file__))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)
# ─────────────────────────────────────────────────────────────────────────────

from database.db_setup import initialize_database
from modules.inspection_form import render_inspection_form
from modules.dashboard       import render_dashboard
from modules.spc_charts      import render_spc_charts
from modules.traceability    import render_traceability
from modules.reports         import render_reports
from modules.filter_assembly import render_filter_assembly   # NEW

# ── Page config — MUST be first Streamlit call ────────────────────────────────
st.set_page_config(
    page_title="Smart QC Dashboard | Uno Minda",
    page_icon="🏭",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ── CSS ───────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@300;400;600;700&display=swap');
    html, body, [class*="css"] { font-family: 'IBM Plex Sans', sans-serif; }
    .main-header {
        background: linear-gradient(135deg, #1a237e 0%, #283593 50%, #1565C0 100%);
        padding: 1.2rem 2rem; border-radius: 10px;
        margin-bottom: 1rem; color: white;
    }
    .main-header h1 { color: white !important; font-size: 1.8rem; font-weight: 700; margin: 0; }
    .main-header p  { color: #90CAF9; font-size: 0.85rem; margin: 0.2rem 0 0 0; }
    [data-testid="metric-container"] {
        background: #F8F9FA; border: 1px solid #E0E0E0;
        border-radius: 8px; padding: 1rem; border-left: 4px solid #1565C0;
    }
    [data-testid="stSidebar"] { background: #1a237e; }
    [data-testid="stSidebar"] * { color: #E8EAF6 !important; }
    .stButton > button[kind="primary"] { background: #1565C0; border: none; font-weight: 600; }
    .stButton > button[kind="primary"]:hover { background: #0D47A1; border: none; }
    hr { border-color: #E0E0E0; }
</style>
""", unsafe_allow_html=True)

# ── Init database ─────────────────────────────────────────────────────────────
initialize_database()

# ── Sidebar ───────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("# 🏭")
    st.markdown("### Smart QC Dashboard")
    st.markdown("*Uno Minda | Quality Control*")
    st.divider()

    st.markdown("#### Navigation")
    page = st.radio(
        label="Select Page",
        options=[
            "📋 Inspection Form",
            "📊 Analytics Dashboard",
            "📉 SPC Charts",
            "🔍 Traceability",
            "📄 Reports & Export",
            "🧰 Filter Assembly PCC",   # NEW
        ],
        label_visibility="collapsed"
    )

    st.divider()
    st.markdown("#### Quick Stats")

    from utils.helpers import load_all_inspections, calculate_kpis
    sidebar_df   = load_all_inspections()
    sidebar_kpis = calculate_kpis(sidebar_df)
    st.metric("Total Inspections", sidebar_kpis["total"])
    rejection = sidebar_kpis["rejection_rate"]
    if rejection <= 1.0:
        st.success(f"✅ Rejection Rate: {rejection}%")
    elif rejection <= 3.0:
        st.warning(f"⚠️ Rejection Rate: {rejection}%")
    else:
        st.error(f"❌ Rejection Rate: {rejection}%")

    st.divider()
    st.markdown("#### Developer Tools")

    if st.button("🎲 Load Sample Data", help="Generates 300 synthetic records for testing"):
        with st.spinner("Generating sample data..."):
            try:
                data_dir = os.path.join(ROOT, "data")
                if data_dir not in sys.path:
                    sys.path.insert(0, data_dir)
                from generate_sample_data import generate_sample_data
                generate_sample_data(300)
                st.success("✅ 300 sample records loaded!")
                st.rerun()
            except Exception as e:
                st.error(f"Error: {e}")

    if st.button("🗑️ Clear All Records", help="Deletes all inspection records"):
        try:
            from database.db_setup import get_connection
            conn = get_connection()
            conn.execute("DELETE FROM inspections")
            conn.execute("DELETE FROM filter_assembly_inspections")  # NEW
            conn.commit()
            conn.close()
            st.success("✅ All records cleared!")
            st.rerun()
        except Exception as e:
            st.error(f"Error: {e}")

    st.divider()
    st.caption("v1.1.0 | IATF 16949 Compliant")
    st.caption("Built with Python + Streamlit")

# ── Header ────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="main-header">
    <h1>🏭 Smart QC Inspection & Traceability Dashboard</h1>
    <p>Uno Minda Group | Quality Control Division | Real-time Defect Tracking & SPC Analysis</p>
</div>
""", unsafe_allow_html=True)

# ── Page routing ──────────────────────────────────────────────────────────────
if   page == "📋 Inspection Form":     render_inspection_form()
elif page == "📊 Analytics Dashboard": render_dashboard()
elif page == "📉 SPC Charts":          render_spc_charts()
elif page == "🔍 Traceability":        render_traceability()
elif page == "📄 Reports & Export":    render_reports()
elif page == "🧰 Filter Assembly PCC": render_filter_assembly()   # NEW
