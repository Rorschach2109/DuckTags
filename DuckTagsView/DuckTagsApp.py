from DuckTagsView.DuckTagsAppMenuBar import DuckTagsAppMenuBar
from DuckTagsView.DuckTagsAppToolBar import DuckTagsAppToolBar
from DuckTagsView.DuckTagsAppMainWidget import DuckTagsAppMainWidget

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

    def on_save(self):
        print 'on_save'

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

    @staticmethod
    def __compute_app_size__():
        width = QtGui.QDesktopWidget().availableGeometry().width() / 2
        height = QtGui.QDesktopWidget().availableGeometry().height() * 0.66
        return width, height