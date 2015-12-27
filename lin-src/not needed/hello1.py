__author__ = 'noor'
import sys
from PySide.QtCore import *
from PySide.QtGui import *

class btn(QPushButton):
    def __init__(self, *args):
        super(QPushButton.__init__, (self,) + args)
        self.setText("Hello World")

class window(QMainWindow):
    def __init__(self, *args):
        super(QMainWindow.__init__, (self,) + args)
        self.button=btn(self)
        self.setCentralWidget(self.button)

def main(args):
    app=QApplication(args)
    win=window()
    win.show()
    app.connect(app, SIGNAL("lastWindowClosed()"),
                app, SLOT("quit()"))
    app.exec_loop()

if __name__=="__main__":
    main(sys.argv)