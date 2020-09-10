#import necesssary libraries
from pytrie import StringTrie

valid_words = [] #list containing all words greater than 2 letters long

with open("scrabble.txt", 'r') as f: #file name, mode --> names the file 'f'
	for line in f:
		if len(line) > 3: #have to put 3 bc the new line character counts as a character
			valid_words.append(line)

#count = 0
#for word in valid_words:
	#if count > 5:
		#break
	
	#print(word)
	#count += 1

# 3) The game of ghost is played by taking turns
#    with a partner to add a letter to an increasingly
#    long word. The first person to make a valid scrabble word
#    of length 3 or more loses.
#    You must be thinking of a valid word when you name a letter.
#    write a game that implements ghost
#    addendum: write a bot to play ghost against you.


#take out all 2 letter words √

#in a loop they enter a letter, check if there is a word that has that
#first letter

#robot generates a second letter (prior to print check that it exists, if
#not pick a different one -- make random for now

#enter another letter -- check if its a word -- yes = lose, no = exists then
#robot turn -- lose if wrong

#prefix search (find all words that start with this prefix)

done = False

while(!done):
	user_letter = input("Please enter a letter: ")
	#print(user_letter)

	#use is valid method (see implemenation below the method)

	#implement check method


"""
	Function which returns all strings that contains given prefix
"""
def is_valid(valid_list, letters):
	# create empty trie
	trie=StringTrie()


	# traverse through list of string to insert it in trie.
	# Here value of key is itself key because at last we need to retun
	for key in arr:
		trie[key] = key

	# values(search) method returns list of values of keys
	# which contains search pattern as prefix
	return trie.values(prefix)


# Driver program
arr = ['geeksforgeeks','forgeeks','geeks','eeksfor']
prefix = 'geek'
output = is_valid(arr,prefix)
if len(output) > 0:
	print(output)
else:
	print('Pattern not found')







