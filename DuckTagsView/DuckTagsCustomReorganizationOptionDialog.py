from PySide import QtGui
from PySide import QtCore


class DuckTagsCustomReorganizationOptionDialog(QtGui.QDialog):
    def __init__(self, *args, **kwargs):
        super(DuckTagsCustomReorganizationOptionDialog, self).__init__(*args, **kwargs)

        self.dialog_name = 'Custom Reorganization Option'
        self.__init_ui__()

    def on_confirm(self):
        custom_pattern = self.custom_pattern_input.text()

        if not self.__validate_custom_pattern__(custom_pattern):
            self.on_decline()
        else:
            self.close()

    def on_decline(self):
        self.close()
        self.parent().on_custom_reorganization_decline()

    def __validate_custom_pattern__(self, custom_pattern):
        return self.title_variable in custom_pattern \
            or self.artist_variable in custom_pattern \
            or self.album_variable in custom_pattern \
            or self.date_variable in custom_pattern \
            or self.genre_variable in custom_pattern \
            or self.track_number_variable in custom_pattern

    def __init_ui__(self):
        self.setWindowTitle(self.dialog_name)
        width = self.parent().width() * 0.6
        height = self.parent().height() * 0.3
        self.setFixedSize(width, height)

        layout_box = QtGui.QHBoxLayout()
        layout_box.setContentsMargins(10, 10, 10, 10)
        layout_box.setSpacing(10)

        self.__init_variables__()
        self.__init_input_panel__(layout_box)
        self.__init_info_panel__(layout_box)

        self.setLayout(layout_box)

    def __init_variables__(self):
        self.title_variable = '{{ title }}'
        self.artist_variable = '{{ artist }}'
        self.album_variable = '{{ album }}'
        self.date_variable = '{{ date }}'
        self.genre_variable = '{{ genre }}'
        self.track_number_variable = '{{ track_number }}'

    def __init_input_panel__(self, layout_box):
        input_panel_layout = QtGui.QVBoxLayout()

        pattern_label = QtGui.QLabel('Insert Custom Pattern')
        pattern_label.setAlignment(QtCore.Qt.AlignCenter)
        input_panel_layout.addWidget(pattern_label)

        self.custom_pattern_input = QtGui.QLineEdit()
        input_panel_layout.addWidget(self.custom_pattern_input)

        input_panel_layout.addStretch(1)

        buttons_layout = QtGui.QHBoxLayout()

        confirm_button = QtGui.QPushButton('Confirm')
        confirm_button.clicked.connect(self.on_confirm)
        buttons_layout.addWidget(confirm_button)

        decline_button = QtGui.QPushButton('Decline')
        decline_button.clicked.connect(self.on_decline)
        buttons_layout.addWidget(decline_button)

        buttons_layout.addStretch(1)

        input_panel_layout.addLayout(buttons_layout)

        layout_box.addLayout(input_panel_layout, stretch=2)

    def __init_info_panel__(self, layout_box):
        text_layout = QtGui.QTextEdit()
        text_layout.setReadOnly(True)
        text_layout.setAlignment(QtCore.Qt.AlignCenter)

        text_layout.append('Available Variables')
        text_layout.append('')
        text_layout.append('Title   ->   %s' % self.title_variable)
        text_layout.append('Artist   ->   %s' % self.artist_variable)
        text_layout.append('Album   ->   %s' % self.album_variable)
        text_layout.append('Date   ->   %s' % self.date_variable)
        text_layout.append('Genre   ->   %s' % self.genre_variable)
        text_layout.append('Track No   ->   %s' % self.track_number_variable)

        layout_box.addWidget(text_layout)