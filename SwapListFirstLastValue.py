"""
Frequently Asked Python Program 8: How To Swap First & Last Elements of a List
"""

mylist = [204,4224,"This is Akhilesh",29,00,90]

print("This is original list:", mylist)
mylist[0],mylist[-1] = mylist[-1],mylist[0]

print("Replacing list is not displaying like:", mylist)