import streamlit as st
import pandas as pd

st.markdown("# Page 2")
st.sidebar.markdown("# Page 2")

df = pd.read_csv("data/EuropeanSanctions.csv")

st.dataframe(df)