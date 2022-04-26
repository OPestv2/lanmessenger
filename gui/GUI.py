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
from gui.MenuBar import MenuBar
from gui.Messenger import Messenger
from gui.Registration import Registration
from gui.ResetPasswd import ResetPasswd
from gui.SendEmail import SendEmail


def dict_is_empty(dictionary):
    """
    Check if err dictionary is empty. Just to understand why dict is mapped to boolean

    :param dictionary: Dictionary containing wrong values added in validation
    :type dictionary: dict
    :return: Returns true if dict is empty or false if not
    :rtype: bool
    """
    return not bool(dictionary)


class GUI(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("LanMessenger")
        self.setFont(STD_FONT_SIZE)

        self.current_screen = None
        self.auth = Auth()

        # add menu bar and status bar
        self.menubar = MenuBar(self)
        self.setMenuBar(self.menubar)
        self.statusBar()

        # store screens
        self.login_screen = None
        self.register_screen = None
        self.messenger_screen = None
        self.config_screen = None
        self.send_email_screen = None
        self.reset_passwd_screen = None

        # set icon
        self.ICON_PATH = ABS_PATH + "resources/icon/favicon.ico"
        self.setWindowIcon(QIcon(self.ICON_PATH))

        # if user object is null display registration screen, otherwise login screen
        if self.auth.user_exists():
            self.set_screen(LOGIN)
        else:
            self.set_screen(REGISTRATION)

    def set_screen(self, screen_type, err=dict(), old_values=dict()):
        """
        Function sets appropriate QWidget.

        :param screen_type:
        :type screen_type: int
        :return: None
        """

        if screen_type == LOGIN:
            self.__display_login_screen(err)
        elif screen_type == REGISTRATION:
            self.__display_register_screen(err, old_values)
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
        self.login_screen = Login(self, err)
        self.setCentralWidget(self.login_screen)

    def __display_register_screen(self, err, old_values):
        self.register_screen = Registration(self, err, old_values)
        self.setCentralWidget(self.register_screen)

    def __display_messenger_screen(self):
        self.messenger_screen = Messenger(self)
        self.setCentralWidget(self.messenger_screen)

    def __display_config_screen(self, err):
        self.config_screen = Config(self, err)
        self.setCentralWidget(self.config_screen)

    def __display_send_email_screen(self):
        self.send_email_screen = SendEmail(self)
        self.setCentralWidget(self.send_email_screen)

    def __display_reset_passwd_screen(self, err):
        self.register_screen = ResetPasswd(self, err)
        self.setCentralWidget(self.register_screen)

    def register(self):
        print("registration")

        # retrieve data from form
        data = self.register_screen.get_values()

        # authenticate user
        err = self.auth.register_user(data)

        # no errors
        if dict_is_empty(err):
            # redirect to login form
            self.set_screen(LOGIN)
        # there are errors
        else:
            # redirect to registration form with attached errors
            self.set_screen(REGISTRATION, err, data)

    def login(self):
        print("login")

        # retrieve data from form
        data = self.login_screen.get_values()

        # authenticate user
        err = self.auth.login_user(data)

        # no errors
        if dict_is_empty(err):
            # redirect to messenger
            print("GUI.login success")
            self.menubar.enable_settings()
            self.set_screen(MESSENGER)
        # there are errors
        else:
            # redirect to login form with attached errors
            print("GUI.login fail")
            self.set_screen(LOGIN, err)

    def config(self, data=dict()):
        print("config")

        if bool(data):
            # save changes
            pass

        self.set_screen(CONFIG)
