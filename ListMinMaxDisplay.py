"""
17. Frequently Asked Python Program 6: Find Maximum & Minimum Elements in an Array
"""
arr = [14,56,63,24]
max=arr[0]
n =int(len(arr))
print("legth of the list is:", str(n))
for i in range(1,n):
	if arr[i] > max:
		max= arr[i]
	

print(max)

arr1 = [14,56,63,24,248,0,56]
min=arr1[0]
n =int(len(arr1))
for i in range(1,n):
	if arr1[i] < min:
		min= arr1[i]


print(min)