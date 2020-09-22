## python program to reverse the string

inp = input("Please enter your string \n")
leng = len(inp)
b= ""
for i in range((leng-1),-1,-1):
	b =  b+inp[i]
	print(inp[i])

print("\n")
print("Your reverse String is :"+b)
#print(inp[i])

if(inp==b):
	print("You have entered Palendrome String")

else:
	print("String is not Palendrome String")