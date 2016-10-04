from users import *
from variables import *
from utils import *


class Command:

	def __init__(self, type, variableName=None, variableValue=None, userInstance=None, delegatedBy=None, right=None, delegatedTo=None):
		self.type = type
		self.variableName = variableName
		self.variableValue = variableValue
		self.newUserInstance = userInstance
		self.delegatedBy = delegatedBy
		self.right = right
		self.delegatedTo = delegatedTo

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

	def setVariable(self, variablesList, activePrincipal):
		debug("setting variable - BEGIN")
		# checking if variable exists
		for variable in variablesList:
			if variable.name == self.variableName:
				debug("setting variable - FOUND")
				debug(variable)
				debug(variable.name)
				debug(variable.value)
				debug(variable.permissions)

				# checking permissions
				for (rights, delegatedBy, delegatedTo) in variable.permissions:
					print rights, delegatedBy, delegatedTo
					if delegatedTo == activePrincipal and 'r' in rights:
						variable.value = self.variableValue
						debug("setting variable - FOUND - PERMITTED")
						return '{"status":"SET"}\n'

				debug("setting variable - FOUND - NOT PERMITTED")
				return '{"status":"DENIED"}\n'

		variablesList.append(Variable(self.variableName, self.variableValue, ('rwad', activePrincipal, activePrincipal)))
		debug("setting variable - NOT FOUND - CREATED")
		return '{"status":"SET"}\n'

	def setDelegation(self, variablesList, activePrincipal):
		debug("setting delegation - BEGIN")
		# checking if variable exists
		for variable in variablesList:
			if variable.name == self.variableName:
				debug("setting delegation - FOUND")
				debug(variable)
				debug(variable.name)
				debug(variable.value)
				debug(variable.permissions)

				# checking permissions
				for (rights, delegatedBy, delegatedTo) in variable.permissions:
					print rights, delegatedBy, delegatedTo
					if delegatedTo == activePrincipal and 'd' in rights:
						variable.permissions.append((self.right[0], activePrincipal, self.delegatedTo))
						debug("setting delegation - FOUND - PERMITTED")
						return '{"status":"SET"}\n'

				debug("setting delegation - FOUND - NOT PERMITTED")
				return '{"status":"DENIED"}\n'

		return '{"status":"FAILED"}\n'

	def createPrincipal(self, usersList):
		debug("creating principal")
		debug(usersList)

		for user in usersList:
			debug(user.name)
			if user.name == self.newUserInstance.name:
				debug("creating principal - ALREADY EXISTS")
				return '{"status":"FAILED"}\n'

		usersList.append(self.newUserInstance)
		debug("creating principal - CREATED")
		return '{"status":"CREATE_PRINCIPAL"}\n'

	def execute(self, variablesList=None, usersList=None, activePrincipal=None):
		if self.type == 'return':
			return self.returnVariable(variablesList)
		elif self.type == 'create principal':
			return self.createPrincipal(usersList)
		elif self.type == 'set':
			return self.setVariable(variablesList, activePrincipal)
		elif self.type == 'set delegation':
			return self.setDelegation(variablesList, activePrincipal)


