"""
Create list it colud be anything number or string 

if it is number then check it is greater then 6 or not 
"""

lsit1 = [12,13444,41455,"Akhilesh", "MarkSon", "Richirich",24]


# for item in lsit1:

# 	if str(item).isnumeric() and item > 6:
# 		print(item)

list2 = [x for x in lsit1 if str(x).isdigit() and x >6]
print(list2) 