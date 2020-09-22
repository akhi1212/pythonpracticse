"""
Programm to find factorial of a number.
"""

m = int(input("PLease enter number to check factorial: "))

if m < 0:
	print("Sorry factorial does not exist for negative numbers")
elif m == 0 or m == 1:
	print("The factorial of 0 is 1")
else:
	fact = 1
	for i in range(1, m+1):
		fact = fact *i
		print("The factorial of", m, "is: ", fact)