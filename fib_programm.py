def getNthFib(n):
    # Write your code here.
    if n==2:
		return n
	elif n ==1:
		return n
	else:
		return getNthFib(n-1) + getNthFib(n-2)