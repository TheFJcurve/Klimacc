from tkinter import *
from PIL import Image, ImageTk


def clickedexisting():
    window.destroy()
    import login


def clickednewuser():
    window.destroy()
    import signupfree


# making the introductory window
window = Tk()
window.geometry("600x600")
window.minsize(600, 600)
window.maxsize(600, 600)
window.title("Klimacc : One Click to Sustainaibility")
canvas = Canvas(window, height=600, width=600, bg='#fb5b8d')
canvas.pack()

# formatting the elements in the window
frame = Frame(window, bg='#000834', bd=5)
frame.place(relx=0.5, rely=0.05, relwidth=0.69, relheight=0.17, anchor='n')

# adding the heading and quote on upper frame
lblheading = Label(frame, text="Welcome to Klimacc", font=("Helvetica Bold", 20), anchor="center", bg="#000834", fg="white")
lblheading.place(relx=0.195, rely=0.05)
lblquote = Label(frame, text="Your Safety is our Priority!", font=("Ubuntu Light", 10), anchor="center", bg="#000834",
                 fg="white")
lblquote.place(relx=0.32, rely=0.6)

# making lower frame
frame2 = Frame(window, bg='#000834', bd=5)
frame2.place(relx=0.5, rely=0.3, relwidth=0.69, relheight=0.6, anchor='n')

# importing, resizing and using background image
background_image = Image.open(R"userlogin.jpg")
background_image = background_image.resize((150, 150))
background_image = ImageTk.PhotoImage(background_image)

background_label1 = Label(frame2, image=background_image)
background_label1.place(relx=0.1, rely=0.3, relheight=0.35, relwidth=0.35)

background_label2 = Label(frame2, image=background_image)
background_label2.place(relx=0.55, rely=0.3, relheight=0.35, relwidth=0.35)

# making heading on lower frame
lblheading = Label(frame2, text="Join Klimacc!", font=("Helvetica Bold", 20), anchor="center", bg="#000834", fg="white")
lblheading.place(relx=0.3, rely=0.01)

# making the login and sign in buttons
btnloginexisting = Button(frame2, text="Sign In", font = ('Ubuntu Light', 13, 'bold'),  fg="#000834", bg='#fb5b8d', command=clickedexisting)
btnloginexisting.place(relx=0.17, rely=0.75, relheight=0.1, relwidth=0.2)

btnloginnewuser = Button(frame2, text="Sign Up", font = ('Ubuntu Light', 13, 'bold'), fg="#000834", bg='#fb5b8d', command=clickednewuser)
btnloginnewuser.place(relx=0.625, rely=0.75, relheight=0.1, relwidth=0.2)

window.mainloop()
