from tkinter import *
root=Tk()
canvas_width=800
canvas_height=400
root.geometry(f"{canvas_width}x{canvas_height}")
root.title("Canvas and Event")
#function
def pro(event):
    print("My name is Pro")
#canvas
canvas_widget= Canvas(root, width=canvas_width, height=canvas_height)
canvas_widget.grid()

canvas_widget.create_text(50,50,text="Protik")
canvas_widget.create_line(0,0,800,400)
#Event
event_widget= Button(root, text="click here")
event_widget.grid(row=2, column=5)
#event handelling with functions
event_widget.bind("<Button-1>",pro)
event_widget.bind("<Double-1>", quit)

root.mainloop()