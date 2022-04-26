#!/bin/python3
import os
import sys

from PyQt5.QtWidgets import QApplication

from gui.GUI import GUI


class Main:
    def __init__(self, argv):
        self.app = QApplication(argv)
        # self.app.setStyle("Fusion")
        self.GUI = GUI()
        self.GUI.show()
        self.app.exec_()


if __name__ == '__main__':
    main = Main(sys.argv)





