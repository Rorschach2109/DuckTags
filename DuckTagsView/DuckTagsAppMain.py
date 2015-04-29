from DuckTagsView.DuckTagsApp import DuckTagsApp

from PySide import QtGui
import sys


class DuckTagsAppMain(object):

    @staticmethod
    def run_duck_tags_app():
        app = QtGui.QApplication(sys.argv)
        duck_tags_app = DuckTagsApp()

        sys.exit(app.exec_())