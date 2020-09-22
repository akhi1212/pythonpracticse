"""
Exercise Question 4: Arrange string characters such that lowercase letters should come first
"""


str1 = "PyNaTive"
lower = []
upper = []
for char in str1:
    if char.islower():
        lower.append(char)
    else:
        upper.append(char)
sorted_string = ''.join(lower + upper)
print("arranging characters giving precedence to lowercase letters:")
print(sorted_string)