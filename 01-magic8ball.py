#Made for Python 2.7
#Needs upgrade to Python 3.5

import random
import time
import sys


list = ["Yes, most definitely!", "The chances are high!", "Not likely!",
        "May the odds be ever in your favor.", "You got no shot, kid.",
        "Try it out and see!", "A 33.3% chance for success",
        "A 99.9% chance for success", "Congratulations, yes!",
        "Ask a probably question", "Ask again later",
        "Better not tell you now", "Cannot predict now",
        "Concentrate and ask again", "Don't count on it"
	]

def userinput():
	question = 'Enter your question:'
	print(question)
	stuff = eval(input("> "))

	print("\nThinking..\n")
	time.sleep(3)
	print((random.choice(list)))
	
	final()
	
def final():
	print("Would you like to ask another question?")
	print("Type yes to continue...")
	user_reply = input('> ').lower()
	while(input):
		if user_reply == "yes":
			userinput()
		else:
			print("Thanks for playing!")
			sys.exit(0)
print("Welcome to the Magic 8 Ball!")
userinput()

#   Goal
#   I'm sure you've used a magic 8 ball at one point in your life.
#   You ask it a question, turn it right side up and it gives an answer by way of a
#   floating die with responses written on it. You can create one in python. You must:
#       Allow the user to enter their question
#       Display an in progress message( i.e. "thinking")
#       Create 20 responses, and show a random response
#       Allow the user to ask another question or quit
#   Bonus Using whatever module you like, add a gui. Your gui must have:
#       A box for users to enter the question
#       At least 4 buttons: Ask , clear(the text box), play again and quit(this must close the window)
