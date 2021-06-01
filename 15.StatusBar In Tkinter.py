from tkinter import *
root=Tk()
root.geometry("500x350")
root.title("15.StatusBar In Tkinter")
#function
def upload():
    statusvar.set("Busy..")
    statusbar.update()
    import time
    time.sleep(2)
    statusvar.set("Ready")

statusvar= StringVar()
statusvar.set("Ready")

statusbar=Label(root,textvariable=statusvar, relief=SUNKEN,anchor="w")
statusbar.pack(side=BOTTOM,fill=X)

Button(root,text="Upload",command=upload).pack()

root.mainloop()