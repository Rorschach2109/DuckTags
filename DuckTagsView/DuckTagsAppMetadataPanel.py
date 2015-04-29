import wx
import os


class DuckTagsAppMetadataPanel(wx.Panel):
    def __init__(self, *args, **kwargs):
        super(DuckTagsAppMetadataPanel, self).__init__(*args, **kwargs)

        self.home_path = os.path.expanduser('~')
        self.text_controls = dict()

        self.__init_left_panel__()

    def __init_left_panel__(self):
        self.box = wx.BoxSizer(wx.VERTICAL)
        self.__create_dir_dialog_button__()
        self.__create_tags_section__()

    def __create_tags_section__(self):
        grid_box = wx.FlexGridSizer(6, 2, 3, 3)

        title_label = wx.StaticText(self, label='Title:')
        artist_label = wx.StaticText(self, label='Artist:')
        album_label = wx.StaticText(self, label='Album:')
        year_label = wx.StaticText(self, label='Year:')
        track_number_label = wx.StaticText(self, label='Track Number:')
        genre_label = wx.StaticText(self, label='Genre:')

        self.text_controls['title'] = wx.TextCtrl(self)
        self.text_controls['artist'] = wx.TextCtrl(self)
        self.text_controls['album'] = wx.TextCtrl(self)
        self.text_controls['date'] = wx.TextCtrl(self)
        self.text_controls['tracknumber'] = wx.TextCtrl(self)
        self.text_controls['genre'] = wx.TextCtrl(self)

        for text_ctrl in self.text_controls.values():
            text_ctrl.Enable(False)

        grid_box.AddMany([title_label, (self.text_controls['title'], 1, wx.EXPAND),
                          artist_label, (self.text_controls['artist'], 1, wx.EXPAND),
                          album_label, (self.text_controls['album'], 1, wx.EXPAND),
                          year_label, (self.text_controls['date'], 1, wx.EXPAND),
                          track_number_label, (self.text_controls['tracknumber'], 1, wx.EXPAND),
                          genre_label, (self.text_controls['genre'], 1, wx.EXPAND)])

        grid_box.AddGrowableCol(1)

        self.box.Add(grid_box, 0, wx.EXPAND | wx.ALL, border=5)

    def __create_dir_dialog_button__(self):
        get_dir_button = wx.Button(self, label='Get Directories')
        get_dir_button.Bind(wx.EVT_BUTTON, self.on_get_dir)
        self.box.Add(get_dir_button, 0, wx.EXPAND | wx.ALL, border=5)

        self.SetSizer(self.box)

    def on_get_dir(self, event):
        dialog = wx.DirDialog(self, style=wx.DD_DEFAULT_STYLE, defaultPath=self.home_path)

        if dialog.ShowModal() == wx.ID_OK:
            path = dialog.GetPath()
            self.Parent.process_path(path)

    def on_music_file_select(self, music_file_model):
        try:
            music_file_dict = music_file_model.serialize()
        except AttributeError:
            pass
        else:
            for text_ctrl in self.text_controls:
                self.text_controls[text_ctrl].SetValue(music_file_dict[text_ctrl])
                self.text_controls[text_ctrl].Enable(True)