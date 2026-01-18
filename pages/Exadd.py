import streamlit as st
import db as d

st.set_page_config(page_title="Add Student", page_icon="➕", layout="wide", initial_sidebar_state="collapsed")
left_margin, center_content, right_margin = st.columns([1, 4, 1])

with center_content :
    # ENLARGED TITLE SECTION
    st.markdown(
        "<h1 style='text-align:center; font-size: 55px; font-weight: bold; color: #ffffff; margin-bottom: 0px;'>➕ Add Student</h1>",
        unsafe_allow_html=True
    )

    st.markdown("""
        <style>
        .stApp {
            background: radial-gradient(circle at center, #1e1e1e 0%, #000000 100%);
            color: #e0e0e0;
        }

        /* Input Field & Selectbox Styling */
        .stTextInput input, .stSelectbox div[data-baseweb="select"] {
            background-color: #262626 !important;
            color: #ffffff !important;
            border-radius: 8px !important;
            border: 1px solid #444 !important;
        }
        
        .stTextInput input:focus {
            border-color: #00d4ff !important;
            box-shadow: 0 0 10px rgba(0, 212, 255, 0.5) !important;
        }

        /* Button Styling */
        .stButton>button {
            width: 100%;
            border-radius: 8px;
            border: 1px solid #00d4ff;
            background-color: transparent;
            color: #00d4ff;
            font-weight: bold;
            transition: 0.3s all ease;
            height: 3em;
        }
        
        .stButton>button:hover {
            background-color: #00d4ff;
            color: #000000;
            box-shadow: 0 0 15px rgba(0, 212, 255, 0.5);
        }

        /* Success & Warning Alert Styling */
        .stAlert {
            background-color: #1a1a1a !important;
            color: #ffffff !important;
            border: 1px solid #333 !important;
        }
        
        h2, h3 {
            color: #ffffff !important;
        }
        </style>
        """, unsafe_allow_html=True)

    with st.form("Add Student", clear_on_submit=True):

        name = st.text_input("Name", placeholder="Enter full name")
        roll = st.text_input("Roll No", placeholder="e.g., 101")
        dept = st.text_input("Department", placeholder="e.g., Computer Science")
        year = st.selectbox("Year", [1, 2, 3, 4])

        submitted = st.form_submit_button("Add Student")

        if submitted:
            if name and roll:
                try:
                    d.add(name, roll, dept, year)
                    st.success(f"✅ Student {name} added successfully")
                except Exception as e:
                    st.error(f"❌ Error: {e}")
            else:
                st.warning("⚠️ Name and Roll No are required")

    if st.button("Back"):
        st.switch_page("pages/Exfunctionality.py")
