from tkinter import Tk
from src.game_window import GameWindow


def main():
    root = Tk()
    root.title("ПЯТНАШКИ")
    root.geometry("600x600")
    game = GameWindow(root)
    root.mainloop()

if __name__ == "__main__":
    main()
