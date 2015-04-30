from DuckTags_API.DuckTagsFileAPI import DuckTagsFileAPI

from PySide import QtGui


class DuckTagsAppFilesPanel(QtGui.QListWidget):
    def __init__(self, *args, **kwargs):
        super(DuckTagsAppFilesPanel, self).__init__(*args, **kwargs)

        self.file_api = DuckTagsFileAPI()

    def on_browse_folder(self, selected_directory):
        files_dict = self.file_api.get_files_dict_from_folder(selected_directory)
