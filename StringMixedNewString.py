"""
Exercise Question 6: Given two strings, s1 and s2, create a mixed String

Note: create a third-string made of the first char of s1 then the last char of s2, 
Next, the second char of s1 and second last char of s2, and so on. 
Any leftover chars go at the end of the result.

"""

s1 = "Abc"
s2 = "Xyz"

first_char = s1[0:1] + s2[len(s2) - 1]
last_char = s1[0:1] + s2[int(len(s2))-1: int(len(s2))-1 +1]