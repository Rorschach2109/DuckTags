from DuckTagsView.DuckTagsAppMetadataPanel import DuckTagsAppMetadataPanel
from DuckTagsView.DuckTagsAppFilesPanel import DuckTagsAppFilesPanel
from DuckTagsView.DuckTagsAppMenuBar import DuckTagsAppMenuBar
from DuckTagsView.DuckTagsAppToolBar import DuckTagsAppToolBar

import wx


class DuckTagsApp(wx.Frame):

    def __init__(self, *args, **kwargs):
        super(DuckTagsApp, self).__init__(*args, **kwargs)

        self.min_size = (900, 600)
        self.app_name = 'DuckTags'
        self.__init_ui__()

    def process_path(self, path):
        self.files_panel.process_path(path)

    def on_music_file_select(self, music_file_model):
        self.metadata_panel.on_music_file_select(music_file_model)

    def on_quit(self, event):
        self.Close()

    def __init_ui__(self):
        self.__create_menu_bar__()
        self.__create_toolbar__()
        self.__create_layout__()

        self.SetSize(self.min_size)
        self.SetMinSize(self.min_size)
        self.SetTitle(self.app_name)

        self.Center()
        self.Show(True)

    def __create_menu_bar__(self):
        menu_bar = DuckTagsAppMenuBar()
        self.SetMenuBar(menu_bar)
        self.Bind(wx.EVT_MENU, self.on_quit, id=wx.ID_EXIT)

    def __create_toolbar__(self):
        toolbar = DuckTagsAppToolBar(parent=self)
        self.SetToolBar(toolbar)

    def __create_layout__(self):
        main_box = wx.BoxSizer(wx.HORIZONTAL)

        self.metadata_panel = DuckTagsAppMetadataPanel(self, -1, style=wx.SIMPLE_BORDER)
        self.files_panel = DuckTagsAppFilesPanel(self, -1)

        main_box.Add(self.metadata_panel, 2, wx.EXPAND | wx.ALL, 1)
        main_box.Add(self.files_panel, 3, wx.EXPAND | wx.ALL, 1)

        self.SetSizer(main_box)