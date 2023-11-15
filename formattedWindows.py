# This file contains all the Tkinter related windows for each step of the program

# Importing the required modules
from tkinter import messagebox, Tk, Canvas, Frame, Label, Entry, Button
from variableValues import windowLength, windowBreadth, minWindowLength, minWindowBreadth, maxWindowLength, maxWindowBreadth, pink, darkBlue, white, normalFont, boldFont, appTitle
from PIL import Image, ImageTk


# Defining Generic Window Functions
class KlimaccWindow(Tk):
    """
    Creates and returns a generic window for the program Klimacc
    """

    def __init__(self, message=appTitle, minLength=minWindowLength, minBreadth=minWindowBreadth, maxLength=maxWindowLength, maxBreadth=maxWindowBreadth):
        """
        Assigns window, canvas and frame to the class.
        """

        super().__init__()

        # Setting the Window
        self.title(message)
        self.minsize(
            minLength,
            minBreadth
        )
        self.maxsize(
            maxLength,
            maxBreadth
        )

    def create_canvas(self, canvasName, height=windowLength, width=windowBreadth, backGroundColor=pink):
        """
        Defining the Canvas on the Window
        """

        self.canvasName = Canvas(
            master=self,
            height=height,
            width=width,
            bg=backGroundColor
        )
        self.canvasName.pack()

    def create_frame(self, frameName, relx, rely, relwidth, relheight, anchor='n', backGroundColor=darkBlue, bd=5):
        """
        Formatting the elements in the window
        """

        self.frameName = Frame(
            master=self,
            bg=backGroundColor,
            bd=bd
        )
        self.frameName.place(
            relx=relx,
            rely=rely,
            relwidth=relwidth,
            relheight=relheight,
            anchor=anchor
        )

    def create_heading(self, headingName, parent, message, relx, rely, fontName=boldFont, fontSize=20, backGroundColor=darkBlue, foreGroundColor=white, anchor='center'):
        """
        Adding the Heading in the Window
        """

        self.headingName = Label(
            master=parent,
            text=message,
            font=(
                fontName,
                fontSize
            ),
            anchor=anchor,
            bg=backGroundColor,
            fg=foreGroundColor
        )
        self.headingName.place(
            relx=relx,
            rely=rely
        )

    def create_label(self, labelName, parent, image, relx, rely, relheight, relwidth):
        self.labelName = Label(
            master=parent,
            image=image
        )
        self.labelName.place(
            relx=relx,
            rely=rely,
            relheight=relheight,
            relwidth=relwidth
        )

    def create_button(self, buttonName, parent, message, command, relx, rely, relwidth, relheight, fontName=normalFont, fontSize=15, foreGroundColor=white, backGroundColor=darkBlue,):
        """
        """
        self.buttonName = Button(
            master=parent,
            text=message,
            font=(
                fontName,
                fontSize
            ),
            fg=foreGroundColor,
            bg=backGroundColor,
            command=command
        )
        self.buttonName.place(
            relx=relx,
            rely=rely,
            relwidth=relwidth,
            relheight=relheight
        )


# Defining Windows for each step of the program

def main_window(buttonFunction):
    """
    Takes the window size constraints and creates the main window of the program.
    """

    # Creating the Tkinter Window
    window = KlimaccWindow()

    canvas = window.create_canvas(
        canvasName='canvas'
    )

    # Defining the Frames
    upper_frame = window.create_frame(
        frameName='upper_frame',
        relx=0.5,
        rely=0.02,
        relwidth=0.69,
        relheight=0.15,
    )

    lower_frame = window.create_frame(
        frameName='lower_frame',
        relx=0.5,
        rely=0.20,
        relwidth=0.69,
        relheight=0.69,
    )

    # Defining the Heading
    main_heading = window.create_heading(
        headingName='main_heading',
        parent=upper_frame,
        message='Welcome to Klimacc',
        relx=0.28,
        rely=0.07
    )

    # Defining the Button that takes us to the next page
    next_button = window.create_button(
        buttonName='next_button',
        parent=canvas,
        message="Next",
        command=lambda: buttonFunction(window),
        relx=0.42,
        rely=0.9,
        relwidth=0.18,
        relheight=0.07
    )

    # Inserting the Background Image
    background_image = Image.open(R"klimacclogo.jpeg")
    background_image = background_image.resize((400, 400))
    background_image = ImageTk.PhotoImage(background_image)

    # Defining the Background Label for the Image
    background_label = window.create_label(
        labelName='background_label',
        parent=lower_frame,
        image=background_image,
        relx=0.154,
        rely=0.2,
        relheight=0.69,
        relwidth=0.69
    )

    window.mainloop()


def login_and_signup_window(buttonFunction1, buttonFunction2):
    """
    Takes the window size constraints and creates the window containing options for both Login and Sign Up.
    """

    # Making the introductory window
    window = KlimaccWindow()

    # Defining the Canvas on the Window
    canvas = window.create_canvas(
        canvasName='canvas'
    )

    # formatting the elements in the window
    upper_frame = window.create_frame(
        frameName='upper_frame',
        relx=0.5,
        rely=0.05,
        relwidth=0.69,
        relheight=0.17,
    )

    # adding the heading and quote on upper frame
    main_heading = window.create_heading(
        headingName='main_heading',
        parent=upper_frame,
        message='Welcome to Klimacc',
        relx=0.195,
        rely=0.05
    )

    main_quote = window.create_heading(
        headingName='main_quote',
        parent=upper_frame,
        message='Your Safety is our Priority!',
        relx=0.32,
        rely=0.6,
        fontName=normalFont,
        fontSize=10,
        anchor='center'
    )

    # making lower frame
    lower_frame = window.create_frame(
        frameName='lower_frame',
        relx=0.5,
        rely=0.3,
        relwidth=0.69,
        relheight=0.6,
    )

    # importing, resizing and using background image
    background_image = Image.open(R"userlogin.jpg")
    background_image = background_image.resize((150, 150))
    background_image = ImageTk.PhotoImage(background_image)

    # Creating Labels for Images
    first_image = window.create_label(
        labelName='first_image',
        parent=lower_frame,
        image=background_image,
        relx=0.1,
        rely=0.3,
        relheight=0.35,
        relwidth=0.35
    )

    second_image = window.create_label(
        labelName='second_image',
        parent=lower_frame,
        image=background_image,
        relx=0.55,
        rely=0.3,
        relheight=0.35,
        relwidth=0.35
    )

    # making heading on lower frame
    lower_main_heading = window.create_heading(
        headingName='lower_main_heading',
        parent=lower_frame,
        message='Join Klimacc!',
        relx=0.3,
        rely=0.01,
        anchor='center'
    )

    # making the login and sign in buttons
    sign_in_button = window.create_button(
        buttonName='sign_in_button',
        parent=canvas,
        message="Sign In",
        command=lambda: buttonFunction1(window),
        relx=0.17,
        rely=0.75,
        relwidth=0.2,
        relheight=0.1,
        fontSize=13
    )

    sign_up_button = window.create_button(
        buttonName='sign_up_button',
        parent=canvas,
        message="Sign Up",
        command=lambda: buttonFunction2(window),
        relx=0.625,
        rely=0.75,
        relwidth=0.2,
        relheight=0.1,
        fontSize=13
    )

    window.mainloop()
