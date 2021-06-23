# MAria Suarez
#06/14/2021
#We are going to learn how to open files. read files, write to files
#How to read files per line
#How to make a list from file
#How to manipulate the elements to find what we need
import os
import sys
import time
os.system('cls')
# print("Hello... let me guess your name ...")
# time.sleep(2)
# print("... almost... ")
# print("... Yes, you are MAria")
# time.sleep(2)
# os.system('cls')
# file=input("Please enter the file name add extension of the file. Ex file.txt :")
# #check if the file exist
# if os.path.exists(file):
#     PENCIL= open(file,'r')
#     print(PENCIL.read())
#     PENCIL.close()
# else:
#     print ("The file does not exit")
file="asdfre.txt"
FILE= open(file, 'r')
content = FILE.read()  #is string with full content of the file
print(content)
FILE.close()
FILE=open(file,'r')
content_List=FILE.readlines() #is a list of each line of the text file
print(content_List)
FILE.close()
for element in content_List:
    print("line : ",element)
    elem_list=element.split()
    print(elem_list)
    time.sleep(1)
#How do we reorder our score file highest to lowest score