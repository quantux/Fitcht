#!/usr/bin/python
#-*-coding: utf-8 -*-
import sys
import socket
import urllib2
import select

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

			host_ip = str(mylocal())

			#Inicia todo processo para formação de uma sala aqui
			host_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			host_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
			host_socket.bind((host_ip, port))
			host_socket.listen(10)

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
					print "A sala foi fechada, voltando para o programa..."
					break
				
				if next == "/add":
						print "Iniciando adição de arquivos."
						break




			return True;

		if command == "/join":
			#Inicia todo o processo para conectar na sala
			client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			client_socket.settimeout(2)
			print "Entrando em modo cliente."
			print "Sala IP:"
			host = raw_input(">")
			try:
				client_socket.connect((host, port))
			except:
				print "Impossivel conectar a essa sala, tenha certeza que o IP esta correto"
				return True

			print "Conectado com o servidor! Digite /help para ajuda."

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