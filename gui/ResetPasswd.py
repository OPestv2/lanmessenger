from PyQt5.QtWidgets import QPushButton, QLineEdit, QLabel, QVBoxLayout, QWidget

from Static import SEND_EMAIL, LOGIN, MAX_INPUT_LENGTH


class ResetPasswd(QWidget):
    def __init__(self, parent=None):
        super(ResetPasswd, self).__init__(parent)
        self.layout = QVBoxLayout()

        # title
        self.label = QLabel(self)
        self.label.setText("Set new password")
        self.layout.addWidget(self.label)

        # code
        self.code = QLabel(self)
        self.code.setText("Code")
        self.layout.addWidget(self.code)

        # code input
        self.code_input = QLineEdit(self)
        self.code_input.setMaxLength(MAX_INPUT_LENGTH)
        self.layout.addWidget(self.code_input)

        # passwd
        self.passwd = QLabel(self)
        self.passwd.setText("New Password")
        self.layout.addWidget(self.passwd)

        # passwd input
        self.passwd_input = QLineEdit(self)
        self.passwd_input.setEchoMode(QLineEdit.Password)
        self.passwd_input.setMaxLength(MAX_INPUT_LENGTH)
        self.layout.addWidget(self.passwd_input)

        # re passwd
        self.re_passwd = QLabel(self)
        self.re_passwd.setText("Confirm Password")
        self.layout.addWidget(self.re_passwd)

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
