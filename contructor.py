class Exp:
	def __init__(self,test):
		print("testing single constructor")
	def __init__(self, model, color):
		self.color = color
		self.model = model
		print("testing second constructor")
	

t = Exp("test","cgek")
p = Exp("akhilesh")
	