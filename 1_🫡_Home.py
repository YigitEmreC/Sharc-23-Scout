import streamlit as st
import plotly.graph_objects as go


# streamlit run 1_🫡_Home.py

# Basics ------------------
st.set_page_config(

page_title = "Home",
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



# Add some space between the logo and the content
st.sidebar.image("https://media.discordapp.net/attachments/1078818849182457906/1080141834833113189/QyLctghW_400x400-removebg-preview.png")

#---------------------------------------------------


st.title("Welcome!")

st.write('Welcome to our new scouting app for 2023 Charged Up. In this page you can find the necesseary information for the new game and more information about our scouting system.')

st.image('https://thumbs.gfycat.com/AlertNastyGrunion-size_restricted.gif')

st.text('       ')
st.text('       ')


st.subheader('Information about Charged Up')

st.video('https://www.youtube.com/watch?v=0zpflsYc4PA')



    
