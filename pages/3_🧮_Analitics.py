import streamlit as st
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import altair as alt


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

# Create a search bar for filtering the data
search = st.sidebar.text_input('Search')
if search:
    data = data[data.astype(str).apply(lambda x: x.str.contains(search, case=False)).any(axis=1)]

# Create a dropdown menu for selecting a variable to sort the data by
sort_variable = st.sidebar.selectbox('Sort By', data.columns)

# Create a checkbox for selecting the sort order
sort_order = st.sidebar.checkbox('Descending', value=True)

# Sort the data based on the selected variable and sort order
data = data.sort_values(by=sort_variable, ascending=not sort_order)

# Display the sorted and filtered data in a table
st.write(data)

# Create a chart based on the selected data
selected_data = st.multiselect('Select Data', data[sort_variable])
if selected_data:
    chart_data = data[data[sort_variable].isin(selected_data)]
    chart = alt.Chart(chart_data).mark_bar().encode(
        alt.X(sort_variable),
        alt.Y('count()')
    ).interactive()
    st.altair_chart(chart, use_container_width=True)
