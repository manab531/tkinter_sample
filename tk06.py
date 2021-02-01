import tkinter as tk

def print_txtval():
    val_en=en.get()
    print(val_en)
root =tk.Tk()
root.title('get text box')
root.geometry('450x250')
lb=tk.Label(text='LABEL')
en=tk.Entry()
bt=tk.Button(text='BUTTON',command=print_txtval)
lb.pack()
en.pack()
bt.pack()
root.mainloop()