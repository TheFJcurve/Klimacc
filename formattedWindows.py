# This file contains all the Tkinter related windows for each step of the program

# Importing the required modules
from tkinter import messagebox, Tk, Canvas, Frame, Label, Entry, Button
from variableValues import windowLength, windowBreadth, minWindowLength, minWindowBreadth, maxWindowLength, maxWindowBreadth, pink, darkBlue, white
from PIL import Image, ImageTk


def main_window(buttonFunction):
    """
    Takes the window size constraints and creates the main window of the program.
    """

    # Creating the Tkinter Window
    window = Tk()
    window.title("Klimacc : One Click to Sustainaibility")
    window.minsize(
        minWindowLength,
        minWindowBreadth
    )
    window.maxsize(
        maxWindowLength,
        maxWindowBreadth
    )

    # Defining the Canvas on the Window
    canvas = Canvas(
        window,
        height=windowLength,
        width=windowBreadth,
        bg=pink
    )
    canvas.pack()

    # Defining Tkinter Frame. We will write and draw everything on this.
    frame = Frame(
        window,
        bg=darkBlue,
        bd=5
    )
    frame.place(
        relx=0.5,
        rely=0.05,
        relwidth=0.69,
        relheight=0.1,
        anchor='n'
    )

    # Defining the Heading
    lblheading = Label(
        frame,
        text='Welcome to Klimacc',
        font=(
            'Helvetica Bold',
            27
        ),
        anchor='center',
        bg=darkBlue,
        fg=white
    )
    lblheading.place(relwidth=0.99, relheight=1)

    # Inserting the Background Image
    background_image = Image.open(R"klimacclogo.jpeg")
    background_image = background_image.resize((400, 400))
    background_image = ImageTk.PhotoImage(background_image)

    # Defining the Lower Frame
    lower_frame = Frame(
        window,
        bg=darkBlue,
        bd=10
    )
    lower_frame.place(
        relx=0.5,
        rely=0.18,
        relwidth=0.69,
        relheight=0.69,
        anchor='n'
    )

    # Defining the Background Label for the Image
    background_label = Label(
        lower_frame,
        image=background_image
    )
    background_label.place(
        x=0,
        y=0,
        relheight=1,
        relwidth=1
    )

    # Defining the Button that takes us to the next page
    btnnext = Button(
        canvas,
        text="Next",
        padx=10,
        pady=5,
        font=(
            'Ubuntu Light',
            15
        ),
        fg=white,
        bg=darkBlue,
        command=lambda: buttonFunction(window)
    )
    btnnext.place(
        relx=0.8,
        rely=0.9,
        relwidth=0.18,
        relheight=0.07
    )

    window.mainloop()
