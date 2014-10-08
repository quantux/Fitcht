import sys
from PyQt4 import QtGui, QtCore
from entryPoint import Ui_dialog
import fitcht

class MainEntryPoint(QtGui.QMainWindow, Ui_dialog):
	def __init__(self):
		QtGui.QMainWindow.__init__(self)
		self.setupUi(self)

		self.pushButton.clicked.connect(self.startServer)
		self.pushButton_2.clicked.connect(self.connectServer)

	def startServer(self):
		serverName, status = QtGui.QInputDialog.getText(self, 'Server Name', 'Type your server name:')
		if status:
			self.close()
			dialog = QtGui.QDialog()
			dialog.ui = fitcht.Ui_Dialog()
			dialog.ui.setupUi(dialog, serverName)
			dialog.setAttribute(QtCore.Qt.WA_DeleteOnClose)
			dialog.exec_()

	def connectServer(self):
		print 'something'

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MainEntryPoint()
    window.show()
    sys.exit(app.exec_())