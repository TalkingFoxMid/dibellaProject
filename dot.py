class Dot:
    def __init__(self,x , y):
        self.x = x
        self.y = y
        self.setRemoveFlag = False
        self.inv = 1
        self.inv_cooldown = 0
    def invert(self):
        if self.inv_cooldown == 0:
            self.inv *= -1
    def setRemove(self):
        self.setRemoveFlag = True
    def tick(self):
        pass
    def force(self, x, y):
        self.x += x*self.inv*5
        self.y += y*self.inv*5