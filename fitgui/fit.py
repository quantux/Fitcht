import sys
from PyQt4 import QtGui, QtCore

from fitcht import Ui_Dialog

class Main(QtGui.QMainWindow, Ui_Dialog):
	def __init__(self):
		QtGui.QMainWindow.__init__(self)
		self.setupUi(self)
		self.pushButton.clicked.connect(self.callbackOpenFile)

	def callbackOpenFile(self):
		print 'something'
		#filename = QtGui.QFileDialog.getOpenFileName(self, 'Open File', '.')
		#f = open(filename, 'r')
