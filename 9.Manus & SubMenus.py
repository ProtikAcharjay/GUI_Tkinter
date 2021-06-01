from tkinter import *
root=Tk()
root.geometry("800x500")
root.title("Manus In Tkinter")
#function
def function1():
    print("New file created")
def function2():
    print("Opening a file")
def function3():
    print("File saved")
def function4():
    print("File Coppied")
def function5():
    print("File Pasted")
def function6():
    print("File Deleted")
#Menu _ Basic one(Non drop down menubar)

# normalmenu=Menu(root)
# normalmenu.add_command(label="File",command=function1)
# normalmenu.add_command(label="Exit",command=quit)
# root.config(menu=normalmenu)

#Drop Down Menubar:
dropdownmenu=Menu(root)

#1st drop of a menubar
drop1= Menu(dropdownmenu,tearoff=0)
drop1.add_command(label="New",command=function1)
drop1.add_command(label="Open",command=function2)
drop1.add_separator()
drop1.add_command(label="Save",command=function3)
dropdownmenu.add_cascade(label="File",menu=drop1)
root.config(menu=dropdownmenu)

#2nd drop of a menubar
drop2= Menu(dropdownmenu,tearoff=0)
drop2.add_command(label="Copy",command=function4)
drop2.add_command(label="Paste",command=function5)
drop2.add_separator()
drop2.add_command(label="Delete",command=function6)
dropdownmenu.add_cascade(label="Edit",menu=drop2)
root.config(menu=dropdownmenu)

dropdownmenu.add_command(label="Exit",command=quit)
root.config(menu=dropdownmenu)

root.mainloop()