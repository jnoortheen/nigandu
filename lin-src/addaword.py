__author__ = 'noor'

from PySide.QtGui import QDialog, QLabel, QLineEdit, QDialogButtonBox, QIcon, QHBoxLayout, QWidget
from PySide.QtCore import QRect, QSize

class addawrd(QDialog):
	def __init__(self, parent=None):
		super(addawrd, self).__init__(parent)
		appicom = QIcon(":/icons/njnlogo.png")
		self.setWindowIcon(appicom)
		self.setWindowTitle("Nigandu | Add a word")
		self.setFixedSize(364, 188)

		self.horizontalLayoutWidget = QWidget(self)
		self.horizontalLayoutWidget.setGeometry(QRect(10, 10, 341, 61))
		self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")

		self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
		self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
		self.horizontalLayout.setObjectName("horizontalLayout")

		self.label = QLabel(self.horizontalLayoutWidget)
		self.label.setMinimumSize(QSize(70, 25))
		self.horizontalLayout.addWidget(self.label)
		self.label.setText("English Word:")

		self.lineEdit = QLineEdit(self.horizontalLayoutWidget)
		self.lineEdit.setEnabled(True)
		self.lineEdit.setMinimumSize(QSize(0, 25))
		self.lineEdit.setObjectName("lineEdit_2")
		self.horizontalLayout.addWidget(self.lineEdit)
		self.lineEdit.setFocus()

		self.buttonBox = QDialogButtonBox(self)
		self.buttonBox.setGeometry(QRect(10, 150, 341, 25))
		self.buttonBox.setMinimumSize(QSize(70, 25))
		self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Save)
		self.buttonBox.setObjectName("buttonBox")

		self.horizontalLayoutWidget_2 = QWidget(self)
		self.horizontalLayoutWidget_2.setGeometry(QRect(10, 80, 341, 61))
		self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
		self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget_2)
		self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
		self.horizontalLayout_2.setObjectName("horizontalLayout_2")

		self.label_2 = QLabel(self.horizontalLayoutWidget_2)
		self.label_2.setMinimumSize(QSize(70, 25))
		self.label_2.setObjectName("label_2")
		self.horizontalLayout_2.addWidget(self.label_2)
		self.label_2.setText("Tamil Word:")

		self.lineEdit_2 = QLineEdit(self.horizontalLayoutWidget_2)
		self.lineEdit_2.setMinimumSize(QSize(0, 25))
		self.lineEdit_2.setObjectName("lineEdit_3")
		self.horizontalLayout_2.addWidget(self.lineEdit_2)

		self.setTabOrder(self.lineEdit, self.lineEdit_2)
		self.setTabOrder(self.lineEdit_2, self.buttonBox)