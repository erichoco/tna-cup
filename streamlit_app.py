import streamlit as st
import pandas as pd

SHEET_ID = '1P4qLMUxjbXFY2-FtoIQNhSdcogLgoE0aM1yjvaQbt3Y'
SHEET_NAME = 'Leaderboard'
url = f'https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet={SHEET_NAME}'
df = pd.read_csv(url)


st.title("TNA Cup Test")
st.dataframe(df)
# st.markdown(df.head())