#!/usr/bin/env python

from PySide.QtCore import QUrl, Qt
from PySide.QtGui import (QDialog, QLabel, QIcon, QToolBar, QPixmap, QTextBrowser, QVBoxLayout)
import qrc

class HelpForm(QDialog):
	def __init__(self, page, parent=None):
		super(HelpForm, self).__init__(parent)
		self.pageLabel = QLabel("<font color=purple size=30><b>Help Contents</b></font>")
		self.pageLabel.setMinimumSize(400, 50)
		self.pageLabel.setAlignment(Qt.AlignCenter)
		appicom = QIcon(":/icons/njnlogo.png")
		self.setWindowIcon(appicom)
		toolBar = QToolBar()

		pixmap = QPixmap(":/icons/njnlogo.png")
		lbl = QLabel(self)
		lbl.setPixmap(pixmap)
		lbl.setFixedSize(70, 70)
		toolBar.setMinimumHeight(70)
		toolBar.setMaximumHeight(80)
		toolBar.addWidget(lbl)
		toolBar.addWidget(self.pageLabel)

		self.textBrowser = QTextBrowser()

		layout = QVBoxLayout()
		layout.addWidget(toolBar)
		layout.addWidget(self.textBrowser, 1)
		self.setLayout(layout)

		self.textBrowser.setSource(QUrl(page))
		self.setMinimumSize(650, 650)
		self.setMaximumSize(650, 660)
		self.setWindowTitle("Nigandu English to Tamil Dictionary | HELP")