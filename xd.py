import streamlit as st
from PIL import Image
#audio_file = open("一心兄弟.mp3", "rb")
#st.audio(audio_file.read()) 

################################

add_selectbox = st.sidebar.selectbox(
    "歌手",
    ("林", "ALIN")
)

################################

with st.sidebar:
    add_radio = st.radio(
        "歌手",
        ("林", "陳")
    )
    
################################
       
if add_selectbox == '林':     
    st.header("林")
    name={'一心兄弟','cd','dd'}        #放入歌名
    option= st.selectbox( '請選擇想聽的音樂',name)
    audio_file = open(option+'.mp3', "rb")
    st.audio(audio_file.read())   

################################
    
if add_selectbox == 'ALIN':     
    st.header("林")
    name={'摯友'}        #放入歌名
    option= st.selectbox( '請選擇想聽的音樂',name)
    audio_file = open(option+'.mp3', "rb")
    st.audio(audio_file.read())
    
################################

    
    

option = st.selectbox(
    'How would you like to be contacted?',
    ('1', '2', '3'), key="disabled")
st.write('You selected:', option)
if option == '3':
   audio_file = open("一心兄弟.mp3", "rb")
   st.audio(audio_file.read()) 
         





#https://docs.streamlit.io/library/api-reference/widgets/st.selectbox














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





      




