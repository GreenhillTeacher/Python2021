# MAria Suarez
# Learn how to use files
import os
import sys
import time

#using time to pause your games

print(" HEllo")
time.sleep(2)
print(" there")
def readFile():
    file= input("What is the name of the file? ")
    if os.path.exists(file):  #It is to make sure the file exists
        #it opens the file
        PEN=open(file, 'r')
        #prints the whole file
        print(PEN.read())
        PEN.close()
    else:
        print("The file does not exist! Thank you")
    
fileName="MariaGame.txt"
if os.path.exists(fileName):
    print("sorry that file exists ")
else:
    FILE=open(fileName, 'w')
    FILE.write("********   THIS IS MARIA's   FILE *****")
    FILE.close()
    time.sleep(1)
    FILE=open(fileName, 'r')
    print(FILE.read())
    FILE.close()
File=open("MariaGame.txt",'a')
newline= "\n \n What ever   or else"
File.write(newline)
File.close()

