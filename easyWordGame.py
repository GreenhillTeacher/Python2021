#Maria Suarez
#06/11/2021
#Word Game
# We are creating a list of words
# randomly select a word from the list for the user to guess
# give the user some turns
# show the word to the user with the characters guessed  
# play as long as the user has turns or has guessed the word
import random

def updateWord(word):
    for char in word:
        if char in guesses:
            print(char, end=' ')
        else:
            print('_', end=' ')
gameWords= ['python','java','trackpad','computer','keyboard','geeks','laptop','headphones','charger','mouse','software','hardware']
name =input("What is your name?")
print(name, end = " ")
answer = input(" Do you want to play? ").upper()
print("\n ",gameWords) #delete when code works properly 
#This is a function that needs a value ---> parameter
while "Y" in answer:
    #Beginning of the game
    print(name," Good luck")
    word=random.choice(gameWords)
    print(word)
    turns=10  # find better way to create turns
    guesses=''
    counter=len(word)
    updateWord(word)
    #control the active  word part of the game
    while turns >0 and counter>0:
           #print dashes the first time and replace letters later
        newGuess=input("\n Give me a letter ")
        if newGuess in word:
            rept=word.count(newGuess)
            counter -=rept
            guesses += newGuess    #guesses= guesses+newGuesses
            print("You are Right!!" )
        else:
            turns -= 1
            print ("Sorry that is wrong you still have ", turns," turns") 
        updateWord(word)
    if(counter ==0):
        print(" You guessed right!!! ")
    else:
        print("oops better luck next time")
    answer=input("Would like to play again?").upper()
print("\n Goodbye")