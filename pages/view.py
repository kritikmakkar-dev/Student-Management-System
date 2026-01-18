import streamlit as st
import db as d
import pandas as pd
st.subheader("📋 Student List")

search = st.text_input("Search by Roll No")
data = d.view_a()
if search:
    data = d.view(search)

if data:
    df = pd.DataFrame(
        data,
        columns=[ "Name", "Roll", "Department", "Year"]
    )
    st.dataframe(df)
else:
    st.info("No student records found")
if st.button("Back"):
                st.switch_page("pages/functionality.py")