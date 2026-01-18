import streamlit as st
import db as d
import pandas as pd
from datetime import date

# 1. Page Configuration
st.set_page_config(page_title="Attendance Management", layout="wide", initial_sidebar_state="collapsed")

# 2. Cyber Dark Theme Injection
st.markdown("""
    <style>
    .stApp {
        background: radial-gradient(circle at center, #1e1e1e 0%, #000000 100%);
        color: #e0e0e0;
    }

    /* Input & Selectbox Styling */
    .stTextInput input, .stSelectbox div[data-baseweb="select"], .stDateInput div {
        background-color: #262626 !important;
        color: #ffffff !important;
        border-radius: 8px !important;
        border: 1px solid #444 !important;
    }

    /* Radio Button Styling */
    div[data-testid="stRadio"] label {
        color: #ffffff !important;
        font-weight: bold;
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

    /* Dataframe Styling */
    [data-testid="stDataFrame"] {
        border: 1px solid #333;
        border-radius: 8px;
    }

    h2, h3 {
        color: #ffffff !important;
        text-shadow: 0 0 5px rgba(255, 255, 255, 0.1);
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Structural Layout
left_margin, center_content, right_margin = st.columns([1, 4, 1])

with center_content:
    st.title("🗓️ Attendance Management")
    st.write("---")

    # Data Fetching
    students = d.view_a()

    if not students:
        st.info("No students available in the database.")
        if st.button("Back"):
            st.switch_page("pages/functionality.py")
        st.stop()

    # Section 1: Mark Attendance
    st.subheader("Mark New Attendance")
    col_a, col_b = st.columns(2)
    
    with col_a:
        student = st.selectbox("Select Student", students, format_func=lambda x: f"{x[0]} (Roll: {x[1]})")
        att_date = st.date_input("Date", date.today())
    
    with col_b:
        status = st.radio("Status", ["Present", "Absent"], horizontal=True)
        st.write("<br>", unsafe_allow_html=True)
        if st.button("Save Attendance"):
            d.add_attendance(student, status, att_date)
            st.success(f"Attendance for {student[0]} saved!")

    st.write("<br>", unsafe_allow_html=True)
    st.write("---")

    # Section 2: View Records
    st.subheader("📊 Attendance Records")
    records = d.record()
    
    if records:
        df = pd.DataFrame(
            records,
            columns=["Name", "Date", "Status"] # Ensure these match your DB columns
        )
        st.dataframe(df, use_container_width=True)
    else:
        st.info("No attendance records found.")

    # Navigation
    st.write("<br>", unsafe_allow_html=True)
    col_back, _ = st.columns([1, 3])
    with col_back:
        if st.button("Back"):
            st.switch_page("pages/Exfunctionality.py")