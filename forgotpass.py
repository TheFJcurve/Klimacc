# number is +17174290730

import mysql.connector
from tkinter import *
from tkinter import messagebox
import mysql.connector


def clickedsendotp():
    if txtaskusernamereset.get() == '' or txtasksecuritykeyreset == '':
        messagebox.showinfo('Reset Password', 'Fields cannot be left blank')
    elif txtaskusernamereset.get() not in lstusernamesreset:
        messagebox.showinfo('Reset Password', 'Incorrect username')
    else:
        # getting the security key of the username that was stored previously
        indexofusername = lstusernamesreset.index(txtaskusernamereset.get())
        global storedsecuritykey
        storedsecuritykey = lstsecuritykeyreset[indexofusername]
        # getting the stored password for use in resetpage
        global oldpassword
        oldpassword = lstpasswordsreset[indexofusername]
        import twilio
        from twilio.rest import Client
        accountsid = 'AC6d502dd14d7cf89e864d81d15e55b2d1'
        authtoken = 'c76df270ca3c94af92562587306b03fe'
        client = Client(accountsid, authtoken)
        import random
        global x
        x = random.randint(1000, 9999)
        # getting the phone number of the registered user
        phonenoregistered = lstphonenoreset[indexofusername]
        message = client.messages.create(body=x, from_='+17174290730', to=f'+{phonenoregistered}')
        messagebox.showinfo('Reset Password', 'OTP has been sent to the registered mobile number')


def clickedreset():
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
                            messagebox.showinfo('Reset Password', 'Password updated successfully')
                            import mysqlconnector
                            window.destroy()
                        else:
                            messagebox.showinfo('Reset Password', 'Cannot use old password')
                    else:
                        messagebox.showinfo('Reset Password', 'Passwords do not match')
                else:
                    messagebox.showinfo('Reset Password', 'Incorrect otp entered')
            else:
                messagebox.showinfo('Reset Password', 'Incorrect security key')


window = Tk()
window.title("Reset Password")

# setting the window size
window.geometry('600x600')
window.minsize(600, 600)
window.maxsize(600, 600)
canvas = Canvas(window, height=600, width=600, bg='#fb5b8d')
canvas.pack()

frame = Frame(window, bg='#000834', bd=5)
frame.place(relx=0.5, rely=0.05, relwidth=0.75, relheight=0.1, anchor='n')

frame2 = Frame(window, bg='#000834', bd=5)
frame2.place(relx=0.5, rely=0.2, relwidth=0.75, relheight=0.75, anchor='n')

# adding the necessary headings and other formatting
lblloginheading = Label(frame, text="Reset Password", font=("Helvetica Bold", 20), anchor="center", fg="white",
                        bg="#000834")
lblloginheading.place(relx=0.29, rely=0.1)

lblaskusername = Label(frame2, text="Username", font=("Ubuntu Light", 13), anchor="center", fg="white", bg="#000834")
lblaskusername.place(relx=0.01, rely=0.1)
lblasksecuritykey = Label(frame2, text="Security Key", font=("Ubuntu Light", 13), anchor="center", fg="white", bg="#000834")
lblasksecuritykey.place(relx=0.51, rely=0.1)

lblaskotp = Label(frame2, text="Enter OTP", font=("Ubuntu Light", 13), anchor="center",  fg="white", bg="#000834")
lblaskotp.place(relx=0.04, rely=0.53)
lblresetpass1 = Label(frame2, text="New Password", font=("Ubuntu Light", 13), anchor="center", fg="white", bg="#000834")
lblresetpass1.place(relx=0.01, rely=0.7)
lblresetpass1confirm = Label(frame2, text="Confirm New Password", font=("Ubuntu Light", 13), anchor="center", fg="white", bg="#000834")
lblresetpass1confirm.place(relx=0.51, rely=0.7)

# making text boxes to accept input from the user

txtaskusernamereset = Entry(frame2)
txtaskusernamereset.place(relx=0.04, rely=0.17, relwidth=0.4, relheight=0.05)
txtasksecuritykeyreset = Entry(frame2)
txtasksecuritykeyreset.place(relx=0.54, rely=0.17, relwidth=0.4, relheight=0.05)
txtaskotp = Entry(frame2)
txtaskotp.place(relx=0.3, rely=0.53, relwidth=0.6, relheight=0.05)
txtresetpass1 = Entry(frame2)
txtresetpass1.place(relx=0.04, rely=0.77, relwidth=0.4, relheight=0.05)
txtresetpass1confirm = Entry(frame2)
txtresetpass1confirm.place(relx=0.54, rely=0.77, relwidth=0.4, relheight=0.05)

# connecting to mysql

mydb = mysql.connector.connect(host="localhost", user="root", password="Sargun05", database='klimaccdata', port=3307)
mycursor = mydb.cursor()
mycursor.execute('USE klimaccdata')
mydb.commit()

# creating the list of all users' data
lstdata = []

# getting the records of the registered users
mycursor.execute("SELECT * FROM nameandpass")
myresult = mycursor.fetchall()
for x in myresult:
    lstdata.append(list(x))

# making a separate list of usernames,passwords,securitykeys,and phonenos
lstusernamesreset = []
lstpasswordsreset = []
lstsecuritykeyreset = []
lstphonenoreset = []
for i in range(len(lstdata)):
    lstusernamesreset.append(lstdata[i][1])
    lstpasswordsreset.append(lstdata[i][2])
    lstsecuritykeyreset.append(lstdata[i][3])
    lstphonenoreset.append(lstdata[i][4])

btnsendotp = Button(frame2, text="Send OTP", font = ('Ubuntu Light', 12, 'bold'), fg="#000834", bg='#fb5b8d', command=clickedsendotp)
btnsendotp.place(relx=0.38, rely=0.324, relheight=0.1, relwidth=0.2)
btnresetpass = Button(frame2, text="Reset",font = ('Ubuntu Light', 13, 'bold'), fg="#000834", bg='#fb5b8d', command=clickedreset)
btnresetpass.place(relx=0.38, rely=0.872, relheight=0.1, relwidth=0.2)

window.mainloop()
