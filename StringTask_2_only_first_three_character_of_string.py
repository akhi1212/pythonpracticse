## Compare only first three character of string
def comparisonFirstThreeChars(s1_inp,s2_inp):
	a = len(s1_inp)
	b = len(s2_inp)
	c_newa = s1_inp[0:3]
	print(c_newa)
	d_newb = s2_inp[0:3]
	print(d_newb)
	if c_newa == d_newb:
		print("first three chars matched enjoy your are become code in coding")
	else:
		print("Chage your logic First three char is not matched")

input3 = input("PLease enter your string more then 3 ")
input4 = input("PLease enter your second string more then 3 ")
comparisonFirstThreeChars(input3,input4)