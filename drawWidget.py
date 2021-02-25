import math

from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QPixmap, QPainter, QPen, QBrush, QColor, QWheelEvent, QMouseEvent
from PyQt5.QtWidgets import QLabel

from chunkProvider import ChunkProvider
from color_provider import ColorProvider
from theState import TheState


class DrawWidget(QLabel):
    def __init__(self):
        self.lastx = 0
        self.lasty = 0
        self.cp: ChunkProvider = ChunkProvider()
        super().__init__()
        self.setPixmap(QPixmap(800, 800))
        self.zoom = 1
        self.bias = 400
        self.mouse_type = 1
        self.center_x = 0
        self.center_y = 0
        self.drawing_pixmap = QPixmap(800, 800)
        self.drawing_pixmap.fill(QColor(255,255,255))
        self.pixmap().fill(QColor(255,255,255))
        self.timer = QTimer()
        self.timer.timeout.connect(self.tick)
        self.timer.start(20)
        self.color_provider = ColorProvider()
        self.state = TheState()
        self.counter = 0

    def tick(self):
        self.counter += 1
        self.state.set_center(self.center_x,
                              self.center_y)
        self.paintDots()
        self.state.tick()

    def mousePressEvent(self, ev: QMouseEvent) -> None:
        self.mouse_type = ev.button()
    def mouseMoveEvent(self, e: QMouseEvent):
        real_x = e.x() + self.center_x - 400
        real_y = e.y() + self.center_y - 400
        x = e.pos().x()
        y = e.pos().y()
        dx = self.lastx - x
        dy = self.lasty - y
        if self.mouse_type == 1:
            clr = self.color_provider.getColor()
            self.state.add_dot(real_x, real_y, clr)
            self.state.add_dot_inv(real_x, real_y, clr)
        else:


            if abs(dx) < 30 and abs(dy) < 30:
                print(dx, dy)
                self.center_x += dx/2
                self.center_y += dy/2
        self.lasty = y
        self.lastx = x

    def wheelEvent(self, a0: QWheelEvent) -> None:

        self.zoom += a0.angleDelta().y()/1200
    def paintDots(self):


        for i in self.state.get_dots():
            self.cp.draw_point(i.x, i.y, self.center_x-400,self.center_y-400, i.color)

        self.cp.draw_chunks(self.pixmap(), self.center_x-400,self.center_y-400, self.zoom)
        self.update()
