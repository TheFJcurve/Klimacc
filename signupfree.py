# checking the password matching condition
def clickedsignupfree():
    if txtfullname.get not in lstfullname:
        if not txtfullname.get() == "" and not txtusername.get() == '' and not txtsecuritykey.get() == '' and not txtphoneno.get() == '' and not txtpassword.get() == '' and not txtconfirmpassword.get() == '':
            if txtpassword.get() == txtconfirmpassword.get():
                if txtusername.get() not in lstusernames:
                    sql = f'INSERT INTO nameandpass VALUES ("{txtfullname.get()}","{txtusername.get()}","{txtpassword.get()}","{txtsecuritykey.get()}",{txtphoneno.get()})'
                    mycur2.execute(sql)
                    mydb.commit()
                    messagebox.showinfo('Message title', 'Successfully signed up!')
                    window.destroy()
                    import login
                elif txtusername.get() in lstusernames:
                    messagebox.showinfo('Sign Up', 'Username already in use')
            else:
                messagebox.showinfo('Sign Up', 'Passwords do not match')
        else:
            messagebox.showinfo('Sign Up', 'Fields cannot be left blank')
    elif txtfullname.get() in lstfullname:
        res = messagebox.askyesno('Sign Up', 'Account already exists, want to login?')
        if res == 'True':
            window.destroy()
            import login


# making the introductory window
import time
import mysql.connector
from tkinter import *
from tkinter import messagebox

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
lblfullname = Label(frame, text='Full Name', font=('Ubuntu Bold', 12), bg="#000834", fg="white")
lblfullname.place(relx=0, rely=0.05)
lblusername = Label(frame, text='Username', font=('Ubuntu Bold', 12), bg="#000834", fg="white")
lblusername.place(relx=0.5, rely=0.05)
lblsecuritykey = Label(frame, text='Provide a Backup Security Key', font=('Ubuntu Bold', 12), bg="#000834", fg="white")
lblsecuritykey.place(relx=0, rely=0.4)
lblphoneno = Label(frame, text='Phone Number', font=('Ubuntu Bold', 12), bg="#000834", fg="white")
lblphoneno.place(relx=0.5, rely=0.4)
lblpassword = Label(frame, text='Password', font=('Ubuntu Bold', 12), bg="#000834", fg="white")
lblpassword.place(relx=0, rely=0.75)
lblconfirmpassword = Label(frame, text='Confirm password', font=('Ubuntu Bold', 12), bg="#000834", fg="white")
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
txtconfirmpassword.place(relx=0.53, rely=0.85, relwidth=0.45, relheight=0.08)

# creating lists for checking conditions in password check
lstusernamesandpasswords = []

# connecting to mysql
mydb = mysql.connector.connect(host="localhost", user="root", password="Sargun05", database='klimaccdata', port=3307)
mycursor = mydb.cursor()
mycursor.execute('USE klimaccdata')

# creating table using the existing condition
mycur2 = mydb.cursor(buffered=True)
mycur2.execute(
    'Create table if not exists nameandpass (Name Varchar(50), Username Varchar(50), Password Varchar(50), SecurityKey Varchar(20), Phoneno Numeric(13));')

mydb.commit()

# getting the records of the registered users
mycursor.execute("SELECT * FROM nameandpass")
myresult = mycursor.fetchall()
for x in myresult:
    lstusernamesandpasswords.append(list(x))

# making a separate list of usernames,passwords,securitykeys,and phonenos
lstusernames = []
lstfullname = []
for i in range(len(lstusernamesandpasswords)):
    lstusernames.append(lstusernamesandpasswords[i][1])
    lstfullname.append(lstusernamesandpasswords[i][0])

btnsignupfree = Button(canvas, text="Sign Up", font = ('Ubuntu Bold', 13), fg="white", bg='#000834', command=clickedsignupfree)
btnsignupfree.place(relx=0.38, rely=0.88, relheight=0.05, relwidth=0.25)

window.mainloop()
