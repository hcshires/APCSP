import random
import time

playAgain = "yes"

def displayIntro():
	print("Welcome to The Dragon's Lair! You will approach two caves inhabited by dragons. One contains a friendly dragon that will share its treasure. In the other dwells a dragon that eats anyone who enters. You must choose which cave to enter, and thus decide your fate!")
	
def chooseCave():
	cave = ""
	while cave != "1" and cave != "2":
		cave = input("Choose a cave and decide your fate: Cave 1 or Cave 2? ")
		if cave != "1" and cave != "2":
			print('Invalid Input. Please choose 1 or 2.')
		else:
			cave = int(cave)
			break
	return cave
		
def checkCave(chooseCave):
	enemyCave = random.randint(1, 2)
	print("Let's see if you chose wisely...")
	time.sleep(2)
	if chooseCave == enemyCave:
		print("It looks safe so fa-OH NO! HELP! HE'S GONNA EAT ME!")
		print("You Died.")
	else:
		print("Good job! You found the friendly dragon!")

while playAgain == "yes" or playAgain == "y":
	displayIntro()
	cave = chooseCave()
	checkCave(cave)
	playAgain = input("Wanna play again? ")