import string
import random
import socket
import re
import sys
from decimal import *


class ret255(Exception):
	pass


class ret63(Exception):
	pass


class ret0(Exception):
	pass


def sendMessage(conn, msg):
	conn.send(msg)


def receiveMessage(conn):
	messageReceived = conn.recv(609)
	debug(messageReceived)


def debug(s):
	#change to 'pass' to deliver.
	print(s)

	# with open('./debug.txt', 'a') as debugFile:
	#     debugFile.write(s)
	#     debugFile.write('\n')
	pass


def validateNumbers(number):
	if not re.match('^(0|[1-9][0-9]*)$', number):
		raise ret255


def validatePortNumber(port):
	if port < 1024 or port > 65535:
		raise ret255
