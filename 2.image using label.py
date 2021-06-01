from tkinter import *
from PIL import Image,ImageTk

root = Tk()
root.geometry("4000x2248")
# normally tkinter only support pnj format
#for jpg/jpeg format
image=Image.open("1.jpeg")
photo=ImageTk.PhotoImage(image)

# photo = PhotoImage(file="photo.png")
label = Label(image=photo)
label.pack()
root.mainloop()