class A:

	def methodOveriding(self):
		print("I called from Class A")



class B(A):

	def methodOveriding(self):
		print("I called from Class B")




a = A()
a.methodOveriding()