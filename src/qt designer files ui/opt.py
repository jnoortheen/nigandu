# -*- coding: utf-8 -*-
from PySide import QtCore, QtGui
import sys

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(484, 399)

        self.buttonBox = QtGui.QDialogButtonBox(Form)
        self.buttonBox.setEnabled(True)
        self.buttonBox.setGeometry(QtCore.QRect(350, 20, 121, 161))

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonBox.sizePolicy().hasHeightForWidth())

        self.buttonBox.setSizePolicy(sizePolicy)
        self.buttonBox.setAutoFillBackground(True)
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Apply|QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")

        self.groupBox = QtGui.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 331, 141))
        self.groupBox.setObjectName("groupBox")

        self.spinBox = QtGui.QSpinBox(self.groupBox)
        self.spinBox.setGeometry(QtCore.QRect(100, 20, 81, 21))
        self.spinBox.setMinimum(8)
        self.spinBox.setMaximum(26)
        self.spinBox.setProperty("value", 11)
        self.spinBox.setObjectName("spinBox")

        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 20, 71, 21))
        self.label.setObjectName("label")

        self.groupBox_5 = QtGui.QGroupBox(self.groupBox)
        self.groupBox_5.setGeometry(QtCore.QRect(20, 50, 291, 91))
        self.groupBox_5.setObjectName("groupBox_5")

        self.label_2 = QtGui.QLabel(self.groupBox_5)
        self.label_2.setGeometry(QtCore.QRect(20, 20, 251, 61))
        self.label_2.setObjectName("label_2")

        self.groupBox_2 = QtGui.QGroupBox(Form)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 160, 331, 61))
        self.groupBox_2.setObjectName("groupBox_2")

        self.checkBox = QtGui.QCheckBox(self.groupBox_2)
        self.checkBox.setGeometry(QtCore.QRect(20, 20, 301, 31))
        self.checkBox.setObjectName("checkBox")

        self.groupBox_3 = QtGui.QGroupBox(Form)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 230, 331, 91))
        self.groupBox_3.setObjectName("groupBox_3")

        self.checkBox_2 = QtGui.QCheckBox(self.groupBox_3)
        self.checkBox_2.setGeometry(QtCore.QRect(20, 60, 301, 17))
        self.checkBox_2.setChecked(True)
        self.checkBox_2.setObjectName("checkBox_2")

        self.checkBox_3 = QtGui.QCheckBox(self.groupBox_3)
        self.checkBox_3.setGeometry(QtCore.QRect(20, 30, 301, 17))
        self.checkBox_3.setObjectName("checkBox_3")

        self.groupBox_4 = QtGui.QGroupBox(Form)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 330, 331, 61))
        self.groupBox_4.setObjectName("groupBox_4")

        self.checkBox_4 = QtGui.QCheckBox(self.groupBox_4)
        self.checkBox_4.setGeometry(QtCore.QRect(20, 30, 301, 17))
        self.checkBox_4.setChecked(True)
        self.checkBox_4.setObjectName("checkBox_4")

        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(354, 360, 121, 23))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("Form", "Font", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "Font Size:", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_5.setTitle(QtGui.QApplication.translate("Form", "Sample Text", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Form", "AaBbCcDdEeFfGgHhIiJjKkLlYyZz", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("Form", "Clip Board OPtions", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox.setText(QtGui.QApplication.translate("Form", "Allow copy from Clip Board on startup", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("Form", "History", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_2.setText(QtGui.QApplication.translate("Form", "Show History Dockl on the right side.", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_3.setText(QtGui.QApplication.translate("Form", "Clear all the history records.", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_4.setTitle(QtGui.QApplication.translate("Form", "Book Marks", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_4.setText(QtGui.QApplication.translate("Form", "Show Book Marks Dock on the right side.", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("Form", "&RestoreDefaults", None, QtGui.QApplication.UnicodeUTF8))

