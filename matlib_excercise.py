"""
Create a program to help the user type faster. Give him a word and ask him to write it five times. Check how many seconds it look him to type the word at
each round.
 
 In the end of the program user many mistake were made and show a chart with the typing speed evolution during the 5 seconds.
"""
__author__= "Akhilesh Gairola"
import time as t
import matplotlib.pyplot as plt

times = []
mistake = 0 
#value1 = input("Please enter some text to write first time: ")

#value2 = input("Please enter some text to write second time: ")

#value3 = input("Please enter some text to write third time: ")

#value4 = input("Please enter some text to write fourth time: ")

#value5 = input("Please enter some text to write fifth time: ")

print("Enter one faster as you can five in a row.This program evaluate your speed to typing")
input("Press enter to continue ")
print(len(times))
while len(times) < 5:
	start = t.time()
	word = input("Type the word: ")
	end = t.time()
	time_elapsed = end - start
	
	times.append(time_elapsed)
	
	
	if(word.lower() != "one"):
		mistake += 1

print("you made " + str(mistake) + "mistakes.")
print("Now let's see your evulations")
t.sleep(2)

x = [1,2,3,4,5]
y = times
plt.plot(x,y)
legend = ["1","2","3","4","5"]
plt.xticks(x,legend)
plt.ylabel("Time in seconds ")
plt.xlabel("Attempts")
plt.title("your typing evolution")
plt.show()