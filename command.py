from users import *
from variables import *
from utils import *


class Command:

	def __init__(self, type, variableName=None, variableValue=None, userInstance=None):
		self.type = type
		self.variableName = variableName
		self.variableValue = variableValue
		self.newUserInstance = userInstance

	def __iter__(self):
		return self

	def returnVariable(self, variablesList):
		debug("returning variable - BEGIN")
		print variablesList
		for variable in variablesList:
			if variable.name == self.variableName:
				debug("returning variable - FOUND")
				return '{"status":"RETURNING","output":' + variable.value + '}\n'

		debug("returning variable - NOT FOUND")

	def setVariable(self, variablesList):
		debug("setting variable - BEGIN")
		for variable in variablesList:
			if variable.name == self.variableName:
				# TODO: check permission
				variable.value = self.variableValue
				debug("setting variable - FOUND")
				return '{"status":"SET"}\n'

		variablesList.append(Variable(self.variableName, self.variableValue))
		debug("setting variable - NOT FOUND")
		return '{"status":"SET"}\n'

	def createPrincipal(self, usersList):
		debug("creating principal")
		debug(usersList)
		userExists = False

		for user in usersList:
			debug(user.name)
			if user.name == self.newUserInstance.name:
				userExists = True

		if userExists:
			debug("creating principal - ALREADY EXISTS")
			return '{"status":"FAILED"}\n'

		usersList.append(self.newUserInstance)
		debug("creating principal - CREATED")
		return '{"status":"CREATE_PRINCIPAL"}\n'

	def execute(self, variablesList=None, usersList=None):
		if self.type == 'return':
			return self.returnVariable(variablesList)
		elif self.type == 'create principal':
			return self.createPrincipal(usersList)
		elif self.type == 'set':
			return self.setVariable(variablesList)


