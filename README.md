# Command-Line-HANGMAN

## Summary
Created a game of Hangman, with the user playing against the computer. The computer thinks of a word and the user’s objective is to guess the word one letter at a time. To begin, the number of letters in this secret word are revealed with '_' along with an empty ASCII image of the hangman post.  The user has six lives (incorrect guesses) and if the word is not completely solved by the time all six parts are drawn, the game is over. 

When a correct letter is guessed, all occurrences of that letter are revealed. 
Scenario 1, All letters revealed (guessed) before maximizing the 6 incorrect attempts mean the user has won. 
Scenario 2, The ASCII image saved as a list of stages within a global variable, where a body part is attached per incorrect guess, is updated and displayed along with a statement to alert the user of remaining attempts out of six. A full drawn figure (last index in the HANGMAN_PICS) means player lost. 
 
For player's reference, a visible record of all guessed letters is maintained and the program logic supports duplicate guesses by alerting the user to try again without it counting against their progress in the game.

## Tech Stack
* Python 2 </br>
* Word dictionary REST API </br>

## Word dictionary REST API setup:
This command line hangman game uses a dictionary list of words from the word dictionary REST API. I imported urllib2 (at the very top of my hangman.py file).urllib2 is a Python module that can be used for fetching URLs for the user to then massage data retrieved into the ideal format.

To randomly generate a word from this string of words, from the word dictionary REST API, I setup a global variable 'WORD' as shown below:

WORDS = urllib2.urlopen('http://app.linkedin-reach.io/words').read().split() 

The .read() method on WORDS will return the response body of that url.
The .split() menthod on WORDS will convert the string of words into a list containing each of the words as a string.

## Installation
* Python 2.0

To run Hangman Command Line Game:
* Open a terminal window </br>
* Navigate to location where hangman.py file is stored (I.e. src/hangman/hangman.py) </br>

Run the app: </br>
python hangman.py </br>

If testing functions in interactive python import the following: </br>
* Import random </br>
* Import urllib2 </br>
 
## Features

* Length of secret word is displayed to player as a set of underscores.
* Correct guesses made are displayed in each instance where the letter appears in the secret word.
* Letters not yet guessed remain hidden with '_' until with the full word or letters are guessed within 6 tries.
* With each attempt the number of guesses out of 6 is displayed.
* List of incorrect guesses is also displayed.

## Extension
* With each incorrect attempt (wrong letter or full word) the ASKEE image is updated and displayed alongside countdown.

## Version 2.0
* Enable user to input full word

## About the Developer
Command-Line-HANGMAN was created by Benish Sarinelli, a software engineer in San Francisco, CA. Learn more about the developer on [LinkedIn](https://www.linkedin.com/in/bsarinelli/).
