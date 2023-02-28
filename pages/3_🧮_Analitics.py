import streamlit as st
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Define the scope of access to the Google Sheets API
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

st.title('scouting')

    # Display the data in a table
st.write(data)