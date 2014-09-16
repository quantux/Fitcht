#!/usr/bin/python
#-*-coding: utf-8 -*-
import sys
import socket

#Função que vem junto ao inicio do programa, todo codigo que precisa ser inciado vem aqui!
def setup():
	#Sobre versão e outros dados.
	print "Welcome to Fitcht!"

	print "Type /help to get help."

#Captura uma linha de comando para o nuke
def get():
	command = raw_input(">")
	return command

#Esse função vai tratar toda a entrada de comandos no programa
def nuke(command):
	if  command != "/start" and \
		command != "/help" and \
		command != "/join" and \
		command != "/exit":
		print "Comando inválido! Digite /help para ajuda."

	else:
		if command == "/exit":
				return -1

		return 1;	

#Função main do programa
if __name__ == '__main__':
	
	#Iniciando
	setup()

	#Loop do programa ate que tenha o /exit
	while(1):
		command = get()

		if nuke(command) == -1:
			sys.exit()

		if nuke(command) == 1:
			continue