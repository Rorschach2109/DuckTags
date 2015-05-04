from PySide import QtGui


class DuckTagsAppToolBar(QtGui.QToolBar):
    def __init__(self, *args, **kwargs):
        super(DuckTagsAppToolBar, self).__init__(*args, **kwargs)

        self.setMovable(False)

        self.__add_save_action__()

    def __add_save_action__(self):
        self.save_action = QtGui.QAction('Save', self.parent())
        self.save_action.setShortcut('Ctrl+S')
        self.save_action.triggered.connect(self.parent().on_save)

        self.addAction(self.save_action)