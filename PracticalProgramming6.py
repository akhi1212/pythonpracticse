"""
Practical Programming - 6 : Write program to check Number is Prime or Not

"""

x = int(input("Enter your number and check your number is Prime or not: "))
z=0
for i in range (2,x):
    if(x%i==0):
        print("Its not a Prime number")
        z=1
        break
    i=i+1
if(z==0):
    print("This is Prime number")
