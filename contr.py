class A:
	def __init__(self):
		print("testing single constructor")
	def __init__(self, model, color):
		self.color = color
		self.model = model
		print(f"Your mode is {model}  and color is {color}")
	


a = A("CherryRe","Hundai")