"""
Alternamte method to revrse string 
"""

str1 = "MagicMoment"

print(str1[::-1])
b=""
for i in range(int(len(str1)-1),-1,-1):
	b += str1[i]

print(b)
