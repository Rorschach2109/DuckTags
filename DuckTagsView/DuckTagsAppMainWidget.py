from DuckTagsView.DuckTagsAppMetadataPanel import DuckTagsAppMetadataPanel
from DuckTagsView.DuckTagsAppFilesPanel import DuckTagsAppFilesPanel

from PySide import QtGui


class DuckTagsAppMainWidget(QtGui.QWidget):
    def __init__(self, *args, **kwargs):
        super(DuckTagsAppMainWidget, self).__init__(*args, **kwargs)

        self.__init_layout__()

    def on_browse_folder(self, selected_directory):
        self.files_panel.on_browse_folder(selected_directory)

    def on_save(self):
        self.metadata_panel.on_save()

    def insert_metadata_tags(self, selected_paths):
        self.metadata_panel.insert_metadata_tags(selected_paths)

    def __init_layout__(self):
        main_box = QtGui.QHBoxLayout()

        self.metadata_panel = DuckTagsAppMetadataPanel()
        main_box.addLayout(self.metadata_panel, stretch=5)

        self.files_panel = DuckTagsAppFilesPanel()
        main_box.addWidget(self.files_panel, stretch=7)

        self.setLayout(main_box)