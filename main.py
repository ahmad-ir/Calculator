from tkinter import Tk, Button, Entry, StringVar



class Calculator():


    def __init__(self, master):
       master.title('Calculator') 
       master.geometry("357x420+0+0") 
       master.resizable(False, False)
       master.config(bg = 'gray')


root = Tk()
calculator = Calculator(root)
root.mainloop()