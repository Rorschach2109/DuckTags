from PySide import QtGui


class DuckTagsAppStatusBar(QtGui.QStatusBar):
    def __init__(self, *args, **kwargs):
        super(DuckTagsAppStatusBar, self).__init__(*args, **kwargs)
        self.showMessage('DuckTags by AK')