from DuckTags_API.DuckTagsFileAPI import DuckTagsFileAPI
from DuckTags_API.DuckTagsMetadataAPI import DuckTagsMetadataAPI

from PySide import QtGui
from PySide import QtCore


class DuckTagsAppFilesPanel(QtGui.QListWidget):
    def __init__(self, *args, **kwargs):
        super(DuckTagsAppFilesPanel, self).__init__(*args, **kwargs)

        self.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.itemSelectionChanged.connect(self.on_item_selection_changed)

        self.file_api = DuckTagsFileAPI()
        self.metadata_api = DuckTagsMetadataAPI()
        self.root_items_rows_list = list()

    def on_browse_folder(self, selected_directory):
        self.__clean_widget_list__()

        files_dict = self.file_api.get_files_dict_from_folder(selected_directory)
        self.__insert_list_items__(files_dict)

    def on_item_selection_changed(self):
        selected_rows = [self.row(item) for item in self.selectedItems()]

        self.__process_selected_roots__(selected_rows)

    def __process_selected_roots__(self, selected_rows):
        bottom_bound_list = filter(lambda row: row in self.root_items_rows_list, selected_rows)

        for bottom_bound in bottom_bound_list:
            bottom_bound_index = self.root_items_rows_list.index(bottom_bound)

            try:
                upper_bound = self.root_items_rows_list[bottom_bound_index+1]
            except IndexError:
                upper_bound = self.count()

            self.item(bottom_bound).setSelected(False)
            for item_row in range(bottom_bound+1, upper_bound):
                self.item(item_row).setSelected(True)

    def __clean_widget_list__(self):
        self.root_items_rows_list = []
        self.clear()

    def __insert_list_items__(self, files_dict):
        for root_folder in sorted(files_dict):
            self.__insert_root_element__(root_folder)
            self.addItems(files_dict[root_folder])

    def __insert_root_element__(self, root_folder):
        root_item = QtGui.QListWidgetItem()
        root_item.setText(root_folder)
        root_item.setTextAlignment(QtCore.Qt.AlignCenter)
        root_item.setBackground(QtGui.QBrush(QtCore.Qt.gray))

        root_item.setFont(QtGui.QFont('Helvetica', pointSize=12, weight=QtGui.QFont.Bold))

        self.addItem(root_item)
        self.root_items_rows_list.append(self.row(root_item))