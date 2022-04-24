"""
GUI class is used to create, render and switch between screens
"""
import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from Static import ABS_PATH, CONFIG, MESSENGER, REGISTRATION, LOGIN, SEND_EMAIL, RESET_PASSWD

MAX_INPUT_LENGTH = 30
STD_WIDTH = 550
STD_HEIGHT = 350


class Login(QWidget):
    """
    Display login widget
    """

    def __init__(self, parent=None):
        super(Login, self).__init__(parent)
        self.resize(STD_WIDTH, STD_HEIGHT)
        self.layout = QVBoxLayout()

        # title
        self.label = QLabel(self)
        self.label.setText("Login")
        self.layout.addWidget(self.label)

        # name
        self.name = QLabel(self)
        self.name.setText("Username")
        self.layout.addWidget(self.name)

        # name input
        self.name_input = QLineEdit(self)
        self.name_input.setMaxLength(MAX_INPUT_LENGTH)
        self.layout.addWidget(self.name_input)

        # passwd
        self.passwd = QLabel(self)
        self.passwd.setText("Password")
        self.layout.addWidget(self.passwd)

        # passwd input
        self.passwd_input = QLineEdit(self)
        self.passwd_input.setEchoMode(QLineEdit.Password)
        self.passwd_input.setMaxLength(MAX_INPUT_LENGTH)
        self.layout.addWidget(self.passwd_input)

        # login button
        self.login_btn = QPushButton(self)
        self.login_btn.setText("Login")
        self.login_btn.clicked.connect(lambda: parent.set_screen(MESSENGER))
        self.layout.addWidget(self.login_btn)

        # send email button
        self.send_email_btn = QPushButton(self)
        self.send_email_btn.setText("Reset password")
        self.send_email_btn.clicked.connect(lambda: parent.set_screen(SEND_EMAIL))
        self.layout.addWidget(self.send_email_btn)

        self.setLayout(self.layout)


class Registration(QWidget):
    """
    Display registration widget
    """

    def __init__(self, parent=None):
        super(Registration, self).__init__(parent)
        self.resize(STD_WIDTH, STD_HEIGHT)
        self.layout = QVBoxLayout()

        # title
        self.label = QLabel(self)
        self.label.setText("Registration")
        self.label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.label)

        # username
        self.name = QLabel(self)
        self.name.setText("Username")
        self.layout.addWidget(self.name)

        # username input
        self.name_input = QLineEdit(self)
        self.name_input.setMaxLength(MAX_INPUT_LENGTH)
        self.layout.addWidget(self.name_input)

        # password
        self.passwd = QLabel(self)
        self.passwd.setText("Password")
        self.layout.addWidget(self.passwd)

        # password input
        self.passwd_input = QLineEdit(self)
        self.passwd_input.setEchoMode(QLineEdit.Password)
        self.passwd_input.setMaxLength(MAX_INPUT_LENGTH)
        self.layout.addWidget(self.passwd_input)

        self.setLayout(self.layout)


class Messenger(QWidget):
    """
    Display messenger widget
    """

    def __init__(self, parent=None):
        super(Messenger, self).__init__(parent)


class Config(QWidget):
    """
    Display configuration widget
    """

    def __init__(self, parent=None):
        super(Config, self).__init__(parent)


class SendEmail(QWidget):
    """
    Display password restore widget
    """
    def __init__(self, parent=None):
        super(SendEmail, self).__init__(parent)
        self.resize(STD_WIDTH, STD_HEIGHT)
        self.layout = QVBoxLayout()

        # title
        self.label = QLabel(self)
        self.label.setText("Send email to reset password")
        self.layout.addWidget(self.label)

        # email
        self.email = QLabel(self)
        self.email.setText("Email")
        self.layout.addWidget(self.email)

        # email input
        self.email_input = QLineEdit(self)
        self.email_input.setMaxLength(MAX_INPUT_LENGTH)
        self.layout.addWidget(self.email_input)

        # reset button
        self.reset_btn = QPushButton(self)
        self.reset_btn.setText("Send email")
        self.reset_btn.clicked.connect(lambda: parent.set_screen(RESET_PASSWD))
        self.layout.addWidget(self.reset_btn)

        # back button
        self.back_btn = QPushButton(self)
        self.back_btn.setText("Back")
        self.back_btn.clicked.connect(lambda: parent.set_screen(REGISTRATION))
        self.layout.addWidget(self.back_btn)

        self.setLayout(self.layout)


class ResetPasswd(QWidget):
    def __init__(self, parent=None):
        super(ResetPasswd, self).__init__(parent)
        self.resize(STD_WIDTH, STD_HEIGHT)
        self.layout = QVBoxLayout()

        # title
        self.label = QLabel(self)
        self.label.setText("Set new password")
        self.layout.addWidget(self.label)

        # passwd
        self.passwd = QLabel(self)
        self.passwd.setText("New Password")
        self.layout.addWidget(self.passwd)

        # passwd input
        self.passwd_input = QLineEdit(self)
        self.passwd_input.setEchoMode(QLineEdit.Password)
        self.passwd_input.setMaxLength(MAX_INPUT_LENGTH)
        self.layout.addWidget(self.passwd_input)

        # re passwd input
        self.re_passwd_input = QLineEdit(self)
        self.re_passwd_input.setEchoMode(QLineEdit.Password)
        self.re_passwd_input.setMaxLength(MAX_INPUT_LENGTH)
        self.layout.addWidget(self.re_passwd_input)

        # save button
        self.save_btn = QPushButton(self)
        self.save_btn.setText("Save password")
        self.save_btn.clicked.connect(lambda: parent.set_screen(LOGIN))
        self.layout.addWidget(self.save_btn)

        # resend button
        self.resend_btn = QPushButton(self)
        self.resend_btn.setText("Resend email")
        self.resend_btn.clicked.connect(lambda: parent.set_screen(SEND_EMAIL))
        self.layout.addWidget(self.resend_btn)

        self.setLayout(self.layout)


""" GUI CLASS """


class GUI(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.resize(STD_WIDTH, STD_HEIGHT)
        self.setWindowTitle("LanMessenger")
        self.current_screen = None

        self.ICON_PATH = ABS_PATH + "resources/icon/favicon.ico"
        self.setWindowIcon(QIcon(self.ICON_PATH))

    def set_screen(self, screen_type):
        """
        Function sets appropriate QWidget.

        :param screen_type:
        :type screen_type: int
        :return: None
        """

        if self.current_screen != screen_type:
            self.current_screen = screen_type
            if screen_type == LOGIN:
                self.__display_login_screen()
            elif screen_type == REGISTRATION:
                self.__display_register_screen()
            elif screen_type == MESSENGER:
                self.__display_messenger_screen()
            elif screen_type == CONFIG:
                self.__display_config_screen()
            elif screen_type == SEND_EMAIL:
                self.__display_send_email_screen()
            elif screen_type == RESET_PASSWD:
                self.__display_reset_passwd_screen()
            # selected screen not found
            else:
                print("[!!!] Selected screen not found")
                sys.exit(0)

    def __display_login_screen(self):
        self.setCentralWidget(Login(self))

    def __display_register_screen(self):
        self.setCentralWidget(Registration(self))

    def __display_messenger_screen(self):
        self.setCentralWidget(Messenger(self))

    def __display_config_screen(self):
        self.setCentralWidget(Config(self))

    def __display_send_email_screen(self):
        self.setCentralWidget(SendEmail(self))

    def __display_reset_passwd_screen(self):
        self.setCentralWidget(ResetPasswd(self))
