"""
Exercise Question 2: Given 2 strings, s1 and s2, create a new string by appending s2 in the middle of s1

"""

s1 = "Ault"
s2 = "Kelly"


a = int(len(s1)/2)
middleThree = s1[:a:]+ s2 +s1[a:]
print("After appending new string in middle", middleThree)
