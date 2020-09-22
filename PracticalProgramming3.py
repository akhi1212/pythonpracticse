"""
Programm to print table where only display  selective numbers.
"""
n = int(input("Enter your number: "))
for i in range(1,11):
	i = i * n
	if(i%3 ==0 or i%5 ==0 or i%7 == 0):
		continue
	else:		
		print(i)


