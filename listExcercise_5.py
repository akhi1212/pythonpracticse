"""
Write one line of code to get a list of names that start with character "j"
"""

list1 = ['Tack','Rack','Mack','Jack','Adam','John','Sunil']

names = [names for names in list1 if names[0] == "J"]
print(names)