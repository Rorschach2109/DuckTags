import wx


class DuckTagsAppMenuBar(wx.MenuBar):
    def __init__(self, *args, **kwargs):
        super(DuckTagsAppMenuBar, self).__init__(*args, **kwargs)

        file_menu = wx.Menu()

        file_menu.AppendSeparator()

        quit_item = wx.MenuItem(file_menu, wx.ID_EXIT, '&Quit\tCtrl+Q')
        file_menu.AppendItem(quit_item)
        self.Append(file_menu, '&File')