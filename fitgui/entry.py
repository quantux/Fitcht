import sys
from PyQt4 import QtGui, QtCore
from entryPoint import Ui_dialog
import fitcht
import clientFitcht

# This is where the program Starts. It'll call other Dialog class such as clientFitcht.py
class MainEntryPoint(QtGui.QMainWindow, Ui_dialog):

	# Constructor Class used to Start UI and set event signals to buttons
	def __init__(self):
		QtGui.QMainWindow.__init__(self)
		self.setupUi(self)

		self.pushButton.clicked.connect(self.startServer)
		self.pushButton_2.clicked.connect(self.connectServer)
		self.center()

	# Center the application on the screen
	def center(self):
		frameGm = self.frameGeometry()
		centerPoint = QtGui.QDesktopWidget().availableGeometry().center()
		frameGm.moveCenter(centerPoint)
		self.move(frameGm.topLeft())

	# Method to call fitcht Dialog and destroy this class itself
	def startServer(self):
		serverName, status = QtGui.QInputDialog.getText(self, 'Server Name', 'Type your server name:')
		if serverName != '' and status:
			self.close()
			dialog = QtGui.QDialog()
			dialog.ui = fitcht.Ui_Dialog()
			dialog.ui.setupUi(dialog, serverName)
			dialog.setAttribute(QtCore.Qt.WA_DeleteOnClose)
			dialog.exec_()

	# Method to call clientFitcht Dialog and destroy this class itself
	def connectServer(self):
		serverName, status = QtGui.QInputDialog.getText(self, 'Server Name', 'Type server name or IP to connect:')
		if serverName != '' and status:
			self.close()
			dialog = QtGui.QDialog()
			dialog.ui = clientFitcht.Ui_Dialog()
			dialog.ui.setupUi(dialog, serverName)
			dialog.setAttribute(QtCore.Qt.WA_DeleteOnClose)
			dialog.exec_()

# Entry point... it's where everything starts
if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	window = MainEntryPoint()
	window.show()
	sys.exit(app.exec_())