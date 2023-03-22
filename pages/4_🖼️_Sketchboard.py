import streamlit as st
from PIL import Image
from streamlit_drawable_canvas import st_canvas

# Set up the page layout
st.set_page_config(page_title="Draw on Image", page_icon=":pencil2:")
st.title("Draw on Image")

# Get the URL of the image from the user
img_url = "https://cdn.discordapp.com/attachments/738557702330122283/1078717809225379860/Screenshot_7.png"

# Download the image and display it
if img_url:
    try:
        image = Image.open(img_url)
        st.image(image, caption="Original Image", use_column_width=True)
    except:
        st.error("Error loading image. Please check the URL and try again.")

    # Set up the drawing canvas
    canvas_result = st_canvas(
        fill_color="rgba(255, 165, 0, 0.3)",  # Fixed fill color with some opacity
        stroke_width=3,
        stroke_color="black",
        background_image=image,
        height=300,
        width=300,
        drawing_mode="freedraw",
        key="canvas",
    )

    # Display the result image with the drawing
    if canvas_result.image_data is not None:
        st.image(canvas_result.image_data, caption="Modified Image", use_column_width=True)
