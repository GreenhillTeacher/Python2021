#MAria Suarez     ctrl /
# We are learning about List and Tuples
# Learn their functions and looping with List

# HOw to use a module or library by oimporting
import random

myFruit=["apples","berries", "mangos", "banana"]
print(myFruit)
for fruit in myFruit:
    print(fruit)
fruity=("apple", "kiwi", "banana")
print(fruity)
temp=list(fruity)
temp.insert(1,"papaya")
fruity= tuple(temp)
print(fruity)

for fruit in myFruit: # for each element of the  array get the element
    print(fruit, end=" , ")
print()
counter=len(myFruit) #the lenght of your list is one more than your last index 
#finding a random number to be the index to select randint()
indx= random.randint(0,counter-1)
print(indx)
print("your lucky fruit is ", myFruit[indx] )
word=random.choice(myFruit)
print("your lucky fruit is ", word)
input()
#random method choice()
word=random.choice(myFruit)
print("Your random fruit is ", word)

for x in range(0,counter-1):
    print(myFruit[x], end=" , ")

print(myFruit[counter-1]) #print the last element

if "apples" in myFruit:
    print("Yes you got apples")
    myFruit.remove("apples")
    print(myFruit)
myFruit.insert(0,"kiwi")
myFruit.insert(2,"papaya")
myFruit.append("beets")
print(myFruit)

fruity=("apple", "pears", "banana")  #tuple
print("tuple", fruity)
temp= list(fruity)     #temp is a list
print("list",temp)
temp.insert(1,"kiwi")
fruity=tuple(temp)
print("tuple modified ", fruity)
print("list modified ",temp)
for element in fruity:
    print(element)