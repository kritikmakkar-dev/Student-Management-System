import streamlit as st
import db as d
import pandas as pd
from datetime import date
st.subheader("🗓️ Attendance Management")


students = d.view_a()

if not students:
    st.info("No students available")
    st.stop()

student = st.selectbox("Select Student", students, format_func=lambda x: x[1])
status = st.radio("Status", ["Present", "Absent"])
att_date = st.date_input("Date", date.today())

if st.button("Save Attendance"):
    d.add_attendance(student,status,att_date)
    st.success("Attendance saved successfully")

st.subheader("📊 Attendance Records")

records = d.record()
if records:
    df = pd.DataFrame(
        records,
        columns=["Name", "Date", "Year"]
    )
    st.dataframe(df)
else:
    st.info("No student records found")
if st.button("Back"):
                st.switch_page("pages/functionality.py")
