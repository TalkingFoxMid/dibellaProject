from PyQt5.QtGui import QColor


class ColorProvider:
    def __init__(self):
        self.state = 0
    def getColor(self):
        x = self.state
        self.state += 1
        return QColor((x*2) % 255,(x*3) % 255,x % 255)