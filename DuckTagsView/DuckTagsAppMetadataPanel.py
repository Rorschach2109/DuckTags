from PySide import QtGui


class DuckTagsAppMetadataPanel(QtGui.QVBoxLayout):
    def __init__(self, *args, **kwargs):
        super(DuckTagsAppMetadataPanel, self).__init__(*args, **kwargs)

        self.Direction = QtGui.QBoxLayout.TopToBottom
