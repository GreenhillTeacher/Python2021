#Maria
# lists and their functions
#indexing a list always start in 0
myNumber=[1,2,37,8,9]
myFruits=["apples", "merries", "mango", "banana"]
print(myFruits)
myFruits.append("kiwi")
for fruit in myFruits:  # for each element in your array get the value
    print(fruit, end= " , ")
print()
counter=len(myFruits)   #len of Array is one ore than the last index
#for loop limit your array order
for x in range(0,counter-1):
    print(myFruits[x], end= " , ")
print(myFruits[counter-1])
myFruits[1]="berries"
print (myFruits[1:3])
if "apples" in myFruits:
    print("I got apples")
else:
    print ("I need apples")

