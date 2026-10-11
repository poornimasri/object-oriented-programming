from tkinter import *
root=Tk()
root.title("Login App")
root.geometry("400x400")
frame=Frame(master=root,height=200,width=360,bg="#D0EFFF")
label1=Label(frame,text="Full Name",bg="#3895d3",fg="white",width=12)
label2=Label(frame,text="Email ID",bg="#3895d3",fg="white",width=12)
label3=Label(frame,text="Enter Password",bg="#3895d3",fg="white",width=12)
nameentry=Entry(frame,bg="white",fg="black")
emailentry=Entry(frame,bg="white",fg="black")
passentry=Entry(frame,show='*',bg="white",fg="black")

def display():
    name=nameentry.get()
    greet="Hey "+name
    message="\n Congragulations for your new account"
    textbox.insert(END,greet) 
    textbox.insert(END,message)

textbox=Text(bg="#bebebe",fg="black")
btn=Button(text="Create Account",command=display,bg="red")

frame.place(x=20,y=0)
label1.place(x=20,y=20)
nameentry.place(x=150,y=20)
label2.place(x=20,y=80)
emailentry.place(x=150,y=80)
label3.place(x=20,y=140)
passentry.place(x=150,y=140)

btn.place(x=130,y=210)
textbox.place(y=250)

root.mainloop()

