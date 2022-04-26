from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QFormLayout, QGridLayout

from Static import SEND_EMAIL, MESSENGER, MAX_INPUT_LENGTH, FORM_ERR_FONT_SIZE, ERR_FONT_COLOR, TITLE_FONT_SIZE
from gui.ComponentTemplates import get_label


class Login(QWidget):
    """
    Display login widget

    Input fields
        password_input
    """

    def __init__(self, parent=None, err=dict()):
        """
        Function creates QWidget object - login view

        :param parent: GUI object that holds this widget
        :param err: Dict of errors encountered while validating this form
        :type err: dict
        :return: None
        """

        super(Login, self).__init__(parent)
        self.parent = parent
        self.layout = QVBoxLayout()

        # title
        self.label = get_label(self, "Login", font_size=TITLE_FONT_SIZE)
        self.layout.addWidget(self.label)

        # # name
        # self.name = QLabel(self)
        # self.name.setText("Username")
        # self.layout.addWidget(self.name)
        #
        # # name input
        # self.name_input = QLineEdit(self)
        # self.name_input.setMaxLength(MAX_INPUT_LENGTH)
        # self.layout.addWidget(self.name_input)

        # form layout
        form_widget = QWidget(self)
        form_layout = QFormLayout()

        # passwd
        self.passwd = get_label(self, "Password")
        # passwd input
        self.passwd_input = QLineEdit(self)
        self.passwd_input.setEchoMode(QLineEdit.Password)
        self.passwd_input.setMaxLength(MAX_INPUT_LENGTH)
        form_layout.addRow(self.passwd, self.passwd_input)

        # passwd error
        if 'passwd' in err:
            self.passwd_err = get_label(self, err['passwd'], FORM_ERR_FONT_SIZE, ERR_FONT_COLOR)
            form_layout.addRow(self.passwd_err)

        form_widget.setLayout(form_layout)
        self.layout.addWidget(form_widget)

        # grid layout
        grid_widget = QWidget(self)
        grid_layout = QGridLayout()

        # login button
        self.login_btn = QPushButton(self)
        self.login_btn.setText("Login")
        self.login_btn.clicked.connect(parent.login)
        grid_layout.addWidget(self.login_btn, 0, 0)

        # send email button
        self.send_email_btn = QPushButton(self)
        self.send_email_btn.setText("Reset password")
        self.send_email_btn.clicked.connect(lambda: parent.set_screen(SEND_EMAIL))
        grid_layout.addWidget(self.send_email_btn, 0, 1)

        grid_widget.setLayout(grid_layout)
        self.layout.addWidget(grid_widget)

        self.setLayout(self.layout)

    def get_values(self):
        """
        Function returns dict of input fields

        :return: form values
        :rtype: dict
        """

        return {'passwd': self.passwd_input.text()}