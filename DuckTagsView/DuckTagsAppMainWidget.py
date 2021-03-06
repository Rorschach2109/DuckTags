from DuckTagsView.DuckTagsAppMetadataPanel import DuckTagsAppMetadataPanel
from DuckTagsView.DuckTagsAppFilesPanel import DuckTagsAppFilesPanel

from PySide import QtGui


class DuckTagsAppMainWidget(QtGui.QWidget):
    def __init__(self, *args, **kwargs):
        super(DuckTagsAppMainWidget, self).__init__(*args, **kwargs)

        self.metadata_panel_stretch = 5
        self.files_panel_stretch = 7
        self.__init_layout__()

    def on_browse_folder(self, selected_directory):
        self.files_panel.on_browse_folder(selected_directory)

    def on_uppercase(self):
        return self.metadata_panel.on_uppercase()

    def on_save(self):
        return self.metadata_panel.on_save()

    def on_reorganize(self):
        return self.metadata_panel.on_reorganize()

    def on_select_all(self):
        return self.files_panel.on_select_all()

    def on_select_folder(self):
        self.metadata_panel.on_browse_folder_button()

    def insert_metadata_tags(self, selected_paths):
        self.metadata_panel.insert_metadata_tags(selected_paths)
        self.parentWidget().on_select_file(len(selected_paths))

    def get_reorganize_pattern_index(self):
        return self.parent().get_reorganize_pattern_index()

    def __init_layout__(self):
        main_box = QtGui.QHBoxLayout()

        self.metadata_panel = DuckTagsAppMetadataPanel(self)
        main_box.addLayout(self.metadata_panel, stretch=self.metadata_panel_stretch)

        self.files_panel = DuckTagsAppFilesPanel()
        main_box.addWidget(self.files_panel, stretch=self.files_panel_stretch)

        self.setLayout(main_box)