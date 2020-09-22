print("This programm purpose to understand the static method with out class")

class A: 
	@staticmethod
	def isOpen(day):
		if day == "Sunday":
			print("Today is holiday")
		else : 
			print("Today is the working day")

"""
TypeError: 'staticmethod' object is not callable 
when you create programm with out class and use static method
"""

u  = input("Check today status: ")
a = A()
A.isOpen(u)
a.isOpen("MOnday")