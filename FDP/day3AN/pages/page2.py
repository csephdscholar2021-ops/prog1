import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
st.title("student performance visualizer")
st.write("upload csv file ")
#uploaded_file = st.file_uploader("student-data.csv ", type=["csv"])
uploaded_file = "data/student-data.csv"
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.dataframe(df)
    st.data_editor(df.tail(10)) 
    st.subheader("tail")
    st.data_editor(df.head(10))
    st.subheader("head")
    st.write(df.describe())
    st.info(df)
    st.snow()
