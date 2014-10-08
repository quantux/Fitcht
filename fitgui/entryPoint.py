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

class Ui_dialog(object):
	def setupUi(self, dialog):
		dialog.setObjectName(_fromUtf8("dialog"))
		dialog.resize(615, 488)
		dialog.setMinimumSize(QtCore.QSize(615, 488))
		dialog.setMaximumSize(QtCore.QSize(615, 488))
		icon = QtGui.QIcon()
		icon.addPixmap(QtGui.QPixmap(_fromUtf8("fitcht.bmp")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		dialog.setWindowIcon(icon)
		dialog.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
		self.graphicsView = QtGui.QGraphicsView(dialog)
		self.graphicsView.setGeometry(QtCore.QRect(-90, -110, 891, 611))
		self.graphicsView.setStyleSheet(_fromUtf8("background-image: url(:/FitchtBackgroundImage/FitchtLogo.jpg);"))
		self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
		self.pushButton = QtGui.QPushButton(dialog)
		self.pushButton.setGeometry(QtCore.QRect(240, 390, 141, 26))
		self.pushButton.setStyleSheet(_fromUtf8("background-color: rgb(245, 245, 245);\n"
"outline: none;"))
		self.pushButton.setObjectName(_fromUtf8("pushButton"))
		self.pushButton_2 = QtGui.QPushButton(dialog)
		self.pushButton_2.setGeometry(QtCore.QRect(240, 430, 141, 26))
		self.pushButton_2.setStyleSheet(_fromUtf8("background-color: rgb(245, 245, 245);\n"
"outline: none;"))
		self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))

		self.retranslateUi(dialog)
		QtCore.QMetaObject.connectSlotsByName(dialog)

	def retranslateUi(self, dialog):
		dialog.setWindowTitle(_translate("dialog", "Fitcht", None))
		self.pushButton.setText(_translate("dialog", "Create Server", None))
		self.pushButton_2.setText(_translate("dialog", "Connect to Room", None))

import resourceFile_rc