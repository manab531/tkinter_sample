import tkinter as tk


def print_txtval():
    val_en=en.get()
    val_en2=en2.get()
    val_en3=en3.get()
    val_en4=en4.get()
    print('name:{} name:{}'.format(val_en,val_en2))
    print(val_en,val_en2)
    print(val_en3)
    print(val_en4)

    en.delete(0, tk.END)
    en2.delete(0, tk.END)
    en3.delete(0, tk.END)
    en4.delete(0, tk.END)

    en4.insert(0,'AP')

def clear():
    print('पुन : लेख्नुहोस ')

root =tk.Tk()
root.title('get text box')
root.geometry('450x250')



lb=tk.Label(text='आफ्नो नाम लेख्नुहोस 名前', font=("20"))
en=tk.Entry()
en.insert(0,'first name')
lb2=tk.Label(text='आफ्नो थर लेख्नुहोस 苗字', font=("20"))
en2=tk.Entry()
en2.insert(0,'last name')
lb3=tk.Label(text='आफ्नो जन्म मिति  लेख्नुहोस 生年月日', font=("20"))
en3=tk.Entry()
en3.insert(0,'year only')
lb4=tk.Label(text='where are you born?')
en4=tk.Entry(text='メッセージ')
en4.insert(0,'country')


bt=tk.Button(text='पक्का गर्नुहोस OK', relief='raised', font=("20"),command=print_txtval)
[widget.pack() for widget in [lb,en,lb2,en2,lb3,en3,lb4,en4,bt]]


bt1=tk.Button(bitmap='question',command=clear)
bt1.pack()



root.mainloop()