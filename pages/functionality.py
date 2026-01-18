import streamlit as st
from streamlit_extras.switch_page_button import switch_page
if st.button("Log out"):
    st.session_state.logged_in = False
    st.switch_page("login.py")

st.title("Admin Panel Functionalities")
st.markdown(
    '<br>',unsafe_allow_html=True
)
col1, col2, col3,col4 = st.columns(4)
with col1:
    if st.button("Add Student"):
        st.switch_page("pages/add.py")

with col2:
    if st.button("View Students"):
        st.switch_page("pages/view.py")

with col3:
    if st.button("Attendance"):
        st.switch_page("pages/attendence.py")

with col4:
    if st.button("Delete Student"):
        st.switch_page("pages/delete.py")
