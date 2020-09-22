"""
Creating a quizzing game. Make an HTTP request to the Open Trivia API at each round of the game to get a new question and present it to the user to answser.
At the end of  each round ask the user if he wants to play again. Keep playing forever until the user type "quit".

** don't forgot to tell if the answer is correct or not at each round and keep the user's once.
"""
__author__="Akhilesh Gairola"

import requests
import json
import pprint
import random
import html

url = "https://opentdb.com/api.php?amount=1"
engame = ""
while engame != "quit":
	r = requests.get(url)
	if(r.status_code !=200):
		engame = input("Sorry there is problem in reterving the question.Press enter to try again or type 'quit' to 'quit' the game:")
	else:
		ans_num = 1
		data = json.loads(r.text)
		#pprint.pprint(data)
		#input("Press enter to get a new question")
		que = data['results'][0]['question']
		answ = data['results'][0]['incorrect_answers']
		correct_answ = data['results'][0]['correct_answer']
		answ.append(correct_answ)
		random.shuffle(answ)
		
		print(html.unescape(que + "\n"))
		
		for answ in answ:
			print(str(ans_num)+" _ "+html.unescape(answ))
			ans_num +=1
			
			
		user_answ = input("\nType the number of correct answer: ")
		user_answ = answ[int(user_answ)-1]
		
		if user_answ == correct_answ:
			print("\nCongratulations!! you  answer correctly!! the correct answer!! The correct answer was: " + html.unescape(correct_answ))
		else:
			print("Sorry, " + html.unescape(user_answ) + " is incorrect.The correct answer was: " + html.unescape(correct_answ))
		
		engame = input("\nPress enter to play again or type quit to quit the game ").lower()
		
print("\nThanks for playing")
