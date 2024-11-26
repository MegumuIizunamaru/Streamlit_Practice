import streamlit as st
import pandas as pd

genshin = pd.read_csv("genshin.csv",encoding='ISO-8859-1')

st.title("Genshin Impact Data Analysis")

DF = genshin.groupby('vision').agg({'hp_1_20':'mean'})

st.title("Genshin Dashboard")

st.subheader("Genshin Dashboard")

st.bar_chart(DF["hp_1_20"])
# D:\DataScience\genshin.py
