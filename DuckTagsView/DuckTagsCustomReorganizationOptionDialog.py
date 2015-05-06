from Utils.DuckTagsCustomPatternParser import DuckTagsCustomPatternParser

from PySide import QtGui
from PySide import QtCore


class DuckTagsCustomReorganizationOptionDialog(QtGui.QDialog):
    previous_custom_pattern = ''

    def __init__(self, *args, **kwargs):
        super(DuckTagsCustomReorganizationOptionDialog, self).__init__(*args, **kwargs)

        self.custom_pattern_parser = DuckTagsCustomPatternParser()

        self.dialog_name = 'Custom Reorganization Option'
        self.__init_ui__()

        self.rejected.connect(self.on_reject)

    def on_confirm(self):
        custom_pattern = self.custom_pattern_input.text()

        if not self.custom_pattern_parser.validate_custom_pattern(custom_pattern):
            self.on_decline()
        else:
            self.previous_custom_pattern = custom_pattern
            self.custom_pattern_parser.append_pattern(custom_pattern)

            self.rejected.disconnect(self.on_reject)
            self.close()
            self.rejected.connect(self.on_reject)

    def on_decline(self):
        self.close()

    def on_reject(self):
        self.previous_custom_pattern = ''
        self.custom_pattern_input.setText(self.previous_custom_pattern)
        self.parent().on_custom_reorganization_decline()

    def __init_ui__(self):
        self.setWindowTitle(self.dialog_name)
        width = self.parent().width() * 0.6
        height = self.parent().height() * 0.3
        self.setFixedSize(width, height)

        layout_box = QtGui.QHBoxLayout()
        layout_box.setContentsMargins(10, 10, 10, 10)
        layout_box.setSpacing(10)

        self.__init_input_panel__(layout_box)
        self.__init_info_panel__(layout_box)

        self.setLayout(layout_box)

    def __init_input_panel__(self, layout_box):
        input_panel_layout = QtGui.QVBoxLayout()

        pattern_label = QtGui.QLabel('Insert Custom Pattern')
        pattern_label.setAlignment(QtCore.Qt.AlignCenter)
        input_panel_layout.addWidget(pattern_label)

        self.custom_pattern_input = QtGui.QLineEdit(self.previous_custom_pattern)
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

    @staticmethod
    def __init_info_panel__(layout_box):
        text_layout = QtGui.QTextEdit()
        text_layout.setReadOnly(True)
        text_layout.setAlignment(QtCore.Qt.AlignCenter)

        text_layout.append('Available Variables')
        text_layout.append('')
        text_layout.append('Title   ->   %s' % DuckTagsCustomPatternParser.title_variable)
        text_layout.append('Artist   ->   %s' % DuckTagsCustomPatternParser.artist_variable)
        text_layout.append('Album   ->   %s' % DuckTagsCustomPatternParser.album_variable)
        text_layout.append('Date   ->   %s' % DuckTagsCustomPatternParser.date_variable)
        text_layout.append('Genre   ->   %s' % DuckTagsCustomPatternParser.genre_variable)
        text_layout.append('Track No   ->   %s' % DuckTagsCustomPatternParser.track_number_variable)

        layout_box.addWidget(text_layout)