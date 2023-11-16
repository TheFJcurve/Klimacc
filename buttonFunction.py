# Given a particular button and page, this will give instruction on what to do once the button is pressed


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
    global count
    if count == 3:
        window.destroy()
        messagebox.showinfo(
            'Login In', 'too many incorrect tries, reset password')
        import forgotPassword
    else:
        if txtusername.get() in lstusernames:
            indexofusername = lstusernames.index(txtusername.get())
            passwordatindex = lstpasswords[indexofusername]
            if txtpassword.get() == passwordatindex:
                count = -1
                messagebox.showinfo('Login In', 'Login successful')
                window.destroy()
                import connectToDatabase
            else:
                messagebox.showinfo(
                    'Login In', f'Incorrect password, tries left {3 - count}')
                count = count + 1
        else:
            messagebox.showinfo(
                'Login In', 'Account does not exist with this username')


def signUpButton(window):
    if txtfullname.get not in lstfullname:
        if not txtfullname.get() == "" and not txtusername.get() == '' and not txtsecuritykey.get() == '' and not txtphoneno.get() == '' and not txtpassword.get() == '' and not txtconfirmpassword.get() == '':
            if txtpassword.get() == txtconfirmpassword.get():
                if txtusername.get() not in lstusernames:
                    sql = f'INSERT INTO {table} VALUES ("{txtfullname.get()}", "{txtusername.get()}", "{txtpassword.get()}", "{txtsecuritykey.get()}", {txtphoneno.get()});'
                    mycur2.execute(sql)
                    mydb.commit()
                    messagebox.showinfo(
                        'Message title', 'Successfully signed up!')
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


def userWrapperSignUp(window):
    window.destroy()
    import signUp
