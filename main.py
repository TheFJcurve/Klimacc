# making the introductory window

# Importing the Necessary Modules
from formattedWindows import main_window
from establishConnection import establish_connection


def clickednext(window):
    window.destroy()
    import userWrapper


# Creating the Window
main_window(clickednext)

# connecting to mysql to creating the databases required for further purposes
mycursor = establish_connection()
