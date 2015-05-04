from DuckTags_API.DuckTagsMetadataAPI import DuckTagsMetadataAPI
from DuckTags_API.DuckTagsFolderStructureAPI import DuckTagsFolderStructureAPI
from Utils.DuckTagsExceptions import DuckTagsRenameException

from PySide import QtGui
from PySide import QtCore

import os


class DuckTagsAppMetadataPanel(QtGui.QVBoxLayout):
    def __init__(self, *args, **kwargs):
        super(DuckTagsAppMetadataPanel, self).__init__(*args, **kwargs)

        self.Direction = QtGui.QBoxLayout.TopToBottom
        self.default_path = os.path.expanduser('~')

        self.metadata_api = DuckTagsMetadataAPI()
        self.folder_structure_api = DuckTagsFolderStructureAPI()
        self.current_paths = list()
        self.current_directory = None

        self.__init_layout__()

    def on_save(self):
        music_file_model_dict = dict()
        for line_edit_name in self.line_edits_dict:
            music_file_model_dict[line_edit_name] = self.line_edits_dict[line_edit_name][0].text()

        self.metadata_api.set_music_file_list_metadata(self.current_paths, music_file_model_dict)

    def on_reorganize(self):
        if not self.current_directory:
            return

        self.on_save()

        reorganize_pattern_index = self.parentWidget().get_reorganize_pattern_index()
        try:
            self.folder_structure_api.reorganize_files_with_pattern(self.current_paths, reorganize_pattern_index)
        except DuckTagsRenameException:
            pass
        else:
            self.__clean_lines_edit__()
            self.parentWidget().on_browse_folder(self.current_directory)

    def on_browse_folder_button(self):
        directory_dialog = QtGui.QFileDialog()

        directory_dialog.setFileMode(QtGui.QFileDialog.Directory)
        directory_dialog.setOption(QtGui.QFileDialog.ShowDirsOnly)

        self.current_directory = directory_dialog.getExistingDirectory(caption="Select Directory",
                                                                       dir=self.default_path)

        if self.current_directory:
            self.__clean_lines_edit__()
            self.current_paths = list()

            self.parentWidget().on_browse_folder(self.current_directory)

    def insert_metadata_tags(self, selected_paths):
        self.current_paths = selected_paths
        music_file_model = self.metadata_api.get_music_files_list_metadata(self.current_paths)

        try:
            music_file_model_dict = music_file_model.serialize()
        except AttributeError:
            self.__clean_lines_edit__()
            return

        for key in music_file_model_dict:
            text = music_file_model_dict[key]
            try:
                self.line_edits_dict[key][0].setText(text)
                self.line_edits_dict[key][0].setEnabled(True)
            except KeyError:
                pass

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

        metadata_box.addWidget(self.line_edits_dict['title'][0], *self.line_edits_dict['title'][1])
        metadata_box.addWidget(self.line_edits_dict['artist'][0], *self.line_edits_dict['artist'][1])
        metadata_box.addWidget(self.line_edits_dict['album'][0], *self.line_edits_dict['album'][1])
        metadata_box.addWidget(self.line_edits_dict['date'][0], *self.line_edits_dict['date'][1])
        metadata_box.addWidget(self.line_edits_dict['tracknumber'][0], *self.line_edits_dict['tracknumber'][1])
        metadata_box.addWidget(self.line_edits_dict['genre'][0], *self.line_edits_dict['genre'][1])

        for line_edit_name in self.line_edits_dict:
            line_edit = self.line_edits_dict[line_edit_name][0]
            line_edit.setEnabled(False)

        self.__set_validators__()

    def __set_validators__(self):
        date_regexp = QtCore.QRegExp("[1-2]{1}\d{3}")
        date_validator = QtGui.QRegExpValidator(date_regexp)
        self.line_edits_dict['date'][0].setValidator(date_validator)

        track_number_regexp = QtCore.QRegExp("\d{3}")
        track_number_validator = QtGui.QRegExpValidator(track_number_regexp)
        self.line_edits_dict['tracknumber'][0].setValidator(track_number_validator)

    def __clean_lines_edit__(self):
        for line_edit_name in self.line_edits_dict:
            line_edit = self.line_edits_dict[line_edit_name][0]
            line_edit.clear()
            line_edit.setEnabled(False)