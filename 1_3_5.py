word = "happenstance"

print(word[2]) # Prints the second index/letter (third if counted from 1) of the string
print(word[3:7]) # Prints a series of indexes starting at 3 and ending at 6 (it does not include 7)
print(word[1:8]) # Prints a series of indexes starting at 1 and ending at 7 (it does not include 8)
print(word[:5]) # Prints the start of the string until it reaches index 4
print(word[9:]) # Prints the string starting at index 9 to the end.

def find_email_and_spam_it(text):
	for i in range(len(text)):
		chars = text[i:i+4] # a chunk of 4 characters from the text
		if chars == ".org" or chars == ".com" or chars == ".gov":
			print("FOUND AN EMAIL AT POSITION:", i)
			
some_text = "hahahahaahhahahahahahhaahhahhahahgentryc@wdmcs.orgfdasfjsdkalfdmyemail@gmail.comas fjdsklw wq;"
find_email_and_spam_it(some_text)