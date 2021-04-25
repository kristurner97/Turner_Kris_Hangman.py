## Python3
## File: 20210425-Hangman_Python3.py
## Author: Kris Turner

import random

## Select random word from list and other variables

wordListFileName = "word_list.txt"

def chooseRandomWordFromFile():
  listOfWords = []
  with open(wordListFileName) as file:
    for line in file:
      listOfWords.append(line.strip("\n"))

  randomWordIndex = random.randrange(0, len(listOfWords))
  return listOfWords[randomWordIndex]

## Show current word with stars

def showWordWithAsterics(word, knownLetters=[]):
  hiddenWord = ""
  for letter in word.lower():
    hiddenWord += (letter if letter in knownLetters else "*")
  return hiddenWord

## Ask for user guess

def askAndCheckUserGuess(correctWord, lives, knownLetters):
  rawGuess = input("Please enter your next guess: ")
  if isinstance(rawGuess, str):
    guess = rawGuess.lower()
  else:
    print("Your guess can't contain numbers.")
    exit(0)

  ## Check if guess is word

  if (len(guess) > 1) and (guess == correctWord):
      knownLetters = list(correctWord)
  elif (len(guess) == 1) and (guess in correctWord):
    knownLetters.append(guess)
  else:
    lives -= 1

  return (lives, knownLetters)

## Game Loop

def game():
    knownLetters = []
    lives = 7
    isGameOver = False
    print("Welcome to Mini-hangman! We're about to choose a random word from our dictionary and all you have to do is guess it in 7 tries or less.")
    wordToGuess = chooseRandomWordFromFile()
    while isGameOver == False:
      hiddenWord = showWordWithAsterics( wordToGuess, knownLetters)

      #Check whether the player has guessed all the characters
      if not "*" in hiddenWord:
        isGameOver = True
        print("The word was", wordToGuess)
        print("Congratulations you win")
        break

      #Check whether the player still has lives
      if lives == 0:
        isGameOver = True
        print("The word was", wordToGuess)
        print("You lose")
        break

      # Else continue with the game
      print("You have", lives, "lives left. The word to guess:", hiddenWord)
      lives, known_letters = askAndCheckUserGuess(wordToGuess, lives, knownLetters)

game()
