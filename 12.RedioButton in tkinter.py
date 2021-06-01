from tkinter import *
import tkinter.messagebox as tmsg
root=Tk()
root.geometry("500x350")
root.title("RedioButton In Tkinter")
#function
def order():
    tmsg.showinfo("Order Received", f"We have received your order for {var.get()}\nThanks for ordering")
#variable declear
# var=IntVar()
var=StringVar()
var.set(0)
#var.set(1)
#label
Label(root, text="What you would like to have?",font="newtimesroman 20 bold", justify=LEFT).pack(anchor="w")

#redio buttons
redio=Radiobutton(root,text="Vat",padx=12,variable= var, value="Vat").pack(anchor="w")
redio=Radiobutton(root,text="polao",padx=12,variable= var, value="polao").pack(anchor="w")
redio=Radiobutton(root,text="Biriani",padx=12,variable= var, value="Biriani").pack(anchor="w")
#button
Button(text="Order Now",command =order).pack()

root.mainloop()