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

