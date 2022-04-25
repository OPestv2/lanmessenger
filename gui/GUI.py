"""
GUI class is used to create, render and switch between screens
"""
import sys

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from Static import ABS_PATH, CONFIG, MESSENGER, REGISTRATION, LOGIN, SEND_EMAIL, RESET_PASSWD, USER_OBJECT, STD_FONT_SIZE
from auth.Auth import Auth
from gui.Config import Config
from gui.Login import Login
from gui.Messenger import Messenger
from gui.Registration import Registration
from gui.ResetPasswd import ResetPasswd
from gui.SendEmail import SendEmail


STD_WIDTH = 550
STD_HEIGHT = 350


class GUI(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("LanMessenger")
        self.setFont(STD_FONT_SIZE)

        self.current_screen = None
        self.auth = Auth()

        # set icon
        self.ICON_PATH = ABS_PATH + "resources/icon/favicon.ico"
        self.setWindowIcon(QIcon(self.ICON_PATH))

        # store screen objects
        self.login_screen = Login(self)
        self.register_screen = Registration(self)
        self.messenger_screen = Messenger(self)
        self.config_screen = Config(self)
        self.send_email_screen = SendEmail(self)
        self.reset_passwd_screen = ResetPasswd(self)

        # if user object is null display registration screen, otherwise login screen
        if self.auth.user_exists():
            self.set_screen(LOGIN)
        else:
            self.set_screen(REGISTRATION)

    def set_screen(self, screen_type, err={}):
        """
        Function sets appropriate QWidget.

        :param screen_type:
        :type screen_type: int
        :return: None
        """

        # if err is None:
        #     err = {}
        # if self.current_screen != screen_type:
        #     self.current_screen = screen_type
        if screen_type == LOGIN:
            self.__display_login_screen(err)
        elif screen_type == REGISTRATION:
            self.__display_register_screen(err)
        elif screen_type == MESSENGER:
            self.__display_messenger_screen()
        elif screen_type == CONFIG:
            self.__display_config_screen(err)
        elif screen_type == SEND_EMAIL:
            self.__display_send_email_screen()
        elif screen_type == RESET_PASSWD:
            self.__display_reset_passwd_screen(err)
        # selected screen not found
        else:
            print("[!!!] Selected screen not found")
            sys.exit(0)

    def __display_login_screen(self, err):
        self.setCentralWidget(self.login_screen.construct(err))

    def __display_register_screen(self, err):
        self.setCentralWidget(self.register_screen.construct(err))

    def __display_messenger_screen(self):
        self.setCentralWidget(self.messenger_screen.construct())

    def __display_config_screen(self, err):
        self.setCentralWidget(self.config_screen.construct(err))

    def __display_send_email_screen(self):
        self.setCentralWidget(self.send_email_screen.construct())

    def __display_reset_passwd_screen(self, err):
        self.setCentralWidget(self.reset_passwd_screen.construct(err))

    def register(self):
        print("registration")

        # retrieve data from form
        data = self.register_screen.get_values()


        # authenticate user
        err = self.auth.register_user(data)

        print(err)

        # no errors
        if self.__dict_is_empty(err):
            # redirect to login form
            print("GUI.register registration successful")
            self.set_screen(LOGIN)
        # there are errors
        else:
            # redirect to registration form with attached errors
            print("GUI.register registration failed")
            self.set_screen(REGISTRATION, err)



    def __dict_is_empty(self, dict):
        """
        Check if err dictionary is empty. Just to understand why dict is mapped to boolean

        :param dict: Dictionary containing wrong values added in validation
        :type dict: dict
        :return: Returns true if dict is empty or false if not
        :rtype: bool
        """
        return not bool(dict)

