from PySide import QtGui


class DuckTagsAppToolBar(QtGui.QToolBar):
    def __init__(self, *args, **kwargs):
        super(DuckTagsAppToolBar, self).__init__(*args, **kwargs)

        self.setMovable(False)