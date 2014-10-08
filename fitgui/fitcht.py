import sys, os
from PyQt4 import QtCore, QtGui

try:
	_fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
	def _fromUtf8(s):
		return s

try:
	_encoding = QtGui.QApplication.UnicodeUTF8
	def _translate(context, text, disambig):
		return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
	def _translate(context, text, disambig):
		return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(QtGui.QMainWindow):
	def setupUi(self, Dialog, serverName):
		Dialog.setObjectName(_fromUtf8("Dialog"))
		Dialog.setWindowModality(QtCore.Qt.NonModal)
		Dialog.resize(615, 488)
		Dialog.setMinimumSize(QtCore.QSize(615, 488))
		Dialog.setMaximumSize(QtCore.QSize(615, 488))
		Dialog.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
		self.list = []
		icon = QtGui.QIcon()
		icon.addPixmap(QtGui.QPixmap(_fromUtf8("resources/fitcht.bmp")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		Dialog.setWindowIcon(icon)
		Dialog.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
		self.selectedFiles = QtGui.QTreeView(Dialog)
		self.selectedFiles.setGeometry(QtCore.QRect(-10, 40, 191, 461))
		self.selectedFiles.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
		self.selectedFiles.setStyleSheet(_fromUtf8("background-color: rgb(200, 200, 200);"))
		self.selectedFiles.setAlternatingRowColors(False)
		self.selectedFiles.setObjectName(_fromUtf8("selectedFiles"))
		self.declarativeView = QtDeclarative.QDeclarativeView(Dialog)
		self.declarativeView.setGeometry(QtCore.QRect(0, 0, 621, 41))
		self.declarativeView.setStyleSheet(_fromUtf8("background-color: rgb(57, 51, 51);"))
		self.declarativeView.setObjectName(_fromUtf8("declarativeView"))
		self.pushButton = QtGui.QPushButton(Dialog)
		self.pushButton.clicked.connect(self.openFileButtonCallback)
		self.pushButton.setGeometry(QtCore.QRect(26, 80, 111, 41))
		self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
		self.pushButton.setStyleSheet(_fromUtf8("border-width: 0px; border-style: solid;\n"
"background-color: rgb(200, 200, 200);\n"
"outline: none;"))
		icon1 = QtGui.QIcon()
		icon1.addPixmap(QtGui.QPixmap(_fromUtf8("resources/new10.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.pushButton.setIcon(icon1)
		self.pushButton.setObjectName(_fromUtf8("pushButton"))
		self.pushButton_2 = QtGui.QPushButton(Dialog)
		self.pushButton_2.clicked.connect(self.deleteCallBackFunction)
		self.pushButton_2.setGeometry(QtCore.QRect(30, 150, 111, 41))
		self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
		self.pushButton_2.setStyleSheet(_fromUtf8("border-width: 0px; border-style: solid;\n"
"background-color: rgb(200, 200, 200);\n"
"outline: none;"))
		icon2 = QtGui.QIcon()
		icon2.addPixmap(QtGui.QPixmap(_fromUtf8("resources/big60.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.pushButton_2.setIcon(icon2)
		self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
		self.pushButton_3 = QtGui.QPushButton(Dialog)
		self.pushButton_3.clicked.connect(self.DisconnectButtonCallback)
		self.pushButton_3.setGeometry(QtCore.QRect(30, 220, 111, 41))
		self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
		self.pushButton_3.setStyleSheet(_fromUtf8("border-width: 0px; border-style: solid;\n"
"background-color: rgb(200, 200, 200);\n"
"outline: none;"))
		icon3 = QtGui.QIcon()
		icon3.addPixmap(QtGui.QPixmap(_fromUtf8("resources/system_log_out.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.pushButton_3.setIcon(icon3)
		self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
		self.toolButton = QtGui.QToolButton(Dialog)
		self.toolButton.setGeometry(QtCore.QRect(550, 10, 31, 25))
		self.toolButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
		self.toolButton.setToolTip(_fromUtf8(""))
		self.toolButton.setStatusTip(_fromUtf8(""))
		self.toolButton.setStyleSheet(_fromUtf8("border-width: 0px; border-style: solid;\n"
"background-color: rgb(57, 51, 51);\n"
""))
		icon4 = QtGui.QIcon()
		icon4.addPixmap(QtGui.QPixmap(_fromUtf8("resources/settings-32.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.toolButton.setIcon(icon4)
		self.toolButton.setObjectName(_fromUtf8("toolButton"))
		self.listWidget = QtGui.QListWidget(Dialog)
		self.listWidget.setGeometry(QtCore.QRect(200, 60, 401, 411))
		self.listWidget.setObjectName(_fromUtf8("listWidget"))

		self.retranslateUi(Dialog)
		QtCore.QMetaObject.connectSlotsByName(Dialog)

	def openFileButtonCallback(self):
		fileName = QtGui.QFileDialog.getOpenFileName(self, 'Open File', '.')
		fileNameWithoutDirectory = os.path.basename(str(fileName))
		fileExtension = os.path.splitext(fileNameWithoutDirectory)[1][1:]
		item = QtGui.QListWidgetItem()
		icon8 = QtGui.QIcon()
		if not os.path.isfile('resources/fileExtensionIcons/%s-icon.png' % fileExtension):
			fileExtension = 'undefined'
		icon8.addPixmap(QtGui.QPixmap(_fromUtf8("resources/fileExtensionIcons/%s-icon.png" % str(fileExtension))), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		item.setIcon(icon8)
		item.setText(_translate("Dialog", ("%s" % fileNameWithoutDirectory), None))
		self.listWidget.addItem(item)
		self.list.append([item, str(fileName)])
		print self.list

	def deleteCallBackFunction(self):
		for itemIndex, itemDirectory in self.list:
			if self.listWidget.currentItem() == itemIndex:
				self.list.remove([itemIndex, itemDirectory])
		self.listWidget.takeItem(self.listWidget.currentRow())
		print self.list

	def DisconnectButtonCallback(self):
		self.close()
		sys.exit()


	def retranslateUi(self, Dialog):
		Dialog.setWindowTitle(_translate("Dialog", "Fitcht", None))
		self.pushButton.setText(_translate("Dialog", "Add Files", None))
		self.pushButton_2.setText(_translate("Dialog", "Delete File", None))
		self.pushButton_3.setText(_translate("Dialog", "Disconnect", None))
		self.toolButton.setText(_translate("Dialog", "...", None))
		__sortingEnabled = self.listWidget.isSortingEnabled()
		self.listWidget.setSortingEnabled(False)
		self.listWidget.setSortingEnabled(__sortingEnabled)

from PyQt4 import QtDeclarative

