"""
Question 5: Given a list of numbers, return True if first and last number of a list is same

"""
listItem = [1.3,23,42,1.3,2,43,1.3,3,1.3]
totalItem = int(len(listItem))

if listItem[0] == listItem[totalItem-1]:
	print("List First and Last items are Ture and the items are: ", listItem[0] and listItem[totalItem-1])
