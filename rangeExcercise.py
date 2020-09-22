"""
Question 2: Given a range of first 10 numbers, Iterate from start number to the end number and
 print the sum of the current number and previous number
"""
previous=0
for i in range(10):
	current = i
	sumNum = current + previous
	print("Current Number", current, "Previous Number",previous,"Sum: ",sumNum)
	previous = current
	continue


