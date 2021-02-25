from PyQt5.QtGui import QColor


class ColorProvider:
    def __init__(self):
        self.state = (0,0,-1)
        self.color = [255,255,255]
        self.count = 0
    def getColor(self):

        self.count += 1
        if self.count % 1 == 0:
            self.color[0] += self.state[0]*3
            self.color[1] += self.state[1]*3
            self.color[2] += self.state[2]*3
            if self.state == (0,0,-1) and self.color == [255,255,0]:
                self.state = (0,-1,0)
            if self.state == (0,-1,0) and self.color == [255,0,0]:
                self.state = (0,0,1)
            if self.state == (0,0,1) and self.color == [255,0,255]:
                self.state = (-1,0,0)
            if self.state == (-1,0,0) and self.color == [0,0,255]:
                self.state = (0,1,0)
            if self.state == (0,1,0) and self.color == [0,255,255]:
                self.state = (1,0,0)
            if self.state == (1,0,0) and self.color == [255,255,255]:
                self.state = (0,0,-1)
        red, green, blue = self.color
        return QColor(red, green, blue)