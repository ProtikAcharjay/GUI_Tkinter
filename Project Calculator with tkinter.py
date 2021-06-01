from tkinter import *
root=Tk()
root.geometry("500x700")
root.title("Calculator by Protik")
root.wm_iconbitmap("1.ico")
#functions
def click(event):
    global screenvar
    text=event.widget.cget("text")
    print(text)
    if text=="=":
        if screenvar.get().isdigit():
            try:
                value=int(screenvar.get())
            except Exception as e:
                print(e)
                value="Error"
        else:
            try:
                value=eval(screenvar.get())
            except Exception as e:
                print(e)
                value="Error"
        screenvar.set(value)
        screen.update()
    elif text=="C":
        screenvar.set("")
        screen.update()
    else:
        screenvar.set(screenvar.get()+text)
        screen.update()
#variables
screenvar=StringVar()
#Entries
screen= Entry(root,textvar=screenvar,font="newtimesroman 33 bold")
screen.pack(fill=X,padx=7,pady=14,ipadx=11)
#Frames
f1= Frame(root,bg="grey")
f1.pack()
f2= Frame(root,bg="grey")
f2.pack()
f3= Frame(root,bg="grey")
f3.pack()
f4= Frame(root,bg="grey")
f4.pack()
f5= Frame(root,bg="grey")
f5.pack()
#labels
#buttons for frame one
b1=Button(f1,text="9",font="newtimesroman 33 bold",padx=12,pady=10)
b1.pack(side=LEFT,padx=11,pady=11)
b1.bind("<Button-1>",click)

b1=Button(f1,text="8",font="newtimesroman 33 bold",padx=12,pady=10)
b1.pack(side=LEFT,padx=11,pady=11)
b1.bind("<Button-1>",click)

b1=Button(f1,text="7",font="newtimesroman 33 bold",padx=12,pady=10)
b1.pack(side=LEFT,padx=11,pady=11)
b1.bind("<Button-1>",click)

#buttons for frame two
b1=Button(f2,text="6",font="newtimesroman 33 bold",padx=12,pady=10)
b1.pack(side=LEFT,padx=11,pady=11)
b1.bind("<Button-1>",click)

b1=Button(f2,text="5",font="newtimesroman 33 bold",padx=12,pady=10)
b1.pack(side=LEFT,padx=11,pady=11)
b1.bind("<Button-1>",click)

b1=Button(f2,text="4",font="newtimesroman 33 bold",padx=12,pady=10)
b1.pack(side=LEFT,padx=11,pady=11)
b1.bind("<Button-1>",click)

#buttons for frame three
b1=Button(f3,text="3",font="newtimesroman 33 bold",padx=12,pady=10)
b1.pack(side=LEFT,padx=11,pady=11)
b1.bind("<Button-1>",click)

b1=Button(f3,text="2",font="newtimesroman 33 bold",padx=12,pady=10)
b1.pack(side=LEFT,padx=11,pady=11)
b1.bind("<Button-1>",click)

b1=Button(f3,text="1",font="newtimesroman 33 bold",padx=12,pady=10)
b1.pack(side=LEFT,padx=11,pady=11)
b1.bind("<Button-1>",click)
#buttons for frame four
b1=Button(f4,text="0",font="newtimesroman 33 bold",padx=12,pady=10)
b1.pack(side=LEFT,padx=14,pady=11)
b1.bind("<Button-1>",click)

b1=Button(f4,text="-",font="newtimesroman 33 bold",padx=12,pady=10)
b1.pack(side=LEFT,padx=14,pady=11)
b1.bind("<Button-1>",click)

b1=Button(f4,text="*",font="newtimesroman 33 bold",padx=12,pady=10)
b1.pack(side=LEFT,padx=14,pady=11)
b1.bind("<Button-1>",click)
#buttons for frame five
b1=Button(f5,text="/",font="newtimesroman 33 bold",padx=12,pady=10)
b1.pack(side=LEFT,padx=12,pady=11)
b1.bind("<Button-1>",click)

b1=Button(f5,text="C",font="newtimesroman 33 bold",padx=12,pady=10)
b1.pack(side=LEFT,padx=12,pady=11)
b1.bind("<Button-1>",click)

b1=Button(f5,text="=",font="newtimesroman 33 bold",padx=12,pady=10)
b1.pack(side=LEFT,padx=12,pady=11)
b1.bind("<Button-1>",click)

root.mainloop()