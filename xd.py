import streamlit as st
from PIL import Image
audio_file = open("一心兄弟.mp3", "rb")
st.audio(audio_file.read()) 

col1, col2, col3 = st.columns(3)

with col1:
   st.header("A cat")
   st.image("https://static.streamlit.io/examples/cat.jpg")

with col2:
   st.header("A dog")
   st.image("https://static.streamlit.io/examples/dog.jpg")

with col3:
   st.header("An owl")
   st.audio(audio_file.read())
   #st.audio("https://drive.google.com/file/d/1WTw30Gu2WqBRYcbrDTQ3cno6qvlh6ykO/view?usp=share_link")
