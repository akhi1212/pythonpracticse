import numbers



lst = ["Akhilesh", 1 ,3,"Rahul", "OOPS", "Tesf",2]

# temp = list(map(lambda i: isinstance(i, int), lst)) 
# print(temp)


mynewlist = [s for s in lst if str(s).isdigit()]
print(mynewlist)

# y = [x for x in lst if isinstance(x, numbers.Number)]
# print(y)


