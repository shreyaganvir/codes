class Calculator():

	def __init__(self):
		pass


	def add(self, a, b):
		return a + b

	def subtract(self, a, b):
		if a > b:
			return a - b
		else:
			return b - a

	def multiply(self, a, b):
		return a * b

	def divide(self, a, b):
		if b == 0:
			raise ZeroDivisionError("Division by zero is not allowed")
		return a / b
