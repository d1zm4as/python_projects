import tkinter as tk 
from tkinter import ttk

def hello():
    print('Hello')

# window
window = tk.Tk()
window.title("Window and Widgets")
window.geometry('400x250')



#tkk text
text = tk.Text(master = window) # colocando o texto na window


#ttk entry

entry = ttk.Entry(master =window)

entry.pack()

#ttk label
label  = ttk.Label(master = window,text = 'my label')
label.pack()


#ttk button

button  = ttk.Button(master = window, text = 'A button', command = lambda:print("hello"))
button.pack()


#Run

window.mainloop()
#updates the gui and checks for events(button clicks, mouse, closing window)