from tkinter import *
from tkinter import messagebox

root=Tk()
window_size=("200x200")

def messages():
    messagebox.showwarning("Alert!","Stop! virus detected")

def messages2():
    messagebox.showinfo("Greeting","Welcome to coding")

def messages3():
    messagebox.showerror("Error","Close the window")


button=Button(root,text="Scan for virus",command=messages)
button.pack()
button.place(x=40,y=80)

button_2=Button(root,text="Welcome",command=messages2)
button_2.pack()
button.place(x=40,y=40)

button_3=Button(root,text="Check Error",command=messages3)
button_3.pack()
button.place(x=40,y=120)

root.mainloop()