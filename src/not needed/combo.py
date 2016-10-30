#!/usr/bin/Python
# -*- coding: utf-8 -*-
__author__ = 'noor'
from PySide.QtCore import Qt
from PySide.QtGui import QCompleter, QComboBox, QSortFilterProxyModel

class ExtendedComboBox(QComboBox):
	def __init__(self, parent=None):
		super(ExtendedComboBox, self).__init__(parent)
		self.setFocusPolicy(Qt.StrongFocus)
		self.setEditable(True)
		self.pFilterModel = QSortFilterProxyModel(self)
		self.pFilterModel.setFilterCaseSensitivity(Qt.CaseInsensitive)
		self.pFilterModel.setSourceModel(self.model())
		self.completer = QCompleter(self.pFilterModel, self)
		self.completer.setCompletionMode(QCompleter.UnfilteredPopupCompletion)
		self.setCompleter(self.completer)

		self.lineEdit().textEdited[unicode].connect(self.pFilterModel.setFilterFixedString)
	def setModel(self, model):
		super(ExtendedComboBox, self).setModel(model)
		self.pFilterModel.setSourceModel(model)
		self.completer.setModel(self.pFilterModel)
	def setModelColumn(self, column):
		self.completer.setCompletionColumn(column)
		self.pFilterModel.setFilterKeyColumn(column)
		super(ExtendedComboBox, self).setModelColumn(column)

if __name__=="__main__":
	import sys
	from PySide.QtGui import QStringListModel, QApplication
	app = QApplication(sys.argv)
	string_list = ['hola modf', 'ghjkli', 'father', 'application', 'man', 'fashion']
	combo = ExtendedComboBox()
	combo.addItems(string_list)
	combo.resize(300, 40)
	combo.show()
	sys.exit(app.exec_())