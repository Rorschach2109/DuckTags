from DuckTagsView.DuckTagsApp import DuckTagsApp

import wx


class DuckTagsAppMain(object):

    @staticmethod
    def run_duck_tags_app():
        app = wx.App()
        DuckTagsApp(None)

        app.MainLoop()