""" 10K Hours: a timer that will track your progress in coding

    Interface: GUI (PyQt5)
    Language: Python 3.5.2
    Author: mokachokokarbon <tokidokitalkyou@gmail.com>
    Created: 23 Oct 2015 @ 03:20 AM
 """

import sys
from PyQt5.QtWidgets import QApplication
from src.main_window import Ten
from src.dialog.preferences import Preferences

__author__ = 'mokachokokarbon'

APP = QApplication(sys.argv)


def configure_app_icon() -> None:
    """ This will show the icon of Betty in the taskbar """

    import ctypes
    APP_ID = u'novus.mokachokokarbon.tenny.02'
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(APP_ID)

if __name__ == '__main__':
    configure_app_icon()
    #window = Ten()
    window = Preferences()
    window.show()
    APP.exec_()
