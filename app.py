import streamlit as st
import db as d

# 1. MUST BE FIRST: Page Configuration
st.set_page_config(page_title="SMS Admin Login", layout="centered", initial_sidebar_state="collapsed")

# 2. Premium "Cyber Dark" CSS Styling
st.markdown("""
    <style>
    /* Main Background - Deep Black/Grey */
    .stApp {
        background: radial-gradient(circle at center, #1e1e1e 0%, #000000 100%);
        color: #e0e0e0;
    }

    /* Input Field Styling - Darker with Neon Border focus */
    .stTextInput input {
        background-color: #262626 !important;
        color: #ffffff !important;
        border-radius: 8px !important;
        border: 1px solid #444 !important;
        padding: 10px !important;
    }
    
    .stTextInput input:focus {
        border-color: #00d4ff !important;
        box-shadow: 0 0 10px rgba(0, 212, 255, 0.5) !important;
    }

    /* Professional Button Styling - Cyan/Neon Accents */
    .stButton>button {
        width: 100%;
        border-radius: 8px;
        border: 1px solid #00d4ff;
        height: 3em;
        background-color: transparent;
        color: #00d4ff;
        font-weight: bold;
        transition: 0.3s all ease;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    .stButton>button:hover {
        background-color: #00d4ff;
        color: #000000;
        box-shadow: 0 0 20px rgba(0, 212, 255, 0.6);
        transform: translateY(-2px);
    }
    
    /* Title Styling with Subtle Neon Glow */
    h1 {
        color: #ffffff;
        text-shadow: 0 0 10px rgba(255, 255, 255, 0.2);
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        font-weight: 700;
    }
    
    h3 {
        color: #888888 !important;
        font-weight: 300 !important;
    }

    /* Success/Error override for Dark Theme */
    .stAlert {
        background-color: #262626 !important;
        color: white !important;
        border: 1px solid #333 !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Logic & UI
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

st.title("🎓 Student Management System")
st.subheader("Admin login")

# Using columns to center the login form even tighter if desired
user = st.text_input("Username", placeholder="Enter username")
pwd = st.text_input("Password", type="password", placeholder="••••••••")

# Adding a spacer for better vertical rhythm
st.write("") 

if st.button("login"):
    admin_data = d.admin_login(user, pwd)
    if admin_data:
        st.session_state.logged_in = True
        st.success("Access Granted. Redirecting...")
        st.switch_page("pages/Exfunctionality.py")
    else:

        st.error("Invalid Credentials. Please try again.")

