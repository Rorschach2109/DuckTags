from PySide import QtGui

import os


class DuckTagsAppMetadataPanel(QtGui.QVBoxLayout):
    def __init__(self, *args, **kwargs):
        super(DuckTagsAppMetadataPanel, self).__init__(*args, **kwargs)

        self.Direction = QtGui.QBoxLayout.TopToBottom
        self.default_path = os.path.expanduser('~')
        self.__init_layout__()

    def on_browse_folder_button(self):
        directory_dialog = QtGui.QFileDialog()

        directory_dialog.setFileMode(QtGui.QFileDialog.Directory)
        directory_dialog.setOption(QtGui.QFileDialog.ShowDirsOnly)

        selected_directory = directory_dialog.getExistingDirectory(caption="Select Directory",
                                                                   dir=self.default_path)

        if selected_directory:
            self.parentWidget().on_browse_folder(selected_directory)

    def __init_layout__(self):
        self.__create_browse_folder_button__()
        self.__create_metadata_section__()

    def __create_browse_folder_button__(self):
        browse_button = QtGui.QPushButton('Select Folder')
        browse_button.clicked.connect(self.on_browse_folder_button)

        self.addWidget(browse_button)

    def __create_metadata_section__(self):
        metadata_box = QtGui.QGridLayout()
        self.__create_labels__(metadata_box)
        self.__create_lines_edit__(metadata_box)

        self.addLayout(metadata_box, stretch=1)
        self.addStretch(2)

    @staticmethod
    def __create_labels__(metadata_box):
        labels_dict = {
            'title': (QtGui.QLabel('Title'), (0, 0)),
            'artist': (QtGui.QLabel('Artist'), (1, 0)),
            'album': (QtGui.QLabel('Album'), (2, 0)),
            'date': (QtGui.QLabel('Date'), (3, 0)),
            'track_number': (QtGui.QLabel('Track_number'), (4, 0)),
            'genre': (QtGui.QLabel('Genre'), (5, 0)),
            }

        for label in labels_dict:
            metadata_box.addWidget(labels_dict[label][0], *labels_dict[label][1])

    def __create_lines_edit__(self, metadata_box):
        self.line_edits_dict = {
            'title': (QtGui.QLineEdit(), (0, 1)),
            'artist': (QtGui.QLineEdit(), (1, 1)),
            'album': (QtGui.QLineEdit(), (2, 1)),
            'date': (QtGui.QLineEdit(), (3, 1)),
            'tracknumber': (QtGui.QLineEdit(), (4, 1)),
            'genre': (QtGui.QLineEdit(), (5, 1)),
        }

        for line_edit_name in self.line_edits_dict:
            line_edit = self.line_edits_dict[line_edit_name][0]
            position = self.line_edits_dict[line_edit_name][1]

            line_edit.setEnabled(False)

            metadata_box.addWidget(line_edit, *position)