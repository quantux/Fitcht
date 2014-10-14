#!/usr/bin/python
#-*-coding: utf-8 -*-
import sys, os
import socket
import urllib2
import select
import thread
import time
import readline
from PyQt4 import QtCore, QtGui

# Encoding and String formats stuff
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

# Class that holds all Fitcht.py Stuff
class Ui_Dialog(QtGui.QMainWindow):

	# This method starts UI Elements and handles all User Interface things
	def setupUi(self, Dialog, serverName):
		Dialog.setObjectName(_fromUtf8("Dialog"))
		Dialog.setWindowModality(QtCore.Qt.NonModal)
		Dialog.resize(615, 488)
		Dialog.setMinimumSize(QtCore.QSize(615, 488))
		Dialog.setMaximumSize(QtCore.QSize(615, 488))
		Dialog.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))

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
		self.center()
		self.startServer()

	# Callback Function to Add Files Button
	def openFileButtonCallback(self):

		fileName = QtGui.QFileDialog.getOpenFileName(self, 'Open File', '.')
		if fileName != '':
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
			self.FILES_LIST.append([str(item), str(fileName)])
			print self.FILES_LIST

	# Callback Method to handle Delete click Event
	def deleteCallBackFunction(self):
		for itemIndex, itemDirectory in self.FILES_LIST:
			if self.listWidget.currentItem() == itemIndex:
				self.FILES_LIST.remove([itemIndex, itemDirectory])
		self.listWidget.takeItem(self.listWidget.currentRow())
		print self.FILES_LIST

	# Callback Method to handle Disconnect click Event
	def DisconnectButtonCallback(self):
		self.close()
		sys.exit()

	# This method Center the application in startup
	def center(self):
		frameGm = self.frameGeometry()
		centerPoint = QtGui.QDesktopWidget().availableGeometry().center()
		frameGm.moveCenter(centerPoint)
		self.move(frameGm.topLeft())

	# This is the first method Called AFTER setupUI() and handles server Routines
	def startServer(self):
		#Start Server Sockets Routine

		#Port
		self.port = 10647

		#Listas 
		self.USERS_LIST = []
		self.CONNECTION_LIST = []
		self.FILES_LIST = []

		host_ip = str(self.mylocal())

		#Inicia todo processo para formação de uma sala aqui
		host_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		host_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		host_socket.bind((host_ip, self.port))
		host_socket.listen(10)

		self.CONNECTION_LIST.append(host_socket)

		#Incia a thread para verificações de socket
		try:
			thread.start_new_thread(self.serverListen_thread, (host_socket, self.CONNECTION_LIST, self.USERS_LIST, self.FILES_LIST))
		except:
			print('Não foi possível receber os dados do servidor')

		print "Sala de arquivos iniciada em: " + host_ip + ":" + str(self.port) + "."

	# Gets local IP
	def mylocal(self):
		local = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		local.connect(('google.com', 0))
		return local.getsockname()[0]

	# Thread para ouvir o socket do servidor
	def serverListen_thread(self, sock, listt, users, files):
		while True:

			BUFFER = 4096
			CONNECTION_LIST = listt
			USERS_LIST = users
			host_socket = sock
			FILES_LIST = files

			read_sockets, write_sockets, error_sockets = select.select(CONNECTION_LIST, [], [])

			for sock in read_sockets:
				if sock == host_socket:
					sockfd, addr = host_socket.accept()
					self.CONNECTION_LIST.append(sockfd)
					print "Cliente (%s, %s) conectado" %addr
					self.awnser(host_socket, sock, str(FILES_LIST), CONNECTION_LIST)
					usr = "(%s, %s)" %addr
					USERS_LIST.append(usr)
				else:
					try:
						data = sock.recv(BUFFER)
						if data:
							print data
					except:
						print "Cliente (%s, %s) esta offline" %addr
						sock.close()
						self.CONNECTION_LIST.remove(sock)
						USERS_LIST.remove(usr)
						continue

			time.sleep(2)


	#Função para o servidor responder a todos os clientes
	def awnser(self, host, sock, message, lista):
		CONNECTION_LIST = lista
		for socket in CONNECTION_LIST:
			if socket != host and socket != sock:
				try:
					socket.send(message)
				except:
					socket.close()
					CONNECTION_LIST.remove(socket)

	# This method rename the UI elements such as buttons, Dialog Title, etc.
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

