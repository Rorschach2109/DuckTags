from DuckTagsView.DuckTagsAppMenuBar import DuckTagsAppMenuBar
from DuckTagsView.DuckTagsAppToolBar import DuckTagsAppToolBar
from DuckTagsView.DuckTagsAppStatusBar import DuckTagsAppStatusBar
from DuckTagsView.DuckTagsAppMainWidget import DuckTagsAppMainWidget
from DuckTagsView.DuckTagsCustomReorganizationOptionDialog import DuckTagsCustomReorganizationOptionDialog
from Utils.DuckTagsExceptions import DuckTagsRenameException

import functools

from PySide import QtGui


def show_message_with_exception(foo):

    @functools.wraps(foo)
    def wrapper(app):
        try:
            edited_files_number = foo(app)
        except DuckTagsRenameException as rename_exception:
            message = app.rename_exception_message % rename_exception.error_path
        else:
            message = app.edit_message % edited_files_number
        app.on_show_status_message(message)

    return wrapper


class DuckTagsApp(QtGui.QMainWindow):
    def __init__(self):
        super(DuckTagsApp, self).__init__()

        self.min_size = self.__compute_app_size__()
        self.app_name = 'DuckTags'
        self.icon_path = ''

        self.main_widget = DuckTagsAppMainWidget(parent=self)

        self.__init_ui__()
        self.__init_messages__()

    def on_close(self):
        self.close()

    @show_message_with_exception
    def on_uppercase(self):
        return self.main_widget.on_uppercase()

    def on_save(self):
        saved_files_number = self.main_widget.on_save()
        self.on_show_status_message(self.save_message % saved_files_number)

    @show_message_with_exception
    def on_reorganize(self):
        return self.main_widget.on_reorganize()

    def on_select_all(self):
        files_number = self.main_widget.on_select_all()
        self.on_show_status_message(self.select_message % files_number)

    def on_select_file(self, selected_files_number):
        self.on_show_status_message(self.select_message % selected_files_number)

    def on_select_folder(self):
        self.main_widget.on_select_folder()

    def on_show_status_message(self, message):
        self.statusBar().showMessage(message)

    def on_custom_reorganization_option(self):
        self.custom_reorganization_dialog.show()

    def on_custom_reorganization_decline(self):
        self.menuBar().on_custom_reorganization_decline()

    def get_reorganize_pattern_index(self):
        return self.menuBar().get_reorganize_pattern_index()

    def __init_messages__(self):
        self.rename_exception_message = 'Cannot Rename File %s'
        self.select_message = 'Selected %s Files'
        self.save_message = 'Saved %s Files'
        self.edit_message = 'Edited %s Files'

    def __init_ui__(self):
        self.setWindowTitle(self.app_name)
        self.setWindowIcon(QtGui.QIcon(self.icon_path))

        self.resize(*self.min_size)
        self.__center_window__()
        self.__add_bars__()
        self.__create_custom_reorganization_dialog__()

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

    def __create_custom_reorganization_dialog__(self):
        self.custom_reorganization_dialog = DuckTagsCustomReorganizationOptionDialog(parent=self)
        self.custom_reorganization_dialog.setModal(True)

    @staticmethod
    def __compute_app_size__():
        width = QtGui.QDesktopWidget().availableGeometry().width() / 2
        height = QtGui.QDesktopWidget().availableGeometry().height() * 0.66
        return width, height