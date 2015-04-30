from DuckTagsView.DuckTagsAppMenuBar import DuckTagsAppMenuBar
from DuckTagsView.DuckTagsAppToolBar import DuckTagsAppToolBar

from PySide import QtGui


class DuckTagsApp(QtGui.QMainWindow):
    def __init__(self):
        super(DuckTagsApp, self).__init__()

        self.min_size = self.__compute_app_size__()
        self.app_name = 'DuckTags'
        self.icon_path = ''

        self.__init_ui__()

    def on_close(self):
        self.close()

    def __init_ui__(self):
        self.setWindowTitle(self.app_name)
        self.setWindowIcon(QtGui.QIcon(self.icon_path))

        self.resize(*self.min_size)
        self.__center_window__()

        menu_bar = DuckTagsAppMenuBar(parent=self)
        self.setMenuBar(menu_bar)

        tool_bar = DuckTagsAppToolBar(parent=self)
        self.addToolBar(tool_bar)

        self.show()

    def __center_window__(self):
        center_pos = QtGui.QDesktopWidget().availableGeometry().center()
        frame_rect = self.frameGeometry()

        frame_rect.moveCenter(center_pos)
        self.move(frame_rect.topLeft())

    @staticmethod
    def __compute_app_size__():
        width = QtGui.QDesktopWidget().availableGeometry().width() / 2
        height = QtGui.QDesktopWidget().availableGeometry().height() * 0.66
        return width, height