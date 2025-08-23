import streamlit as st
import pandas as pd
import numpy as np

st.title("WELCOME TO MY WEBAPP")
name=st.text_input("Enter your name")
if name:
    st.write(f"Hello,{name}")
age=st.slider("Select your age",0,100,18)
st.write(f"Your age is {age}")
options=['CSE','ECE','EEE']
choice=st.selectbox("Choose your branch",options)
st.write(f"Acha!{choice} wala hai tu")
file=st.file_uploader("Choose a CSV file",type="CSV")
if file is not None:
    df=pd.read_csv(file)
    st.write(df)



