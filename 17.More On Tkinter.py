from tkinter import *
root=Tk()
root.geometry("500x350")
root.title("17.More on Tkinter")
#Changing the Icon of GUI window (left)
root.wm_iconbitmap("1.ico")
#changng basic things in gui with configure
root.configure(bg="grey")
#destroying
Button(text="Close",command=root.destroy).pack()

root.mainloop()