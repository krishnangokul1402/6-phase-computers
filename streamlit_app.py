"""6 Phase Computers | Streamlit Community Cloud presentation.

Run locally: streamlit run streamlit_app.py
Publishes the same interactive showcase as index.html with original image assets.
No customer messages are transmitted or stored in this public demo.
"""
from pathlib import Path
import streamlit as st

ROOT = Path(__file__).resolve().parent
st.set_page_config(page_title="6 Phase Computers | Sales, Service & CCTV", page_icon="💻", layout="wide", initial_sidebar_state="collapsed")

# The iframe supports the complete HTML/CSS/JS design, with automatic resizing.
# st.iframe is available in Streamlit 1.60.0 (pinned in requirements.txt).
# The alt= argument was introduced later and must be omitted for 1.60.0.
st.html("""
<style>
[data-testid="stAppViewContainer"] { background:#fbfbff; }
[data-testid="stHeader"] { display:none; }
[data-testid="stMainBlockContainer"] { padding:0 !important; max-width:100% !important; }
[data-testid="stMain"] { padding:0 !important; }
[data-testid="stVerticalBlock"] { gap:0 !important; }
[data-testid="stVerticalBlockBorderWrapper"] { padding:0 !important; }
iframe { border:0 !important; }
</style>
""")
st.iframe(ROOT / "streamlit_site.html", height="content")
