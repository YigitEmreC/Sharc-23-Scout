import streamlit as st
from streamlit_extras.no_default_selectbox import selectbox
from streamlit_image_coordinates import streamlit_image_coordinates
from PIL import Image
import time
import gspread_asyncio
from oauth2client.service_account import ServiceAccountCredentials
import asyncio
import urllib.request





# Function to make sure that the app is connected to internet to prevent errors.
def check_internet():
    try:
        urllib.request.urlopen('http://google.com')
        return True
    except:
        return False
    
    
    
                

# integer values assigned for future use.
parkPoints = 0
aparkPoints = 0
st.sidebar.image("https://media.discordapp.net/attachments/1078818849182457906/1080141834833113189/QyLctghW_400x400-removebg-preview.png")




scope = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]

creds = ServiceAccountCredentials.from_json_keyfile_name('./pages/scoutingapi23.json', scope)

async def main():
    agcm = gspread_asyncio.AsyncioGspreadClientManager(creds)
    agc = await agcm.authorize()
    spreadsheet = await agc.open('scouting')
    sheet = await spreadsheet.get_worksheet(0)  # assume the sheet is the first one

    async def write_sheet_429(data):
        while True:
            try:
                await sheet.append_row(data)
                break  # Exit the loop if the process is successful
            except gspread.exceptions.APIError as e:
                if e.response.status_code == 429:
                    # If there is a 429 error, wait for a certain amount of time before retrying
                    await asyncio.sleep(60)  # Put the app to sleep for 60 seconds since the quota resets per minute
                else:
                    # If it's not a 429 error, raise the exception
                    raise e

 
asyncio.run(main())
# possible cargo locations.
numberInput = ['0','1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38']



# custom css to delete streamlit elements such as footer and header.
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
            
st.markdown(hide_st_style, unsafe_allow_html=True)

# team

st.title("Scouting")

# Data form and inputs.
with st.expander("Pre-Match Menu"):


    name = st.text_input('Scouter Name')

    level = st.radio(
    "Match Level",
    ( 'Quals', 'Practice Match', 'Eighth-Final', 'Quarter-Final', 'Semi-Final', 'Final'))

    match = st.text_input('Match')

    team = selectbox("Which side are you scouting", ['Red', 'Blue'])

    robot = st.radio(
    "Which one is your assigned robot?",
    ('Robot 1', 'Robot 2', 'Robot 3'))

    teamTag = st.number_input('Team Tag', min_value=0, max_value=10000, step=1)

    teamName = st.text_input(' Team Name ')

with st.expander("Autonomous"):


    # Spawn Point Seçme
    st.subheader('Select the Starting Point')


    xyz = streamlit_image_coordinates("https://media.discordapp.net/attachments/738557702330122283/1078717809225379860/Screenshot_7.png", width=700)

    st.write('The selected point is : ') 
    st.text(xyz)

    spawnPoint = st.text_input('Write the x and y in "x y" format')


    st.subheader('Cargo Placement')

    acol1, acol2 = st.columns(2)

    with acol1:

     cargoAuto = st.multiselect(
    'Auto Cargo Placement',
    numberInput)
   

    with acol2:
        
        st.image('https://media.discordapp.net/attachments/738557702330122283/1078714733835866242/Screenshot_2.png', caption='Purple = Cube and Yellow = Cone')

    st.subheader('Autonomous Attributes')

    c = st.checkbox('Crossed Cable',)
    if c:
        cable = 'yes'
    else:
        cable = 'No'


    b = st.checkbox('Crossed Charging Station',)
    if b:
        chargeStation = 'yes'
    else:
        chargeStation = 'No'

    mobility = selectbox('Was it mobile?', ['Extremely Mobile', 'Mobile Enough', 'Not Enough'])
    
    docked = st.radio(
    "Did it docked?",
        ('Parked', 'Docked ','Engaged',"Didn't Attempted",'Failed 😥'))

with st.expander("Manual"):


    st.subheader('Cargo Placement')

    mcol1, mcol2 = st.columns(2)

    with mcol1:

     leftNumbers = [x for x in numberInput if x not in cargoAuto] 
    
    cargoManual = st.multiselect(
    'Manual Cargo Placement',
    leftNumbers)
   
    with mcol2:
        
        st.image('https://media.discordapp.net/attachments/738557702330122283/1078714733835866242/Screenshot_2.png', caption='Purple = Cube and Yellow = Cone')

    st.subheader('Manual Attributes')

    feeder = st.number_input('Fed another bot', min_value=0, max_value=15, value=0, step=1)

    d = st.checkbox('Has been defended')
    if d:
        defended = 'yes'
    else: 
        defended = 'no'

    f = st.checkbox('Got fed by another bot')
    if f:
        fed = "yes"
    else: 
        fed = 'no'

    pickUp = st.radio(
    "Picked Up:",
    ('Cones and Cubes', 'Cones',  'Cubes', "Didn't attempted"))

with st.expander("Finale"):

    st.markdown('Use the timer to calculate the time taken until the robot parked ')

    tcol1, tcol2 = st.columns(2)

    with tcol1:
        st.text("Timer")
        st.text('')

        dockingTime = st.number_input('', min_value=0, max_value=100, step=1, label_visibility="collapsed")

    with tcol2:
        def count_down(ts):
             with st.empty():
                 while ts:
                      mins, secs = divmod(ts,60)
                      time_now = '{:02d}'.format(secs)
                      st.subheader(time_now)
                      time.sleep(1)
                      ts += 1

        def main():
            time_in_minutes = 1
            time_in_seconds = time_in_minutes*60
            if st.button("START"):
                count_down(time_in_seconds)

        if __name__ =='__main__':
            main()
            
           

    parkState = st.radio(
        "Parking State:",
        ('Parked', 'Docked ','Engaged',"Didn't Attempt",'Failed 😥'))

    robotsParked = st.number_input('Total Number of Robots that Docked or Engaged :', min_value=0, max_value=3, value=0, step=1)

with st.expander("After-Match"):

    skillLevel = selectbox('How talented was the driver?', ('Extremely Bad', 'Bad', 'Enough', 'More than enough', 'Good', 'Extremely Good', 'Karadayı'))

    linkScored = st.number_input('Scored Links :', min_value=0, max_value=15, value=0, step=1)

    skillDefenseLevel = selectbox('How  was the defense?', ("Didn't played defense", 'Extremely Bad', 'Bad', 'Enough', 'More than enough', 'Good', 'Extremely Good', 'Kalede Ersin'))

    t = st.checkbox('Has swerve')
    if t:
        swerve = "yes"
    else: 
        swerve = 'no'

    speed = st.slider('How fast was the robot', 0, 10, 5)

    s = st.checkbox('Nearly dropped or literally dropped')
    if s:
        slippy = 'yes'
    else: 
        slippy = 'no'

    dr = st.checkbox('Dropped Cones or Cubes more than 5 times')
    if dr:
        drop = 'yes'
    else: 
        drop = 'no'

    comment = st.text_area('Any comments on the robot or the driver performance')

with st.expander("Results"):
            
    intAutoCargo = []  

    for cargo in cargoAuto:
        intAutoCargo.append(int(cargo))
  
# cargo point calculator to calculate the total point comes from auto cargo input
            
    def autoPointCalculator(intAutoCargo):
        autoTotalPoint = 0
        for num in intAutoCargo:
            if 1 <= num <= 9:
                autoTotalPoint += 6
            elif 10 <= num <= 18:
                autoTotalPoint += 4
            elif 18 <= num <= 38:
                autoTotalPoint += 3
        return autoTotalPoint

    manualAutoCargo = []  
    
    # cargo point calculator to calculate the total point comes from manual cargo input


    for cargo in cargoManual:
        manualAutoCargo.append(int(cargo))
            
    def manualPointCalculator(manualAutoCargo):
        manualTotalPoint = 0
        for num in manualAutoCargo:
            if 1 <= num <= 9:
                manualTotalPoint += 5
            elif 10 <= num <= 18:
                manualTotalPoint += 3
            elif 18 <= num <= 38:
                manualTotalPoint += 2
            
        return manualTotalPoint
    
    # point calculator for autonomous and manual state
    
    if parkState == "Parked":
        parkPoints += 2
    elif parkState == "Docked":
        parkPoints += 6
    elif parkState =="Engaged":
        parkPoints += 10

    if docked == "Engaged":
        aparkPoints += 12
    elif docked == "Docked":
        aparkPoints += 8
    
    # total point result calculator for auto, manual and general scores
 
    autoTotalPointResult = aparkPoints + autoPointCalculator(intAutoCargo)

    st.text(f"Total points made during the autonomous state: {autoTotalPointResult}")
    
    linkPoint = linkScored * 5
     
    manualTotalPointResult = parkPoints + manualPointCalculator(manualAutoCargo) + linkPoint

    st.text(f"Total points made during the teleop state: {manualTotalPointResult}")

    totalPointOverall = autoTotalPointResult + manualTotalPointResult
            
    st.subheader(f"Total points made in both autonomous and manual: {totalPointOverall}")

if st.button('Submit'):
    
    # checks the internet connection when the submit button is activated
        
    if check_internet():
            row = [name, level, match, team, robot, teamTag, teamName, autoTotalPointResult, manualTotalPointResult, totalPointOverall,''.join(spawnPoint), '-'.join(cargoAuto), cable, chargeStation, mobility, docked, '-'.join(cargoManual), feeder, defended, fed, pickUp, dockingTime, parkState, skillLevel, 
                   linkScored, skillDefenseLevel, swerve, speed, slippy, drop, comment]
            writeSheet429(row) # error 429 checker
            st.success('The data is successfully sent to the sheet ', icon="✅")
            st.balloons()
    else:
            st.error('Device is not connected to net, try again', icon="🚨")
            st.stop()


