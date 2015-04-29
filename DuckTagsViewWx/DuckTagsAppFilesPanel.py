from DuckTags_API.DuckTagsFileAPI import DuckTagsFileAPI
from DuckTags_API.DuckTagsMetadataAPI import DuckTagsMetadataAPI

import wx


class DuckTagsAppFilesPanel(wx.Panel):

    root_folder_data = -1

    def __init__(self, *args, **kwargs):
        super(DuckTagsAppFilesPanel, self).__init__(*args, **kwargs)

        self.__init_layout__()
        self.__bind_events__()

        self.files_api = DuckTagsFileAPI()
        self.metadata_api = DuckTagsMetadataAPI()
        self.files_dict = dict()

    def on_list_item_click(self, event):
        selected_indexes = self.__get_selected_item_indexes__()

        selected_file_paths_list = self.__get_selected_file_paths__(selected_indexes)
        music_file_model = self.metadata_api.get_music_files_list_metadata(selected_file_paths_list)
        self.Parent.on_music_file_select(music_file_model)

    def on_size(self, event):
        new_size = event.GetSize()
        self.control_list.SetColumnWidth(0, 0.96*new_size[0])
        event.Skip()

    def process_path(self, path):
        self.control_list.DeleteAllItems()

        self.files_dict = self.files_api.get_files_dict_from_folder(path)

        root_folders_list = sorted(self.files_dict.keys(), reverse=True)
        for root_folder_index in range(len(root_folders_list)):
            root_folder = root_folders_list[root_folder_index]
            if not self.files_dict[root_folder]:
                continue

            for file_name in sorted(self.files_dict[root_folder], reverse=True):
                file_name_item = self.__create_files_item__(file_name, root_folder_index)
                self.control_list.InsertItem(file_name_item)

            root_folder_item = self.__create_folder_item__(root_folder)
            self.control_list.InsertItem(root_folder_item)

        self.control_list.InsertItem(wx.ListItem())

    def __get_selected_file_paths__(self, selected_indexes_list):
        selected_paths = []

        root_folders_list = sorted(self.files_dict.keys(), reverse=True)

        for index in selected_indexes_list:
            item_text = self.control_list.GetItemText(index)
            item_data = self.control_list.GetItemData(index)

            if item_data == self.root_folder_data:
                selected_paths.extend(map(
                    lambda file_name: '/'.join([item_text, file_name]),
                    self.files_dict[item_text]))
            else:
                root_folder = root_folders_list[item_data]
                selected_paths.append('/'.join([root_folder, item_text]))

        return list(set(selected_paths))

    def __get_selected_item_indexes__(self):
        start_index = 0
        selected_indexes = []

        for count in range(self.control_list.GetSelectedItemCount()):
            start_index = self.control_list.GetNextSelected(start_index)
            selected_indexes.append(start_index)

        return selected_indexes

    def __init_layout__(self):
        sizer = wx.BoxSizer(wx.VERTICAL)

        self.control_list = wx.ListCtrl(self, -1, style=wx.LC_REPORT | wx.LC_NO_HEADER)
        self.control_list.InsertColumn(0, '')
        self.control_list.SetBackgroundColour('LIGHT GREY')

        sizer.Add(self.control_list, 1, wx.ALL | wx.EXPAND, 5)
        self.SetSizerAndFit(sizer)

    def __bind_events__(self):
        self.Bind(wx.EVT_SIZE, self.on_size)
        self.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.on_list_item_click)

    @staticmethod
    def __create_folder_item__(root):
        root_item = wx.ListItem()
        root_item.SetText(root)
        root_item.SetAlign(wx.LIST_FORMAT_LEFT)
        root_item.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
        root_item.SetBackgroundColour('GREY')
        root_item.SetData(DuckTagsAppFilesPanel.root_folder_data)

        return root_item

    @staticmethod
    def __create_files_item__(files_name, root_folder_index):
        file_item = wx.ListItem()
        file_item.SetText(files_name)
        file_item.SetAlign(wx.LIST_FORMAT_CENTER)
        file_item.SetData(root_folder_index)

        return file_item