# Preference Dialog(s)

from string import (ascii_uppercase,
                    digits)
from PyQt5.QtWidgets import (QDialog,
                             QCheckBox,
                             QComboBox,
                             QPushButton,
                             QGroupBox,
                             QHBoxLayout,
                             QVBoxLayout)
from keyboard import read_key, KeyboardEvent


class SetShortcut(QDialog):
    """ A dialog that will let the user choose his/her preferred hotkey. """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.modifier_keys = []
        self.single_key = ''
        self.selected_hotkeys = ''      # Combination of self.modifier_keys and self.single_key
        self._widgets()
        self._layout()
        self._properties()
        self._connections()

    def _widgets(self) -> None:
        """ List of QWidgets used in this dialog. """

        self.shiftCheckBox = QCheckBox('Shift')
        self.ctrlCheckBox = QCheckBox('Ctrl')
        self.winCheckBox = QCheckBox('Win')
        self.altCheckBox = QCheckBox('Alt')
        self.keyComboBox = QComboBox()
        self.okPushButton = QPushButton('&OK')

    def _layout(self) -> None:
        """ Layout design in this dialog. """

        horizontal = QHBoxLayout()
        horizontal.addWidget(self.shiftCheckBox)
        horizontal.addWidget(self.ctrlCheckBox)
        horizontal.addWidget(self.winCheckBox)
        horizontal.addWidget(self.altCheckBox)
        horizontal.addWidget(self.keyComboBox)

        groupbox = QGroupBox('Keys')
        groupbox.setLayout(horizontal)

        button = QHBoxLayout()
        button.addStretch()
        button.addWidget(self.okPushButton)

        vertical = QVBoxLayout()
        vertical.addWidget(groupbox)
        vertical.addLayout(button)

        self.setLayout(vertical)

    def _properties(self) -> None:
        """ Settings of all QObjects stored are all here. """

        # self.keyComboBox properties
        self.keyComboBox.addItems(iter(digits))
        self.keyComboBox.addItems(iter(ascii_uppercase))

        # SetShortcut(QDialog)
        self.resize(300, 104)
        self.setModal(True)

    def _connections(self) -> None:
        """ Connect all signals and slots here. """

        self.shiftCheckBox.clicked.connect(self.on_anyCheckBox_clicked)
        self.altCheckBox.clicked.connect(self.on_anyCheckBox_clicked)
        self.ctrlCheckBox.clicked.connect(self.on_anyCheckBox_clicked)
        self.winCheckBox.clicked.connect(self.on_anyCheckBox_clicked)

        self.keyComboBox.currentIndexChanged.connect(self.on_keyComboBox_currentIndexChanged)

        self.okPushButton.clicked.connect(self.accept)

    def on_anyCheckBox_clicked(self) -> None:
        """ Call self.update_modifier_keys() everytime the user clicked any of the four (4) checkboxes. """

        self.update_modifier_keys()

    def update_modifier_keys(self) -> None:
        """ Update self.modifier_keys based on the checkbox clicked. """

        checkbox = self.sender()
        text = checkbox.text().lower()
        if checkbox.isChecked():
            self.modifier_keys.append(text)
        else:
            self.modifier_keys.remove(text)

    def on_keyComboBox_currentIndexChanged(self) -> None:
        """ Call self.update_single_key() everytime the combobox selection changes. """

        self.update_single_key()

    def update_single_key(self):
        """ Update self.single_key based on self.keyComboBox' selected text. """

        self.single_key = self.keyComboBox.currentText()

    def accept(self):
        """ Call self.update_user_hotkeys() based on the user's selected keys. """

        self.update_user_hotkeys()
        self.done(1)

    def update_user_hotkeys(self) -> None:
        """ Update self.selected_hotkeys based on the combined self.modifier_keys and self.single_key. """

        self.selected_hotkeys = '+'.join(self.get_combined_modifier_and_single_keys())

    def get_combined_modifier_and_single_keys(self) -> list:
        """ Return combined self.modifier_keys and self.single_key. """

        return self.modifier_keys + [self.single_key]
