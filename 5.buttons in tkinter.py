from tkinter import *
root=Tk()

root.geometry("500x300")
#functions for command
def name():
    print("Name: Protik Acharjay")
def id():
    print("id: 20-42715-1")
def versity():
    print("University: American International University Bangladesh")
def location():
    print("Location: Dhaka,Bangladesh")

#Frame
f1= Frame(root, borderwidth= 6, bg="grey", relief= SUNKEN)
f1.pack(side=LEFT, anchor="nw")

#buttons
b1= Button(f1, fg="red", text="name", command=name)
b1.pack(side=LEFT)
b2=Button(f1,fg="red", text= "id", command=id)
b2.pack(side=LEFT)
b3= Button(f1,fg="red",text="University", command=versity)
b3.pack(side=LEFT)
b4= Button(f1, fg="red", text="location", command=location)
b4.pack(side=LEFT)


root.mainloop()