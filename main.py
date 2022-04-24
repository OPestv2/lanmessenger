#!/bin/python3
import os.path
import sys

from PyQt5.QtWidgets import QApplication

from GUI import GUI
from JSONParser import JSONParser
from Messenger import Messenger
from Static import USER_OBJECT, REGISTRATION, LOGIN


class Main:
    def __init__(self, argv):
        self.app = QApplication(argv)
        # possible OSError if config file does not exist or could not read it
        self.parser = JSONParser()
        self.messenger = Messenger()
        self.GUI = GUI()

        # if user object is null display registration screen, otherwise login screen
        if self.parser.read_json(USER_OBJECT) is None:
            auth_screen_type = REGISTRATION
        else:
            auth_screen_type = LOGIN
        self.GUI.set_screen(auth_screen_type)

        self.GUI.show()
        self.app.exec_()


if __name__ == '__main__':
    main = Main(sys.argv)





