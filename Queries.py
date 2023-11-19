import mysql.connector as mysql
from variableValues import host, user, password, port, database, table_user, table_renewables


def establishConnection():
    """
    Establishes the connection with the database, sets up the database and tables, and returns the cursor.
    """

    # Creating the Connection and the Cursor
    mydb = mysql.connect(
        host=host,
        user=user,
        password=password,
        port=port
    )
    mycursor = mydb.cursor(buffered=True)

    # Creating the Database
    mycursor.execute(
        f"CREATE DATABASE IF NOT EXISTS {database};"
    )

    mycursor.execute(
        f"USE {database};"
    )

    # Creating the Tables
    mycursor.execute(
        f"""CREATE TABLE IF NOT EXISTS {table_user} 
        (NAME Varchar(50), 
        USERNAME Varchar(50), 
        PASSWORD Varchar(50), 
        SECURITYKEY Varchar(20), 
        PHONENUMBER Numeric(13));"""
    )
    mycursor.execute(
        f"""CREATE TABLE IF NOT EXISTS {table_renewables} 
        (NAME varchar(20) primary key, 
        TEMPERATUREDEGREE int, 
        HUMIDITYPERCENTAGE int, 
        WIND int);"""
    )

    # Returning the Cursor
    return mycursor


def loginQueries():

    lstusernamesandpasswords = []

    mycursor = establish_connection()

    # making the list of existing usernames and passwords using mysql

    # getting the records of the registered users
    mycursor.execute(
        f"SELECT * FROM {table_user}"
    )
    myresult = mycursor.fetchall()
    for x in myresult:
        lstusernamesandpasswords.append(list(x))

    # making a separate list of usernames and passwords
    lstusernames = []
    lstpasswords = []

    for i in range(len(lstusernamesandpasswords)):
        lstusernames.append(lstusernamesandpasswords[i][1])
        lstpasswords.append(lstusernamesandpasswords[i][2])

    print(lstusernames, lstpasswords)

    # defining count to calculate incorrect password tries
    count = 0


def getLocationWeather():
    """According to the user's inputed location, this function interacts with the API to get info of that place"""
    weather_key = APIkey
    url = APIurl
    params = {'APPID': weather_key, 'q': user_location, 'units': 'Metric'}
    response = requests.get(url, params=params)
    weather = response.json()

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


def settingRenewableBaseValues():
    """
    Creates the databases and the table
    """

    mycursor = establish_connection()
    mycur.execute(
        f"""INSERT INTO {table_renewables} VALUES 
        ('SOLAR ENERGY', NULL, NULL, NULL),
        ('BIOMASS ENERGY', NULL, 50, NULL),
        ('WIND ENERGY', 15, NULL, 12),
        ('GEOTHERMAL ENERGY', NULL, NULL, NULL);"""
    )

    mycursor.close()


def signUpQueries():
    # creating lists for checking conditions in password check
    lstusernamesandpasswords = []

    mycursor = establish_connection()
    mycursor.execute(
        f"""CREATE TABLE IF NOT EXISTS {table} 
        (Name Varchar(50), 
        Username Varchar(50),
        Password Varchar(50), 
        SecurityKey Varchar(20), 
        Phoneno Numeric(13));"""
    )

    # getting the records of the registered users
    mycursor.execute(
        f"SELECT * FROM {table}"
    )
    myresult = mycursor.fetchall()
    for x in myresult:
        lstusernamesandpasswords.append(list(x))

    # making a separate list of usernames,passwords,securitykeys,and phonenos
    lstusernames = []
    lstfullname = []
    for i in range(len(lstusernamesandpasswords)):
        lstusernames.append(lstusernamesandpasswords[i][1])
        lstfullname.append(lstusernamesandpasswords[i][0])

    mycursor.close()

    return (lstusernames, lstfullname)
