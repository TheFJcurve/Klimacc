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
    window = Tk()
    window.geometry('600x600')
    window.title("Klimacc : One Click to Sustainaibility")
    canvas = Canvas(window, height=600, width=600, bg='#fb5b8d')
    canvas.pack()

    frame1 = Frame(canvas, bg='#000834', bd=10)
    frame1.place(relx=0.5, rely=0.06, relwidth=0.8, relheight=0.1, anchor='n')

    frame = Frame(canvas, bg='#000834', bd=10)
    frame.place(relx=0.5, rely=0.23, relwidth=0.8, relheight=0.6, anchor='n')

    # adding the headings for the text boxes
    lblloginheading = Label(frame1, text="User Sign Up", font=("Helvetica Bold", 20), anchor="center", bg="#000834",
                            fg="white")
    lblloginheading.place(relx=0.32, rely=0)
    lblfullname = Label(frame, text='Full Name', font=(
        'Ubuntu Bold', 12), bg="#000834", fg="white")
    lblfullname.place(relx=0, rely=0.05)
    lblusername = Label(frame, text='Username', font=(
        'Ubuntu Bold', 12), bg="#000834", fg="white")
    lblusername.place(relx=0.5, rely=0.05)
    lblsecuritykey = Label(frame, text='Provide a Backup Security Key', font=(
        'Ubuntu Bold', 12), bg="#000834", fg="white")
    lblsecuritykey.place(relx=0, rely=0.4)
    lblphoneno = Label(frame, text='Phone Number', font=(
        'Ubuntu Bold', 12), bg="#000834", fg="white")
    lblphoneno.place(relx=0.5, rely=0.4)
    lblpassword = Label(frame, text='Password', font=(
        'Ubuntu Bold', 12), bg="#000834", fg="white")
    lblpassword.place(relx=0, rely=0.75)
    lblconfirmpassword = Label(frame, text='Confirm password', font=(
        'Ubuntu Bold', 12), bg="#000834", fg="white")
    lblconfirmpassword.place(relx=0.5, rely=0.75)

    # adding the textboxes
    txtfullname = Entry(frame)
    txtfullname.place(relx=0.03, rely=0.15, relwidth=0.45, relheight=0.08)
    txtusername = Entry(frame)
    txtusername.place(relx=0.53, rely=0.15, relwidth=0.45, relheight=0.08)
    txtsecuritykey = Entry(frame)
    txtsecuritykey.place(relx=0.03, rely=0.5, relwidth=0.45, relheight=0.08)
    txtphoneno = Entry(frame)
    txtphoneno.place(relx=0.53, rely=0.5, relwidth=0.45, relheight=0.08)
    txtpassword = Entry(frame)
    txtpassword.place(relx=0.03, rely=0.85, relwidth=0.45, relheight=0.08)
    txtconfirmpassword = Entry(frame)
    txtconfirmpassword.place(relx=0.53, rely=0.85,
                             relwidth=0.45, relheight=0.08)

    # creating lists for checking conditions in password check
    lstusernamesandpasswords = []

    # connecting to mysql
    mydb = mysql.connect(
        host=host, user=user, password=password, database=database, port=port)
    mycursor = mydb.cursor()

    # creating table using the existing condition
    mycur2 = mydb.cursor(buffered=True)
    mycur2.execute(
        f"CREATE TABLE IF NOT EXISTS {table} (Name Varchar(50), Username Varchar(50), Password Varchar(50), SecurityKey Varchar(20), Phoneno Numeric(13));")

    mydb.commit()

    # getting the records of the registered users
    mycursor.execute(f"SELECT * FROM {table}")
    myresult = mycursor.fetchall()
    for x in myresult:
        lstusernamesandpasswords.append(list(x))

    # making a separate list of usernames,passwords,securitykeys,and phonenos
    lstusernames = []
    lstfullname = []
    for i in range(len(lstusernamesandpasswords)):
        lstusernames.append(lstusernamesandpasswords[i][1])
        lstfullname.append(lstusernamesandpasswords[i][0])

    btnsignupfree = Button(canvas, text="Sign Up", font=(
        'Ubuntu Bold', 13), fg="white", bg='#000834', command=clickedsignupfree)
    btnsignupfree.place(relx=0.38, rely=0.88, relheight=0.05, relwidth=0.25)

    window.mainloop()


def locationDataWindow(buttonFunction):
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

    heading = Label(frame, text="Enter Your Location", font=(
        "Helvetica Bold", 20), fg="white", bg="#000834")
    heading.place(relx=0.23, rely=0.08)

    location_user = Entry(frame, justify="center")
    location_user.place(relx=0.2, rely=0.4, relheight=0.08, relwidth=0.6)

    button = Button(frame, text="Submit", font=('Ubuntu Light', 13,
                    'bold'), fg='#000834', command=clickedlocation, bg="#fb5b8d")
    button.place(relx=0.41, rely=0.7, relheight=0.1, relwidth=0.2)

    root.mainloop()


def locationDataWindow(buttonFunction):
    window = Tk()
    window.title('View Data Regarding Your Location!')
    window.geometry("600x600")
    window.minsize(600, 600)
    window.maxsize(600, 600)
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

    label1 = Label(frame2, text=f"Graphs for the Location",
                   font=("Ubuntu Light", 14), bg="#000834", fg="white")
    label1.place(relx=0.525, rely=0.01)
    button = Button(frame2, text='Show the Graphs',
                    fg="#000834", bg="#fb5b8d", command=graphs)
    button.place(relx=0.62, rely=0.15, relheight=0.09, relwidth=0.25)
    image1 = Label(frame2, image=background_image1)
    image1.place(relx=0.05, rely=0, relheight=0.3, relwidth=0.35)

    label2 = Label(frame2, text=f"Predicted Disasters", font=(
        "Ubuntu Light", 14), bg="#000834", fg="white")
    label2.place(relx=0.55, rely=0.4)
    label_disaster = Label(
        frame2, text=f"{disaster_string}", bg="#000834", fg="white")
    label_disaster.place(relx=0.62, rely=0.5, relheight=0.09, relwidth=0.25)
    image2 = Label(frame2, image=background_image2)
    image2.place(relx=0.05, rely=0.35, relheight=0.3, relwidth=0.35)

    # for showing info regarding every renewable energy source
    label3 = Label(frame2, text=f"Renewable Info", font=(
        "Ubuntu Light", 14), bg="#000834", fg="white")
    label3.place(relx=0.58, rely=0.76)
    renewables = Button(frame2, text=f'Show Info of all the Compatible Renewables', fg="#000834", bg="#fb5b8d",
                        command=infopage)
    renewables.place(relx=0.47, rely=0.85, relheight=0.09, relwidth=0.52)
    image3 = Label(frame2, image=background_image3)
    image3.place(relx=0.05, rely=0.7, relheight=0.3, relwidth=0.35)

    window.mainloop()
