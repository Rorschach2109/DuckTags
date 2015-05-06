from PySide import QtGui
from PySide import QtCore


class DuckTagsAppCoverButton(QtGui.QAbstractButton):
    def __init__(self, cover_button_size):
        super(DuckTagsAppCoverButton, self).__init__()

        self.no_cover_image_path = ''
        self.cover_image_path = str()
        self.button_size = cover_button_size

        self.clicked.connect(self.on_click)

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)

        button_image_path = self.cover_image_path if self.cover_image_path else self.no_cover_image_path
        painter.drawPixmap(QtCore.QRect(0, 0, *self.button_size), QtGui.QPixmap(button_image_path))

    def sizeHint(self):
        return QtCore.QSize(*self.button_size)

    def on_click(self):
        pass