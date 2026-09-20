from tkinter import *
from datetime import date
root=Tk()
root.title("Getting started with widgets")
root.geometry('400x300')
lbl=Label(text="Hey There!!",fg="white", bg="#072f5f", height=1,width=300)
lbl_name=Label(text="full name",bg="#3859d3")
entry_name=Entry()

def display():
    name=entry_name.get()
    global message
    message="Welcome to the Applications!!\n Todays date is: "
    greet="Hello" + name + "\n"
    textbox.insert(END,greet)
    textbox.insert(END,message)
    textbox.insert(END,date.today())

textbox=Text(height=3)
btn=Button(text="begin",command=display,height=1,bg="#1261a0",fg="#1261a0")

lbl.pack()
lbl_name.pack()
entry_name.pack()
btn.pack()
textbox.pack()
root.mainloop()
