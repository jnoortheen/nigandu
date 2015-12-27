__author__ = 'noor'
import sys
from PySide.QtCore import *
from PySide.QtGui import *

app = QApplication(sys.argv)
alist = [
            u'\u0b9a', u'\u0b9f', u'\u0bcd', u'\u0b9f', u'\u0b9a',
            u'\u0baa', u'\u0bc8', u'\u0baf', u'\u0bbf', u'\u0bb2',
            u'\u0bcd', u'\u0ba8', u'\u0bc7', u'\u0bb1', u'\u0bcd',
            u'\u0bb1', u'\u0bc1',
            ]
msg = u''.join(alist)

lbl = QLabel("<font color=red size=72><b>" + msg + "</b></font>")
lbl.setWindowFlags(Qt.SplashScreen)
lbl.show()
QTimer.singleShot(3000, app.quit)
app.exec_()