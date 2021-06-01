from tkinter import *
root=Tk()
root.geometry("500x300")
root.title("Protik's Form")
#functions
def log():
    print("User Name is: ",uservalue.get())
    print("Password is: ",passvalue.get())
#Labels
user= Label(root, text="UserName")
password= Label(root,text="Password")
user.grid()
password.grid(row=1)

#variable classes in Tkinter
# BooleanVar, DoubleVar, IntVar, StringVar
#variables
uservalue=StringVar()
passvalue=StringVar()
#entries
userentry= Entry(root, textvariable= uservalue)
passentry= Entry(root, textvariable= passvalue)

userentry.grid(row=0,column=1)
passentry.grid(row=1,column=1)
#checkbox and pack
staylogin= IntVar() #variable for checkbox
staylogentry= Checkbutton(text="Want to Stay Logged In?",variable=staylogin)
staylogentry.grid(row=2,column=1)

#buttons
Button(text="Log In", command= log).grid()
root.mainloop()