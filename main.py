from tkinter import Tk
from src import *

def main():
    root = Tk()
    root.title("ПЯТНАШКИ")
    root.geometry("600x600")
    game = GameWindow(root)
    root.mainloop()

if __name__ == "__main__":
    main()