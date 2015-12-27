#!usr/bin/Python3
# -*- coding: utf-8 -*-
__version__ = "1.0.0"
__version_info__ = "Alpha level; not tested yet."
__author__ = 'noor'

import sys, sqlite3
from PySide.QtCore import (SIGNAL, Qt, QSize)
from PySide.QtGui import (QStatusBar, QIcon, QDockWidget, QLabel, QApplication, QMainWindow,
                          QAction, QKeySequence, QPushButton, QGridLayout, QVBoxLayout, QWidget,
                          QTextBrowser, QCompleter, QLineEdit, QStringListModel,
                          QMessageBox, QListWidget, QDialogButtonBox, QFont)
import helpform
import webbrowser
from addaword import addawrd
from managebkm import managebkm
from options import optdlg
import qrc

con = sqlite3.connect("nofts.sqlite")
cur = con.cursor()


class mainwin(QMainWindow):
	def __init__(self, parent=None):
		super(mainwin, self).__init__(parent)
		self.setWindowTitle("Nigandu English to Tamil Dictionary")
		self.setGeometry(200, 50, 650, 600)
		self.setMinimumHeight(640)
		self.setMinimumWidth(700)
		self.setMaximumHeight(660)
		self.setMaximumWidth(800)
		#Setting up status bar
		self.myStatusBar = QStatusBar()
		self.myStatusBar.showMessage('Ready', 7000)
		self.setStatusBar(self.myStatusBar)
		#Setting up application icon
		appIcon = QIcon(":/icons/njnlogo.png")
		self.setWindowIcon(appIcon)

		# defining the central widget
		self.central = QWidget(self)

		#combobox plus search button
		self.whole = QVBoxLayout(self.central)
		self.gridlayout = QGridLayout()
		self.comboBox = QLineEdit(self)
		#self.comboBox.setEditable(True)
		self.comboBox.setObjectName("comboBox")
		self.completer = QCompleter(self.comboBox)
		self.completer.setCompletionMode(QCompleter.UnfilteredPopupCompletion)
		self.completer.setCaseSensitivity(Qt.CaseInsensitive)
		self.completer.setMaxVisibleItems(10)
		self.comboBox.setCompleter(self.completer)
		#self.comboBox.setCompleter()
		self.gridlayout.addWidget(self.comboBox, 1, 1, 1, 2)

		self.searchbtn = QPushButton()
		self.searchbtn.setObjectName("searchbtn")
		self.searchbtn.setText("&Search")
		self.gridlayout.addWidget(self.searchbtn, 1, 3)

		vbox = QVBoxLayout()
		self.tamtext = QTextBrowser()
		self.listview = QListWidget(self)
		#self.listview.setEditTriggers(QAbstractItemView.NoEditTriggers)
		self.listview.setWindowTitle("Suggested words")
		self.tamtext.setMinimumHeight(100)
		self.tamtext.setMaximumHeight(150)
		vbox.addWidget(self.tamtext)
		self.suglbl = QLabel(self)
		self.suglbl.setText("Suggested Words:")
		vbox.addWidget(self.suglbl)
		vbox.addWidget(self.listview)

		self.whole.addLayout(self.gridlayout)
		self.whole.addLayout(vbox)
		self.setCentralWidget(self.central)

		#setting docks
		self.histdockwidg = QDockWidget("History", self)
		self.bkmdockwidg = QDockWidget("Book Marks", self)
		self.histdockwidg.setObjectName("self.histdockwidg")
		self.bkmdockwidg.setObjectName("self.bkmdockwidg")

		#self.histdockwidg.setMaximumWidth(histwidth)
		self.histdockwidg.setAllowedAreas(Qt.RightDockWidgetArea)
		self.bkmdockwidg.setAllowedAreas(Qt.RightDockWidgetArea)
		self.histdockwidg.setMaximumWidth(250)
		self.bkmdockwidg.setMaximumWidth(250)
		self.histdockwidg.setMinimumWidth(200)
		self.bkmdockwidg.setMinimumWidth(200)

		#self.bkmdockwidg.setMaximumWidth(histwidth)
		self.histli = QListWidget()
		self.bkmli = QListWidget()
		self.histlis = [0]
		self.bkmlistfromfile = []
		self.histdockwidg.setWidget(self.histli)
		self.bkmdockwidg.setWidget(self.bkmli)
		self.addDockWidget(Qt.RightDockWidgetArea, self.histdockwidg)
		self.addDockWidget(Qt.RightDockWidgetArea, self.bkmdockwidg)

		#file menu
		fi_addwrd = self.createactions("&Add a word...", self.addwrdf, "Alt+A", ":/icons/add.png",
		                               "Add a word to the dictionary. . .")
		fi_options = self.createactions("&Options", self.optionsf, "None", ":/icons/options.png",
		                                "Change the default settings. . .")
		fi_help = self.createactions("&Help", self.helpf, QKeySequence.HelpContents, ":/icons/help.png",
		                             "Help contents. . .")
		fi_quit = self.createactions("&Quit", self.close, QKeySequence.Close, ":/icons/quit.png",
		                             "Close the application. . .")
		fplus = self.createactions("FontPlus", self.fplusf, "None", ":/icons/fplus.png", "Increase the font size")
		fminus = self.createactions("FontMinus", self.fminusf, "None", ":/icons/fminus.png", "Decrease the font size")
		#list of file actions
		fi_menu = (fi_addwrd, fi_options, fi_help, None, fi_quit)

		#go menu
		self.go_prev = self.createactions("&Previous Word", self.prevf, "Alt+Z", ":/icons/prev.png",
		                                  "Previous Word")
		self.go_next = self.createactions("&Next Word", self.nextf, "Alt+X", ":/icons/next.png", "Next Word")
		self.go_rand = self.createactions("&Random Word", self.randf, "Ctrl+R", ":/icons/rand.png",
		                                  "Select a random word")
		#list of go actions
		go_menu = (self.go_prev, self.go_next, self.go_rand )
		self.go_next.setEnabled(False)
		self.go_prev.setEnabled(False)

		#book mark menu
		self.bkm_addfav = self.createactions("&Bookmark", self.addfavf, "Ctrl+B", ":/icons/bookmark.png",
		                                     "Book mark this word")
		self.bkm_viewbkm = self.createactions("&View Bookmarks", self.viewbkmf, "Alt+V", ":/icons/viewbkm.png",
		                                      "View bookmarked words")
		#list of book mark items
		bkm_menu = (self.bkm_addfav, self.bkm_viewbkm)

		#help menu
		hlp_about = self.createactions("Abo&ut", self.aboutf, "Ctrl+U", ":/icons/about.png", "About")
		hlp_visitblog = self.createactions("&Visit Blog", self.visitblogf, "None", ":/icons/visitblog.png",
		                                   "Visit our blog")
		hlp_help = self.createactions("&Help", self.helpf, "Ctrl+H", ":/icons/help.png", "Help Contents")
		#list of help menu items
		hlp_menu = (hlp_about, hlp_visitblog, hlp_help)

		#Setting up the menubar
		filemenu = self.menuBar().addMenu("&File")
		self.addmenu(filemenu, fi_menu)
		gomenu = self.menuBar().addMenu("&Go")
		self.addmenu(gomenu, go_menu)
		bkmmenu = self.menuBar().addMenu("&Book Mark")
		self.addmenu(bkmmenu, bkm_menu)
		helpmenu = self.menuBar().addMenu("&Help")
		self.addmenu(helpmenu, hlp_menu)
		intn = QSize(40, 40)
		self.setIconSize(intn)
		#Setting up the tool bar
		filetools = self.addToolBar("File")
		filetools.setObjectName("filetools")
		self.addmenu(filetools, (fi_addwrd, fplus, fminus))

		gotools = self.addToolBar("Go")
		gotools.setObjectName("gotools")
		self.addmenu(gotools, go_menu)

		bkmtools = self.addToolBar("Bkm")
		bkmtools.setObjectName("bkmtools")
		self.addmenu(bkmtools, bkm_menu)

		hlptools = self.addToolBar("Help")
		hlptools.setObjectName("helptools")
		self.addmenu(hlptools, hlp_menu)

		self.loadfiles()
		self.returncount = 0
		self.bkm_addfav.setEnabled(False)

		#clipboard function
		if str(self.clipauto)=="True":
			clip = QApplication.clipboard()
			cliptxt = clip.text()
			self.comboBox.setText(cliptxt)
			self.setevent()

		#connections
		self.connect(self.comboBox, SIGNAL("textChanged(QString)"), self.search)
		self.connect(self.comboBox, SIGNAL("returnPressed()"), self.returnpressedevent)
		self.connect(self.searchbtn, SIGNAL("clicked()"), self.onenter)
		self.connect(self.listview, SIGNAL("itemDoubleClicked(QListWidgetItem*)"), self.listwidcall)
		self.connect(self.histli, SIGNAL("itemDoubleClicked(QListWidgetItem*)"), self.listwidcall)
		self.connect(self.bkmli, SIGNAL("itemDoubleClicked(QListWidgetItem*)"), self.listwidcall)

	def writehistlis(self, lis):
		if len(lis) >= 2:
			for i in range(1, len(lis)):
				cur.execute("insert into HISTORY values(?)", (lis[i], ))

	def writebkmlis(self, lis):
		cur.execute("delete from BOOKMARKS")
		if len(lis) > 0:
			for i in range(len(lis)):
				cur.execute("insert into BOOKMARKS values(?)", (lis[i], ))

	def listwidcall(self, item):
		self.comboBox.setText(item.text())
		self.setevent()

	def search(self, text, *args):
		li = []
		tplus = text + "%"
		cur.execute("select ENGW from ENGTAM where ENGW like ? limit 20", (tplus, ))
		cuf = cur.fetchall()
		model = QStringListModel()
		for i in range(len(cuf)):
			k = cuf[i][0]
			li.append(k)
		model.setStringList(li)
		self.completer.setModel(model)

	def returnpressedevent(self, *args):
		self.comboBox.selectAll()
		self.returncount += 1
		if self.returncount % 2 == 0:
			self.setevent()
		else:
			self.comboBox.selectAll()

	def setevent(self):
		self.comboBox.selectAll()
		self.bkm_addfav.setEnabled(True)
		lis = []
		eng = self.comboBox.text()
		cur.execute("SELECT rowid, TAMW FROM ENGTAM WHERE ENGW like ? limit 1", (eng,))
		cuf = cur.fetchall()
		if len(cuf) == 0:
			self.tamtext.setText("No words found. . . ")
			self.listview.addItem("No Suggestions. . .")
		else:
			for i in range(len(cuf)):
				tam = cuf[0][1]
				rowid = cuf[0][0]
				self.tamtext.setText(tam)
				if rowid <= 25:
					start = 0
					end = 50
				elif rowid >= 190513:
					start = rowid - 190487
					end = rowid + 190537
				else:
					start = rowid - 25
					end = rowid + 25
				cur.execute("SELECT ENGW FROM ENGTAM WHERE rowid>=? and rowid<=?", (start, end, ))
				cuff = cur.fetchall()
				for i in range(len(cuff)):
					engw = cuff[i][0]
					lis.append(engw)
				if self.listview.count() is not None:
					self.listview.clear()
				self.listview.addItems(lis)
				self.addtoli(eng, self.histlis)
				if self.histlis[0] >= 2:
					self.go_prev.setEnabled(True)
				self.comboBox.setFocus()
				if self.histdock:
					self.histli.addItem(eng)

	def addtoli(self, addw, lis, c=1):
		if len(lis) > 0:
			if type(lis[0]) == int:
				if len(lis) >= 2:
					for i in range(1, len(lis)):
						if lis[i] == addw:
							c = 0
							pass
					if c == 1:
						lis.append(addw)
				else:
					lis.append(addw)
				lis[0] = len(lis) - 1

	def addtobkmli(self, addw, lis, nc=1):
		for i in range(len(lis)):
			if lis[i] == addw:
				nc = 0
				pass
		if nc == 1:
			lis.append(addw)

	def onenter(self, *args):
		self.comboBox.selectAll()
		self.setevent()

	def loadfiles(self):
		self.loadsettings()
		self.loadhistlis()
		self.loadbkm()
		self.setfontsize(int(self.fontsize))
		self.setdocks()


	def setdocks(self):
		ist = str(self.histdock)
		jst = str(self.bkmdock)

		if ist == "False":
			self.removedock(self.histdockwidg)
		else:
			self.adddock(self.histdockwidg)

		if jst == "False":
			self.removedock(self.bkmdockwidg)
		else:
			self.adddock(self.bkmdockwidg)

	def loadsettings(self):
		cur.execute("select * from SETTINGS")
		cuffun = cur.fetchall()
		fn = int(cuffun[0][1])
		self.fontsize = fn
		self.clipauto = cuffun[1][1]
		self.histdock = cuffun[2][1]
		self.savehist = cuffun[3][1]
		self.bkmdock = cuffun[4][1]
		self.delhist = cuffun[5][1]
		self.delbkm = cuffun[6][1]

	def loadhistlis(self):
		histtodockli = []
		cur.execute("select * from HISTORY")
		historyfetch = cur.fetchall()
		for i in range(len(historyfetch)):
				self.addtobkmli(historyfetch[i][0], histtodockli)
		for i in histtodockli:
			self.histli.addItem(i)

	def loadbkm(self):
		cur.execute("select * from BOOKMARKS")
		bkmfetch = cur.fetchall()
		for i in range(len(bkmfetch)):
				self.addtobkmli(bkmfetch[i][0], self.bkmlistfromfile)
		for i in self.bkmlistfromfile:
			self.bkmli.addItem(i)

	def createactions(self, text, slot=None, shortcut="None", icon=None, tip=None, checkable=False,
	                  signal="triggered()"):
		action = QAction(text, self)
		if icon is not None:
			action.setIcon(QIcon(icon))
		if shortcut is not None:
			action.setShortcut(shortcut)
		if tip is not None:
			action.setToolTip(tip)
			action.setStatusTip(tip)
		if slot is not None:
			self.connect(action, SIGNAL(signal), slot)
		if checkable:
			action.setCheckable(True)
		return action

	def addmenu(self, target, actions):
		for action in actions:
			if action is None:
				target.addSeparator()
			else:
				target.addAction(action)

	#Actions
	def addwrdf(self):
		self.dlg = addawrd()
		self.dlg.show()
		self.connect(self.dlg.buttonBox, SIGNAL("rejected()"), self.dlg.close)
		self.connect(self.dlg.buttonBox, SIGNAL("accepted()"), self.addawordtodb)


	def addawordtodb(self):
		eng = self.dlg.lineEdit.text()
		tam = self.dlg.lineEdit_2.text()
		if len(eng) != 0 and len(tam) != 0:
			cur.execute("INSERT INTO ENGTAM(ENGW, TAMW) VALUES(?, ?)", (eng, tam, ))
			self.dlg.close()
			QMessageBox.information(self, "Nigandu Eng -> Tam Dictionary", "Added Successfully. . .")
		else:
			self.dlg.lineEdit.setFocus()
			self.dlg.close()
			QMessageBox.warning(self, "Nigandu Eng -> Tam Dictionary", "Invalid Entry. . .")

	def optionsf(self):
		self.opt = optdlg(self)
		self.opt.spinBox.setProperty("value", int(self.fontsize))
		font = QFont()
		font.setPixelSize(int(self.fontsize))
		self.opt.sampletxt.setFont(font)

		if str(self.clipauto) == "True":
			self.opt.checkclip.setChecked(True)
		elif str(self.clipauto) == "False":
			self.opt.checkclip.setChecked(False)

		if str(self.histdock) == "True":
			self.opt.checkshowhistdock.setChecked(True)
		elif str(self.histdock) == "False":
			self.opt.checkshowhistdock.setChecked(False)

		if str(self.bkmdock) == "True":
			self.opt.checkshowbkmdock.setChecked(True)
		elif str(self.bkmdock) == "False":
			self.opt.checkshowbkmdock.setChecked(False)

		self.opt.show()
		self.connect(self.opt.buttonBox, SIGNAL("accepted()"), self.optok)
		self.connect(self.opt.buttonBox.button(QDialogButtonBox.Apply), SIGNAL("clicked()"), self.optapply)
		self.connect(self.opt.checkdelhist, SIGNAL("stateChanged(int)"), self.deleteallhist)
		self.connect(self.opt.checkshowhistdock, SIGNAL("stateChanged(int)"), self.shownexttime)
		self.connect(self.opt.checkshowbkmdock, SIGNAL("stateChanged(int)"), self.shownexttime)

	def shownexttime(self, i):
		if i == 0:
			pass
		if i == 2:
			QMessageBox.information(self, self.windowTitle(), "Click Apply or Ok \n The Dock window will be added, \n the next time you start the application. . .")

	def optok(self):
		self.optapply()
		self.opt.close()

	def optapply(self):
		self.updatesettings()
		self.applyopt()

	def updatesettings(self):
		self.fontsize = self.opt.spinBox.value()
		self.clipauto = self.opt.checkclip.isChecked()
		self.histdock = self.opt.checkshowhistdock.isChecked()
		self.bkmdock = self.opt.checkshowbkmdock.isChecked()
		self.delhist = self.opt.checkdelhist.isChecked()

		for i, j in [("fontsize", self.fontsize),("clipauto", str(self.clipauto)),("histdock", str(self.histdock)),
		             ("bkmdock", str(self.bkmdock)),("delhist", str(self.delhist))]:
			cur.execute("UPDATE SETTINGS SET setting=? WHERE field=?", (j, i, ))


	def applyopt(self):
		self.loadsettings()
		self.setfontsize(int(self.fontsize))
		if str(self.bkmdock) == "False" or str(self.histdock) == "False":
			self.setdocks()

	def removedock(self, dock):
		self.removeDockWidget(dock)

	def adddock(self, dock):
		self.addDockWidget(Qt.RightDockWidgetArea, dock)

	def deleteallhist(self, i):
		if i == 0:
			pass
		elif i == 2:
			self.histli.clear()
			self.histlis = [0]
			cur.execute("delete from HISTORY")
			QMessageBox.information(self, self.windowTitle(), "All the History Records are deleted. . .")

	def setfontsize(self, i):
		if i >= 8 or i <= 24:
			font = QFont()
			font.setPixelSize(i)
			self.comboBox.setFont(font)
			self.searchbtn.setFont(font)
			self.bkmli.setFont(font)
			self.histli.setFont(font)
			self.listview.setFont(font)
			self.tamtext.setFont(font)

	def helpf(self):
		form = helpform.HelpForm("index.html", self)
		form.show()

	def closeEvent(self, *args, **kwargs):
		self.writehistlis(self.histlis)
		self.writebkmlis(self.bkmlistfromfile)

		for i, j in [("fontsize", int(self.fontsize)),("clipauto", str(self.clipauto)),("histdock", str(self.histdock)),
		             ("bkmdock", str(self.bkmdock)),("delhist", str(self.delhist))]:
			cur.execute("UPDATE SETTINGS SET setting=? WHERE field=?", (j, i, ))

		con.commit()
		con.close()

	def fplusf(self):
		self.fontsize += 1
		if self.fontsize <= 24:
			self.setfontsize(self.fontsize)

	def fminusf(self):
		self.fontsize -= 1
		if self.fontsize >= 10:
			self.setfontsize(self.fontsize)

	def prevf(self):
		pr = self.histlis[0] - 1
		if pr > 1:
			self.comboBox.setText(self.histlis[pr])
			self.setevent()
			self.histlis[0] = pr
			self.go_next.setEnabled(True)
		elif pr == 1:
			self.comboBox.setText(self.histlis[pr])
			self.setevent()
			self.histlis[0] = pr
			self.go_next.setEnabled(True)
			self.go_prev.setEnabled(False)
		else:
			pass

	def nextf(self):
		pr = self.histlis[0] + 1
		if pr < len(self.histlis) - 1:
			self.comboBox.setText(self.histlis[pr])
			self.setevent()
			self.histlis[0] = pr
			self.go_prev.setEnabled(True)
		elif pr == len(self.histlis) - 1:
			self.comboBox.setText(self.histlis[pr])
			self.setevent()
			self.histlis[0] = pr
			self.go_prev.setEnabled(True)
			self.go_next.setEnabled(False)
		else:
			pass

	def randf(self):
		import random

		n = random.randrange(190538)
		cur.execute("select ENGW from ENGTAM where rowid = ?", (n, ))
		cuf = cur.fetchone()
		self.comboBox.setText(cuf[0])
		self.setevent()

	def addfavf(self):
		txt = self.comboBox.text()
		if len(txt) != 0:
			self.addtobkmli(txt, self.bkmlistfromfile)
			self.writetolistwidget(self.bkmlistfromfile, self.bkmli)


	def sortit(self):
		self.bkmlistfromfile.sort()
		self.writetolistwidget(self.bkmlistfromfile, self.form.listWidget)
		self.writetolistwidget(self.bkmlistfromfile, self.bkmli)
		cur.execute("delete from BOOKMARKS")


	def writetolistwidget(self, lis, liswid):
		liswid.clear()
		for i in lis:
			liswid.addItem(i)

	def deletecurrentbkm(self):
		ct = self.form.listWidget.currentItem().text()
		self.bkmlistfromfile.remove(ct)
		self.writetolistwidget(self.bkmlistfromfile, self.bkmli)
		self.writetolistwidget(self.bkmlistfromfile, self.form.listWidget)
		cur.execute("delete from BOOKMARKS")

	def deleteallbkm(self):
		self.form.listWidget.clear()
		self.bkmli.clear()
		self.bkmlistfromfile = []
		cur.execute("delete from BOOKMARKS")

	def viewbkmf(self):
		self.form = managebkm(self)
		self.writetolistwidget(self.bkmlistfromfile, self.form.listWidget)
		self.form.show()
		self.connect(self.form.closebtn, SIGNAL("clicked()"), self.form.close)
		self.connect(self.form.sortbtn, SIGNAL("clicked()"), self.sortit)
		self.connect(self.form.deletebtn, SIGNAL("clicked()"), self.deletecurrentbkm)
		self.connect(self.form.deleteallbtn, SIGNAL("clicked()"), self.deleteallbkm)

	def aboutf(self):
		QMessageBox.about(self, "About Nigandu English to Tamil Dictionary",
		                  """<b>Nigandu English to Tamil Dictionary</b> v %s
			                  <p>This is the first corss-platform English to Tamil
			                  bilingual dictionary; Free to use.</p>
			                  <p>&copy; copyright 2014-05-01 12:51:57 - All Rights Reserved.</p>
	                          <p>Thanks to Python and PySide Project.</p>
	                          <p>Using Python 3.3, Qt 4.8 and PySide 1.2.1</p>
	                        """ % (__version__))

	def visitblogf(self):
		webbrowser.open("http://www.nigandu.blogspot.com")

def main():
	QApplication.setColorSpec(QApplication.ManyColor)
	app = QApplication(sys.argv)
	app.setOrganizationName("NJN Ltd.")
	app.setOrganizationDomain("e-nool.blogspot.com")
	app.setApplicationName("Nigandu English to Tamil Dictionary")
	app.setWindowIcon(QIcon(":/icons/njnlogo.png"))
	form = mainwin()
	form.show()
	app.exec_()


if __name__ == '__main__':
	main()
