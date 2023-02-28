import streamlit as st
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials



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

st.sidebar.image("https://media.discordapp.net/attachments/1078818849182457906/1080141834833113189/QyLctghW_400x400-removebg-preview.png")


scope = [
'https://www.googleapis.com/auth/spreadsheets',
'https://www.googleapis.com/auth/drive'
]

# Load the credentials from the JSON file
creds = ServiceAccountCredentials.from_json_keyfile_name('./pages/scoutingapi23.json', scope)

# Authorize your application to access the Google Sheets API
client = gspread.authorize(creds)

# Define the Google Sheet URL
sheet_url = 'https://docs.google.com/spreadsheets/d/1YANIA50_sZWRVGueXH3d2HYuqPAw9gVZJ9lIRb9P1jI/edit#gid=0'

# Open the Google Sheet by its URL
sheet = client.open_by_url(sheet_url).sheet1

# Read the data from the Google Sheet into a Pandas DataFrame
data = pd.DataFrame(sheet.get_all_records())

# Create the Streamlit app

st.title('Scouting')

    # Display the data in a table
st.write(data)