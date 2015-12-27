__author__ = 'noor'
from PySide.QtGui import (QDialog, QLabel, QIcon, QWidget, QVBoxLayout, QPushButton, QListWidget, QFont)
from PySide.QtCore import QRect

class managebkm(QDialog):
	def __init__(self, parent=None):
		super(managebkm, self).__init__(parent)
		appicom = QIcon(":/icons/njnlogo.png")
		self.setWindowIcon(appicom)
		self.setWindowTitle("Nigandu | Manage Book Marks")
		self.setFixedSize(463, 242)

		self.verticalLayoutWidget = QWidget(self)
		self.verticalLayoutWidget.setGeometry(QRect(350, 30, 101, 201))
		self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
		self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
		self.verticalLayout.setContentsMargins(0, 0, 0, 0)
		self.verticalLayout.setObjectName("verticalLayout")

		self.sortbtn = QPushButton(self.verticalLayoutWidget)
		self.sortbtn.setText("&Sort")
		self.verticalLayout.addWidget(self.sortbtn)

		self.deletebtn = QPushButton(self.verticalLayoutWidget)
		self.deletebtn.setText("&Delete")
		self.verticalLayout.addWidget(self.deletebtn)

		self.deleteallbtn = QPushButton(self.verticalLayoutWidget)
		self.deleteallbtn.setText("Delete &All")
		self.verticalLayout.addWidget(self.deleteallbtn)

		self.closebtn = QPushButton(self.verticalLayoutWidget)
		self.closebtn.setText("&Close")
		self.verticalLayout.addWidget(self.closebtn)

		self.listWidget = QListWidget(self)
		self.listWidget.setGeometry(QRect(10, 30, 331, 201))

		self.label = QLabel(self)
		self.label.setGeometry(QRect(20, 10, 91, 25))
		font = QFont()
		font.setPointSize(10)
		self.label.setFont(font)
		self.label.setBuddy(self.listWidget)
		self.label.setText("Book Mark List:")
