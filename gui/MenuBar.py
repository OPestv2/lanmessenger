from PyQt5.QtWidgets import QMenuBar, QAction, qApp
from webbrowser import open

def get_action(parent, text, action_method, shortcut="", statustip="", enabled=True):
    """
    Method creates a QAction object

    :param parent: Parent object
    :type parent: QMenuBar object
    :param text: Menu item text
    :type text: str
    :param action_method: Action to be executed on trigger
    :type action_method: function
    :param shortcut: Key combination
    :type shortcut: str
    :param statustip: Text to be shown in status bar
    :type statustip: str
    :return: QAction object
    :rtype: QAction
    """

    action = QAction(text, parent)
    action.setShortcut(shortcut)
    action.setStatusTip(statustip)
    action.triggered.connect(action_method)
    return action

class MenuBar(QMenuBar):
    def __init__(self, parent=None):
        super(MenuBar, self).__init__(parent)
        file_menu = self.addMenu("&File")
        self.settings = get_action(self, "&Settings", parent.config, "Ctrl+E", "Open settings", False)
        file_menu.addAction(self.settings)
        file_menu.addSeparator()
        file_menu.addAction(get_action(self, "&Exit", qApp.quit, "Ctrl+Q", "Quit the program"))

        help_menu = self.addMenu("&Help")
        help_menu.addAction(get_action(self, "GitHub", lambda: open("https://github.com/OPestv2/lanmessenger", new=2),
                                       statustip="Open project in browser"))


    def enable_settings(self):
        self.settings.setEnabled(True)