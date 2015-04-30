from PySide import QtGui


class DuckTagsAppFilesPanel(QtGui.QListWidget):
    def __init__(self, *args, **kwargs):
        super(DuckTagsAppFilesPanel, self).__init__(*args, **kwargs)