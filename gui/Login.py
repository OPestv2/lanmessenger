from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton

from Static import SEND_EMAIL, MESSENGER, MAX_INPUT_LENGTH


class Login(QWidget):
    """
    Display login widget
    """

    def __init__(self, parent=None):
        super(Login, self).__init__(parent)
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
