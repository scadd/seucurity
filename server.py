import socket
import os
import sys
import signal
from utils import *

class Server:

	def __init__(self):

		# default configurations
		self.port = 3000
		self.adminPassword = 'admin'

		# parse input arguments
		self.checkArguments()

		# exit bindings
		signal.signal(signal.SIGINT, self.exit_clean)
		signal.signal(signal.SIGTERM, self.exit_clean)

		self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.listen2network()

	def checkArguments(self):
		argcLen = len(sys.argv)

		if argcLen == 2: # only port specified
			self.port = int(sys.argv[1])
		elif argcLen == 3: # port and admin password specified
			self.port = int(sys.argv[1])

			self.adminPassword = sys.argv[2]
		else:
			raise ret255

		# TODO: validations
		debug('Validating inputs')
		validatePortNumber(self.port)

		debug('SeuCurity Server running on port:' + str(self.port))

	def exit_clean(self, signum, frame):
		self.s.shutdown(socket.SHUT_RDWR)
		self.s.close()
		raise ret0

	def listen2network(self):
		self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		self.s.bind(('127.0.0.1', self.port))
		self.s.listen(1)

		while 1:
			self.fieldsDict = dict()

			c = self.s.accept()
			self.cli_conn, cli_addr = c

			try:
				receiveMessage(self.cli_conn)

			except ret255:
				sys.stdout.flush()
			except ret63:
				print 'protocol_error'
				sys.stdout.flush()
			except Exception, e:
				debug('Exception' + str(e))
			finally:
				self.cli_conn.shutdown(socket.SHUT_RDWR)
				self.cli_conn.close()


	# def sendReply(self):

try:
	seuCurityServer=Server()
except ret255, e:
	debug('ret255: ' + str(e))
	sys.exit(-1)
except ret0:
	sys.exit(0)
except Exception, e:
	debug('Exception: ' + str(e))
	sys.exit(-1)