import sys,random,time
#define global variables
filename='TRIVSCORES'
scores=0
choice=0
name =input("What is your name?")
print(name, end = " ")
l1='+  +  +  +  +  +  +  +  +  +  +  +  '
l2='+       ********************       +'
l3='+       ******Level 1*******       +'
l4='+       ******Level 3*******       +'
l5='+       ******Level 2*******       +'
l6='+       ****Print Scores****       +'
l7='+       ******Exit**********       +'
l8='+       ********************       +'
l9='+  +  +  +  +  +  +  +  +  +  +  +  '
#game functions
def menu():
    print(l1)  
    print(l2)
    print(l3)
    print(l4)
    print(l5)
    print(l6)
    print(l7)
    print(l8)
    print(l9)
    choice=input('please enter selection 1-5') #convert to an integer
    return choice

def writescores():
    FILE= open(filename, 'w')
    line='you had a score of' +str(scores)  
    FILE.write(line)
    FILE.write('')
    FILE.close

def printscores():
    FILE=open(filename, 'r')
    print(FILE.read())
    input('enter when you no longer want to see scores')
    FILE.close()


choice = menu()
check=True
while check:
    if "1" in choice:
        print("Level 1 Chosen: Movies!")
        #create loop to repeat level until they are done
        #call function that play this game
        break
    if "2" in choice:
        print('Level 2 Chosen: Celebrities!')
        break
    while choice==3:
        print('Level 3 Chosen: Books!')
        break
    while choice==4:
        printscores()
        break
    while choice==5:
        print('Thank you for playing, Goodbye! :)')
        sys.exit()
    choice=menu() 
