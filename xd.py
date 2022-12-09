import streamlit as st
from PIL import Image
audio_file = open("一心兄弟.mp3", "rb")
st.audio(audio_file.read()) 









#################################分塊
col1, col2, col3 = st.columns(3)

with col1:
   st.header("A cat")
   st.image("https://static.streamlit.io/examples/cat.jpg")

with col2:
   st.header("A dog")
   st.audio("https://drive.google.com/file/d/1WTw30Gu2WqBRYcbrDTQ3cno6qvlh6ykO/view?usp=share_link")

with col3:
   st.header("An owl")
   audio_file = open("一心兄弟.mp3", "rb")
   st.audio(audio_file.read())
   #st.audio("https://drive.google.com/file/d/1WTw30Gu2WqBRYcbrDTQ3cno6qvlh6ykO/view?usp=share_link")

   
   
   
########################################sidebar
   
   
add_selectbox = st.sidebar.selectbox(
    "要不要吃哈密瓜?",
    ("要", "喔", "哈密瓜")
)

with st.sidebar:
    add_radio = st.radio(
        "Choose a shipping method",
        ("Standard (5-15 days)", "Express (2-5 days)")
    )
