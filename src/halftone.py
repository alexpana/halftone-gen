import sys

from PyQt5.QtCore import QSize, QPointF, QPoint
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtWidgets import (QApplication, QFrame,
                             QGridLayout, QPushButton)


class HalftoneCanvas(QPushButton):
    def __init__(self, parent=None):
        super(HalftoneCanvas, self).__init__(parent)
        self.setText("Canvas?")
        self.grid_size = 20
        self.max_point_size = 10
        self.min_point_size = 3

    def paintEvent(self, event):
        print("Rendering")
        qp = QPainter()
        qp.begin(self)
        qp.setRenderHint(QPainter.Antialiasing)
        qp.setBrush(QColor(20, 20, 20))
        qp.setPen(QPen(0))

        grid_width = int(self.size().width() / self.grid_size)
        grid_height = int(self.size().height() / self.grid_size)

        for x in range(grid_width + 1):
            for y in range(grid_height + 1):
                grid_point = QPoint(x * self.grid_size if y % 2 == 0 else ((x + 0.5) * self.grid_size),
                                    y * self.grid_size)

                scale_factor = 1 - y / grid_height

                dot_size = self.max_point_size * scale_factor + self.min_point_size * (1 - scale_factor)

                qp.drawEllipse(grid_point, dot_size, dot_size)

        qp.end()

    def sizeHint(self):
        return QSize(800, 600)


class MainWindow(QFrame):
    MESSAGE = "<p>Message boxes have a caption, a text, and up to three " \
              "buttons, each with standard or custom texts.</p>" \
              "<p>Click a button to close the message box. Pressing the Esc " \
              "button will activate the detected escape button (if any).</p>"

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.canvas = HalftoneCanvas()

        layout = QGridLayout()
        layout.setColumnStretch(1, 1)
        # layout.setColumnMinimumWidth(1, 250)
        layout.addWidget(self.canvas, 0, 0)

        self.setLayout(layout)

        self.setWindowTitle("Halftone Generator")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwindow = MainWindow()
    mainwindow.show()

    sys.exit(app.exec_())
