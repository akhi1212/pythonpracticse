"""
find the duplicate characters in a string

"""

# s = "Great responsibility"

# print("Duplicate characters in a given string: ")  
# #Counts each character present in the string  
# for i in range(0, len(s)):  
#     count = 1  
#     for j in range(i+1, len(s)):  
#         if(s[i] == s[j] and s[i] != ' '):  
#             count = count + 1  
#             #Set string[j] to 0 to avoid printing visited character  
#             s = s[:j] + '0' + s[j+1:]  
   
#     #A character is considered as duplicate if count is greater than 1  
#     if(count > 1 and s[i] != '0'):  
#         print(s[i])  

## initializing string
string = "tutorialspoint"
## initializing a list to append all the duplicate characters
duplicates = []
for char in string:
	print(char)
	if string.count(char) > 1:

   ## checking whether the character have a duplicate or not
   ## str.count(char) returns the frequency of a char in the str


## appending to the list if it's already not present
		if char not in duplicates:
			duplicates.append(char)

print(*duplicates)