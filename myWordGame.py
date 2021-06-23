#MAria Suarez
# 06/11/2021
#Word Game
# We are creating a list of words
# randomly select a word from the list for the user to guess
# give the user some turns
# show the word to the user with the characters guessed  
# olay the gane as long as the user has turns or has guessed the word

import random
import sys
import os
import time
import datetime
import pygame
os.system('cls')
#Global variables
gameWords= ['python','java','trackpad','computer','keyboard','geeks','laptop','headphones','charger','mouse','software','hardware']
name=" "
score=0 #to total the number of wins
file="MariaGame.txt"
dt=datetime.datetime.now()
linef=str(dt.month)+"/"+str(dt.day)+"/"+str(dt.year)+"\t"+dt.strftime("%A")




def menu():  #create menu and get choice
    print("*"*28)

    print("*"," "*3,"Choice 1 - Play"," "*4,"*")

    print("*"," "*3,"Choice 2 = Scores"," "*2,"*")

    print("*"," "*3," 3 = Change Player"," "*1,"*")

    print("*"," "*3,"Choice 4 = Exit"," "*4,"*")

    print("*"*28)
    #1 PLay game
    #2 print score board
    #3change player
    #Exit
    return input("What is your choice? ")
def updateWord(word, guesses):  # function with a parameter to update word
    for char in word:
        if char in guesses:
            print(char,end=' ')
            displayWord += char+" "
        else:
            displayWord += "_ "
            print('_', end =' ')
    
def printScore():
    FileRead=open(file,'r')
    print(FileRead.read())
    FileRead.close()
    #Open file as read and print the file
def updateScore(score):
    FileWrite=open(file,'a')
    line=name+"\t"+ linef+ "\t\t"+str(score)
    FileWrite.write("\n"+ line)
    FileWrite.close()
    #open the file and update the score list 
    # date     NAme    score
#Start my main program
def PlayGame(answer, score):    #My function to play game
    while "Y" in answer:
        os.system('cls')
        print("Good luck ", name, "!")
        word=random.choice(gameWords)
        counter=len(word)
        print(counter)
        print (word)    #delete when we finish the code
        turns= 10   #should we conider controlling this number when he/she misses
        guesses=''
        updateWord(word, guesses)
        while turns>0 and counter >0:
            newGuess=input("\n\n Give me a letter ")
            #check that the new letter has not been used before
            if newGuess not in guesses:
                if newGuess not in word:
                    turns -=1    #       turns = turns -1
                    print("Wrong! You have  ", turns, "guesses left")
                else:
                    counter -=word.count(newGuess) #deleten repeated letters
                    print("nice guess!")
                guesses += newGuess 
            else:
                print("you used this one already")
            updateWord(word, guesses)
            #end of whole loop with 

        if counter==0:
            #print("")
            print("\n Fantastic you are Champion")
            score +=1
        else:
            print("Sorry, try harder next time")
        # find a way to decide if the person won the game or not 
        # keep a count of how many words they guessed   
        # #ask user if the want to play again
        answer=input("Do you want to play again? ").upper()
    updateScore(score)
#your main Program
check=True

while check:

    varChoice= menu()
    if "1" in varChoice:
        PlayGame("Y",score)
    elif "2" in varChoice:
        printScore()
        input("press enter when done")
        os.system('cls')
    elif "3" in varChoice:
        name=input("What is your name? ")
    else:
        print("Thank you ! ")
        check=False
    time.sleep(1)
    


