from PyQt5.QtWidgets import QLabel

from Static import STD_FONT_SIZE


def get_label(parent=None, text="", font_size=STD_FONT_SIZE, font_color=None):
    """
    Function is used to limit amount of code in gui templates.
    It allows to create a customized QLabel in one line.

    :param parent: Set parent element in which this obj will be placed
    :type parent: GUI object
    :param text: Set text of element
    :type text: str
    :param font_size: Set color of special message type. Default is black
    :type font_size: Static::*_FONT_COLOR
    :param font_color: Set font size.
    :type font_color: Static::*_FONT
    :return: Returns new QLabel object
    :rtype: QLabel
    """
    label = QLabel(parent)
    label.setText(text)
    label.setFont(font_size)
    if font_color is not None:
        label.setStyleSheet(font_color)
    return label
