"""
Take 2 input from user and interchange variable value

"""

x = input("Please enter your first value: ")
y = input("Please enter your second value: ")
print("Your swap value is : ")
x = int(x) + int(y) 
y = int(x) - int(y) 
x = int(x) - int(y) 
print("YOur change value is:  ",str(x) ,str(y))