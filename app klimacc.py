# making the introductory window
import mysql.connector
import time
from tkinter import *
from PIL import Image, ImageTk


def clickednext():
    window.destroy()
    import finalloginandsignup


window = Tk()
window.title("Klimacc : One Click to Sustainaibility")
window.minsize(600, 600)
window.maxsize(600, 600)
canvas = Canvas(window, height=600, width=600, bg='#fb5b8d')
canvas.pack()

frame = Frame(window, bg='#000834', bd=5)
frame.place(relx=0.5, rely=0.05, relwidth=0.69, relheight=0.1, anchor='n')

lblheading = Label(frame, text='Welcome to Klimacc', font=('Helvetica Bold', 27), anchor='center', bg='#000834', fg='white')
lblheading.place(relwidth=0.99, relheight=1)

background_image = Image.open(R"klimacclogo.jpeg")
background_image = background_image.resize((400, 400))
background_image = ImageTk.PhotoImage(background_image)

lower_frame = Frame(window, bg='#000834', bd=10)
lower_frame.place(relx=0.5, rely=0.18, relwidth=0.69, relheight=0.69, anchor='n')

background_label = Label(lower_frame, image=background_image)
background_label.place(x=0, y=0, relheight=1, relwidth=1)

btnnext = Button(canvas, text="Next", padx=10, pady=5, font = ('Ubuntu Light',15), fg="white", bg='#000834', command=clickednext)
btnnext.place(relx=0.8, rely=0.9, relwidth=0.18, relheight=0.07)

# connecting to mysql to creating the databases required for further purposes

mydb = mysql.connector.connect(host="localhost", user="root", password="Sargun05", database='test', port=3307)
mycursor = mydb.cursor()
mycursor = mydb.cursor(buffered=True)
mycursor.execute("Create database if not exists klimaccdata")

window.mainloop()
