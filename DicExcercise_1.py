"""
Create a dic and take input from user and return the meaning of the word from the dictionary. 
"""

dic = {
		"mutable" : "This is used for mutable object can be changed after it is created",
		"immutable" : "This is used for immutable  object can not be changed after it is created",
		"PythonicWay" : "Write small and do more",
		"StringValues" : "The sequence of character is knows as string"
	}
	
s  = input("Please enter the word to search the meaning of word you want to search: ")

try:
	print("The value whcih you asked is : ",dic[s])
	
except KeyError:
	print("You have enter wrong key please correct it and try again ",KeyError)