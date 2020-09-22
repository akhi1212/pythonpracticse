"""
Exercise Question 1: Given a string of odd length greater 7, 
return a string made of the middle three chars of a given String
"""

str1 = "JhonDipPeta"
str2 = "JaSonAy"

a = int(len(str1)/2)

middleThree = str1[a-1:a+2]
print("Middle three chars are", middleThree)