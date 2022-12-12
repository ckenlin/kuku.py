import streamlit as st
from PIL import Image
audio_file = open("一心兄弟.mp3", "rb")
st.audio(audio_file.read()) 




option = st.selectbox(
    'How would you like to be contacted?',
    ('1', '2', '3'))
st.write('You selected:', option)
if option="3":
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
      
      
      
      
      
      
      
      
      
      
      
      
   
   
#st.button(label, key=None, help=None, on_click=None, args=None, kwargs=None, *, type="secondary", disabled=False)

st.title("maling a button")
#result = st.button("Say hello")
if st.button('Say hello'):
    st.write('Why hello there')
else:
    st.write('Goodbye')
   
tab1, tab2 = st.tabs(["📈 Chart", "🗃 Data"])
data = np.random.randn(10, 1)

tab1.subheader("A tab with a chart")
tab1.line_chart(data)

tab2.subheader("A tab with the data")
tab2.write(data)





      




