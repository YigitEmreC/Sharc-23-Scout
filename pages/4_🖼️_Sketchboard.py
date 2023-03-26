import streamlit as st
import numpy as np
from PIL import Image
import io
import requests

# Define function to convert image to RGBA format
def image_to_rgba(image):
    if image.mode == 'RGB':
        r, g, b = image.split()
        a = Image.new('L', image.size, 255)
        image = Image.merge('RGBA', (r, g, b, a))
    return image

# Load image from URL
url = 'https://cdn.discordapp.com/attachments/738557702330122283/1078717809225379860/Screenshot_7.png'
response = requests.get(url)
image = Image.open(io.BytesIO(response.content))
image = image_to_rgba(image)

# Create a canvas to draw on
canvas_size = st.sidebar.slider('Canvas size', 200, 800, 400)
canvas = st_canvas(
    fill_color='rgba(255, 255, 255, 0.3)',  # Set background color to transparent
    stroke_width=5,
    stroke_color='red',
    background_image=image,
    width=canvas_size,
    height=canvas_size,
    drawing_mode='freedraw',
    key='canvas')

# Convert the canvas to an image
if canvas.image_data is not None:
    img = Image.fromarray(canvas.image_data.astype('uint8'), 'RGBA')
    img.save('drawing.png')
    st.image(img, caption='Your drawing', use_column_width=True)

