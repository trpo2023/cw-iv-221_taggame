from tkinter import *
from tkinter import ttk, messagebox
from random import randint
import tkinter.font as tkFont
from functools import partial
from tkinter.messagebox import showinfo
from .game_logic import GameLogic

class GameWindow:
    def __init__(self, root):
        self.root = root
        self.logic = GameLogic()
        self.flag = 0
        self.change_index = []
        self.Bt = []
        self.Btn = []
        self.C = []
        self.w = 500
        self.h = 500

        self.root["bg"] = self.from_rgb(0, 0, 0)
        self.canvas = Canvas(bg="white", width=600, height=600)
        self.canvas.focus_set()
        self.pixelVirtual = PhotoImage(width=1, height=1)
        self.fontStyle = tkFont.Font(family="Lucida Grande", size=20)
        self.labelExample = Label(self.root, text="20", font=self.fontStyle)
        self.pixelVirtual = PhotoImage(width=1, height=1)
        self.root.option_add("*tearOff", FALSE)

        self.main_menu = Menu()
        self.file_menu = Menu()
        self.file_menu.add_command(label="3x3", command=self.new_game(3))
        self.file_menu.add_command(label="4x4", command=self.new_game(4))
        self.file_menu.add_command(label="5x5", command=self.new_game(5))
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Выход", command=self.root.destroy)

        self.main_menu.add_cascade(label="Новая игра", menu=self.file_menu)
        self.main_menu.add_cascade(label="Помощь", command=self.edit_click)
        self.main_menu.add_cascade(label="Инфо", command=self.about)

        self.root.config(menu=self.main_menu)

    def from_rgb(self, r, g, b):
        return str(f'#{r:02x}{g:02x}{b:02x}')

    def edit_click(self):
        messagebox.showinfo("GUI Python", "Чтобы начать игру, нажмите на кнопку Новая Игра, и выберите размер поля.\n\nЦель игры:\nрасставить все цифры по порядку так, чтобы клетка\nс цифрой 1 находилась сверху слева,а пустая клетка - снизу справа.\n\nПравила:\nВы можете менять местами только клетку с цифрой с пустой клеткой, и только по горизонтали и вертикали!")

    def about(self):
        messagebox.showinfo("GUI Python", "Разработал Козлов Семён, студент группы ИВ-221")

    def proverka(self):
        if self.C == self.Bt:
            self.root["bg"] = self.from_rgb(255, 127, 39)
            showinfo(title="Победа!", message="Игра окончена, вы победили!")
        else:
            self.root["bg"] = self.from_rgb(20, 20, 20)
            

    def clicked(self, i, j, n):
        f = False
        if self.Bt[i][j] == "":
            f = True
        if i - 1 >= 0:
            if self.Bt[i - 1][j] == "":
                f = True
        if j - 1 >= 0:
            if self.Bt[i][j - 1] == "":
                f = True
        if i + 1 <= n - 1:
            if self.Bt[i + 1][j] == "":
                f = True
        if j + 1 <= n - 1:
            if self.Bt[i][j + 1] == "":
                f = True
        if f:
            if self.flag == 0:
                self.change_index.append(i)
                self.change_index.append(j)
                self.Btn[i][j]["bg"] = self.from_rgb(44, 117, 255)
                print("Clic", i, j)
                self.flag += 1
            elif self.flag == 1:
                if self.Bt[self.change_index[0]][self.change_index[1]] == "" or self.Bt[i][j] == "":
                    self.change_index.append(i)
                    self.change_index.append(j)
                    print(self.change_index)
                    self.Btn[self.change_index[0]][self.change_index[1]]["bg"] = self.from_rgb(0, 0, 255)
                    x = self.Btn[int(self.change_index[0])][int(self.change_index[1])]["text"]
                    y = self.Btn[int(self.change_index[2])][int(self.change_index[3])]["text"]
                    self.Btn[int(self.change_index[0])][int(self.change_index[1])]["text"] = y
                    self.Btn[int(self.change_index[2])][int(self.change_index[3])]["text"] = x
                    self.Bt[self.change_index[0]][self.change_index[1]], self.Bt[self.change_index[2]][self.change_index[3]] = self.Bt[self.change_index[2]][self.change_index[3]], self.Bt[self.change_index[0]][self.change_index[1]]

                    print("Clic", i, j)
                    self.flag = 0
                    self.change_index = []

                    self.proverka()

    def mixed(self, n):
        for i in range(n ** 2):
            x1 = randint(0, n - 1)
            y1 = randint(0, n - 1)
            x2 = randint(0, n - 1)
            y2 = randint(0, n - 1)
            self.Bt[x1][y1], self.Bt[x2][y2] = self.Bt[x2][y2], self.Bt[x1][y1]
            x = self.Btn[x1][y1]["text"]
            y = self.Btn[x2][y2]["text"]
            self.Btn[x1][y1]["text"] = y
            self.Btn[x2][y2]["text"] = x

    def new_game(self, m):
        def func():
            for i in self.Btn:
                for j in i:
                    j.destroy()

            self.Bt = [[0] * m for i in range(m)]
            self.Btn = [[0] * m for i in range(m)]
            self.C = [[0] * m for i in range(m)]
            index = 1
            for i in range(m):
                self.root.columnconfigure(index=i, weight=1)
            for j in range(m):
                self.root.rowconfigure(index=j, weight=1)
            for i in range(m):
                for j in range(m):
                    self.Bt[i][j] = j + i * m + 1
                    self.Btn[i][j] = Button(
                        self.root,
                        text=str(index),
                        image=self.pixelVirtual,
                        width=self.w // m,
                        height=self.h // m,
                        command=partial(self.clicked, i, j, m),
                        compound="c",
                        bg="blue",
                        activebackground="cyan",
                        fg="white",
                        font="Courier 50",
                    )
                    self.Btn[i][j].grid(row=i, column=j)
                    index += 1
            self.Btn[m - 1][m - 1]["text"] = ""
            self.Bt[m - 1][m - 1] = ""
            for i in range(m):
                for j in range(m):
                    self.C[i][j] = self.Bt[i][j]
            self.mixed(m)

        return func
