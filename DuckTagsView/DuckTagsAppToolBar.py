from PySide import QtGui


class DuckTagsAppToolBar(QtGui.QToolBar):
    def __init__(self, *args, **kwargs):
        super(DuckTagsAppToolBar, self).__init__(*args, **kwargs)

        self.setMovable(False)

        self.__add_save_action__()
        self.__add_reorganization_action__()
        self.__add_select_all_action__()

    def __add_save_action__(self):
        save_action = QtGui.QAction('Save', self.parent())
        save_action.setShortcut('Ctrl+S')
        save_action.triggered.connect(self.parent().on_save)

        self.addAction(save_action)

    def __add_reorganization_action__(self):
        reorganization_action = QtGui.QAction('Reorganize', self.parent())
        reorganization_action.setShortcut('Ctrl+R')
        reorganization_action.triggered.connect(self.parent().on_reorganize)

        self.addAction(reorganization_action)

    def __add_select_all_action__(self):
        select_all_action = QtGui.QAction('Select All', self.parent())
        select_all_action.setShortcut('Ctrl+W')
        select_all_action.triggered.connect(self.parent().on_select_all)

        self.addAction(select_all_action)