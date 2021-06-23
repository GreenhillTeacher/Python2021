import time, sys, os,hashlib

os.system('cls')
file="MariaGame.txt"
FILE=open(file, 'r')
print(FILE.read())
FILE.close()
FILE=open(file, 'r')
contest_List=FILE.readlines()
#print(contest_List)
#sorted_List=sorted(contest_List, key=lambda x: int(x.split()[4]), reverse=True)
sorted_List=sorted(contest_List)[::-1]
print(sorted_List)
# for line in range(5):
#     print(sorted_List[line])
FILE.close()