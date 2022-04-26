from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QPushButton, QLineEdit, QLabel, QVBoxLayout, QWidget, QFormLayout

from Static import MAX_INPUT_LENGTH, FORM_ERR_FONT_SIZE, ERR_FONT_COLOR, TITLE_FONT_SIZE
from gui.ComponentTemplates import get_label


class Registration(QWidget):
    """
    Display registration widget

    Input fields:
        email_input
        username_input
        password_input
    """

    def __init__(self, parent=None, err=dict(), old_values=dict()):
        """
        Function creates QWidget object - registration view.

        :param parent: GUI object that holds this widget
        :param err: Dict of errors encountered while validating this form
        :type err: dict
        :param old_values: Dict of values processed (non-empty if error occurs)
        :type old_values: dict
        :return: None
        """

        super(Registration, self).__init__(parent)
        self.parent = parent
        self.layout = QVBoxLayout()

        # title
        self.label = get_label(self, "Registration", font_size=TITLE_FONT_SIZE)
        self.layout.addWidget(self.label)

        # form layout
        form_widget = QWidget(self)
        form_layout = QFormLayout()

        # email
        self.email = get_label(self, "Email")
        # email input
        self.email_input = QLineEdit(self)
        if 'email' in old_values:
            self.email_input.setText(old_values['email'])
        self.email_input.setMaxLength(MAX_INPUT_LENGTH)
        form_layout.addRow(self.email, self.email_input)

        # email error
        if 'email' in err:
            self.email_err = get_label(self, err['email'], FORM_ERR_FONT_SIZE, ERR_FONT_COLOR)
            form_layout.addRow(self.email_err)

        # username
        self.name = get_label(self, "Username")
        # username input
        self.name_input = QLineEdit(self)
        if 'name' in old_values:
            self.name_input.setText(old_values['name'])
        self.name_input.setMaxLength(MAX_INPUT_LENGTH)
        form_layout.addRow(self.name, self.name_input)

        # username error
        if 'name' in err:
            self.name_err = get_label(self, err['name'], FORM_ERR_FONT_SIZE, ERR_FONT_COLOR)
            form_layout.addRow(self.name_err)

        # password
        self.passwd = get_label(self, "Password")
        # password input
        self.passwd_input = QLineEdit(self)
        self.passwd_input.setEchoMode(QLineEdit.Password)
        self.passwd_input.setMaxLength(MAX_INPUT_LENGTH)
        form_layout.addRow(self.passwd, self.passwd_input)

        # re passwd error
        if 'passwd' in err:
            self.passwd_err = get_label(self, err['passwd'], FORM_ERR_FONT_SIZE, ERR_FONT_COLOR)
            form_layout.addRow(self.passwd_err)

        # password
        self.re_passwd = get_label(self, 'Confirm Password')
        # password input
        self.re_passwd_input = QLineEdit(self)
        self.re_passwd_input.setEchoMode(QLineEdit.Password)
        self.re_passwd_input.setMaxLength(MAX_INPUT_LENGTH)
        form_layout.addRow(self.re_passwd, self.re_passwd_input)

        # passwd error
        if 're_passwd' in err:
            self.re_passwd_err = get_label(self, err['re_passwd'], FORM_ERR_FONT_SIZE, ERR_FONT_COLOR)
            form_layout.addRow(self.re_passwd_err)

        form_widget.setLayout(form_layout)
        self.layout.addWidget(form_widget)

        # register btn
        self.register_btn = QPushButton(self)
        self.register_btn.setText("Register")
        self.register_btn.clicked.connect(self.parent.register)
        self.layout.addWidget(self.register_btn)

        self.setLayout(self.layout)

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
