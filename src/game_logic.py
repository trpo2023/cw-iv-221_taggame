from random import randint

class GameLogic:
    def init(self):
        pass

    def from_rgb(self, r, g, b):
        return str(f'#{r:02x}{g:02x}{b:02x}')


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