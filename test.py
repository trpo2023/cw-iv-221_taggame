import unittest
from tkinter import Tk
from src.game_logic import GameLogic
from src.game_window import GameWindow

class TestGameLogic(unittest.TestCase):
    def setUp(self):
        self.logic = GameLogic()

    def test_from_rgb(self):
        self.assertEqual(self.logic.from_rgb(255, 0, 0), "#ff0000")
        self.assertEqual(self.logic.from_rgb(0, 255, 0), "#00ff00")
        self.assertEqual(self.logic.from_rgb(0, 0, 255), "#0000ff")


class TestGameWindow(unittest.TestCase):
    def setUp(self):
        self.root = Tk()
        self.window = GameWindow(self.root)

    def test_from_rgb(self):
        self.assertEqual(self.window.from_rgb(255, 0, 0), "#ff0000")
        self.assertEqual(self.window.from_rgb(0, 255, 0), "#00ff00")
        self.assertEqual(self.window.from_rgb(0, 0, 255), "#0000ff")


if __name__ == "__main__":
    unittest.main()