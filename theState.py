from difura import Difura
from dot import Dot
import math

class TheState:
    def __init__(self):
        self.difura = Difura()
        self.dots = []
        self.center_x = 0
        self.center_y = 0
    def set_center(self, x, y):
        self.center_x = x
        self.center_y = y
    def tick(self):
        for i in self.dots:
            i.tick()
            gangle = self.difura.get_angle(i.x, i.y)

            if abs(i.x - self.center_x) < 900 and abs(i.y - self.center_y) < 900:
                i.force(math.cos(gangle),
                        math.sin(gangle))


    def get_dots(self):
        if (len(self.dots) > 1000):
            self.dots = self.dots[100:]
        return self.dots
    def add_dot_inv(self, x, y):
        dot = Dot(x, y)
        dot.invert()
        self.dots.append(dot)
    def add_dot(self, x, y):
        self.dots.append(Dot(x, y))