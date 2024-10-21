import streamlit as st
import pandas as pd

SHEET_ID = '1P4qLMUxjbXFY2-FtoIQNhSdcogLgoE0aM1yjvaQbt3Y'
SHEET_NAME = 'Leaderboard'
url = f'https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet={SHEET_NAME}'
df = pd.read_csv(url)


# def main():
st.title("TNA Cup")
with st.container():
    st.video("https://www.youtube.com/live/kp_W_j-YCzg?si=hspCSsW3L-9tg_ZN")
    
col1, col2= st.columns(2)
with col1:
    st.header("最新對戰")

with col2:
    st.header("積分榜")
    st.dataframe(df.head().iloc[:, 1:12])


# def roster():
#     st.title("玩家介紹")    
    
# pg = st.navigation([st.Page(main), st.Page(roster)])
# pg.run()