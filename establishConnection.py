import mysql.connector as mysql
from variableValues import host, user, password, port, database, table_user, table_renewables


def establish_connection():
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


def establish_login():

    mycursor = establish_connection()

    # making the list of existing usernames and passwords using mysql

    # getting the records of the registered users
    mycursor.execute(
        f"CREATE TABLE IF NOT EXISTS {table} (Name Varchar(50), Username Varchar(50), Password Varchar(50), SecurityKey Varchar(20), Phoneno Numeric(13));")
    mycursor.execute(f"SELECT * FROM {table}")
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
