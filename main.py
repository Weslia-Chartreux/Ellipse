import sys

from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5 import uic
from random import choice


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.do_paint = False
        self.btn.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.run(qp)
            qp.end()

    def run(self, qp):
        qp.setBrush(QColor(255, 255, 0))
        x, y, b = choice(range(654)), choice(range(478)), choice(range(1, 100))
        qp.drawEllipse(x, y, b, b)

    def paint(self):
        self.do_paint = True
        self.repaint()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
