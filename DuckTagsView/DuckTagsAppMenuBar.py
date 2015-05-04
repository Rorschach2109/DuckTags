from Utils.DuckTagsUtils import DuckTagsUtils

from PySide import QtGui


class DuckTagsAppMenuBar(QtGui.QMenuBar):
    def __init__(self, *args, **kwargs):
        super(DuckTagsAppMenuBar, self).__init__(*args, **kwargs)

        self.current_pattern_index = None

        self.__add_file_section__()
        self.__add_reorganize_section__()

    def on_pattern_check(self, checked):
        current_pattern = self.patterns_options[self.current_pattern_index]

        if not checked:
            current_pattern.toggled.disconnect(self.on_pattern_check)
            current_pattern.setChecked(True)
            current_pattern.toggled.connect(self.on_pattern_check)
            return

        current_pattern.toggled.disconnect(self.on_pattern_check)
        current_pattern.setChecked(False)
        current_pattern.toggled.connect(self.on_pattern_check)

        for pattern_option_index in range(len(self.patterns_options)):
            if self.patterns_options[pattern_option_index].isChecked():
                self.current_pattern_index = pattern_option_index
                break

    def get_reorganize_pattern_index(self):
        return self.current_pattern_index

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

    def __add_reorganize_section__(self):
        reorganize_menu = self.addMenu('&Reorganize Patterns')
        self.__add_reorganize_options__(reorganize_menu)

    def __add_reorganize_options__(self, reorganize_menu):
        first_pattern = QtGui.QAction(DuckTagsUtils.file_format_patterns[0][0], self, checkable=True)
        second_pattern = QtGui.QAction(DuckTagsUtils.file_format_patterns[1][0], self, checkable=True)

        self.patterns_options = [first_pattern, second_pattern]

        self.patterns_options[0].setChecked(True)
        self.current_pattern_index = 0

        for pattern_option in self.patterns_options:
            pattern_option.toggled.connect(self.on_pattern_check)

        reorganize_menu.addActions(self.patterns_options)