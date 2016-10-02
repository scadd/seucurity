
class Variable:

	def __init__(self, name, value):
		self.name = name
		self.value = value

	def __iter__(self):
		return self
