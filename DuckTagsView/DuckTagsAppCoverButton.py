import os

from PySide import QtGui
from PySide import QtCore


class DuckTagsAppCoverButton(QtGui.QAbstractButton):
    def __init__(self, cover_button_size):
        super(DuckTagsAppCoverButton, self).__init__()

        self.no_cover_image_path = ''
        self._cover_image_path = str()
        self.button_size = cover_button_size

        self.setEnabled(False)
        self.clicked.connect(self.on_click)

    @property
    def cover_image_path(self):
        return self._cover_image_path

    @cover_image_path.setter
    def cover_image_path(self, new_path):
        if new_path != self.cover_image_path:
            self._cover_image_path = new_path
            self.update()

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)

        button_image_path = self.cover_image_path if self.cover_image_path else self.no_cover_image_path
        painter.drawPixmap(QtCore.QRect(0, 0, *self.button_size), QtGui.QPixmap(button_image_path))

    def sizeHint(self):
        return QtCore.QSize(*self.button_size)

    def on_click(self):
        file_dialog = QtGui.QFileDialog()
        file_dialog.setFileMode(QtGui.QFileDialog.ExistingFile)
        file_dialog.setReadOnly(True)

        cover_filter = '*.png;;*.jpg'

        cover_file_path = file_dialog.getOpenFileName(caption="Select File", dir=os.getcwd(), filter=cover_filter)

        if cover_file_path[0]:
            self.cover_image_path = cover_file_path[0]

    def draw_cover(self, cover_path):
        self.setEnabled(True)
        self.cover_image_path = cover_path

    def clean_button_image(self):
        self.cover_image_path = ''
        self.setEnabled(False)