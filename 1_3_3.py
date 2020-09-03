x = int(input("Type a number: "))

if x == 177: 
	print("You guessed the secret number!")
elif abs(x - 177) < 5:
	print("You were...SO CLOSE!")
else:
	print("Bad guess... :(")

shoppingList = ["gaming pc", "food", "headphones", "keyboard", "mouse"]

if "gaming pc" in shoppingList:
	print(len(shoppingList))