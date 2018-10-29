from tkinter import *

root = Tk()

def log():

    if(Login.get()=="1234"):
        root2 = Tk()
        root.destroy()
        Passwort = Label(root2, text="Welcome")
        Passwort.place(x=20, y=20)

Login = Entry(root, show="*")
Login.place(x=50, y=50, width=100)
Passwort = Label(root, text="Login")
Passwort.place(x=77, y=20)
Confirm = Button(root, text="Confirm", command=log)
Confirm.place(x=50,y=80,width=100)
Login.focus()



root.geometry("200x130")

root.mainloop()