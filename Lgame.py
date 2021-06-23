#Maria Suarez
#starting from Lucas code
# while loop is a loop that repeats until condition is met
# if statement --> branching or selection base on conditions
# functions a piece of code that we create to prevent repetition starts with a def keyword

# i need  7 choice of the String Methods
#Stay in each option until I ado not want to play anymore 
#Exit from main menu
varChoice=" "
def menu():      # declaring a function o
    print("*"*28)
    print("*"," "*6,"Forerunner"," "*6,"*")
    print("*"," "*9,"Menu"," "*9,"*")
    print("*"," "*24,"*")
    print("*"," "*2,"L1- Capitalize"," "*4,"*")
    print("*"," "*2,"L2- EndsWith"," "*5,"*")
    print("*"," "*2,"L3- Centering"," "*7,"*")
    print("*"," "*2,"L4- Exit Game"," "*7,"*")
    print("*"," "*2,"L5- Exit Game"," "*7,"*")
    print("*"," "*2,"L6- Exit Game"," "*7,"*")
    print("*"," "*2,"EX- Exit Game"," "*7,"*")
    print("*"*28)
    print("Enter either L1,L2,L3,or EX", end= " ")
    varChoice= input()  #local variable
    return varChoice
def score():
    print("Your scores:")
    print(" 23434   Peter")
    print(" 1543    Maria")
    print("  978    Lucas")
    print("  567    Ben")
def gamePause():
    print("Do you want to change levels?")
    level = input()
    if level !='no':
        varChoice=menu()
varChoice=menu()   # call function

while varChoice != "EX":
    if varChoice == "L1":
        print ("You are in level 1")
        print("Please enter a phrase")
        answer = input()
        answer = answer.capitalize()
       # print(answer.capitalize())
        print(answer)
        gamePause()

    if varChoice =="L2":
        print("You are in Level 2")
        #ask user for phrase
        #ask for word
        #endswith
        gamePause()
    if varChoice =="L3":
        score()
    if varChoice =="L4":
        print("You are in Level 2")
    if varChoice =="L5":
        score()
print("Goodbye, Have a nice day")