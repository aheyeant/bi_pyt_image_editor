from PyQt5 import QtGui
from PyQt5.QtGui import QIcon, QPainter, QColor

from src.gui.Constants import *
from PyQt5.QtWidgets import QDesktopWidget, QMessageBox, QMainWindow, QAction, QFileDialog, QTextEdit

from src.gui.SettingToolbarCheckBox import SettingsToolbarCheckBox
from src.imageEditor.ImageEditor import ImageEditor


class GUI(QMainWindow):
    """
    _write_to_status_bar(text)

    """

    def __init__(self):
        super().__init__()
        self._changed: bool = False                     # implement
        self._saved: bool = True                        # implement
        self._start_var_declaration()
        self._configure()

    def _start_var_declaration(self):
        self._action_exit = None                        # implement
        self._action_save = None                        # implement
        self._action_save_as = None                     # implement
        self._action_open_image = None                  # implement
        self._action_close_image = None                 # implement
        self._action_settings_toolbar = None            # implement
        self._action_clear_toolbar = None               # implement
        self._action_rotate_left = None                 # implement
        self._action_rotate_right = None                # implement
        self._action_vertical_mirroring = None          # implement
        self._action_horizontal_mirroring = None        # implement
        self._action_color_inverse = None               # implement
        self._action_change_color_value_plus = None     # implement
        self._action_change_color_value_minus = None    # implement
        self._action_convert_to_grey_scale = None       # implement
        self._action_border_focus = None                # implement
        self._action_original_image = None              # implement

        self._toolbar_list = None                       # implement
        self._toolbar_decoder = None                    # implement

        self._toolbar_save = None                       # implement
        self._toolbar_save_as = None                    # implement
        self._toolbar_open_image = None                 # implement
        self._toolbar_close_image = None                # implement
        self._toolbar_rotate_left = None                # implement
        self._toolbar_rotate_right = None               # implement
        self._toolbar_vertical_mirroring = None         # implement
        self._toolbar_horizontal_mirroring = None       # implement
        self._toolbar_color_inverse = None              # implement
        self._toolbar_change_color_value_plus = None    # implement
        self._toolbar_change_color_value_minus = None   # implement
        self._toolbar_convert_to_gray_scale = None      # implement
        self._toolbar_border_focus = None               # implement
        self._toolbar_original_image = None             # implement

        self._image_editor: ImageEditor = None          # implement
        self._text_edit = None                          # implement

        self._image = None                              # implement

    def _configure(self):
        self.setWindowTitle(APPLICATION_NAME)
        self.resize(APPLICATION_WIDTH, APPLICATION_HEIGHT)
        self._center()
        self._init_actions()
        self._write_to_status_bar()
        self._init_menu()
        self._init_toolbar()
        self._image_editor = ImageEditor()
        self._text_edit = QTextEdit()
        self.show()

    def _init_actions(self):
        self._action_exit = self._init_action(ACTION_EXIT_TITTLE,
                                              ACTION_EXIT_SHORTCUT,
                                              ACTION_EXIT_STATUS_TIP,
                                              ACTION_EXIT_ICON_DIR,
                                              self.close)

        self._action_save = self._init_action(ACTION_SAVE_TITTLE,
                                              ACTION_SAVE_SHORTCUT,
                                              ACTION_SAVE_STATUS_TIP,
                                              ACTION_SAVE_ICON_DIR,
                                              self._save)

        self._action_save_as = self._init_action(ACTION_SAVE_AS_TITTLE,
                                                 ACTION_SAVE_AS_SHORTCUT,
                                                 ACTION_SAVE_AS_STATUS_TIP,
                                                 ACTION_SAVE_AS_ICON_DIR,
                                                 self._save_as)

        self._action_open_image = self._init_action(ACTION_OPEN_IMAGE_TITTLE,
                                                    ACTION_OPEN_IMAGE_SHORTCUT,
                                                    ACTION_OPEN_IMAGE_STATUS_TIP,
                                                    ACTION_OPEN_IMAGE_ICON_DIR,
                                                    self._open_image)

        self._action_close_image = self._init_action(ACTION_CLOSE_IMAGE_TITTLE,
                                                     ACTION_CLOSE_IMAGE_SHORTCUT,
                                                     ACTION_CLOSE_IMAGE_STATUS_TIP,
                                                     ACTION_CLOSE_IMAGE_ICON_DIR,
                                                     self._close_image)

        self._action_settings_toolbar = self._init_action(ACTION_SETTINGS_TOOLBAR_TITTLE,
                                                          ACTION_SETTINGS_TOOLBAR_SHORTCUT,
                                                          ACTION_SETTINGS_TOOLBAR_STATUS_TIP,
                                                          ACTION_SETTINGS_TOOLBAR_ICON_DIR,
                                                          self._settings_toolbar)

        self._action_clear_toolbar = self._init_action(ACTION_CLEAR_TOOLBAR_TITTLE,
                                                       ACTION_CLEAR_TOOLBAR_SHORTCUT,
                                                       ACTION_CLEAR_TOOLBAR_STATUS_TIP,
                                                       ACTION_CLEAR_TOOLBAR_ICON_DIR,
                                                       self._clear_toolbar)

        self._action_rotate_left = self._init_action(ACTION_ROTATE_LEFT_TITTLE,
                                                     ACTION_ROTATE_LEFT_SHORTCUT,
                                                     ACTION_ROTATE_LEFT_STATUS_TIP,
                                                     ACTION_ROTATE_LEFT_ICON_DIR,
                                                     self._rotate_left)

        self._action_rotate_right = self._init_action(ACTION_ROTATE_RIGHT_TITTLE,
                                                      ACTION_ROTATE_RIGHT_SHORTCUT,
                                                      ACTION_ROTATE_RIGHT_STATUS_TIP,
                                                      ACTION_ROTATE_RIGHT_ICON_DIR,
                                                      self._rotate_right)

        self._action_vertical_mirroring = self._init_action(ACTION_VERTICAL_MIRRORING_TITTLE,
                                                            ACTION_VERTICAL_MIRRORING_SHORTCUT,
                                                            ACTION_VERTICAL_MIRRORING_STATUS_TIP,
                                                            ACTION_VERTICAL_MIRRORING_ICON_DIR,
                                                            self._vertical_mirroring)

        self._action_horizontal_mirroring = self._init_action(ACTION_HORIZONTAL_MIRRORING_TITTLE,
                                                              ACTION_HORIZONTAL_MIRRORING_SHORTCUT,
                                                              ACTION_HORIZONTAL_MIRRORING_STATUS_TIP,
                                                              ACTION_HORIZONTAL_MIRRORING_ICON_DIR,
                                                              self._horizontal_mirroring)

        self._action_color_inverse = self._init_action(ACTION_COLOR_INVERSE_TITTLE,
                                                       ACTION_COLOR_INVERSE_SHORTCUT,
                                                       ACTION_COLOR_INVERSE_STATUS_TIP,
                                                       ACTION_COLOR_INVERSE_ICON_DIR,
                                                       self._color_inverse)

        self._action_change_color_value_plus = self._init_action(ACTION_CHANGE_COLOR_VALUE_PLUS_TITTLE,
                                                                 ACTION_CHANGE_COLOR_VALUE_PLUS_SHORTCUT,
                                                                 ACTION_CHANGE_COLOR_VALUE_PLUS_STATUS_TIP,
                                                                 ACTION_CHANGE_COLOR_VALUE_PLUS_ICON_DIR,
                                                                 self._change_color_value_plus)

        self._action_change_color_value_minus = self._init_action(ACTION_CHANGE_COLOR_VALUE_MINUS_TITTLE,
                                                                  ACTION_CHANGE_COLOR_VALUE_MINUS_SHORTCUT,
                                                                  ACTION_CHANGE_COLOR_VALUE_MINUS_STATUS_TIP,
                                                                  ACTION_CHANGE_COLOR_VALUE_MINUS_ICON_DIR,
                                                                  self._change_color_value_minus)

        self._action_convert_to_grey_scale = self._init_action(ACTION_CONVERT_TO_GRAY_SCALE_TITTLE,
                                                               ACTION_CONVERT_TO_GRAY_SCALE_SHORTCUT,
                                                               ACTION_CONVERT_TO_GRAY_SCALE_STATUS_TIP,
                                                               ACTION_CONVERT_TO_GRAY_SCALE_ICON_DIR,
                                                               self._convert_to_grey_scale)

        self._action_border_focus = self._init_action(ACTION_BORDER_FOCUS_TITTLE,
                                                      ACTION_BORDER_FOCUS_SHORTCUT,
                                                      ACTION_BORDER_FOCUS_STATUS_TIP,
                                                      ACTION_BORDER_FOCUS_ICON_DIR,
                                                      self._border_focus)

        self._action_original_image = self._init_action(ACTION_ORIGINAL_IMAGE_TITTLE,
                                                        ACTION_ORIGINAL_IMAGE_SHORTCUT,
                                                        ACTION_ORIGINAL_IMAGE_STATUS_TIP,
                                                        ACTION_ORIGINAL_IMAGE_ICON_DIR,
                                                        self._original_image)

    def _init_action(self, tittle: str, shortcut: str, status_tip: str, icon_dir: str, connect_node) -> QAction:
        if icon_dir is None:
            action = QAction(tittle, self)
        else:
            action = QAction(QIcon(icon_dir), tittle)
        if shortcut is not None:
            action.setShortcut(shortcut)
        if status_tip is not None:
            action.setStatusTip(status_tip)
        action.triggered.connect(connect_node)
        return action

    def _init_menu(self):
        menubar = self.menuBar()
        file_menu = menubar.addMenu("&File")
        file_menu.addAction(self._action_open_image)
        file_menu.addAction(self._action_save)
        file_menu.addAction(self._action_save_as)
        file_menu.addAction(self._action_original_image)
        file_menu.addAction(self._action_close_image)
        file_menu.addAction(self._action_exit)

        tools_menu = menubar.addMenu("&Tools")
        tools_menu.addAction(self._action_rotate_left)
        tools_menu.addAction(self._action_rotate_right)
        tools_menu.addAction(self._action_vertical_mirroring)
        tools_menu.addAction(self._action_horizontal_mirroring)
        tools_menu.addAction(self._action_color_inverse)
        tools_menu.addAction(self._action_change_color_value_plus)
        tools_menu.addAction(self._action_change_color_value_minus)
        tools_menu.addAction(self._action_convert_to_grey_scale)
        tools_menu.addAction(self._action_border_focus)

        settings_menu = menubar.addMenu("&Settings")
        settings_menu.addAction(self._action_settings_toolbar)
        settings_menu.addAction(self._action_clear_toolbar)

    def _init_toolbar(self):
        self._toolbar_decoder = {0: [self._toolbar_save,
                                     ACTION_SAVE_TITTLE,
                                     self._action_save],

                                 1: [self._toolbar_save_as,
                                     ACTION_SAVE_AS_TITTLE,
                                     self._action_save_as],

                                 2: [self._toolbar_open_image,
                                     ACTION_OPEN_IMAGE_TITTLE,
                                     self._action_open_image],

                                 3: [self._toolbar_original_image,
                                     ACTION_ORIGINAL_IMAGE_TITTLE,
                                     self._action_original_image],

                                 4: [self._toolbar_close_image,
                                     ACTION_CLOSE_IMAGE_TITTLE,
                                     self._action_close_image],

                                 5: [self._toolbar_rotate_left,
                                     ACTION_ROTATE_LEFT_TITTLE,
                                     self._action_rotate_left],

                                 6: [self._toolbar_rotate_right,
                                     ACTION_ROTATE_RIGHT_TITTLE,
                                     self._action_rotate_right],

                                 7: [self._toolbar_vertical_mirroring,
                                     ACTION_VERTICAL_MIRRORING_TITTLE,
                                     self._action_vertical_mirroring],

                                 8: [self._toolbar_horizontal_mirroring,
                                     ACTION_HORIZONTAL_MIRRORING_TITTLE,
                                     self._action_horizontal_mirroring],

                                 9: [self._toolbar_color_inverse,
                                     ACTION_COLOR_INVERSE_TITTLE,
                                     self._action_color_inverse],

                                 10: [self._toolbar_change_color_value_plus,
                                      ACTION_CHANGE_COLOR_VALUE_PLUS_TITTLE,
                                      self._action_change_color_value_plus],

                                 11: [self._toolbar_change_color_value_minus,
                                      ACTION_CHANGE_COLOR_VALUE_MINUS_TITTLE,
                                      self._action_change_color_value_minus],

                                 12: [self._toolbar_convert_to_gray_scale,
                                      ACTION_CONVERT_TO_GRAY_SCALE_TITTLE,
                                      self._action_convert_to_grey_scale],

                                 13: [self._toolbar_border_focus,
                                      ACTION_BORDER_FOCUS_TITTLE,
                                      self._action_border_focus]}

        self._toolbar_list = [False for _ in range(len(self._toolbar_decoder))]
        self._check_toolbar()

    def _check_toolbar(self) -> bool:
        for i in range(len(self._toolbar_decoder)):
            if self._toolbar_list[i]:
                if self._toolbar_decoder[i][0] is None:
                    self._toolbar_decoder[i][0] = self.addToolBar(self._toolbar_decoder[i][1])
                    self._toolbar_decoder[i][0].addAction(self._toolbar_decoder[i][2])
            else:
                if self._toolbar_decoder[i][0] is not None:
                    self._toolbar_decoder[i][0].close()
                    self._toolbar_decoder[i][0] = None
        return True

    def _clear_toolbar(self) -> bool:
        for i in range(len(self._toolbar_decoder)):
            self._toolbar_list[i] = False
        self._check_toolbar()
        return True

    def _write_to_status_bar(self, text: str = "Ready"):
        self.statusBar().showMessage(text)

    def _center(self):
        qt_rectangle = self.frameGeometry()
        center_point = QDesktopWidget().availableGeometry().center()
        qt_rectangle.moveCenter(center_point)
        self.move(qt_rectangle.topLeft())

    def _save(self) -> bool:
        if self._image_editor.has_image():
            if self._saved:
                return True
            reply = QMessageBox.question(self, "Message", "Overwrite old image?", QMessageBox.No | QMessageBox.Yes,
                                         QMessageBox.No)
            if reply == QMessageBox.No:
                return True
            self._image_editor.save_image()
            self._change_saved_flag(True)
        return True

    def _save_as(self) -> bool:
        if self._image_editor.has_image():
            file_name = QFileDialog.getSaveFileName(self, "Save as", "/home")[0]
            if file_name == "" or file_name[-1] == "/":
                return True
            reply = QMessageBox.question(self, "Message", "Are you really want save image with name\""
                                         + file_name + "\"?", QMessageBox.No | QMessageBox.Yes, QMessageBox.No)
            if reply == QMessageBox.Yes:
                try:
                    self._image_editor.save_image(file_name)
                    self._saved = True
                except ValueError as _:
                    QMessageBox.question(self, "Message", "Bad format", QMessageBox.Close, QMessageBox.Close)
                except Exception as _:
                    pass
        return True

    def _open_image(self) -> bool:
        try:
            file_name = QFileDialog.getOpenFileName(self, 'Open file', '/home')[0]
            if file_name == "" or file_name[-1] == "/":
                return True
            self._image_editor.load_image(file_name)
            self._change_saved_flag(True)
        except NameError as _:
            QMessageBox.question(self, "Message", "Bad image format. Image may be RGB.",
                                 QMessageBox.Close, QMessageBox.Close)
        except FileNotFoundError as _:
            QMessageBox.question(self, "Message", "File not found.",
                                 QMessageBox.Close, QMessageBox.Close)
        except Exception as _:
            pass
        finally:
            self._changed = True
        return True

    def _close_image(self) -> bool:
        if self._saved:
            self._image_editor.close_image()
            self.update()
        else:
            reply = QMessageBox.question(self, "Message", "Image has changes. Exit without saving?", QMessageBox.No
                                         | QMessageBox.Yes, QMessageBox.No)
            if reply == QMessageBox.No:
                return True
            self._image_editor.close_image()
            self.update()
        return True

    def _settings_toolbar(self) -> bool:
        self.s = SettingsToolbarCheckBox(self, self._toolbar_list, self._toolbar_decoder)
        self.s.show()
        self.s.activateWindow()
        return True

    def _rotate_left(self) -> bool:
        if self._image_editor.has_image():
            self._image_editor.rotate(-90)
            self._change_saved_flag(False)
            self.update()
        return True

    def _rotate_right(self) -> bool:
        if self._image_editor.has_image():
            self._image_editor.rotate(90)
            self._change_saved_flag(False)
            self.update()
        return True

    def _vertical_mirroring(self) -> bool:
        if self._image_editor.has_image():
            self._image_editor.vertical_mirroring()
            self._change_saved_flag(False)
            self.update()
        return True

    def _horizontal_mirroring(self) -> bool:
        self._image_editor.horizontal_mirroring()
        self._change_saved_flag(False)
        self.update()
        return True

    def _color_inverse(self) -> bool:
        self._image_editor.inverse()
        self._change_saved_flag(False)
        self.update()
        return True

    def _change_color_value_plus(self) -> bool:
        self._image_editor.increase(10)
        self._change_saved_flag(False)
        self.update()
        return True

    def _change_color_value_minus(self) -> bool:
        self._image_editor.decrease(10)
        self._change_saved_flag(False)
        self.update()
        return True

    def _convert_to_grey_scale(self) -> bool:
        self._image_editor.gray_scale()
        self._change_saved_flag(False)
        self.update()
        return True

    def _border_focus(self) -> bool:
        self._image_editor.convolution()
        self._change_saved_flag(False)
        self.update()
        return True

    def _original_image(self) -> bool:
        self._image_editor.original_image()
        self._change_saved_flag(True)
        self.update()
        return True

    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        qp = QPainter()
        qp.begin(self)
        self._draw_image(qp)
        qp.end()

    def _draw_image(self, qp: QPainter):
        if not self._image_editor.has_image():
            return
        if self._changed:
            self._calculate_image()

        for i in range(self._image[1][1]):
            for j in range(self._image[1][0]):
                qp.setPen(self._image[2][i][j])
                qp.drawPoint(self._image[0][0] + j, self._image[0][1] + i)

    def _calculate_image(self) -> None:
        """
        self._image = ((left_top_x, left_top_y),(size_w, size_h),[QColor...])
        """
        self._changed = False
        size = self.size()
        left_top = [0, 0]
        step = [1.0, 1.0]
        if size.width() > self._image_editor.copy_size[0]:
            left_top[0] = (size.width() - self._image_editor.copy_size[0]) // 2
        else:
            step[0] = self._image_editor.copy_size[0] / size.width()

        if size.height() > self._image_editor.copy_size[1]:
            left_top[1] = (size.height() - self._image_editor.copy_size[1]) // 2
        else:
            step[1] = self._image_editor.copy_size[1] / size.height()

        if step[0] != 1.0 or step[1] != 1.0:
            x_list = []
            y_list = []
            if step[0] == 1:
                for i in range(self._image_editor.copy_size[0]):
                    x_list.append(i)
            else:
                tmp = 0
                while tmp < self._image_editor.copy_size[0]:
                    x_list.append(int(tmp))
                    tmp += step[0]
            if step[1] == 1:
                for i in range(self._image_editor.copy_size[1]):
                    y_list.append(i)
            else:
                tmp = 0
                while tmp < self._image_editor.copy_size[1]:
                    y_list.append(int(tmp))
                    tmp += step[1]
            self._image = ((left_top[0], left_top[1]), (len(x_list), len(y_list)), [])
            for i in enumerate(y_list):
                self._image[2].append([])
                for j in x_list:
                    self._image[2][i[0]].append(QColor(*self._image_editor.copy_image[i[1]][j].get_data(), 255))
        else:
            self._image = ((left_top[0], left_top[1]), (self._image_editor.copy_size[0],
                                                        self._image_editor.copy_size[1]),
                           [])
            for i in range(self._image[1][1]):
                self._image[2].append([])
                for j in range(self._image[1][0]):
                    self._image[2][i].append(QColor(*self._image_editor.copy_image[i][j].get_data(), 255))

    def _change_saved_flag(self, flag: bool):
        self._saved = flag
        if flag:
            self.setWindowTitle(APPLICATION_NAME)
        else:
            self.setWindowTitle(APPLICATION_NAME + "*")

    def get_message(self, msg_type: str, command: str = None) -> None:
        if msg_type == "update":
            if command is None:
                return
            if command == "toolbar_settings":
                self._check_toolbar()
            return None
        return None

    def closeEvent(self, event: QtGui.QCloseEvent) -> None:
        reply = QMessageBox.question(self, "Message", "Are you sure to quit?",
                                     QMessageBox.No | QMessageBox.Yes, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def resizeEvent(self, a0: QtGui.QResizeEvent) -> None:
        self._changed = True
        super().resizeEvent(a0)

    def moveEvent(self, a0: QtGui.QMoveEvent) -> None:
        self._changed = True
        super().moveEvent(a0)

    def update(self) -> None:
        self._changed = True
        super().update()
