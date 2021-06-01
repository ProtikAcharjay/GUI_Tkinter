from tkinter import *
root=Tk()
root.geometry("500x350")
root.title("ScrollBar In Tkinter")

#for connecting a scrollbar with a widget
#1.widget's yscrollcommand == scrollbar.set
#2.scrollbar.config(command=widget.yveiw)

#scrollbar
scrollbar= Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)
#Listbox to use Scrollbar
listbox=Listbox(root, yscrollcommand=scrollbar.set)
for i in range(101):
    listbox.insert(END,f"~Intem no {i}")
listbox.pack(fill=BOTH,pady=12,padx=24)
scrollbar.config(command=listbox.yview)

root.mainloop()