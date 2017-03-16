import string

''' secretWord: the word the user is guessing;
    lettersGuessed: list, what letters have been guessed;
    function hangman(secretWord) starts up an interactive game "Hangman".
    The program should show the user how many letters to be guessed.
    Inform user that only one letter per round is available.
    If user choosed wrong letter, he/she lose 1 round from avalable rounds.
    
'''

# verifying if the letters to guess are in 'secretWord'

def isWordGuessed(secretWord, lettersGuessed):
    for e in secretWord:
        if e not in lettersGuessed:
            return False
    return True # if all of 'lettersGuessed' are in 'secretWord'

# function 'getGuessedWord' indicate where is the guessed letters
# taking the place in 'secretWord', and if there are letters not yet guessed,
# indicate this place with underscore '_ '

def getGuessedWord(secretWord, lettersGuessed):
    result = ''
    for e in secretWord:
        if e in lettersGuessed:
            result += e
        else:
            result += '_ '
    return result # print out something like "a_ _ l_ " if  
                  # lettersGuessed = ['a', 'l'] are in the (secredWord = 'apple')

# now we'll get a string with available letters
def getAvailableLetters(lettersGuessed):
    
    result = ''
    
    for e in string.ascii_lowercase:
        if e not in lettersGuessed:
            result += e
    return result #'abc...xyz'

# the game
def hangman(secretWord):
    print('Hello! Welcome to the game "Hangman"!')
    print('You should guess a word, that has ' \
            + str(len(secretWord)) + ' letters. And you have 8 guesses per game.')
    guessLeft = 8
    print('') # blanc line just for design

    lettersGuessed = []
    while guessLeft > 0 and not isWordGuessed(secretWord, lettersGuessed):
        print('You have ' + str(guessLeft) + ' guesses left.')
        print('Avalable letters: ' + getAvailableLetters(lettersGuessed))
        
        guess = str(input('Plese guess a letter: '))
        guess=guess.lower() #transform UPPERCASE to lowercase
        
    	while len(guess) > 1 and guess not in string.ascii_lowercase:
    	    guess = str(input('Please type one letter per round only: '))
    	if guess not in lettersGuessed:
    	    lettersGuessed.append(guess)
    	    if guess in secretWord:
    		print('Right, go on!')
    		print('')
    	    
    	    else:
    		guessLeft -= 1
    		print('Wrong! there is no that letter in my word, try again...')
    		print('')
    	else:
    	    print('You have already guessed that letter, try again...')
    	print(getGuessedWord(secretWord, lettersGuessed))
    	print('')

    # test, if all the letters guessed are in secretWord	
    if isWordGuessed(secretWord, lettersGuessed):
    	print('Congratulations, that was my word!')
    else:
        print('Sorry, you lose. The word was: ','"',str(secretWord),'"')
