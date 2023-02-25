import streamlit as st
from streamlit_image_coordinates import streamlit_image_coordinates
import time



st.set_page_config(

page_title = "Analitics",
page_icon ="https://media.licdn.com/dms/image/C4E03AQH4UTTZc2oWaQ/profile-displayphoto-shrink_800_800/0/1570104233605?e=2147483647&v=beta&t=qSvofj0Q9GdBP2StB4aV0EEkqL-iUzZ30TE7G2Lm3DE",
)

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
          footer {visibility: hidden;}
         header {visibility: hidden;}
          </style>
         """

st.markdown(hide_st_style, unsafe_allow_html=True)
