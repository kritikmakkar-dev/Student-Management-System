import streamlit as st
import db as d
import pandas as pd

# 1. Page Configuration
st.set_page_config(page_title="View Students", layout="wide", initial_sidebar_state="collapsed")

# 2. Cyber Dark Theme Injection
st.markdown("""
    <style>
    .stApp {
        background: radial-gradient(circle at center, #1e1e1e 0%, #000000 100%);
        color: #e0e0e0;
    }

    /* Search Input Styling */
    .stTextInput input {
        background-color: #262626 !important;
        color: #ffffff !important;
        border-radius: 8px !important;
        border: 1px solid #444 !important;
    }
    
    .stTextInput input:focus {
        border-color: #00d4ff !important;
        box-shadow: 0 0 10px rgba(0, 212, 255, 0.5) !important;
    }

    /* Dataframe Container Styling */
    [data-testid="stDataFrame"] {
        border: 1px solid #333;
        border-radius: 8px;
        overflow: hidden;
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
        margin-top: 20px;
    }
    
    .stButton>button:hover {
        background-color: #00d4ff;
        color: #000000;
        box-shadow: 0 0 15px rgba(0, 212, 255, 0.5);
    }

    /* Info Box Styling */
    .stAlert {
        background-color: #1a1a1a !important;
        color: #00d4ff !important;
        border: 1px solid #00d4ff !important;
    }
    
    h3 {
        color: #ffffff !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Structural Layout
left_margin, center_content, right_margin = st.columns([1, 4, 1])

with center_content:
    st.subheader("📋 Student List")
    st.write("---")

    # Search Section
    search = st.text_input("🔍 Search by Roll No", placeholder="Enter roll number to filter...")
    
    # Data Logic
    data = d.view_a()
    if search:
        data = d.view(search)

    # Display Section
    if data:
        df = pd.DataFrame(
            data,
            columns=["Name", "Roll", "Department", "Year"]
        )
        # use_container_width makes the table fill the center column
        st.dataframe(df, use_container_width=True)
    else:
        st.info("No student records found in the database.")

    # Navigation
    col_back, col_spacer = st.columns([1, 3])
    with col_back:
        if st.button("Back"):
            st.switch_page("pages/Exfunctionality.py")