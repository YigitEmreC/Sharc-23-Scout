import pandas as pd
from PIL import Image
import streamlit as st
from streamlit_drawable_canvas import st_canvas
import os


hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """



st.set_page_config(

page_title = "Sketch",
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

st.sidebar.image("https://media.discordapp.net/attachments/1078818849182457906/1080141834833113189/QyLctghW_400x400-removebg-preview.png")


st.markdown(':blue[**Simple Sketch App for Charged UP Field**]')


drawing_mode = st.sidebar.selectbox(
    "Drawing tool:", ("point", "freedraw", "line", "rect", "circle", "transform")
)

stroke_width = st.sidebar.slider("Stroke width: ", 1, 25, 3)
if drawing_mode == 'point':
    point_display_radius = st.sidebar.slider("Point display radius: ", 1, 25, 3)
stroke_color = st.sidebar.color_picker("Stroke color hex: ")

bg_image = None

for root, dirs, files in os.walk("/"):
    for file in files:
        if file == "field.jpg":
            # Assign the file path to the variable
            bg_image = os.path.join(root, file)
            break

    if bg_image:
        break

realtime_update = st.sidebar.checkbox("Update in realtime", True)

    

canvas_result = st_canvas(
    fill_color="rgba(255, 165, 0, 0.3)",  # Fixed fill color with some opacity
    stroke_width=stroke_width,
    stroke_color=stroke_color,
    background_image=Image.open(bg_image),
    update_streamlit=realtime_update,
    height=400,
    drawing_mode=drawing_mode,
    point_display_radius=point_display_radius if drawing_mode == 'point' else 0,
    key="canvas",
)


