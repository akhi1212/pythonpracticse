"""
Question 3: Given a string, display only those characters which are present at an even index number.
"""

#For example str = "pynative" so you should display ‘p’, ‘n’, ‘t’, ‘v’.

Itemstr = "pynative"

for i in Itemstr:
	if Itemstr.index(i) % 2 == 0:
		print( "index[",Itemstr.index(i),"]", ", ", i)




"""
Out Come displaying is : ------------
###C:Users Akhilesh Desktop python-prac>StringTask_3.py
index[ 0 ] ,  p
index[ 2 ] ,  n
index[ 4 ] ,  t
index[ 6 ] ,  v
"""