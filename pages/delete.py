import streamlit as st
import db as d
import pandas as pd
st.subheader("❌ Delete Student")

roll = st.text_input("Enter Roll No")
data = d.view_a()
if data:
    df = pd.DataFrame(
        data,
        columns=[ "Name", "Roll", "Department", "Year"]
    )
    st.dataframe(df)
else:
    st.info("No student records found")
col1,col2=st.columns(2)
with col1:
    if st.button("Delete"):
        d.delete(roll)
        st.rerun()
with col2:
    if st.button("Back"):
                    st.switch_page("pages/functionality.py")

        