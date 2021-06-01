from tkinter import *
import tkinter.messagebox as tmsg
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os

if __name__ == '__main__':
    #basic tkinter setup
    root=Tk()
    root.title("Untitled ~ Pro-NotePad")
    root.wm_iconbitmap("1.ico")
    root.geometry("600x600")
    #functions
    def newfile():
        global file
        root.title("Untitled ~ Pro-NotePad")
        file=None
        textarea.delete(1.0,END)
    def openfile():
        global file
        file=askopenfilename(defaultextension=".txt",filetype=[("All Files","*.*"),("Text Documents","*.text")])
        if file=="":
            file=None
        else:
            root.title(os.path.basename(file)+" ~ Pro-Notepad")
            textarea.delete(1.0,END)
            f=open(file,"r")
            textarea.insert(1.0,f.read())
            f.close()
    def savefile():
        global file
        if file==None:
            file=asksaveasfilename(initialfile='Untitled.txt',defaultextension=".txt",filetype=[("All Files","*.*"),("Text Documents","*.txt")])
            if file=="":
                file=None
            else:  #saving as a new file
                f=open(file,"w")
                f.write(textarea.get(1.0,END))
                f.close()
                root.title(os.path.basename(file)+" ~ Pro-Notepad")
                # print("File saved")
        else:
            # saving the file
            f = open(file, "w")
            f.write(textarea.get(1.0, END))
            f.close()

    def exitfile():
        root.destroy()
    def cut():
        textarea.event_generate(("<<Cut>>"))
    def copy():
        textarea.event_generate(("<<Copy>>"))
    def paste():
        textarea.event_generate(("<<Paste>>"))
    def about():
        tmsg.showinfo("Pro-NotePad","Developed By Protik Acharjay\nContact in protik7777777@gmail.com")

    #Text area adding
    textarea=Text(root,font="newtimesroman 14 bold")
    file=None
    textarea.pack(fill=BOTH,expand=True,padx=11,pady=11)
    #MenuBar
    menubar=Menu(root)
    #filemenu Start..........
    filemenu=Menu(menubar,tearoff=0)
    #New file opeing
    filemenu.add_command(label="New", command=newfile)

    #to open already existing file
    filemenu.add_command(label="Open",command=openfile)
    #to save the current file
    filemenu.add_command(label="Save",command=savefile)
    filemenu.add_separator() #separting the menu
    filemenu.add_command(label="Exit", command=exitfile)
    menubar.add_cascade(label="File",menu=filemenu)
    #filemenu End..........
    #editmenu start.......
    editmenu=Menu(menubar,tearoff=0)
    editmenu.add_command(label="Cut",command=cut)
    editmenu.add_command(label="Copy",command=copy)
    editmenu.add_command(label="Paste",command=paste)
    menubar.add_cascade(label="Edit",menu=editmenu)
    #editmenu Ends.......
    #helpmenu starts.....
    helpmenu=Menu(menubar,tearoff=0)
    helpmenu.add_command(label="About",command=about)
    menubar.add_cascade(label="Help",menu=helpmenu)
    #helpmenu ends........

    root.config(menu=menubar)
    #Adding Scrollbar
    scrollbar=Scrollbar(textarea)
    scrollbar.pack(side=RIGHT,fill=Y)
    scrollbar.config(command=textarea.yview)
    textarea.config(yscrollcommand=scrollbar.set)

    #statusbar in right bottom of our brand
    statusvariable=StringVar()
    statusvariable.set("~Developed By Protik Acharjay~")
    statusbar=Label(root,textvariable=statusvariable,relief=SUNKEN,anchor="e")
    statusbar.pack(side=BOTTOM,fill=X)




    root.mainloop()
