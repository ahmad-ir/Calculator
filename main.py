from tkinter import Tk
from calculator import *


def main():

    # Create a Tk object
    root = Tk()
    
    # Create a calculator object
    Calculator(root)

    # Run mainloop
    root.mainloop()

if __name__ == "__main__":
    main()