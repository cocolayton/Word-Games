#import necesssary libraries
from pytrie import StringTrie

three_letter_words = [] #list containing all words greater than 2 letters long

with open("scrabble.txt", 'r') as f: #file name, mode --> names the file 'f'
	for line in f:
		if len(line) > 3: #have to put 3 bc the new line character counts as a character
			three_letter_words.append(line)

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


"""
	Function which returns all strings that contains given prefix
"""
def is_valid(valid_list, letters):
	# create empty trie
	trie=StringTrie()


	# traverse through list of string to insert it in trie.
	# Here value of key is itself key because at last we need to retun
	for key in valid_list:
		trie[key] = key

	# values(search) method returns list of values of keys
	# which contains search pattern as prefix
	return trie.values(letters)



done = False
overall_word = ""

while(done == False):
	user_letter = input("Please enter a letter: ")
	
	overall_word = overall_word + user_letter #add to create new overall word
	
	valid_words = is_valid(three_letter_words, overall_word) #returns list of potential words that can be created with the addition of the user letter

	if not valid_words:
		break

	if (overall_word + "\n") in three_letter_words: #need new line character so it matches the word in the file
		print("You lost because you spelled the word: " + overall_word)
		break

	words_to_choose_from = valid_words # this list gives the words that have the letters picked
										#so far and thus potential words for the robot
	odd_words = []

	#find words that have odd number of letters so will land on user
	for word in words_to_choose_from:
		if len(word)%2 == 0: #have to say zero bc the new line charcter counts as a letter so odd number letter appear as even
			odd_words.append(word)

	# sort list from shortest to longest word
	sorted_list = sorted(odd_words, key=len)

	# get only words with relevent lengths
	sorted_list_relevent_length = []

	for word in sorted_list:
		if len(word) > len(overall_word):
			sorted_list_relevent_length.append(word)

	#print(sorted_list_relevent_length)



	#NEED TO DO NEW CHECK TO SEE IF LETTER CREATES A SHORTER WORD -- IN THAT CASE PICK NEXT SMALLEST WORD


	# now get the shortest word because that will likely guarentee that there are no ways
	# for the user to get out of it (SEE IF THERES A DIFFERENCE BETWEEN SHORT WORDS AND WHICH ARE BETTER)
	robot_word = sorted_list_relevent_length[0]
	print("robot word: " + robot_word)

	index_of_letter_to_pick = len(overall_word) #if user enters 1st letter, robot must pick the second letter in the word its thinking of

	robot_letter = robot_word[index_of_letter_to_pick]

	print("Robot choice " + robot_letter)

	overall_word = overall_word + robot_letter
	print("Word so far: " + overall_word)

	if (overall_word + "\n") in three_letter_words:
		print("Robot lost because it spelled the word: " + overall_word)
		break


print("Game Over")




# Driver program
#arr = ['geeksforgeeks','forgeeks','geeks','eeksfor']
#prefix = 'hello'
#output = is_valid(arr,prefix)
#print(output)
#if len(output) > 0:
	#print(output)
#else:
	#print('Pattern not found')



#get robot to pick letter than has fewest number of return words and is also odd # so lands on user







