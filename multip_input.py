#Maria Suarez
#6/4/2021
# We are going to print multiplacation tables
# Using print statements and a variable
# input ---> variable is container that will hold data and an address is assigned to it
# variables need to have valid name 
base = 2
numberBase = "multiplication"
base3= 3.5
#print(base + base3)
print(1 * base)  #multiplication is represented with *
print(2 * base)  #division /
print(3 * base)
print(4 * base)
print(5 * base)
print(6 * base)
print(7 * base)
print(8 * base)
print(9 * base)
print(10* base)
# when we repeat something we should loop loop with counter
for counter in range(1,11):   #initial value that included ending value is not included
    print(counter* base, end="   ")
print()
base =3
for counter in range(1,11):   #initial value that included ending value is not included
    print(counter* base, end="   ")
print()
 #nested for loop
for base in range (2, 10):
    for counter2 in range(1,11):   #initial value that included ending value is not included
        print(counter2* base, end="   ")
    print()

    #        multiplication table 2
    # 1 x 2 = 2
    # 2 x 2 = 4
