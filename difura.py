import math


class Difura():
    def get_angle(self, y, x):
        y -= 0
        x -= 0
        y /= 20
        x /= -20
        top_quot = x
        bot_quot = y
        return math.atan2(bot_quot, -top_quot)
