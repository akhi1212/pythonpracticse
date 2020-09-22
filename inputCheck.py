"""
Take input from use and check it is int or str
"""

i = input("Please enter some thing here: ")


if i.isdigit():
    print("User input is Number ")
else:
    print("User input is string ")
