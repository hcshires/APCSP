from __future__ import print_function
import random
 
def guess_winner(players=('Amy', 'Bill', 'Cathy', 'Dale')):
    ''' A function that randomly selects an input as a "winner" and takes user input for who won.
	Input -> Players - The list of people to choose from (player=('choice', 'choice')
    '''
    winner = random.choice(players) 

    ####
    # Summarize the following section of code here
    ####
    print('Guess which of these people won the lottery: ',end='')
    for p in players[:len(players)-1]: # explain index here
        print(p+', ', end='')
    print(players[len(players)-1]) # explain this line here

    ####
    # Summarize the following section of code here
    ####
    guesses = 1 
    while input() != winner:
        print('Guess again!')
        guesses += 1
    print('You guessed in', guesses, 'guesses!')
    return guesses
	
 # guess_winner()