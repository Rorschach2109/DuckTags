from Utils.DuckTagsUtils import DuckTagsUtils

from PySide import QtGui


class DuckTagsAppMenuBar(QtGui.QMenuBar):
    def __init__(self, *args, **kwargs):
        super(DuckTagsAppMenuBar, self).__init__(*args, **kwargs)

        self.current_pattern_index = None

        self.__add_file_section__()
        self.__add_edit_section__()
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
        self.__add_select_folder__(file_menu)
        self.__add_select_all__(file_menu)
        file_menu.addSeparator()
        self.__add_exit_action__(file_menu)

    def __add_select_folder__(self, file_menu):
        select_folder_action = QtGui.QAction('&Select Folder', self)
        select_folder_action.setShortcut('Ctrl+O')
        select_folder_action.setStatusTip('Select Folder To Scan Files')

        select_folder_function = self.parent().on_select_folder
        select_folder_action.triggered.connect(select_folder_function)

        file_menu.addAction(select_folder_action)

    def __add_select_all__(self, file_menu):
        select_all_action = QtGui.QAction('&Select All', self)
        select_all_action.setShortcut('Ctrl+W')
        select_all_action.setStatusTip('Select All Files')

        select_all_function = self.parent().on_select_all
        select_all_action.triggered.connect(select_all_function)

        file_menu.addAction(select_all_action)

    def __add_exit_action__(self, file_menu):
        exit_action = QtGui.QAction('&Exit', self)
        exit_action.setShortcut('Ctrl+Q')
        exit_action.setStatusTip('Exit application')

        close_function = self.parent().on_close
        exit_action.triggered.connect(close_function)

        file_menu.addAction(exit_action)

    def __add_edit_section__(self):
        edit_menu = self.addMenu('&Edit')
        self.__add_save_action__(edit_menu)
        self.__add_reorganize_action__(edit_menu)

    def __add_save_action__(self, edit_menu):
        save_action = QtGui.QAction('&Save', self)
        save_action.setShortcut('Ctrl+S')
        save_action.setStatusTip('Save changes')

        save_function = self.parent().on_save
        save_action.triggered.connect(save_function)

        edit_menu.addAction(save_action)

    def __add_reorganize_action__(self, edit_menu):
        reorganize_action = QtGui.QAction('&Reorganize', self)
        reorganize_action.setShortcut('Ctrl+R')
        reorganize_action.setStatusTip('Reorganize Files Structure')

        reorganize_function = self.parent().on_reorganize
        reorganize_action.triggered.connect(reorganize_function)

        edit_menu.addAction(reorganize_action)

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