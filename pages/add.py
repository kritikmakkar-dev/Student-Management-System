import streamlit as st
import db as d
st.subheader("➕ Add Student")

name = st.text_input("Name")
roll = st.text_input("Roll No")
dept = st.text_input("Department")
year = st.selectbox("Year", [1, 2, 3, 4])
col1,col2=st.columns(2)
with col1:
        if st.button("Save Student"):
                try:
                        d.add(name,roll,dept,year)
                        st.success("Student added successfully")
                except:
                        st.warning("same roll number exists")
with col2:
        if st.button("Back"):
                st.switch_page("pages/functionality.py")

