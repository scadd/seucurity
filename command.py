
class Command:

	def __init__(self, type, variableName):
		self.type = type
		self.variableName = variableName

	def __iter__(self):
		return self

	def returnVariable(self, variablesList):
		for variable in variablesList:
			if variable.name == self.variableName:
				return '{"status":"RETURNING","output":"' + variable.value + '"}\n'

	def execute(self, variablesList):
		if self.type == 'return':
			return self.returnVariable(variablesList)

