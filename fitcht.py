#!/usr/bin/python
#-*-coding: utf-8 -*-
import sys
import socket
import urllib2
import select
import thread
import time
import os

#Globais
port = 0

#Função que vem junto ao inicio do programa, todo codigo que precisa ser iniciado vem aqui!
def setup():
	#Sobre versão e outros dados.
	print "Welcome to Fitcht!"

	print "Type /help to get help."
	#Seta a porta
	global port
	port = 10647

#Captura uma linha de comando para o nuke
def get():
	command = raw_input(">")
	return command

#Pega o ip do usuario para abrir servidor e outras aplicações
def myip():
	myip = urllib2.urlopen("http://myip.dnsdynamic.org/").read()
	return myip

def mylocal():
	local = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	local.connect(('google.com', 0))
	return local.getsockname()[0]

#Função para tratar a entrada de arquivos
def open_files(path, listt):

	FILES_LIST = listt

	try:
		f = open(str(path), "r")
		name = namebypath(path)
		FILES_LIST.append(name)
		f.close()

	except:
		print "Não foi possivel encontrar o arquivo."

#Função para pegar o nome do arquivo pelo path..
def namebypath(path):
	try:
		name = os.path.basename(str(path))
		return name
	except :
		print "Não foi possivel encontrar o arquivo! Tenha certeza que o caminho esta correto."
	

#Função para printar o prompt na tela
def prompt():
	sys.stdout.write(">")
	sys.stdout.flush()

#Funçao para enviar request para o servidor e armazenar os dados no client-side
def request(sock, listt):
	pass
	
# Thread para ouvir o socket do servidor
def serverListen_thread(sock, listt, users):
	while True:

		BUFFER = 4096
		CONNECTION_LIST = listt
		USERS_LIST = users
		host_socket = sock

		read_sockets, write_sockets, error_sockets = select.select(CONNECTION_LIST, [], [])

		for sock in read_sockets:
			if sock == host_socket:
				sockfd, addr = host_socket.accept()
				CONNECTION_LIST.append(sockfd)
				print "Cliente (%s, %s) conectado" %addr
				usr = "(%s, %s)" %addr
				USERS_LIST.append(usr)
				prompt()
			else:
				try:
					data = sock.recv(BUFFER)
					if data:
						print data
				except:
					print "Cliente (%s, %s) esta offline" %addr
					sock.close()
					CONNECTION_LIST.remove(sock)
					continue


		time.sleep(2)

#Essa função vai tratar toda a entrada de comandos no programa
def nuke(command):
	if  command != "/start" and \
		command != "/help" and \
		command != "/join" and \
		command != "/exit":
		print "Comando inválido! Digite /help para ajuda."

	else:
		if command == "/exit":
				return False

		if command == "/start":

			#Listas 
			USERS_LIST = []
			CONNECTION_LIST = []
			FILES_LIST = []

			host_ip = str(mylocal())

			#Inicia todo processo para formação de uma sala aqui
			host_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			host_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
			host_socket.bind((host_ip, port))
			host_socket.listen(10)

			CONNECTION_LIST.append(host_socket)

			#Incia a thread para verificações de socket
			try:
				thread.start_new_thread(serverListen_thread, (host_socket, CONNECTION_LIST, USERS_LIST))
			except:
				print('Não foi possível receber os dados do servidor')

			print "Sala de arquivos iniciada em: " + host_ip + ":" + str(port) + "."
			print "Digite /add para adicionar arquivos ou /stop para fechar a sala."

			#Loop do /start
			while (True):
				next = get()
				
				if  next != "/add" and \
					next != "/stop" and \
					next != "/list" and \
					next != "/users":
					print "Comando inválido! Digite /help para ajuda."

				if next == "/stop":
					host_socket.close()
					CONNECTION_LIST = []
					FILES_LIST = []
					print "A sala foi fechada, voltando para o programa..."
					break
				
				if next == "/add":
						print "Iniciando adição de arquivos."
						print "Entre com o caminho do arquivo:"
						caminho = str(raw_input(">"))
						open_files(caminho, FILES_LIST)
						print "Feito."

				if next == "/list":
					print FILES_LIST

				if next == "/users":
					print USERS_LIST
						

			return True;

		if command == "/join":

			#Lista de arquivos para o cliente
			CLIENT_FILE_LIST = []

			#Inicia todo o processo para conectar na sala
			client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			client_socket.settimeout(2)
			print "Entrando em modo cliente."
			print "Sala IP:"
			host = raw_input(">")
			lista = ""
			try:
				client_socket.connect((host, port))
			except:
				print "Impossivel conectar a essa sala, tenha certeza que o IP esta correto"
				return True

			print "Conectado com o servidor! Digite /help para ajuda."

			request(client_socket, CLIENT_FILE_LIST)

			#Loop do /join
			while (True):
				next = get()
				
				if  next != "/all" and \
					next != "/quit" and \
					next != "/list":
					print "Comando inválido! Digite /help para ajuda."

				if next == "/quit":
					print "Saindo do modo cliente e desconectando do servidor..."
					client_socket.close()
					break

				if next == "/list":
					break
					
			return True

		if command == "/help":
			print('Bem vindo ao helper do Fitcht.\n')
			print('1. /start - Inicia uma instância de servidor para compartilhar arquivos.\n')
			print('2. /help  - Mostra este guia de Help\n')
			print('3. /join  - Conecta você a um servidor de compartilhamento de arquivos Fitcht\n')
			print('4. /exit  - Sai do Fitcht')
			return True


#Função main do programa
if __name__ == '__main__':
	
	#Iniciando
	setup()

	#Loop do programa ate que tenha o /exit
	while(1):
		command = get()

		if not nuke(command):
			sys.exit()
		else:
			continue