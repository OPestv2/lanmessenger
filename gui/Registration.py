from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QPushButton, QLineEdit, QLabel, QVBoxLayout, QWidget

from Static import MAX_INPUT_LENGTH, FORM_ERR_FONT_SIZE, ERR_FONT_COLOR
from gui.ComponentTemplates import get_label


class Registration(QWidget):
    """
    Display registration widget

    Input fields:
        email_input
        username_input
        password_input
    """

    def __init__(self, parent=None):
        super(Registration, self).__init__(parent)
        self.parent = parent

    def construct(self, err):
        """
        Function creates QWidget object - registration view.

        :param err: Dict of errors encountered while validating
        :type err: dict
        :return: None
        """

        self.layout = QVBoxLayout()

        # title
        self.label = get_label(self, "Registration")
        self.layout.addWidget(self.label)

        # email
        self.email = get_label(self, "Email")
        self.layout.addWidget(self.email)

        # email input
        self.email_input = QLineEdit(self)
        self.email_input.setMaxLength(MAX_INPUT_LENGTH)
        self.layout.addWidget(self.email_input)

        # email error
        if 'email' in err:
            self.email_err = get_label(self, err['email'], FORM_ERR_FONT_SIZE, ERR_FONT_COLOR)
            self.layout.addWidget(self.email_err)

        # username
        self.name = get_label(self, "Username")
        self.layout.addWidget(self.name)

        # username input
        self.name_input = QLineEdit(self)
        self.name_input.setMaxLength(MAX_INPUT_LENGTH)
        self.layout.addWidget(self.name_input)

        # name error
        if 'name' in err:
            self.name_err = get_label(self, err['name'], FORM_ERR_FONT_SIZE, ERR_FONT_COLOR)
            self.layout.addWidget(self.name_err)

        # password
        self.passwd = get_label(self, 'Password')
        self.layout.addWidget(self.passwd)

        # password input
        self.passwd_input = QLineEdit(self)
        self.passwd_input.setEchoMode(QLineEdit.Password)
        self.passwd_input.setMaxLength(MAX_INPUT_LENGTH)
        self.layout.addWidget(self.passwd_input)

        # re passwd error
        if 'passwd' in err:
            self.passwd_err = get_label(self, err['passwd'], FORM_ERR_FONT_SIZE, ERR_FONT_COLOR)
            self.layout.addWidget(self.passwd_err)

        # password
        self.re_passwd = get_label(self, 'Confirm Password')
        self.layout.addWidget(self.re_passwd)

        # password input
        self.re_passwd_input = QLineEdit(self)
        self.re_passwd_input.setEchoMode(QLineEdit.Password)
        self.re_passwd_input.setMaxLength(MAX_INPUT_LENGTH)
        self.layout.addWidget(self.re_passwd_input)

        # passwd error
        if 're_passwd' in err:
            self.re_passwd_err = get_label(self, err['re_passwd'], FORM_ERR_FONT_SIZE, ERR_FONT_COLOR)
            self.layout.addWidget(self.re_passwd_err)

        # register btn
        self.register_btn = QPushButton(self)
        self.register_btn.setText("Register")
        self.register_btn.clicked.connect(self.parent.register)
        self.layout.addWidget(self.register_btn)

        self.setLayout(self.layout)

        return self

    def get_values(self):
        """
        Function returns dict of input fields
        :return: form values
        :rtype: dict
        """

        values = {}
        values['email'] = self.email_input.text()
        values['name'] = self.name_input.text()
        values['passwd'] = self.passwd_input.text()
        values['re_passwd'] = self.re_passwd_input.text()
        return values

    def clear_all(self):
        """
        After successful registration reset all input fields

        :return: None
        """
        self.email_input.setText("")
        self.name_input.setText("")
        self.passwd_input.setText("")
        self.re_passwd_input.setText("")

    def clear_passwd(self):
        """
        In case of failed registration clear password only

        :return: None
        """
        self.passwd_input.setText("")
        self.re_passwd_input.setText("")
