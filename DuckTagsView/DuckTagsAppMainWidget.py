from DuckTagsView.DuckTagsAppMetadataPanel import DuckTagsAppMetadataPanel
from DuckTagsView.DuckTagsAppFilesPanel import DuckTagsAppFilesPanel

from PySide import QtGui


class DuckTagsAppMainWidget(QtGui.QWidget):
    def __init__(self, *args, **kwargs):
        super(DuckTagsAppMainWidget, self).__init__(*args, **kwargs)

        self.__init_layout__()

    def __init_layout__(self):
        main_box = QtGui.QHBoxLayout()

        metadata_panel = DuckTagsAppMetadataPanel()
        main_box.addLayout(metadata_panel, stretch=5)
        files_panel = DuckTagsAppFilesPanel()
        main_box.addWidget(files_panel, stretch=7)

        self.setLayout(main_box)