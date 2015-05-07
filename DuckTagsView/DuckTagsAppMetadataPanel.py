from DuckTagsView.DuckTagsAppCoverButton import DuckTagsAppCoverButton

from DuckTags_API.DuckTagsMetadataAPI import DuckTagsMetadataAPI
from DuckTags_API.DuckTagsFolderStructureAPI import DuckTagsFolderStructureAPI
from Utils.DuckTagsExceptions import DuckTagsRenameException

from PySide import QtGui
from PySide import QtCore

import os


class DuckTagsAppMetadataPanel(QtGui.QVBoxLayout):
    def __init__(self, main_window):
        super(DuckTagsAppMetadataPanel, self).__init__()

        self.Direction = QtGui.QBoxLayout.TopToBottom
        self.default_path = os.path.expanduser('~')

        self.metadata_api = DuckTagsMetadataAPI()
        self.folder_structure_api = DuckTagsFolderStructureAPI()
        self.current_paths = list()
        self.current_directory = None
        self.file_name_line_edit = None
        self.multiple_file_message = 'Multiple Files'

        self.main_window = main_window

        self.__init_layout__()

    def on_uppercase(self):
        current_paths_length = len(self.current_paths)

        self.metadata_api.set_music_file_list_metadata_uppercase(self.current_paths)
        self.__reorganize_files__()

        return current_paths_length

    def on_save(self):
        music_file_model_dict = dict()
        for line_edit_name in self.line_edits_dict:
            music_file_model_dict[line_edit_name] = self.line_edits_dict[line_edit_name][0].text()

        self.metadata_api.set_music_file_list_metadata(self.current_paths, music_file_model_dict)

        return len(self.current_paths)

    def on_reorganize(self):
        if not self.current_directory:
            return 0

        self.on_save()
        return self.__reorganize_files__()

    def on_browse_folder_button(self):
        directory_dialog = QtGui.QFileDialog()

        directory_dialog.setFileMode(QtGui.QFileDialog.Directory)
        directory_dialog.setOption(QtGui.QFileDialog.ShowDirsOnly)

        new_directory = directory_dialog.getExistingDirectory(caption="Select Directory",
                                                              dir=self.default_path)

        if new_directory:
            self.current_directory = new_directory
            self.__clean_lines_edit__()
            self.current_paths = list()

            self.parentWidget().on_browse_folder(self.current_directory)

    def insert_metadata_tags(self, selected_paths):
        self.current_paths = selected_paths
        music_file_model = self.metadata_api.get_music_files_list_metadata(self.current_paths)

        self.__insert_file_name__()

        try:
            music_file_model_dict = music_file_model.serialize()
        except AttributeError:
            self.__clean_lines_edit__()
            self.cover_button.clean_button_image()
            return

        for key in music_file_model_dict:
            text = music_file_model_dict[key]
            try:
                line_edit = self.line_edits_dict[key][0]
                line_edit.setText(text)
                line_edit.setEnabled(True)
            except KeyError:
                pass

        cover_path = self.metadata_api.get_music_files_list_cover(selected_paths)
        self.cover_button.draw_cover(cover_path)

    def __insert_file_name__(self):
        if len(self.current_paths) > 1:
            text = self.multiple_file_message
        elif len(self.current_paths) == 1:
            file_path = self.current_paths[0]
            text = os.path.basename(file_path)
            self.file_name_line_edit.setEnabled(True)
        else:
            text = ''

        self.file_name_line_edit.setText(text)

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

        self.addLayout(metadata_box)
        self.__create_cover_button__()

    def __create_cover_button__(self):
        cover_button_size = self.__compute_cover_button_size__()
        cover_button_layout = QtGui.QGridLayout()
        cover_button_layout.setAlignment(QtCore.Qt.AlignCenter)

        self.cover_button = DuckTagsAppCoverButton(cover_button_size)
        cover_button_layout.addWidget(self.cover_button, 0, 0)

        self.addLayout(cover_button_layout)

    def __compute_cover_button_size__(self):
        stretch_sum = self.main_window.metadata_panel_stretch + self.main_window.files_panel_stretch
        main_window_size = self.main_window.parent().size()

        metadata_panel_width = main_window_size.width() * self.main_window.metadata_panel_stretch / stretch_sum
        metadata_panel_height = main_window_size.height()

        cover_button_height = metadata_panel_height - 8 * 45
        if cover_button_height < metadata_panel_height:
            return cover_button_height, cover_button_height
        else:
            return metadata_panel_width, metadata_panel_width

    @staticmethod
    def __create_labels__(metadata_box):
        labels_dict = {
            'file_name': (QtGui.QLabel('File Name'), (0, 0)),
            'title': (QtGui.QLabel('Title'), (1, 0)),
            'artist': (QtGui.QLabel('Artist'), (2, 0)),
            'album': (QtGui.QLabel('Album'), (3, 0)),
            'date': (QtGui.QLabel('Date'), (4, 0)),
            'track_number': (QtGui.QLabel('Track_number'), (5, 0)),
            'genre': (QtGui.QLabel('Genre'), (6, 0)),
            }

        for label in labels_dict:
            metadata_box.addWidget(labels_dict[label][0], *labels_dict[label][1])

    def __create_lines_edit__(self, metadata_box):
        self.line_edits_dict = {
            'title': (QtGui.QLineEdit(), (1, 1)),
            'artist': (QtGui.QLineEdit(), (2, 1)),
            'album': (QtGui.QLineEdit(), (3, 1)),
            'date': (QtGui.QLineEdit(), (4, 1)),
            'tracknumber': (QtGui.QLineEdit(), (5, 1)),
            'genre': (QtGui.QLineEdit(), (6, 1)),
        }

        self.file_name_line_edit = QtGui.QLineEdit()
        self.file_name_line_edit.setReadOnly(True)
        self.file_name_line_edit.setEnabled(False)
        metadata_box.addWidget(self.file_name_line_edit, *(0, 1))

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

        self.file_name_line_edit.clear()
        self.file_name_line_edit.setEnabled(False)

    def __reorganize_files__(self):
        reorganize_pattern_index = self.parentWidget().get_reorganize_pattern_index()
        try:
            self.folder_structure_api.reorganize_files_with_pattern(self.current_paths, reorganize_pattern_index)
        except DuckTagsRenameException:
            raise
        else:
            reorganized_files_number = len(self.current_paths)
            self.__clean_lines_edit__()
            self.parentWidget().on_browse_folder(self.current_directory)

        return reorganized_files_number

