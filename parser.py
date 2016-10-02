import re
from utils import *
from command import *


class Parser:

	def __init__(self):
		self.autenticationRE = 'as principal (.+) password "(.+)" do'
		self.wrapperRE = 'as principal .*\*\*\*'
		self.returnCommandRE = '\s*return\s+(.*)'

	def extractUserCredentials(self, input):
		search = re.search(self.autenticationRE, input)
		user = search.group(1)
		password = search.group(2)
		return user, password

	def extractCommands(self, input):

		search = re.search(self.returnCommandRE, input)

		if search is not None:
			variableName = search.group(1)
			return Command('return', variableName)

		return None

	def validateInput(self, input):
		search = re.search(self.wrapperRE, input, re.DOTALL)

		if search is not None:
			return True
		else:
			return False