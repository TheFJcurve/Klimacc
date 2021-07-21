import mysql.connector as mysql
import matplotlib.pyplot as plt
from tkinter import *
import requests
import webbrowser
from PIL import Image, ImageTk

def clickedlocation():
    """When the user inputs location, the location is stored and the tab is closed"""
    global user_location
    user_location = location_user.get()
    user_location = str(user_location).capitalize()
    if user_location == "":
        pass
    else:
        get_weather()


def get_weather():
    """According to the user's inputed location, this function interacts with the API to get info of that place"""
    weather_key = '15c0fbbd005a78217416150b445c720e'
    url = 'https://api.openweathermap.org/data/2.5/forecast'
    params = {'APPID': weather_key, 'q': user_location, 'units': 'Metric'}
    response = requests.get(url, params=params)
    weather = response.json()
    format_response(weather)


def format_response(API_data):
    """Uses the API data and takes that data in variables which are stored in a list"""
    for weather in API_data['list']:
        try:
            date = weather['dt_txt']
            temp = weather['main']['temp']
            pressure = weather['main']['pressure']
            humidity = weather['main']['humidity']
            windspeed = weather['wind']['speed'] * 18 // 5
            visibility = weather['visibility']
            dates.append(date)
            temps.append(temp)
            pressures.append(pressure)
            windspeeds.append(windspeed)
            humidities.append(humidity)
            visibilities.append(visibility)
        except:
            print('There was a problem retrieving that information')
    root.destroy()


def tablefunctions(function):
    """It is the primary mysql connector and will give the output in a variable"""
    mycursor = mydb.cursor(buffered=True)
    mycursor.execute(function)
    variable = mycursor
    mydb.close()
    return variable


def mysqlmaking():
    """Creates the databases and the table"""
    global mydb
    mydb = mysql.connect(host="localhost", user="root", password="Sargun05", db="test", port=3307)
    mycur = mydb.cursor(buffered=True)
    mycur.execute("create database if not exists klimaccdata;")
    mycur.execute("use klimaccdata;")
    mycur.execute(
        "create table if not exists renewables(name varchar(20) primary key, temp_Degree_ int, "
        "humidity_percentage_ int, wind int);")
    mycur.execute(
        "insert into renewables values('solar energy', NULL, NULL, NULL),('biomass energy', NULL, 50, "
        "NULL),('wind energy', 15, NULL, 12),('geothermal energy', NULL, NULL, NULL);")
    mycur.close()


def compatiblerenewables_finding(renewable):
    """Calculates is the given renewable will work for the place"""
    try:
        if (renewable[0].lower() == 'wind energy' and (-20 < sum(temps) / len(temps) < 50)) or \
                (renewable[1] is None):
            if (renewable[0].lower() == 'biomass energy' and (50 <= sum(humidities) / len(humidities) <= 80)) or \
                    (renewable[2] is None):
                if (renewable[3] is None) or (sum(windspeeds) // len(windspeeds) >= renewable[3]):
                    return True
    except:
        return "Error in the system"
    return False


def disasterprediction():
    """Tries to predict some disasters based on the given data of the user location"""
    disaster_list = list()
    count_times = 0
    hightemp = False
    # for checking for heat waves
    for temperture in temps:
        if temperture >= sum(temps) / len(temps) + 8:
            hightemp = True
            count_times += 1
    if count_times >= 3:
        disaster_list.append('Possibility of a Heat Wave')
    # for checking for storms
    for pressure in pressures:
        if pressure <= 950:
            disaster_list.append('There is a low pressure, so there is a possibility of a storm.')
    # for checking for wildfires
    if hightemp:
        if humidities[-1] <= 10:
            disaster_list.append('High risk of forest fire')
        elif humidities[-1] > 10:
            disaster_list.append('Low risk of forest fire')
    return ','.join(disaster_list)


def graphs():
    plt.figure(figsize=(19, 19))
    plt.plot(temps, dates, 'r--', label='Temperatures', )
    plt.title(f'{user_location} Temperatures')
    plt.legend()
    plt.xlabel('Temperature (Celsius)')
    plt.show()

    plt.figure(figsize=(19, 19))
    plt.plot(humidities, dates, 'g--', label='Humidity', )
    plt.title(f'{user_location} Percentages')
    plt.legend()
    plt.xlabel('Percentages(%)')
    plt.show()

    plt.figure(figsize=(19, 19))
    plt.plot(windspeeds, dates, 'g--', label='Windspeed', )
    plt.title(f'{user_location} Wind Speed')
    plt.legend()
    plt.xlabel('Wind Speed (km/h)')
    plt.show()

    plt.figure(figsize=(19, 19))
    plt.plot(pressures, dates, 'g--', label='Pressure', )
    plt.title(f'{user_location} Pressure')
    plt.legend()
    plt.xlabel('Pressure (mb)')
    plt.show()


def infopage():
    """Opens up the wikipedia website for the renewable energy"""
    for renewable in compatiblerenewable:
        webbrowser.open(f"https://en.wikipedia.org/wiki/{renewable}")


"""allocation of data from the table locations. Note: this is initialising the values so that they can be
inputted later on when user gives their location"""
dates, temps, pressures, windspeeds, humidities, visibilities = [], [], [], [], [], []

"""Creating the page for user to input his/her location"""
root = Tk()
root.geometry("600x600")
root.minsize(600, 600)
root.maxsize(600, 600)
root.title("User Location")
canvas = Canvas(root, height=600, width=600, bg='#fb5b8d')
canvas.pack()

frame = Frame(canvas, bg='#000834', bd=10)
frame.place(relx=0.5, rely=0.2, relwidth=0.8, relheight=0.6, anchor='n')

heading = Label(frame, text="Enter Your Location", font=("Helvetica Bold", 20), fg="white", bg="#000834")
heading.place(relx=0.23, rely=0.08)

location_user = Entry(frame, justify="center")
location_user.place(relx=0.2, rely=0.4, relheight=0.08, relwidth=0.6)

button = Button(frame, text="Submit", font = ('Ubuntu Light', 13, 'bold'), fg = '#000834', command=clickedlocation, bg="#fb5b8d")
button.place(relx=0.41, rely=0.7, relheight=0.1, relwidth=0.2)

root.mainloop()

"""creating the database using the function and extracting values"""
mysqlmaking()
total_renewables = tablefunctions('select * from renewables;')

"""finding renewable energy sources compatible to the current user location"""
compatiblerenewable = []
for renewable_info in total_renewables:
    if compatiblerenewables_finding(renewable_info):
        compatiblerenewable.append(renewable_info[0])

"""Taking conditions to find for some disaster indication"""
disaster_string = disasterprediction()
if disaster_string == "":
    disaster_string = "None"

"""main display terminal to show the graphs on a button click and the suggested renewables and possible natural
disasters"""

window = Tk()
window.title('View Data Regarding Your Location!')
window.geometry("600x600")
window.minsize(600,600)
window.maxsize(600,600)
canvas = Canvas(window, height=600, width=600, bg='#fb5b8d')
canvas.pack()

# importing the images
background_image1 = Image.open(R"graphspic.jpeg")
background_image1 = background_image1.resize((230, 154))
background_image1 = ImageTk.PhotoImage(background_image1)

background_image2 = Image.open(R"disasterpic.jpeg")
background_image2 = background_image2.resize((150, 138))
background_image2 = ImageTk.PhotoImage(background_image2)

background_image3 = Image.open(R"picrenewables.jpeg")
background_image3 = background_image3.resize((200, 93))
background_image3 = ImageTk.PhotoImage(background_image3)

# setting up the contents of the 2nd page (with formatting)
frame1 = Frame(canvas, bg='#000834', bd=10)
frame1.place(relx=0.5, rely=0.06, relwidth=0.8, relheight=0.1, anchor='n')

frame2 = Frame(canvas, bg='#000834', bd=10)
frame2.place(relx=0.5, rely=0.2, relwidth=0.8, relheight=0.7, anchor='n')

heading = Label(frame1, text="Location Information", font=("Helvetica Bold", 20), anchor="center", bg="#000834",
                fg="white")
heading.place(relx=0.23, rely=0)

label1 = Label(frame2, text=f"Graphs for the Location", font=("Ubuntu Light", 14), bg="#000834", fg="white")
label1.place(relx=0.525, rely=0.01)
button = Button(frame2, text='Show the Graphs', fg="#000834", bg="#fb5b8d", command=graphs)
button.place(relx=0.62, rely=0.15, relheight=0.09, relwidth=0.25)
image1 = Label(frame2, image=background_image1)
image1.place(relx=0.05, rely=0, relheight=0.3, relwidth=0.35)

label2 = Label(frame2, text=f"Predicted Disasters", font=("Ubuntu Light", 14), bg="#000834", fg="white")
label2.place(relx=0.55, rely=0.4)
label_disaster = Label(frame2, text=f"{disaster_string}", bg="#000834", fg="white")
label_disaster.place(relx=0.62, rely=0.5, relheight=0.09, relwidth=0.25)
image2 = Label(frame2, image=background_image2)
image2.place(relx=0.05, rely=0.35, relheight=0.3, relwidth=0.35)

# for showing info regarding every renewable energy source
label3 = Label(frame2, text=f"Renewable Info", font=("Ubuntu Light", 14), bg="#000834", fg="white")
label3.place(relx=0.58, rely=0.76)
renewables = Button(frame2, text=f'Show Info of all the Compatible Renewables', fg="#000834", bg="#fb5b8d",
                    command=infopage)
renewables.place(relx=0.47, rely=0.85, relheight=0.09, relwidth=0.52)
image3 = Label(frame2, image=background_image3)
image3.place(relx=0.05, rely=0.7, relheight=0.3, relwidth=0.35)

window.mainloop()
