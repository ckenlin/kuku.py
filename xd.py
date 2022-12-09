import streamlit as st
from PIL import Image
audio_file = open("一心兄弟.mp3", "rb")
st.audio(audio_file.read()) 
