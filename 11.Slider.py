from tkinter import *
import tkinter.messagebox as tmsg
root=Tk()
root.geometry("400x350")
root.title("Slider with Scale()")
#making a slider vertically
# slider= Scale(root,from_=0,to=800)
# slider.pack()

#funtions
def getbit():
    print(f"We have transfered {slider2.get()} Bitcoins in your wallet.")
    #using message method here
    tmsg.showinfo("Gifted",f"We have transfered {slider2.get()} Bitcoins in your wallet.")
#LABEL
Label(root,text="How many bitcoin you want?").pack()

# making slider horizontally
slider2= Scale(root,from_=0,to=100,orient=HORIZONTAL,tickinterval=50)
slider2.set(50)
slider2.pack()
#button
Button(root, text="Get Bitcoins", command=getbit).pack()

root.mainloop()