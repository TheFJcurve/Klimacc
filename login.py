# defining the window interface
import mysql.connector as mysql
from variableValues import host, user, password, database, port, table_user, table_renewables
from tkinter import messagebox, Tk, Canvas, Frame, Label, Entry, Button

# verifying the login details by checking it with the ones previously stored after clicking the login button


def clickedlogin():
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


window = Tk()
window.geometry("600x600")
window.minsize(600, 600)
window.maxsize(600, 600)
window.title("Login Page")
canvas = Canvas(window, height=600, width=600, bg='#fb5b8d')
canvas.pack()

frame1 = Frame(window, bg='#000834', bd=10)
frame1.place(relx=0.5, rely=0.06, relwidth=0.69, relheight=0.1, anchor='n')


frame = Frame(window, bg='#000834', bd=10)
frame.place(relx=0.5, rely=0.25, relwidth=0.69, relheight=0.5, anchor='n')

# adding the necessary headings and other formatting

lblloginheading = Label(frame1, text="User Login", font=(
    "Helvetica Bold", 20), anchor="center", bg="#000834", fg="white")
lblloginheading.place(relx=0.35, rely=0)
lblusername = Label(frame, text='Enter your username', font=(
    'Ubuntu Light', 15), bg="#000834", fg="white")
lblusername.place(relx=0, rely=0.18)
lblpassword = Label(frame, text='Enter your password', font=(
    'Ubuntu Light', 15), bg="#000834", fg="white")
lblpassword.place(relx=0, rely=0.58)

# making text boxes to accept input from the user

txtusername = Entry(frame)
txtusername.place(relx=0.01, rely=0.3, relwidth=0.98, relheight=0.09)
txtpassword = Entry(frame)
txtpassword.place(relx=0.01, rely=0.7, relwidth=0.98, relheight=0.09)

# making the list of existing usernames and passwords using mysql

# creating lists for checking conditions in password check
lstusernamesandpasswords = []

mydb = mysql.connect(
    host=host, user=user, password=password, database=database, port=port)
mycursor = mydb.cursor()

# getting the records of the registered users
mycursor.execute(
    f"CREATE TABLE IF NOT EXISTS {table} (Name Varchar(50), Username Varchar(50), Password Varchar(50), SecurityKey Varchar(20), Phoneno Numeric(13));")
mycursor.execute(f"SELECT * FROM {table}")
myresult = mycursor.fetchall()
for x in myresult:
    lstusernamesandpasswords.append(list(x))

# making a separate list of usernames and passwords
lstusernames = []
lstpasswords = []
for i in range(len(lstusernamesandpasswords)):
    lstusernames.append(lstusernamesandpasswords[i][1])
    lstpasswords.append(lstusernamesandpasswords[i][2])
print(lstusernames, lstpasswords)

# defining count to calculate incorrect password tries
count = 0

btnlogin = Button(canvas, text="Login", font=(
    'Ubuntu Light', 13), fg="white", bg='#000834', command=clickedlogin)
btnlogin.place(relx=0.4, rely=0.85, relheight=0.05, relwidth=0.2)

window.mainloop()
