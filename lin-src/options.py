# -*- coding: utf-8 -*-
__author__ = 'noor'
from PySide.QtCore import QRect, Qt
from PySide.QtGui import QLabel, QPushButton, QDialogButtonBox, QGroupBox, QSpinBox, QDialog, QIcon, QCheckBox, QFont

class optdlg(QDialog):
	def __init__(self, parent=None):
		super(optdlg, self).__init__(parent)
		self.setFixedSize(484, 399)
		appicom = QIcon(":/icons/njnlogo.png")
		self.setWindowIcon(appicom)
		self.setWindowTitle("Nigandu English to Tamil Dictionary | OPTIONS")

		self.buttonBox = QDialogButtonBox(self)
		self.buttonBox.setEnabled(True)
		self.buttonBox.setGeometry(QRect(350, 20, 121, 200))

		self.buttonBox.setOrientation(Qt.Vertical)
		self.buttonBox.setStandardButtons(QDialogButtonBox.Apply|QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
		self.buttonBox.setCenterButtons(True)
		self.restorebtn = QPushButton(self)
		self.restorebtn.setGeometry(QRect(354, 360, 121, 23))
		self.restorebtn.setText("&RestoreDefults")

		self.fontbox = QGroupBox(self)
		self.fontbox.setGeometry(QRect(10, 10, 331, 141))
		self.spinBox = QSpinBox(self.fontbox)
		self.spinBox.setGeometry(QRect(100, 20, 81, 21))
		self.spinBox.setMinimum(10)
		self.spinBox.setMaximum(24)
		self.label = QLabel(self.fontbox)
		self.label.setGeometry(QRect(20, 20, 71, 21))
		self.label.setText("Font Size:")
		self.fontbox.setTitle("Font")
		self.samplefontbox = QGroupBox(self)
		self.samplefontbox.setGeometry(QRect(20, 50, 291, 91))
		self.samplefontbox.setTitle("Sample Text")
		self.sampletxt = QLabel(self.samplefontbox)
		self.sampletxt.setGeometry(QRect(20, 20, 251, 61))
		self.sampletxt.setText("AaBbCcDdEeFfGgHhIiJjKkLlYyZz")

		self.clipbox = QGroupBox(self)
		self.clipbox.setGeometry(QRect(10, 160, 331, 61))
		self.clipbox.setTitle("ClipBoard Options")
		self.checkclip = QCheckBox(self.clipbox)
		self.checkclip.setGeometry(QRect(20, 20, 301, 31))
		self.checkclip.setText("Allow copy from clipboard on start-up")


		self.histbox = QGroupBox(self)
		self.histbox.setGeometry(QRect(10, 230, 331, 91))
		self.histbox.setTitle("History")
		self.checkshowhistdock = QCheckBox(self.histbox)
		self.checkshowhistdock.setGeometry(QRect(20, 60, 301, 17))

		self.checkshowhistdock.setText("Show History Dock on the right side")
		self.checkdelhist = QCheckBox(self.histbox)
		self.checkdelhist.setGeometry(QRect(20, 30, 301, 17))
		self.checkdelhist.setText("Clear all the past history records")

		self.bkmbox = QGroupBox(self)
		self.bkmbox.setGeometry(QRect(10, 330, 331, 61))
		self.bkmbox.setTitle("Book Marks")
		self.checkshowbkmdock = QCheckBox(self.bkmbox)
		self.checkshowbkmdock.setGeometry(QRect(20, 30, 301, 17))
		self.checkshowbkmdock.setText("Show Book Marks Dock on the right side.")

		self.spinBox.valueChanged[int].connect(self.setsampletxt)
		self.restorebtn.clicked.connect(self.setdeafults)
		self.buttonBox.rejected.connect(self.close)


	def setdeafults(self):
		self.spinBox.setValue(13)
		self.checkshowhistdock.setChecked(True)
		self.checkshowbkmdock.setChecked(True)
		self.checkclip.setChecked(True)
		self.checkdelhist.setChecked(False)

	def setsampletxt(self, i):
		font = QFont()
		font.setPixelSize(i)
		self.sampletxt.setFont(font)


