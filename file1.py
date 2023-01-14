import tkinter as tk
window = tk.Tk()
window.title('file_Menu')
window.geometry('500x500')
string = tk.StringVar()
def selection():
    label.confingtext = ("i like" + string.get())
label = tk.Label(window, bg = '#f00', text = 'have not being chose' )
label.pack()
radio1 = tk.Radiobutton(window,text = 'Python',variable = string,value = 'Python',command = selection)
radio1.pack()
radio2 = tk.Radiobutton(window,text = 'C++',variable = string,value = 'C++',command = selection)
radio2.pack()
window.mainloop()