# Create a method that take two argument and compare last 10 chars of two strings 

# compare Two method 

def compareStringfirstmethod(s1,s2):
	print("Method to compare last 10 character of given string")
	last_s1 = len(s1)
	last_s2 = len(s2)
	a = s1[-10:]
	b = s2[-10:]
	print(len(s1))
	print(str(a))
	print(len(s2))
	if last_s1>10 and last_s2>10:
		print("This condition executes when you enter greater then 10 chars in the string")
		if a == b:
			print("This is updated string :",a ," secon string is: ", b)
		else:
			print("last 10 chars is not matched")
	else:
		print("Please change your input string")

def comparedStringSecondmethod(l,m,n):
	last_l = len(l)
	last_m = len(m)
	num = int(n)
	print("Second method to compare which is dynamic", num, "last char match: ")
	d = l[-num:]
	g = m[-num:]
	#if last_m > num and last_l<num:
	#	print("This condition executes when you comparison begin")
	if d == g:
		print("This is updated string :",d ," secon string is: ", g)
		print("The length of compared string is: ", len(d))
		print("The length of compared string is: ", len(g))
	else:
			print("your char not matched")
	#else:
	#	print("Please change your input string")


compareStringfirstmethod("1244","4567")
comparedStringSecondmethod("j","ahileshtgsgkj","1")




