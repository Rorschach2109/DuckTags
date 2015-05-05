from PySide import QtGui


class DuckTagsAppToolBar(QtGui.QToolBar):
    def __init__(self, *args, **kwargs):
        super(DuckTagsAppToolBar, self).__init__(*args, **kwargs)

        self.setMovable(False)

        self.__add_save_action__()
        self.__add_reorganization_action__()
        self.__add_select_all_action__()
        self.__add_uppercase_action__()

    def __add_save_action__(self):
        save_action = QtGui.QAction('Save', self.parent())
        save_action.setStatusTip('Save Changes')
        save_action.triggered.connect(self.parent().on_save)

        self.addAction(save_action)

    def __add_reorganization_action__(self):
        reorganization_action = QtGui.QAction('Reorganize', self.parent())
        reorganization_action.setStatusTip('Reorganize files')
        reorganization_action.triggered.connect(self.parent().on_reorganize)

        self.addAction(reorganization_action)

    def __add_select_all_action__(self):
        select_all_action = QtGui.QAction('Select All', self.parent())
        select_all_action.setStatusTip('Select All Files')
        select_all_action.triggered.connect(self.parent().on_select_all)

        self.addAction(select_all_action)

    def __add_uppercase_action__(self):
        uppercase_action = QtGui.QAction('Uppercase Tags', self.parent())
        uppercase_action.setStatusTip('Convert Tags To Uppercase')
        uppercase_action.triggered.connect(self.parent().on_uppercase)

        self.addAction(uppercase_action)