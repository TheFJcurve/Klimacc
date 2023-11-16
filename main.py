# making the introductory window

# Importing the Necessary Modules
from genericWindows import mainWindow
from establishConnection import establish_connection
from buttonFunction import mainPageButton


if __name__ == "__main__":
    # Creating the Window
    mainWindow(mainPageButton)

    # connecting to mysql to creating the databases required for further purposes
    mycursor = establish_connection()
