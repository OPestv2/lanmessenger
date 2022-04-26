import os

# STATIC VALUES
from PyQt5.QtGui import QFont

ABS_PATH = os.path.dirname(os.path.abspath(__file__))+"/"

LOGIN = 0
REGISTRATION = 1
MESSENGER = 2
CONFIG = 3
SEND_EMAIL = 4
RESET_PASSWD = 5
AUTHORIZE = 6

USER_OBJECT = ["user"]
USER_NAME = ["user", "name"]
USER_PASSWD = ["user", "passwd"]
USER_CERT = ["user", "cert_path"]
USER_EMAIL = ["user", "email"]

MAX_INPUT_LENGTH = 30

STD_FONT_SIZE = QFont('Arial', 11)
TITLE_FONT_SIZE = QFont('Arial', 13)
FORM_ERR_FONT_SIZE = QFont('Arial', 9)

ERR_FONT_COLOR = 'color: red'
WARN_FONT_COLOR = 'color: yellow'
SUCC_FONT_COLOR = 'color: green'
INFO_FONT_COLOR = 'color: blue'

MAX_EMAIL_LEN = 80
MIN_USERNAME_LEN = 3
MAX_USERNAME_LEN = 30
MIN_PASSWORD_LEN = 8
MAX_PASSWORD_LEN = 40
SPECIAL_CHARACTERS = ['$', '@', '!', '%']