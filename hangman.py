import random
import urllib2

HANGMAN_PICS = ['''
    +----+
         |
         |
         |
       ===== 6 tries remain to start! Goodluck :) ''', '''
    +----+
    O    |
         |
         |
       ===== 5 tries out of 6 remaining! ''', '''
    +----+
    O    |
    |    |
         |
        ===== 4 tries out of 6 remaining! ''', '''
    +----+
    O    |
   /|    |
         |
       ===== 3 tries out of 6 remaining! ''', '''
    +----+
    O    |
   /|\   |
         |
       ===== 2 tries out of 6 remaining! ''', '''
   +----+
   O    |
  /|\   |
  /     |
      ===== 1 more try remaining! ''', '''
   +----+
   O    | 
  /|\   |
  / \   |
      ===== Yikes! You just lost :/ ''']


#Using urllib2 to get a dictionary list of words from the word dictionary REST API.
WORDS = urllib2.urlopen('http://app.linkedin-reach.io/words').read().split()
#.read() will return the response body of that url.
#.split() will convert the string of words into a list of the words as a string.


def getRandomWord(WORDS):
    """ Returns the secret word at a random index. """
   
    word_Index = random.randint(0, len(WORDS) - 1)
    return WORDS[word_Index]

def displayBoard(missed_letters, correct_letters, secret_word):
    """ Displays game progress of all information being maintained. """
    print (HANGMAN_PICS[len(missed_letters)])
    #missed_letters is the string determining which index of Hangman Pics to display with each incorrect guess with the len method being used as a count.

    print ('Missed letters: ')
    for letter in missed_letters:
        print (letter)

    blanks = '_' * len(secret_word)
    # will display the '_' with relation to the len of randomly generated word.

    for letter in range(len(secret_word)):
        # want to replace the blanks with correctly guessed lettters.
        # all instances of a letter guessed should be updated.
        print (letter)

    for i in range(len(secret_word)):
        #comparing i to each letter by index
        if secret_word[i] in correct_letters:
            blanks = blanks[:i] + secret_word[i] + blanks[i+1:]
        #below the letter is printed where it belongs to replace blanks.
    for letter in blanks:
        print (letter)

def getGuess(already_guessed):
    """ Returns guessed letter and makes sure a single letter was entered. """
    while True:
        print ('Guess a letter: ')
        guess = raw_input()
        guess = guess.lower()
        if len(guess) != 1:
            print ('Please enter a single letter.')
        elif guess in already_guessed:
            print (' You have guessed this letter already. Choose again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print ('Enter a letter please!')
        else:
            return guess

        print('Feeling ambitious? Guess the full word: ')
        guess_word = raw_input()
        guess_word.lower()

        if len(guess_word) == len(secret_word):
            print ('Awesome job guessing the full word! You won...\0/...')
        elif guess_word not in 'abcdefghijklmnopqrstuvwxyz':
            print ('Enter a-z letters only please!')
        else:
            
            return guess_word
            break
        

def playAgain():
    """ Allows player to play Hangman again once game is complete. """
    print ('Would you like to play again? (yes or no)')
    return raw_input().lower().startswith('y')
print ('==================')
print('''
_______________
*               *
* H A N G M A N *
*______________ *
         ''')
print ('==================')


missed_letters = ''
correct_letters = ''
secret_word = getRandomWord(WORDS)
# guess_full_word(secret_word)
gameIsDone = False

while True:
    displayBoard(missed_letters, correct_letters, secret_word)

    #Player to enter a letter.
    guess = getGuess(missed_letters + correct_letters)

    if guess in secret_word:
        correct_letters = correct_letters + guess

        # Check to see if all letters have been guessed. Player won.
        foundAllLetters = True
        for i in range(len(secret_word)):
            if secret_word[i] not in correct_letters:
                foundAllLetters = False
                break
            if foundAllLetters:
                print('Yayyyy *** \o/ *** You won! The secret word is '+secret_word+'.')
                gameIsDone = True

    else:
        missed_letters = missed_letters + guess
        #remember we need to control for maximum of 6 tries. 
        if len(missed_letters) == len(HANGMAN_PICS) - 1:
            displayBoard(missed_letters, correct_letters, secret_word)
            print ('You are out of guesses! Check out the results of your play: '
                + str(len(missed_letters)) + ' missed guesses and ' +
                str(len(correct_letters))+ ' correct guesses, the word was "' + secret_word + '"')
            gameIsDone = True 

    #      #player to enter full word.           
    # full_word = guess_full_word(secret_word, correct_letters, missed_letters) #full word
    # if full_word == secret_word:
    #     foundAllLetters = True
    #     print "YOU GUESSED THE FULL WORD OMG!!!"
    #     gameIsDone = True
    # else:
    #     foundAllLetters = False
    #     print('Better luck next time')
    #     missed_letters = missed_letters + full_word # full word


# Ask player if they want to play again. Only if the game is done.
    if gameIsDone:
        if playAgain():
            missed_letters = ''
            print '------'
            correct_letters = ''
            print '------'
            gameIsDone = False
            secret_word = getRandomWord(WORDS)

        else:
            break





