from tkinter import *
root= Tk()

root.geometry("500x300")
#Frames
f1= Frame(root, bg="grey", borderwidth=6, relief=SUNKEN)
f1.pack(side=LEFT , fill=Y)

f2=Frame(root,bg="grey",borderwidth=6, relief=SUNKEN)
f2.pack(side=TOP, fill=X)

#Labels
l1= Label(f1,text="Pycharm - Project \nProtik Acharjay")
l1.pack(pady=55)

l2=Label(f2, text="Welcome to Protik GUI",font=("jokerman", 21, "bold"),fg="dark blue")
l2.pack(padx=8,pady=12)

root.mainloop()