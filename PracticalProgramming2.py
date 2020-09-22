"""
Programm to Print Reactangle.
"""

for i in range(1,11):
	for j in range(1,11):
		if (i == 1 or i == 10):
			print("*", end='')
		else:
			if(j==1 or j==10):
				print("*", end='')
			else:
				print(" ", end = '')
	print()
