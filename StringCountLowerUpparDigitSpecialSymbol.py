"""
Exercise Question 5: Count all lower case, upper case, digits, and special symbols from a given string
"""
inputString = "P@#yn26at^&i5ve"

charCount = 0
digitCount = 0
symbolCount = 0
for char in inputString:
	if char.islower() or char.isupper():
		charCount+=1
	elif char.isnumeric():
		digitCount+=1
	else:
		symbolCount+=1

print("Chars = ", charCount, "Digits = ", digitCount, "Symbol = ", symbolCount)
