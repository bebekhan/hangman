# Command-Line-HANGMAN

## Summary

** In this classic game of Hangman, a player's objective is to identify a hidden word. To begin, only the number of letters in this secret word are revealed along with an empty ASCII image. With each round, the player guesses a letter a-z and if that letter exists in the secret word each instance of where the letter appears will be overwritten with the '-' remaining for the letters not yet guessed.  With each guess that is incorrect, the ASCII image saved as a list of stages, where a body part is attached per incorrect guess, is updated and displayed along with a statement to alert user of remaining attempts out of six. 


For player's reference, a visible record of all guessed letters is maintained and the program logic supports duplicate guesses by alerting the user to try again without it counting against their progress in the game.

This command line hangman game uses a dictionary list of words from the word dictionary REST API. I imported urllib2 (at the very top of my hangman.py file).Urllib2 is a Python module that can be used for fetching URLs for the user to then massage into the ideal format as needed.

To randomly generate a word from this string of words from the word dictionary REST API, I setup a global variable 'WORD' as shown below:

WORDS = urllib2.urlopen('http://app.linkedin-reach.io/words').read().split() 

The .read() method on WORDS will return the response body of that url.
The .split() menthod on WORDS will convert the string of words into a list containing each of the words as a string.

## About the Developer

Command-Line-HANGMAN was created by Benish Sarinelli, a software engineer in San Francisco, CA. Learn more about the developer on [LinkedIn](https://www.linkedin.com/in/bsarinelli/).

## Technologies

**Tech Stack:**

-Python 2
-Word dictionary REST API

## Features

- **Length of secret word is displayed to player as a set of underscores.
- **Correct guesses made are displayed in each instance where the letter appears in the secret word.
- **Letters not yet guessed remain hidden with '_' until with the full word or letters are guessed within 6 tries.
- ** With each attempt the number of guesses out of 6 is displayed.
- ** List of incorrect guesses is also displayed.

## Extension
- ** With each incorrect attempt (wrong letter or full word) the ASKEE image is updated and displayed alongside countdown.
This short clip displays the ASKEE image in the form of a list which is displayed with index at 0 being just the stand (start of game) and with each index the image adds the body parts until index 6 (end of game once complete):


- ** Guessing full words during the game is supported. If guessed incorrectly, the missed letters count is updated the same as with incorrect letters.

The first example below is of the player guessing the full word and winning the game:


The second example below is of the player unsuccessfully attempting to guess the full word. Note that the image increments to behave the same as when the player incorrectly guesses a letter.
