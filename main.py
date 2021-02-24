from PyQt5.QtWidgets import QMainWindow, QApplication

from drawWidget import DrawWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setCentralWidget(DrawWidget())


app = QApplication([])
win = MainWindow()
win.show()
app.exec_()