
class Variable:

	def __init__(self, name, value, permission):
		self.name = name
		self.value = value
		print permission
		self.permissions = []
		self.permissions.append(permission)
		print self.permissions

	def __iter__(self):
		return self
