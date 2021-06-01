from tkinter import *
root= Tk()
root.geometry("500x300")
root.title("Protik's Form")
#function for submiting form
def printall():
    # print("Name: ", namevar.get())
    # print("Father's Name: ", fathervar.get())
    # print("Address: ", addressvar.get())
    # print("Location: ", universityvar.get())
    # if privacypolicyvar.get() == 0:
    #     print("Privacy Policy Not Approved")
    # else:
    #     print("Privacy Policy Approved")

    with open("form_records.txt","a") as w:
        w.write(
            f"Name: {namevar.get()}\nFathers Name: {fathervar.get()}\nAddress: {addressvar.get()}\nUnivcersity: {universityvar.get()}"
        )
        if privacypolicyvar.get() == 0:
            w.write("\nPrivacy Policy Not Approved\n")
        else:
            w.write("\nPrivacy Policy Approved\n")
#Labels

title=Label(root,text="_Register Form_",fg="Blue")
name=Label(root, text="Name:",fg="Blue")
father=Label(root, text="Father's Name:",fg="Blue")
address=Label(root, text="Address:",fg="Blue")
university=Label(root, text="University:",fg="Blue")
#lables packing
title.grid(row=0,column=1,pady=15)
name.grid(row=1,column=0)
father.grid(row=2,column=0)
address.grid(row=3,column=0)
university.grid(row=4,column=0)

#variables for entries
namevar=StringVar()
fathervar=StringVar()
addressvar=StringVar()
universityvar=StringVar()
privacypolicyvar=IntVar() #checkbox variable

#Entries
nameentry= Entry(root,textvariable=namevar)
fatherentry= Entry(root,textvariable=fathervar)
addressentry= Entry(root,textvariable=addressvar)
universityentry= Entry(root,textvariable=universityvar)
#packing the entries
nameentry.grid(row=1 , column=1 )
fatherentry.grid(row=2 , column=1 )
addressentry.grid(row=3 , column=1 )
universityentry.grid(row=4 , column=1 )
#checkbox with packing
privacypolicyentry=Checkbutton(text="I am agree with the privacy policy.", variable= privacypolicyvar,fg="Blue")
privacypolicyentry.grid(row=5,column=1)

#Button One liner
Button(text="Submit",command=printall,fg="Blue").grid(row=6, column=1)

root.mainloop()