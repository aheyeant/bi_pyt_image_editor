from typing import List, Dict

from PyQt5 import QtGui
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QCheckBox


class SettingsToolbarCheckBox(QWidget):
    def __init__(self, parent, answer, decode):
        super().__init__()
        self._parent = parent
        self._answer_list: List = answer
        self._decode: Dict = decode
        self._check_box_list: List[QCheckBox] = []
        self._configure()

    def _configure(self):
        self.setWindowTitle("Toolbar settings")
        self.resize(360, 20 * (len(self._decode) + 2))
        self._center()
        point = QPoint(20, 0)
        for i in range(len(self._answer_list)):
            self._check_box_list.append(QCheckBox(self._decode[i][1], self))
            self._check_box_list[i].resize(300, 20)
            point.setY(point.y() + 20)
            self._check_box_list[i].move(point)
            if self._answer_list[i]:
                self._check_box_list[i].toggle()
            self._check_box_list[i].stateChanged.connect(self._changer(i))

    def _center(self):
        qt_rectangle = self.frameGeometry()
        center_point = QDesktopWidget().availableGeometry().center()
        qt_rectangle.moveCenter(center_point)
        self.move(qt_rectangle.topLeft())

    def _changer(self, identificator: int):
        def change_check(state):
            if state == Qt.Checked:
                self._answer_list[identificator] = True
            else:
                self._answer_list[identificator] = False
            return True
        return change_check

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        self._parent.get_message("update", "toolbar_settings")
        super().closeEvent(a0)
