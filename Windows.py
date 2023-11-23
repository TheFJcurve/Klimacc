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

    def create_label(self, labelName, parent, image, relx, rely, relheight, relwidth, fontName=normalFont, fontSize=15):
        self.labelName = Label(
            master=parent,
            image=image,
            font=(
                fontName,
                fontSize
            )
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

    def create_entry(self, entryName, parent, relx, rely, relwidth, relheight):
        """
        """

        self.entryName = Entry(
            master=parent
        )
        self.entryName.place(
            relx=relx,
            rely=rely,
            relwidth=relwidth,
            relheight=relheight
        )

# Defining Windows for each step of the program


def mainWindow(buttonFunction):
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


def userWrapperWindow(buttonFunction1, buttonFunction2):
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


def loginWindow(buttonFunction):
    """
    """

    window = KlimaccWindow(message="Login Page")

    canvas = window.create_canvas(
        canvasName="canvas"
    )

    upper_frame = window.create_frame(
        frameName="upper_frame",
        relx=0.5,
        rely=0.06,
        relwidth=0.69,
        relheight=0.1,
    )

    lower_frame = window.create_frame(
        frameName="lower_frame",
        relx=0.5,
        rely=0.25,
        relwidth=0.69,
        relheight=0.5,
    )

    # adding the necessary headings and other formatting

    heading_label = window.create_heading(
        headingName="heading_label",
        parent=upper_frame,
        message="User Login",
        relx=0.35,
        rely=0
    )

    username_label = window.create_heading(
        headingName="username_label",
        parent=lower_frame,
        message="Enter Your Username",
        relx=0,
        rely=0.18
    )

    password_label = window.create_heading(
        headingName="password_label",
        parent=lower_frame,
        message="Enter Your Passowrd",
        relx=0,
        rely=0.58
    )

    # making text boxes to accept input from the user

    username_text = window.create_entry(
        entryName="username_text",
        parent=lower_frame,
        relx=0.01,
        rely=0.3,
        relwidth=0.98,
        relheight=0.09
    )

    password_text = window.create_entry(
        entryName="password_text",
        parent=lower_frame,
        relx=0.01,
        rely=0.7,
        relwidth=0.98,
        relheight=0.09
    )

    button_login = window.create_button(
        buttonName="button_login",
        parent=canvas,
        message="Login",
        command=buttonFunction,
        relx=0.4,
        rely=0.85,
        relheight=0.05,
        relwidth=0.2
    )

    window.mainloop()


def signUpWindow(buttonFunction):
    window = KlimaccWindow(
        message="Klimacc : One Click to Sustainaibility"
    )

    canvas = window.create_canvas(
        canvasName="canvas"
    )

    upper_frame = window.create_frame(
        frameName="upper_frame",
        parent=canvas,
        relx=0.5,
        rely=0.06,
        relwidth=0.8,
        relheight=0.1,
    )

    lower_frame = window.create_frame(
        frameName="lower_frame",
        parent=canvas,
        relx=0.5,
        rely=0.23,
        relwidth=0.8,
        relheight=0.6,
    )

    # adding the headings for the text boxes
    login_heading = window.create_heading(
        headingName="login_heading",
        parent=upper_frame,
        message="User Sign Up",
        relx=0.32,
        rely=0
    )

    full_name_heading = window.create_heading(
        headingName="full_name_heading",
        parent=lower_frame,
        message="Full Name",
        relx=0,
        rely=0.05
    )

    user_name_heading = window.create_heading(
        headingName="user_name_heading",
        parent=lower_frame,
        message="Username",
        relx=0.5,
        rely=0.05
    )

    security_key_heading = window.create_heading(
        headingName="security_key_heading",
        parent=lower_frame,
        message="Provide a Backup Security Key",
        relx=0,
        rely=0.4
    )

    phone_no_heading = window.create_heading(
        headingName="phone_no_heading",
        parent=lower_frame,
        message="Phone Number",
        relx=0.5,
        rely=0.4
    )

    password_heading = window.create_heading(
        headingName="password_heading",
        parent=lower_frame,
        message="Password",
        relx=0,
        rely=0.75
    )

    confirm_password_heading = window.create_heading(
        headingName="confirm_password_heading",
        parent=lower_frame,
        message="Confirm Password",
        relx=0.5,
        rely=0.75
    )

    # adding the textboxes

    full_name_text = window.create_entry(
        entryName="full_name_text",
        parent=lower_frame,
        relx=0.03,
        rely=0.15,
        relwidth=0.45,
        relheight=0.08
    )

    user_name_text = window.create_entry(
        entryName="user_name_text",
        parent=lower_frame,
        relx=0.53,
        rely=0.15,
        relwidth=0.45,
        relheight=0.08
    )

    security_key_text = window.create_entry(
        entryName="security_key_text",
        parent=lower_frame,
        relx=0.03,
        rely=0.5,
        relwidth=0.45,
        relheight=0.08
    )

    phone_no_text = window.create_entry(
        entryName="phone_no_text",
        parent=lower_frame,
        relx=0.53,
        rely=0.5,
        relwidth=0.45,
        relheight=0.08
    )

    password_text = window.create_entry(
        entryName="password_text",
        parent=lower_frame,
        relx=0.03,
        rely=0.85,
        relwidth=0.45,
        relheight=0.08
    )

    confirm_password_text = window.create_entry(
        entryName="confirm_password_text",
        parent=lower_frame,
        relx=0.53,
        rely=0.85,
        relwidth=0.45,
        relheight=0.08
    )

    # adding the button to submit the data
    button_submit = window.create_button(
        buttonName="button_submit",
        parent=canvas,
        message="Sign Up",
        command=buttonFunction,
        relx=0.38,
        rely=0.88,
        relheight=0.05,
        relwidth=0.25
    )

    window.mainloop()


def locationFinderWindow(buttonFunction):
    """Creating the page for user to input his/her location"""

    window = KlimaccWindow()

    canvas = window.create_canvas(
        canvasName="canvas"
    )

    frame = window.create_frame(
        frameName="frame",
        parent=canvas,
        relx=0.5,
        rely=0.2,
        relwidth=0.8,
        relheight=0.6,
    )

    heading = window.create_heading(
        headingName="heading",
        parent=frame,
        message="Enter Your Location",
        relx=0.23,
        rely=0.08
    )

    location_text = window.create_entry(
        entryName="location_text",
        parent=frame,
        relx=0.2,
        rely=0.4,
        relwidth=0.6,
        relheight=0.08
    )

    button_submit = window.create_button(
        buttonName="button_submit",
        parent=canvas,
        message="Submit",
        command=buttonFunction,
        relx=0.41,
        rely=0.7,
        relheight=0.1,
        relwidth=0.2
    )

    window.mainloop()


def locationDataWindow(buttonFunction):
    window = KlimaccWindow(
        message="View Data Regarding Your Location!"
    )

    canvas = window.create_canvas(
        canvasName="canvas"
    )

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
    upper_frame = window.create_frame(
        frameName="upper_frame",
        parent=canvas,
        relx=0.5,
        rely=0.06,
        relwidth=0.8,
        relheight=0.1,
    )

    lower_frame = window.create_frame(
        frameName="lower_frame",
        parent=canvas,
        relx=0.5,
        rely=0.2,
        relwidth=0.8,
        relheight=0.7,
    )

    main_heading = window.create_heading(
        headingName="main_heading",
        parent=upper_frame,
        message="View Data Regarding Your Location!",
        relx=0.23,
        rely=0
    )

    graph_heading = window.create_heading(
        headingName="graph_heading",
        parent=lower_frame,
        message="Graphs for the Location",
        relx=0.525,
        rely=0.01
    )

    graph_button = window.create_button(
        buttonName="graph_button",
        parent=lower_frame,
        message="Show the Graphs",
        command=buttonFunction,
        relx=0.62,
        rely=0.15,
        relheight=0.09,
        relwidth=0.25
    )

    graph_image = window.create_label(
        labelName="graph_image",
        parent=lower_frame,
        image=background_image1,
        relx=0.05,
        rely=0,
        relheight=0.3,
        relwidth=0.35
    )

    disaster_heading = window.create_heading(
        headingName="disaster_heading",
        parent=lower_frame,
        message="Predicted Disasters",
        relx=0.55,
        rely=0.4
    )

    disaster_image = window.create_label(
        labelName="disaster_image",
        parent=lower_frame,
        image=background_image2,
        relx=0.05,
        rely=0.35,
        relheight=0.3,
        relwidth=0.35
    )

    # for showing info regarding every renewable energy source
    renewable_heading = window.create_heading(
        headingName="renewable_heading",
        parent=lower_frame,
        message="Renewable Info",
        relx=0.58,
        rely=0.76
    )

    renewable_button = window.create_button(
        buttonName="renewable_button",
        parent=lower_frame,
        message="Show Info of all the Compatible Renewables",
        command=buttonFunction,
        relx=0.47,
        rely=0.85,
        relheight=0.09,
        relwidth=0.52
    )

    renewable_image = window.create_label(
        labelName="renewable_image",
        parent=lower_frame,
        image=background_image3,
        relx=0.05,
        rely=0.7,
        relheight=0.3,
        relwidth=0.35
    )

    window.mainloop()


def forgotPasswordWindow(buttonFunction):

    window = KlimaccWindow(
        message="Reset Password"
    )

    canvas = window.create_canvas(
        canvasName="canvas"
    )

    upper_frame = window.create_frame(
        frameName="upper_frame",
        parent=canvas,
        relx=0.5,
        rely=0.05,
        relwidth=0.75,
        relheight=0.1,
    )

    lower_frame = window.create_frame(
        frameName="lower_frame",
        parent=canvas,
        relx=0.5,
        rely=0.2,
        relwidth=0.75,
        relheight=0.75,
    )

    # adding the necessary headings and other formatting
    login_heading = window.create_heading(
        headingName="login_heading",
        parent=upper_frame,
        message="Reset Password",
        relx=0.29,
        rely=0.1
    )

    user_name_heading = window.create_heading(
        headingName="user_name_heading",
        parent=lower_frame,
        message="Username",
        relx=0.01,
        rely=0.1
    )

    security_key_heading = window.create_heading(
        headingName="security_key_heading",
        parent=lower_frame,
        message="Security Key",
        relx=0.51,
        rely=0.1
    )

    otp_heading = window.create_heading(
        headingName="otp_heading",
        parent=lower_frame,
        message="Enter OTP",
        relx=0.04,
        rely=0.53
    )

    new_password_heading = window.create_heading(
        headingName="new_password_heading",
        parent=lower_frame,
        message="New Password",
        relx=0.01,
        rely=0.7
    )

    confirm_password_heading = window.create_heading(
        headingName="confirm_password_heading",
        parent=lower_frame,
        message="Confirm New Password",
        relx=0.51,
        rely=0.7
    )

    # making text boxes to accept input from the user

    user_name_text = window.create_entry(
        entryName="user_name_text",
        parent=lower_frame,
        relx=0.04,
        rely=0.17,
        relwidth=0.4,
        relheight=0.05
    )

    security_key_text = window.create_entry(
        entryName="security_key_text",
        parent=lower_frame,
        relx=0.54,
        rely=0.17,
        relwidth=0.4,
        relheight=0.05
    )

    otp_text = window.create_entry(
        entryName="otp_text",
        parent=lower_frame,
        relx=0.3,
        rely=0.53,
        relwidth=0.6,
        relheight=0.05
    )

    new_password_text = window.create_entry(
        entryName="new_password_text",
        parent=lower_frame,
        relx=0.04,
        rely=0.77,
        relwidth=0.4,
        relheight=0.05
    )

    confirm_password_text = window.create_entry(
        entryName="confirm_password_text",
        parent=lower_frame,
        relx=0.54,
        rely=0.77,
        relwidth=0.4,
        relheight=0.05
    )

    button_submit_otp = window.create_button(
        buttonName="button_submit_otp",
        parent=canvas,
        message="Submit OTP",
        command=buttonFunction,
        relx=0.38,
        rely=0.324,
        relheight=0.1,
        relwidth=0.2
    )

    button_reset_password = window.create_button(
        buttonName="button_reset_password",
        parent=canvas,
        message="Reset Password",
        command=buttonFunction,
        relx=0.38,
        rely=0.872,
        relheight=0.1,
        relwidth=0.2
    )

    window.mainloop()
