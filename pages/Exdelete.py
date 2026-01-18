import streamlit as st
import db as d
import pandas as pd

# 1. Page Configuration
st.set_page_config(page_title="Delete Student", layout="wide", initial_sidebar_state="collapsed")

# 2. Cyber Dark Theme Injection
st.markdown("""
    <style>
    .stApp {
        background: radial-gradient(circle at center, #1e1e1e 0%, #000000 100%);
        color: #e0e0e0;
    }

    /* Input Styling */
    .stTextInput input {
        background-color: #262626 !important;
        color: #ffffff !important;
        border-radius: 8px !important;
        border: 1px solid #444 !important;
    }

    /* Standard Button Styling (Back) */
    .stButton>button {
        width: 100%;
        border-radius: 8px;
        border: 1px solid #00d4ff;
        background-color: transparent;
        color: #00d4ff;
        font-weight: bold;
        height: 3em;
    }

    /* Red "Delete" Button Style */
    div.stButton > button:first-child:contains("Delete") {
        border: 1px solid #ff4b4b !important;
        color: #ff4b4b !important;
    }
    
    div.stButton > button:first-child:contains("Delete"):hover {
        background-color: #ff4b4b !important;
        color: #ffffff !important;
        box-shadow: 0 0 15px rgba(255, 75, 75, 0.4);
    }

    .stButton>button:hover {
        background-color: #00d4ff;
        color: #000000;
        box-shadow: 0 0 15px rgba(0, 212, 255, 0.5);
    }

    [data-testid="stDataFrame"] {
        border: 1px solid #333;
        border-radius: 8px;
    }

    h3 {
        color: #ffffff !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Structural Layout
left_margin, center_content, right_margin = st.columns([1, 4, 1])

with center_content:
    st.subheader("❌ Delete Student")
    st.write("---")

    # Input and Table Section
    roll = st.text_input("Enter Roll No to Delete", placeholder="e.g. 101")
    
    data = d.view_a()
    if data:
        df = pd.DataFrame(
            data,
            columns=["Name", "Roll", "Department", "Year"]
        )
        st.dataframe(df, use_container_width=True)
    else:
        st.info("No student records found")

    st.write("<br>", unsafe_allow_html=True)

    # Action Buttons
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Delete"):
            if roll:
                # Check if roll exists before trying to delete
                if d.view(roll):
                    d.delete(roll)
                    st.success(f"Student with Roll {roll} deleted successfully")
                    st.rerun()
                else:
                    st.error("Roll Number not found")
            else:
                st.warning("Please enter a Roll Number")

    with col2:
        if st.button("Back"):
            st.switch_page("pages/Exfunctionality.py")