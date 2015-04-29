from PySide import QtGui


class DuckTagsAppMenuBar(QtGui.QMenuBar):
    def __init__(self, *args, **kwargs):
        super(DuckTagsAppMenuBar, self).__init__(*args, **kwargs)

        self.__add_file_section__()

    def __add_file_section__(self):
        file_menu = self.addMenu('&File')

        self.__add_exit_action__(file_menu)

    def __add_exit_action__(self, file_menu):
        exit_action = QtGui.QAction('&Exit', self)
        exit_action.setShortcut('Ctrl+Q')
        exit_action.setStatusTip('Exit application')

        close_function = self.parent().on_close
        exit_action.triggered.connect(close_function)

        file_menu.addAction(exit_action)