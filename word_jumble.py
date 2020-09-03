import random

word_bank = ["helicopter", "frankenstein", "fella", "handstand", "home run"]

def choose_word():
	''' will return a random word from the word bank '''
	word = ""
	spot = random.randint(0, 4) # pick random 0 to 4
	word = word_bank[spot]
	
	return word 
	
def jumble_word(the_word):
	''' given a non-empty string, will return new string with characters in random order '''
	jamble = ""
	if type(the_word) == str:
		for i in range(len(the_word)):
			spot = random.randint(0, len(the_word)-1)	# since .random and indexing aren't on the same value system we need to subtract one from the index
			jamble += the_word[spot] # jamble = jamble + our new letter
			the_word = the_word[0:spot] + the_word[spot+1: ]
			
		return jamble	

		
def main():

	correct = choose_word()
	jumbled = jumble_word(correct)
	print("Welcome to word jamble")
	print ("can you unscramble this: ", jumbled)
	answer = input(">>")
	attempts = 0
	
	while answer != correct and answer != "": # keep going until they hit enter or get it right
		answer = input("wrong, try again >>")
		attempts = attempts + 1

	if attempts == 0 and answer == correct:
		print("YOU GOT IT RIGHT ON THE FIRST TRY! GO YOU!")
	
	elif attempts >= 1 and answer == correct:
		print("YOU GOT IT RIGHT! Next time, try to get it on the first try :)")
	
	else:
		print("COME ON QUITTER! Give it another go!")
	''' determine whether they got it on the first try, 
	they got it on a later try, or they gave up '''
	

main()  # run the program