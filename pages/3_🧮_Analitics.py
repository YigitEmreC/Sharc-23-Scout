import streamlit as st
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import altair as alt

st.set_option('deprecation.showfileUploaderEncoding', False)
st.set_option('browser.showFullScreenButton', False)
st.set_option('browser.showHelp', False)
st.set_option('browser.showLogs', False)
st.set_option('browser.showProfiler', False)
st.set_option('browser.showStaleElementReference', False)

# For determining the page attributes such as its title that will appear on the winfow and icon which will also appear in the window.
st.set_page_config(
page_title = "Analitics",
page_icon ="https://media.licdn.com/dms/image/C4E03AQH4UTTZc2oWaQ/profile-displayphoto-shrink_800_800/0/1570104233605?e=2147483647&v=beta&t=qSvofj0Q9GdBP2StB4aV0EEkqL-iUzZ30TE7G2Lm3DE",
)

# To hide the default header, footer and dropdown menu that comes default with the streamlit libary.
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
          footer {visibility: hidden;}
         header {visibility: hidden;}
          </style>
         """

st.markdown(hide_st_style, unsafe_allow_html=True)

# Logo on the sidebar
st.sidebar.image("https://media.discordapp.net/attachments/1078818849182457906/1080141834833113189/QyLctghW_400x400-removebg-preview.png")


scope = [
'https://www.googleapis.com/auth/spreadsheets',
'https://www.googleapis.com/auth/drive'
]

# Uses the json file to find the required information to open the service account. 
creds = ServiceAccountCredentials.from_json_keyfile_name('./pages/scoutingapi23.json', scope)

# Uses the information that is defined as creds to open the client account of the service account.
# Do not forget to authorize the service account on the google sheet to so that the service account can open the google sheet
client = gspread.authorize(creds)

# Locate the spessific google sheet that you will write the data on.
sheet_url = 'https://docs.google.com/spreadsheets/d/1YANIA50_sZWRVGueXH3d2HYuqPAw9gVZJ9lIRb9P1jI/edit#gid=0'

# Opens the google sheet based on the url defined on the sheet_url; If there is more than one pages on the google sheet you have to choose which one you want to write on such as sheet1
sheet = client.open_by_url(sheet_url).sheet1

# Read the data from the google sheet and convert it into a panda data table
data = pd.DataFrame(sheet.get_all_records())

# Simple seach bar for getting the wanted input from the user, this input will limit the data with only the rows that the inputed variable.
search = st.sidebar.text_input('Search')
if search:
    data = data[data.astype(str).apply(lambda x: x.str.contains(search, case=False)).any(axis=1)]

# A selectbox for selecting which variable you want to create a graph about.
sort_variable = st.sidebar.selectbox('Sort By', data.columns)

# Checkbox for descending or ascending order
sort_order = st.sidebar.checkbox('Low to High', value=True)

# Sort the new data based on the perimeters the user gave
data = data.sort_values(by=sort_variable, ascending=not sort_order)

# Display the data in pandas framework.
st.write(data)

# Create a simple chart for showing the visualized data.
selected_data = st.multiselect('Select Data', data[sort_variable])
if selected_data:
    chart_data = data[data[sort_variable].isin(selected_data)]
    chart = alt.Chart(chart_data).mark_bar().encode(
        alt.X(sort_variable),
        alt.Y('count()')
    ).interactive()
    st.altair_chart(chart, use_container_width=True)
