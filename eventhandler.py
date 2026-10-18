from tkinter import *
window=Tk()
window.title("Event handler")
window.geometry("100x100")

def handlekey_press(event):
    """Print the character associated to the key press"""
    print(event.char)

window.bind("<Key>",handlekey_press)

def handle_click(event):
    print("The button was clicked")

button=Button(text="click me")
button.pack()

button.bind("<Button-1>",handle_click)

window.mainloop()