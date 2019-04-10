#!/usr/bin/env python3
import sys
from PyQt5.QtWidgets import QApplication
from src.gui.gui import GUI

if __name__ == "__main__":
    app = QApplication(sys.argv)
    gui = GUI()
    sys.exit(app.exec_())
