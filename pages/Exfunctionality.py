import streamlit as st

# 1. Page Configuration
st.set_page_config(page_title="SMS Admin Panel", layout="wide", initial_sidebar_state="collapsed")

# 2. Cyber Dark Theme Injection
st.markdown("""
    <style>
    /* Main Background */
    .stApp {
        background: radial-gradient(circle at center, #1e1e1e 0%, #000000 100%);
        color: #e0e0e0;
    }

    /* Button Styling */
    .stButton>button {
        width: 100%;
        border-radius: 8px;
        border: 1px solid #444;
        background-color: #262626;
        color: #ffffff;
        font-weight: 500;
        transition: 0.3s all ease;
    }
    
    .stButton>button:hover {
        border-color: #00d4ff;
        color: #00d4ff;
        box-shadow: 0 0 15px rgba(0, 212, 255, 0.4);
    }

    /* Title Styling */
    h1 {
        color: #ffffff;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        font-weight: 700;
        text-align: left;
        margin-top: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Structural Layout
# This creates the wide margins on the left and right seen in your screenshot
left_margin, center_content, right_margin = st.columns([1, 4, 1])

with center_content:
    # Row 1: Log out button (Small width column)
    col_log, col_empty = st.columns([1, 5])
    with col_log:
        if st.button("Log out"):
            st.session_state.logged_in = False
            st.switch_page("app.py")

    # Row 2: Title
    st.markdown("<br>", unsafe_allow_html=True)
    st.title("Admin Panel Functionalities")
    st.markdown("<br>", unsafe_allow_html=True)

    # Row 3: Action Buttons
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        if st.button("Add Student"):
            st.switch_page("pages/Exadd.py")

    with col2:
        if st.button("View Students"):
            st.switch_page("pages/Exview.py")

    with col3:
        if st.button("Attendance"):
            st.switch_page("pages/Exattendence.py")

    with col4:
        if st.button("Delete Student"):
            st.switch_page("pages/Exdelete.py")