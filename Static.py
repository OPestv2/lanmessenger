import enum
import os

# STATIC VALUES
ABS_PATH = os.path.dirname(os.path.abspath(__file__))+"/"

LOGIN = 0
REGISTRATION = 1
MESSENGER = 2
CONFIG = 3
SEND_EMAIL = 4
RESET_PASSWD = 5

USER_OBJECT = ["user"]
USER_NAME = ["user", "name"]
USER_PASSWD = ["user", "passwd"]
USER_CERT = ["user", "cert_path"]
USER_EMAIL = ["user", "email"]