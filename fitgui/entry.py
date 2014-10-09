import sys
from PyQt4 import QtGui, QtCore
from entryPoint import Ui_dialog
import fitcht
import clientFitcht

class MainEntryPoint(QtGui.QMainWindow, Ui_dialog):
	def __init__(self):
		QtGui.QMainWindow.__init__(self)
		self.setupUi(self)

		self.pushButton.clicked.connect(self.startServer)
		self.pushButton_2.clicked.connect(self.connectServer)
		self.center()

	def center(self):
		frameGm = self.frameGeometry()
		centerPoint = QtGui.QDesktopWidget().availableGeometry().center()
		frameGm.moveCenter(centerPoint)
		self.move(frameGm.topLeft())

	def startServer(self):
		serverName, status = QtGui.QInputDialog.getText(self, 'Server Name', 'Type your server name:')
		if serverName != '' and status:
			self.close()
			dialog = QtGui.QDialog()
			dialog.ui = fitcht.Ui_Dialog()
			dialog.ui.setupUi(dialog, serverName)
			dialog.setAttribute(QtCore.Qt.WA_DeleteOnClose)
			dialog.exec_()

	def connectServer(self):
		serverName, status = QtGui.QInputDialog.getText(self, 'Server Name', 'Type server name or IP to connect:')
		if serverName != '' and status:
			self.close()
			dialog = QtGui.QDialog()
			dialog.ui = clientFitcht.Ui_Dialog()
			dialog.ui.setupUi(dialog, serverName)
			dialog.setAttribute(QtCore.Qt.WA_DeleteOnClose)
			dialog.exec_()

if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	window = MainEntryPoint()
	window.show()
	sys.exit(app.exec_())