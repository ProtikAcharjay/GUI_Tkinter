from tkinter import *
root=Tk()
root.geometry("500x350")
root.title("ListBox In Tkinter")
#function
def add():
    adding=input()
    lb1.insert(ACTIVE,adding)

#empty listbox
lb1=Listbox(root)
lb1.pack()
#inserting values in listbox
lb1.insert(END, "First Item")

Button(root, text="Add Item", command=add).pack()

root.mainloop()