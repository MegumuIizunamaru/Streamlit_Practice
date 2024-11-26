import streamlit as st
import pandas as pd

genshin = pd.read_csv("genshin.csv",encoding='ISO-8859-1')

st.title("Genshin Impact Data Analysis")

DF = genshin.groupby('vision').agg({'hp_1_20':'mean'})
DF = DF.reset_index()

st.title("Genshin Dashboard")

filtered_data = DF['vision']

st.subheader("Genshin Dashboard")

st.write(filtered_data)

st.bar_chart(DF)
# D:\DataScience\genshin.py
