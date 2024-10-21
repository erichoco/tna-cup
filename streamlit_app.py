import streamlit as st
import pandas as pd

SHEET_ID = '1P4qLMUxjbXFY2-FtoIQNhSdcogLgoE0aM1yjvaQbt3Y'
SHEET_NAME = 'Leaderboard'
LIVE_ID = "kp_W_j-YCzg"

url = f'https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet={SHEET_NAME}'
df = pd.read_csv(url)


st.title("TNA Cup")
    
with st.container():
    st.header("積分榜")
    st.dataframe(df.head().iloc[:, 1:12])

col1, col2 = st.columns(2)
with col1:
    st.header("對戰紀錄")

with col2:
    st.header("直播連結")
    preview = f"https://img.youtube.com/vi/{LIVE_ID}/0.jpg"
    livestream_url = f"https://www.youtube.com/live/{LIVE_ID}"
    st.markdown(f"[![live]({preview})]({livestream_url})")

    
    

# def main():

# def roster():
#     st.title("玩家介紹")    
    
# pg = st.navigation([st.Page(main), st.Page(roster)])
# pg.run()