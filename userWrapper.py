from PIL import Image, ImageTk
from tkinter import Tk, Canvas, Frame, Label, Button
from formattedWindows import login_and_signup_window


def clickedexisting(window):
    window.destroy()
    import login


def clickednewuser(window):
    window.destroy()
    import signUp


login_and_signup_window(clickedexisting, clickednewuser)