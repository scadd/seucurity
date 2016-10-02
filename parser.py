import re
from utils import *
from command import *


class Parser:

	def __init__(self):
		self.autenticationRE = 'as principal (.+) password "(.+)" do'
		self.wrapperRE = 'as principal .*\*\*\*'
		self.returnCommandRE = '\s*return\s+(.*)'
		self.createPrincipalCommandRE = '\s*create\s+principal\s+([A-Za-z][A-Za-z0-9_]*)\s+("[A-Za-z0-9_ ,;\.?!-]*")'
		self.setCommandRE = '\s*set\s+([A-Za-z][A-Za-z0-9_]*)\s*=\s*([A-Za-z][A-Za-z0-9_]*|[A-Za-z][A-Za-z0-9_]*\.[A-Za-z][A-Za-z0-9_]*|"[A-Za-z0-9_ ,;\.?!-]*")'

	def extractUserCredentials(self, input):
		search = re.search(self.autenticationRE, input)
		user = search.group(1)
		password = search.group(2)
		return user, password

	def extractCommands(self, input):

		search = re.search(self.returnCommandRE, input)

		if search is not None:
			variableName = search.group(1)
			return Command('return', variableName=variableName)

		search = re.search(self.createPrincipalCommandRE, input)

		if search is not None:
			userName = search.group(1)
			password = search.group(2)
			return Command('create principal', userInstance=User(userName, password))

		search = re.search(self.setCommandRE, input)

		if search is not None:
			variableName = search.group(1)
			variableValue = search.group(2)
			print variableName, variableValue
			return Command('set', variableName=variableName, variableValue=variableValue)

		return None

	def validateInput(self, input):
		search = re.search(self.wrapperRE, input, re.DOTALL)

		if search is not None:
			return True
		else:
			return False