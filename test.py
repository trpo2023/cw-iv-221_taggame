import unittest
from tkinter import Tk
from src.game_logic import GameLogic
from src.game_window import GameWindow

# Попытайтесь импортировать модуль для создания виртуального дисплея
try:
    import xvfbwrapper
    xvfb = xvfbwrapper.Xvfb(width=1920, height=1080)
    xvfb.start()
except ImportError:
    xvfb = None

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

# Остановите виртуальный дисплей после выполнения тестов
if xvfb:
    xvfb.stop()
