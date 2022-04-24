from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton

from Static import RESET_PASSWD, LOGIN, MAX_INPUT_LENGTH


class SendEmail(QWidget):
    """
    Display password restore widget
    """
    def __init__(self, parent=None):
        super(SendEmail, self).__init__(parent)
        self.layout = QVBoxLayout()

        # title
        self.label = QLabel(self)
        self.label.setText("Send email")
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
        self.back_btn.clicked.connect(lambda: parent.set_screen(LOGIN))
        self.layout.addWidget(self.back_btn)

        self.setLayout(self.layout)
