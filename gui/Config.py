from PyQt5.QtWidgets import QMainWindow, QWidget


class Config(QWidget):
    """
    Display configuration widget
    """

    def __init__(self, parent=None, err=dict(), old_values=dict(), tab=0):
        super(Config, self).__init__(parent)
