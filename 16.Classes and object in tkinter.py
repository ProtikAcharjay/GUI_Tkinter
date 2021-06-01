from tkinter import *
class Protik(Tk):
    def __init__(self):
        #in every class we need a contructor and here in this contructor,self is out previous root..))
        super().__init__() #we have to call supper class to ensure calling supper class constructor
        self.geometry("500x350")
        self.title("16.Classes and objects in Tkinter")
    def status(self):
        self.var=StringVar()
        self.var.set("Ready")
        self.statusbar=Label(self,textvariable=self.var, relief=SUNKEN,anchor="w")
        self.statusbar.pack(side=BOTTOM,fill=X)

if __name__ == '__main__':
    gui=Protik()  #now in the main function we have gui that is our previous root and in the classes this is called as self
    gui.status()
    gui.mainloop()