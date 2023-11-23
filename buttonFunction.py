# Given a particular button and page, this will give instruction on what to do once the button is pressed

from variableValues import login_tries
from Queries import signUpQueries


def mainPageButton(window):
    window.destroy()
    import userWrapper


def userWrapperSignInButton(window):
    window.destroy()
    import login


def userWrapperSignUpButton(window):
    window.destroy()
    import signUp


def loginButton(window):
    """
    When the user inputs username and password, the username and password is stored and the tab is closed
    """

    if login_tries == 0:
        window.destroy()
        messagebox.showinfo(
            'Login In', 'Too many incorrect tries, Reset Password')
        import forgotPassword
    else:
        if txtusername.get() in lstusernames:
            indexofusername = lstusernames.index(txtusername.get())
            passwordatindex = lstpasswords[indexofusername]
            if txtpassword.get() == passwordatindex:
                login_tries = -1
                messagebox.showinfo('Login In', 'Login successful')
                window.destroy()
                import connectToDatabase
            else:
                login_tries -= 1
                messagebox.showinfo(
                    'Login In', f'Incorrect password, tries left {login_tries}')
                login
        else:
            messagebox.showinfo(
                'Login In', 'Account does not exist with this username')


def signUpButton(window):
    if txtfullname.get not in lstfullname:
        if (
            (not txtfullname.get() == "") and
            (not txtusername.get() == "") and
            (not txtsecuritykey.get() == "") and
            (not txtphoneno.get() == "") and
            (not txtpassword.get() == "") and
            (not txtconfirmpassword.get() == "")
        ):
            if (txtpassword.get() == txtconfirmpassword.get()):
                if (txtusername.get() not in lstusernames):
                    signUpQueries()
                    window.destroy()
                    import login
                elif txtusername.get() in lstusernames:
                    messagebox.showinfo('Sign Up', 'Username already in use')
            else:
                messagebox.showinfo('Sign Up', 'Passwords do not match')
        else:
            messagebox.showinfo('Sign Up', 'Fields cannot be left blank')
    elif txtfullname.get() in lstfullname:
        res = messagebox.askyesno(
            'Sign Up', 'Account already exists, want to login?')
        if res == 'True':
            window.destroy()
            import login


def locationFinderButton(window):
    """
    When the user inputs location, the location is stored and the tab is closed
    """

    user_location = location_user.get()
    user_location = str(user_location).capitalize()

    if user_location == "":
        pass
    else:
        get_weather(user_location)


def sendOTPButton(window):
    if (
        (txtaskusernamereset.get() == "") or
        (txtasksecuritykeyreset.get() == "")
    ):
        messagebox.showinfo('Reset Password', 'Fields cannot be left blank')
    elif (txtaskusernamereset.get() not in lstusernamesreset):
        messagebox.showinfo('Reset Password', 'Incorrect username')
    else:
        # getting the security key of the username that was stored previously
        indexofusername = lstusernamesreset.index(txtaskusernamereset.get())
        global storedsecuritykey
        storedsecuritykey = lstsecuritykeyreset[indexofusername]
        # getting the stored password for use in resetpage
        global oldpassword
        oldpassword = lstpasswordsreset[indexofusername]
        accountsid = 'AC6d502dd14d7cf89e864d81d15e55b2d1'
        authtoken = 'c76df270ca3c94af92562587306b03fe'
        client = Client(accountsid, authtoken)
        global x
        x = random.randint(1000, 9999)
        # getting the phone number of the registered user
        phonenoregistered = lstphonenoreset[indexofusername]
        message = client.messages.create(
            body=x, from_='+17174290730', to=f'+{phonenoregistered}')
        messagebox.showinfo(
            'Reset Password', 'OTP has been sent to the registered mobile number')


def resetPasswordButton(window):
    if txtaskusernamereset.get() == '' or txtasksecuritykeyreset == '' or txtaskotp.get() == '' or txtresetpass1.get() == '' or txtresetpass1confirm.get() == '':
        messagebox.showinfo('Reset Password', 'Fields cannot be left blank')
    else:
        if txtaskusernamereset.get() not in lstusernamesreset:
            messagebox.showinfo('Reset Password', 'Incorrect username')
        else:
            if storedsecuritykey == txtasksecuritykeyreset.get():
                if str(x) == txtaskotp.get():
                    if txtresetpass1.get() == txtresetpass1confirm.get():
                        if txtresetpass1.get() != oldpassword:
                            sql = f'UPDATE nameandpass SET Password = "{txtresetpass1.get()}" where Username = "{txtaskusernamereset.get()}";'
                            mycursor.execute(sql)
                            mydb.commit()
                            messagebox.showinfo(
                                'Reset Password', 'Password updated successfully')
                            import connectToDatabase
                            window.destroy()
                        else:
                            messagebox.showinfo(
                                'Reset Password', 'Cannot use old password')
                    else:
                        messagebox.showinfo(
                            'Reset Password', 'Passwords do not match')
                else:
                    messagebox.showinfo(
                        'Reset Password', 'Incorrect otp entered')
            else:
                messagebox.showinfo('Reset Password', 'Incorrect security key')
