s = "This is my name Akhilesh"

### I am removing capital letter from the given list

#s1 = [s for i in s if i == s.isupper()]
#s2 = .split(s1)
#print(s1)

#import re

#print(re.sub(r'[A-Z]', '', s))

a= [''.join([j for j in i if not j.isupper()]) for i in s]
print(''.join(a))
