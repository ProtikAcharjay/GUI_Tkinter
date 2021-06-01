from tkinter import *

root = Tk()
root.geometry("500x300")
root.title("Protik Acharjay")
# Important label options in tkinter
# text - adds the text
# bd - background
# fg - foreground
# font - sets the font
# padx - x padding
# pady - y padding
# relief - border styling - SUNKEN,RAISED,GROOVE,RIDGE

title_label= Label(text='''Student | Quick Learner | Singer | Public speaker with different perspectives
~Love to play football~
~Always stay positive & motivated, also keep others motivated~
Favourite quote: Start Now
Prefer staying away from negative and toxic personalities.
Thank You''',bg="orange", fg="purple", padx=111, pady=90, font=("Times New Roman", 11,"bold"), borderwidth=3, relief=RAISED)

# Important pack options in tkinter
# anchor= nw / ne / se / sw
# side= top / bottom / left / right
# fill=make big and window will be expand
# padx + pady

title_label.pack(side=LEFT, fill=Y, padx= 12, pady=10)
root.mainloop()