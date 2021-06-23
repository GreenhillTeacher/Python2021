#Maria Suarez
#Modifying Quentin's program
# while loop
# conditional if
# function is a piece of code that we can reuse
#  to declare a function we must use the keyword def  give a name to the function ()

#Global variables can be used anywhere in your program
l1="******************************"
l2="*       My game              *"
l3="*                            *"
l4="*    1 - Capitalize          *"
l5="*    2 - Uppercase           *"
l6="*    3 - Lowercase           *"
l7="*    4 - Find index of char  *"
l8="*    5 - Split               *"
l9="*    6 - Translate           *"
l10="*    7 - Exit              *"
l11="*****************************"
x=2#global variable
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
    print(l10)
    print(l11)
    print("PLease enter your selction form 1 to 4")
    inputNumber = input()
    x = int(inputNumber)
    return x
def score():
    print("Scores Chosen")
    print(l1)
    print("*        Scores          *")
    print(l3)
    print("*    1 - ???- 999        *")
    print("*    2 - ???- 876        *")
    print("*    3 - ???- 745        *")
    print(l3)
    print(l8)
def pause():
    print ("Do you want to play again? ")
    answer1= input()
    answer1=answer1.upper()
    if "Y" in answer1:
        return True
    else:
        return False

while x != 7:   #loop is conditioned to an event 
    x=menu()    # this is a function call expecting a return value
    if(x==1):                  #if statement are selection or branching
        convert=True    #boolean local variable 
        while convert:
            print("Level 1 Chosen")
            print("Please enter a phrase in lower case")
            answer=input()    #input is a function returns a string
            answer=answer.capitalize() #update your variable to the new change if i dont need original value
            print(answer)
            convert = pause()
            

        # LEt the user stay in the level and reuse it many times until they want to get back to main menu 
        
    if(x==2):
        print("Level 2 Chosen")
        convert=True    #boolean variable
        while convert:
            print("Please enter a phrase in lower case")
            answer=input()    #input is a function returns a string
            answer=answer.upper() #update your variable to the new change if i dont need original value
            print(answer)
            convert = pause()
            
        
    if(x==3):
        score()   #function call
    

print("Goodbye Thank you for playing")
