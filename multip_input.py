#Maria Suarez
#6/4/2021
# We are going to print multiplacation tables
# Asking the user which table
# input ---> user input using the input fuction
# variables need to have valid name 
answer = input()
base = int(answer)
 #nested for loop
for base in range (2, 10):
    print("Multiplication Table", base)
    for counter2 in range(1,11):   #initial value that included ending value is not included
        print(base, " x ", counter2, " = ", base*counter)
    print()

    #        multiplication table 2
    # 1 x 2 = 2
    # 2 x 2 = 4