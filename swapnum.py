x = input("Enter First  number you want to swap: ")
y = input("Enter Second number you want to swap: ")

  
print ("Before swapping: ") 
print("Value of x : ", str(x), " and y : ", str(y)) 
  
# Swap code 
x = int(x) + int(y) # x = 15.7, y = 10.3 
y = int(x) - int(y) # x = 15.7, y = 5.4 
x = int(x) - int(y) # x = 10.3, y = 5.4 
  
print ("After swapping: ") 
print("Value of x : ", str(x), " and y : ", str(y))

## ALERTNATE METHOD 
## X,Y = Y,X