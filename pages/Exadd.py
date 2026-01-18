import streamlit as st
import db as d

# 1. Page Configuration
st.set_page_config(page_title="Add Student", layout="wide", initial_sidebar_state="collapsed")

# 2. Cyber Dark Theme Injection
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

# 3. Structural Layout (Matching the Functionality Page)
left_margin, center_content, right_margin = st.columns([1, 4, 1])

# 3. Structural Layout (Matching the Functionality Page)
# This creates three columns: [1 (empty), 4 (content), 1 (empty)]
left_margin, center_content, right_margin = st.columns([1, 4, 1])

with center_content:
    st.subheader("➕ Add Student")
    st.write("---")
    
    # All inputs MUST be inside this 'with' block to stay centered
    name = st.text_input("Name", placeholder="Enter full name")
    roll = st.text_input("Roll No", placeholder="e.g., 101")
    dept = st.text_input("Department", placeholder="e.g., Computer Science")
    year = st.selectbox("Year", [1, 2, 3, 4])

    # Adding a small spacer before buttons
    st.write("<br>", unsafe_allow_html=True)

    # Action Buttons (Also inside the center_content)
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("Save Student"):
            if name and roll:
                try:
                    d.add(name, roll, dept, year)
                    st.success(f"✅ Student {name} added successfully")
                    
                    st.session_state.name = ""
                    st.session_state.roll = ""
                    st.rerun()
                except Exception as e:
                    st.error(f"Error: {e}")

    with col2:
        if st.button("Back"):
            st.switch_page("pages/Exfunctionality.py")


