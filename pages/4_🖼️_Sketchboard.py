import streamlit as st
from PIL import Image, ImageDraw
import requests
from io import BytesIO

# Set up the canvas
CANVAS_WIDTH = 500
CANVAS_HEIGHT = 500
BACKGROUND_COLOR = (255, 255, 255, 255)

# Set up the image
IMAGE_URL = "https://media.discordapp.net/attachments/1078818849182457906/1080141834833113189/QyLctghW_400x400-removebg-preview.png"
response = requests.get(IMAGE_URL)
image = Image.open(BytesIO(response.content))

# Draw on the image
def draw_on_image(image, drawings):
    draw = ImageDraw.Draw(image)
    for drawing in drawings:
        draw.line(drawing["points"], fill=drawing["color"], width=drawing["width"])

DEFAULT_COLOR = "#000000"
DEFAULT_COLOR_RGBA = (0, 0, 0, 255)
DEFAULT_WIDTH = 5

def rgba_to_hex(rgba):
    r, g, b, a = rgba
    return "#{:02x}{:02x}{:02x}".format(r, g, b)

# Set up the sidebar
st.sidebar.title("Drawing Options")
color_rgba = st.sidebar.color_picker("Color", DEFAULT_COLOR_RGBA)
color = rgba_to_hex(color_rgba)
width = st.sidebar.slider("Width", 1, 20, DEFAULT_WIDTH)


# Set up the canvas
canvas = st.image(image.resize((CANVAS_WIDTH, CANVAS_HEIGHT)), caption="Draw on the image", width=CANVAS_WIDTH, height=CANVAS_HEIGHT, use_column_width=False, format="PNG")

# Listen for drawing events
drawing_mode = st.checkbox("Enable drawing mode", value=False)
if drawing_mode:
    st.write("Click and drag to draw")
    drawing = False
    with canvas:
        while drawing_mode:
            event = st.beta_streamlit_report_thread.get_report_ctx().session_events.get_current().if_type(st.EventData)
            if event:
                if event["event"] == "mousedown":
                    drawing = True
                    drawings.append({"points": [event["x"], event["y"]], "color": color, "width": width})
                elif event["event"] == "mousemove":
                    if drawing:
                        drawings[-1]["points"].extend([event["x"], event["y"]])
                        draw_on_image(image, drawings)
                        canvas.image(image.resize((CANVAS_WIDTH, CANVAS_HEIGHT)).convert("RGBA"), width=CANVAS_WIDTH, height=CANVAS_HEIGHT, use_column_width=False, format="PNG")
                elif event["event"] == "mouseup":
                    drawing = False

# Reset the drawings
if st.button("Reset drawings"):
    drawings = []
    image = Image.open(BytesIO(response.content))
    canvas.image(image.resize((CANVAS_WIDTH, CANVAS_HEIGHT)).convert("RGBA"), width=CANVAS_WIDTH, height=CANVAS_HEIGHT, use_column_width=False, format="PNG")
