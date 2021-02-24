from PyQt5.QtGui import QPixmap, QPainter, QColor, QBrush, QPen

from color_provider import ColorProvider


class ChunkProvider:
    def __init__(self):
        self.chunks = {}
        self.color_provider= ColorProvider()
    def get_chunk_sign(self, x, y):
        zx = 0
        zy = 0
        x += 400
        y += 400
        if x < 0:
            x *= -1
            zx = 1
        if y < 0:
            y *= -1
            zy = 1
        x = ((x // 800))
        y = ((y//800))
        if zx == 1:
            x = -1*(x+1)
        if zy == 1:
            y = -1*(y+1)

        return (x, y)
    def get_pixmap_chunk(self, sgn):
        self.create_chunk_if_need(sgn)
        return self.chunks[sgn]
    def create_chunk_if_need(self,sign):
        if sign not in self.chunks:
            self.chunks[sign] = QPixmap(800, 800)
            self.chunks[sign].fill(QColor(255,255,255))
    def chunk_start(self, xleft,yleft, sign):
        chunk_x_pos = sign[0]*800-400
        chunk_y_pos = sign[1]*800-400

        return (chunk_x_pos - xleft, chunk_y_pos - yleft)
    def get_chunks_signs_by_left(self, x, y):
        sns = {self.get_chunk_sign(x, y), self.get_chunk_sign(x + 800, y), self.get_chunk_sign(x, y + 800),
               self.get_chunk_sign(x + 800, y + 800)}
        return sns
    def draw_point(self, rx, ry, leftx, lefty):
        x = rx - leftx
        y = ry - lefty
        cs = self.get_chunk_sign(rx, ry)

        cstart = self.chunk_start(leftx, lefty, cs)

        pm = self.get_pixmap_chunk(cs)
        pen = QPen()
        pen.setColor(self.color_provider.getColor())
        pen.setWidth(3)
        qp = QPainter(pm)
        qp.setBrush(QBrush(QColor(255, 0, 0)))
        qp.setPen(pen)
        qp.drawPoint(x-cstart[0], y-cstart[1])
        qp.end()
    def draw_chunks(self, our_pixmap, xleft, yleft, zoom):
        cks = self.get_chunks_signs_by_left(xleft, yleft)
        qp = QPainter(our_pixmap)
        for i in cks:
            self.create_chunk_if_need(i)
            cr = self.chunk_start(xleft, yleft, i)

            qp.drawPixmap(cr[0]*zoom, cr[1]*zoom, 800*zoom, 800*zoom,self.get_pixmap_chunk(i))
        qp.end()
