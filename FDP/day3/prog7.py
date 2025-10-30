import streamlit as st
import pandas as pd
# page title
st.title("Student Performance Dashboard")
# st.dataframe
st.subheader("Marks Data")
data = {
"Test 1": [65, 70, 80, 75, 90],
"Test 2": [68, 72, 78, 80, 92],
"Test 3": [70, 75, 82, 85, 95]      
}
# display dataframe
st.dataframe(pd.DataFrame(data))  
st.table()
st.subheader("Performance Trend (Line Chart)")
summary = df.describe()
st.table(summary)

