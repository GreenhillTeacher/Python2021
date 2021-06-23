#Quentin
from hashlib import new
from os import write
import os 

scoredat="MariaGame.txt" 
def pause():
    print("Press enter to continue:") 
    input() 
print("Scores Chosen") 
with open(scoredat,'r') as first_file:#open score archive
    rows = first_file.readlines() 
    sorted_rows = sorted(rows, key=lambda x: int(x.split()[4]), reverse=True) 
    with open(scoredat,'w+') as second_file: 
        for row in sorted_rows:
            second_file.write(row) 
first_file.close() 
second_file.close() 
writenScores = open(scoredat, "r") 
displayScores = writenScores.read() 
print(displayScores) 
writenScores.close() 
pause() 