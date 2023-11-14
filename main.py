# making the introductory window
from formattedWindows import main_window
from connectToDatabase import establish_connection


def clickednext(window):
    window.destroy()
    import finalLoginAndSignUp


# Creating the Window
main_window(clickednext)

# connecting to mysql to creating the databases required for further purposes
mycursor = establish_connection()
