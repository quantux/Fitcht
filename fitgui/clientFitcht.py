#!/usr/bin/python
#-*-coding: utf-8 -*-

import sys
import socket
import urllib2
import select
import thread
import time
import os
import readline
import ast
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

	# This method starts UI Elements and handles all User Interface stuff
	def setupUi(self, Dialog, serverName):
		self.serverName = serverName
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
		self.pushButton.setGeometry(QtCore.QRect(26, 80, 121, 41))
		self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
		self.pushButton.setStyleSheet(_fromUtf8("border-width: 0px; border-style: solid;\n"
"background-color: rgb(200, 200, 200);\n"
"outline: none;"))
		icon1 = QtGui.QIcon()
		icon1.addPixmap(QtGui.QPixmap(_fromUtf8("resources/new10.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.pushButton.setIcon(icon1)
		self.pushButton.setObjectName(_fromUtf8("pushButton"))
		self.toolButton = QtGui.QToolButton(Dialog)
		self.toolButton.setGeometry(QtCore.QRect(550, 10, 31, 25))
		self.toolButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
		self.toolButton.setToolTip(_fromUtf8(""))
		self.toolButton.setStatusTip(_fromUtf8(""))
		self.toolButton.setStyleSheet(_fromUtf8("border-width: 0px; border-style: solid;\n"
"background-color: rgb(57, 51, 51);\n"
""))
		icon2 = QtGui.QIcon()
		icon2.addPixmap(QtGui.QPixmap(_fromUtf8("resources/settings-32.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.toolButton.setIcon(icon2)
		self.toolButton.setObjectName(_fromUtf8("toolButton"))
		self.listWidget = QtGui.QListWidget(Dialog)
		self.listWidget.setGeometry(QtCore.QRect(200, 60, 401, 411))
		self.listWidget.setObjectName(_fromUtf8("listWidget"))
		self.pushButton_2 = QtGui.QPushButton(Dialog)
		self.pushButton_2.clicked.connect(self.exitProgram)
		self.pushButton_2.setGeometry(QtCore.QRect(20, 430, 121, 41))
		self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
		self.pushButton_2.setStyleSheet(_fromUtf8("border-width: 0px; border-style: solid;\n"
"background-color: rgb(200, 200, 200);\n"
"outline: none;"))
		icon3 = QtGui.QIcon()
		icon3.addPixmap(QtGui.QPixmap(_fromUtf8("resources/exit.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.pushButton_2.setIcon(icon3)
		self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
		self.pushButton_3 = QtGui.QPushButton(Dialog)
		self.pushButton_3.setGeometry(QtCore.QRect(20, 370, 131, 41))
		self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
		self.pushButton_3.setStyleSheet(_fromUtf8("border-width: 0px; border-style: solid;\n"
"background-color: rgb(200, 200, 200);\n"
"outline: none;"))
		icon4 = QtGui.QIcon()
		icon4.addPixmap(QtGui.QPixmap(_fromUtf8("resources/report-48.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.pushButton_3.setIcon(icon4)
		self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))

		self.retranslateUi(Dialog)
		QtCore.QMetaObject.connectSlotsByName(Dialog)
		self.startClient()

	# Function to list files on the Client
	def startClient(self):
		self.port = 10647
		#Lista de arquivos para o cliente
		CLIENT_FILE_LIST = []

		#Inicia todo o processo para conectar na sala
		self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.client_socket.settimeout(2)
		print "Entrando em modo cliente."
		print "Sala IP:"
		#host = raw_input(">")
				
		try:
			self.client_socket.connect((self.serverName, self.port))
		except:
			print "Impossivel conectar a essa sala, tenha certeza que o IP esta correto"
			return True

		print "Conectado com o servidor! Digite /help para ajuda."

		# Rotina para instanciamento do Thread client
		try:
			self.clientListen_Qthread = clientListen_Qthread()
			self.connect(self.clientListen_Qthread, QtCore.SIGNAL("update(QString)"), self.clientListen_thread)
			self.clientListen_Qthread.start()
		except:
			print('Não foi possível iniciar a thread do cliente.')

		return True

	# Thread para ouvir o socket do cliente (?)
	def clientListen_thread(self):
		socket_list = [sys.stdin, self.client_socket]
		print 'está rodando a thread'
		
		read_sockets, write_sockets, error_sockets = select.select(socket_list, [], [])
		for sock in read_sockets:
			if sock == self.client_socket:
				data = sock.recv(4096)
				if not data:
					print '\nDesconectado do servidor'
					sys.exit()
				else:
					self.dataList = ast.literal_eval(data)
					for itemIndex, fileName in self.dataList:
						fileNameWithoutDirectory = os.path.basename(str(fileName))
						fileExtension = os.path.splitext(fileNameWithoutDirectory)[1][1:]
						print fileNameWithoutDirectory

						print fileExtension

						item = QtGui.QListWidgetItem()
						icon8 = QtGui.QIcon()
						if not os.path.isfile('resources/fileExtensionIcons/%s-icon.png' % str(fileExtension)):
							fileExtension = 'undefined'
						icon8.addPixmap(QtGui.QPixmap(_fromUtf8("resources/fileExtensionIcons/%s-icon.png" % str(fileExtension))), QtGui.QIcon.Normal, QtGui.QIcon.Off)
						item.setIcon(icon8)
						item.setText(_translate("Dialog", ("%s" % fileNameWithoutDirectory), None))

						self.listWidget.addItem(item)
					#sys.stdout.write(data + "\n")
			else:
				#msg = sys.stdin.readline()
				#cl_socket.send(msg)
				#prompt()
				continue

		time.sleep(2)

	# Method to Close the Program
	def exitProgram(self):
		self.close()
		sys.exit()

	# This method rename the UI elements such as buttons, Dialog Title, etc.
	def retranslateUi(self, Dialog):
		Dialog.setWindowTitle(_translate("Dialog", "Fitcht", None))
		self.pushButton.setText(_translate("Dialog", "Download File", None))
		self.toolButton.setText(_translate("Dialog", "...", None))
		self.pushButton_2.setText(_translate("Dialog", "Sign Out", None))
		self.pushButton_3.setText(_translate("Dialog", "Report Server", None))

from PyQt4 import QtDeclarative

# This is the Secure QThread Class
class clientListen_Qthread(QtCore.QThread):
	def __init__(self):
		QtCore.QThread.__init__(self)
		
	def run(self):
		for i in range(6):
			time.sleep(0.3) # artificial time delay
			self.emit( QtCore.SIGNAL('update(QString)'), "from work thread " + str(i) )
			return