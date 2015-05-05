from DuckTagsView.DuckTagsAppMenuBar import DuckTagsAppMenuBar
from DuckTagsView.DuckTagsAppToolBar import DuckTagsAppToolBar
from DuckTagsView.DuckTagsAppStatusBar import DuckTagsAppStatusBar
from DuckTagsView.DuckTagsAppMainWidget import DuckTagsAppMainWidget
from Utils.DuckTagsExceptions import DuckTagsRenameException

from PySide import QtGui


class DuckTagsApp(QtGui.QMainWindow):
    def __init__(self):
        super(DuckTagsApp, self).__init__()

        self.min_size = self.__compute_app_size__()
        self.app_name = 'DuckTags'
        self.icon_path = ''

        self.main_widget = DuckTagsAppMainWidget(parent=self)

        self.__init_ui__()

    def on_close(self):
        self.close()

    def on_uppercase(self):
        try:
            edited_files_number = self.main_widget.on_uppercase()
        except DuckTagsRenameException as rename_exception:
            message = 'Cannot Rename File %s' % rename_exception.error_path
        else:
            message = 'Edited %s Files' % edited_files_number
        self.on_show_status_message(message)

    def on_save(self):
        saved_files_number = self.main_widget.on_save()
        self.on_show_status_message('Saved %s Files' % saved_files_number)

    def on_reorganize(self):
        try:
            reorganized_files_number = self.main_widget.on_reorganize()
        except DuckTagsRenameException as rename_exception:
            message = 'Cannot Rename File %s' % rename_exception.error_path
        else:
            message = 'Reorganized %s Files' % reorganized_files_number
        self.on_show_status_message(message)

    def on_select_all(self):
        files_number = self.main_widget.on_select_all()
        self.on_show_status_message('Selected %s Files' % files_number)

    def on_select_file(self, selected_files_number):
        self.on_show_status_message('Selected %s Files' % selected_files_number)

    def on_select_folder(self):
        self.main_widget.on_select_folder()

    def on_show_status_message(self, message):
        self.statusBar().showMessage(message)

    def get_reorganize_pattern_index(self):
        return self.menuBar().get_reorganize_pattern_index()

    def __init_ui__(self):
        self.setWindowTitle(self.app_name)
        self.setWindowIcon(QtGui.QIcon(self.icon_path))

        self.resize(*self.min_size)
        self.__center_window__()
        self.__add_bars__()

        self.setCentralWidget(self.main_widget)

        self.show()

    def __center_window__(self):
        center_pos = QtGui.QDesktopWidget().availableGeometry().center()
        frame_rect = self.frameGeometry()

        frame_rect.moveCenter(center_pos)
        self.move(frame_rect.topLeft())

    def __add_bars__(self):
        menu_bar = DuckTagsAppMenuBar(parent=self)
        self.setMenuBar(menu_bar)

        tool_bar = DuckTagsAppToolBar(parent=self)
        self.addToolBar(tool_bar)

        status_bar = DuckTagsAppStatusBar(parent=self)
        self.setStatusBar(status_bar)

    @staticmethod
    def __compute_app_size__():
        width = QtGui.QDesktopWidget().availableGeometry().width() / 2
        height = QtGui.QDesktopWidget().availableGeometry().height() * 0.66
        return width, height