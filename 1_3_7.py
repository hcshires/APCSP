'''
# basic for loop that runs x times
for i in range(10):
	if i == 0:
		print("I can count...")
	print(i+1, "...")
print("Aren't you pround of me?")

# loop that runs in a specific range
for i in range(5, 10, 2):
	print(i)
	
words = ["helmet", "contingent", "stark", "forgetful"]

# if you want to reference the index/position, use a counting for loop
for i in range(len(words)): # i is the stepper variable
	print("The word at position", i, "is", words[i])
	
# if you're just accessing the items in a collection you CAN use this
# for-each loop
# you CANNOT edit the list/collection using a for-each loop
for thing in words:
	print(thing.upper()) # thing is a walker variable, NOT a counter/stepper
	
print(words)

# count the number of vowels in the word
vowels = ['a', 'e', 'i', 'o', 'u']
count = 0
wordSelect = int(input("Choose an index: "))
for letter in words[wordSelect]:
	if letter in vowels:
		count+=1

print("there were", count, "vowels in", words[wordSelect])
'''

import matplotlib.pyplot as plt # standard short name
import random
import time

'''
def picks():
	a = [] # make an empty list

	# Why all the brackets below?
	# a += [  brackets here to add an iterable onto a list      ]
	#    random.choice(   [brackets here to choose from a list] )

	for choices in range(5):
		a += [random.choice([1, 3, 10])]

	plt.hist(a)
	plt.show()
'''

def roll_hundred_pair():
	dice = []
	
	dice += [random.choice([1, 2, 3, 4, 5, 6]), random.choice([1, 2, 3, 4, 5, 6])]
	
	for rolls in range(100):
		dice += [random.choice([1, 2, 3, 4, 5, 6]), random.choice([1, 2, 3, 4, 5, 6])]
		
	plt.hist(dice)
	plt.show()

def dice(diceNum):
	score = []
	score += [random.choice([1, 2, 3, 4, 5, 6])]
	
	for i in range(diceNum):
		score += [random.choice([1, 2, 3, 4, 5, 6])]
		
	print("The roll was", sum(score[:diceNum]))

def matches(ticket, winner):
	correct = 0
	
	for i in range(len(ticket)):
		if ticket[i] in winner:
			correct += 1
	
	print(ticket)
	print(winner)
	return correct


winner = [0, 3, 10, 5]
ticket = []
for i in winner:
	newNum = random.randint(0, 10)
	if newNum not in ticket:
		ticket.append(newNum)

dice(5)
print(matches(ticket, winner))
time.sleep(3)
roll_hundred_pair()