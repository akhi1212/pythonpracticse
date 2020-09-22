"""
Programm to print table where only display  selective numbers.
"""

n = int(input("Enter your number: "))
for i in range(1,11):
	num = i * n
	if(num%3!=0 and num%5!=0 and num%7!=0):
		print(num)