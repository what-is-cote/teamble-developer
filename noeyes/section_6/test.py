import os , sys
from collections import deque
sys.stdin=open("section_6/test.txt", "rt")

a = 5;

for i in range(1,a+1):
  for l in range(i,a):
    print(" ",end="")
  for j in range(0,i):
    print("*",end='')
  print() 
# str = input()
# str = str.upper();
# max1 = 0
# max2 = 0
# maxch = '#';
# sum = 1

# for i in range(0,len(str)):
#   if(i != 0 and str[i] == str[i-1]): continue
#   for j in range(i+1,len(str)):
#     if(str[i] == str[j]):
#       sum += 1
#   if(sum > max1):
#      max2 = max1
#      max1 = sum
#      maxch = str[i];
#   elif(sum > max2):
#     max2 = sum
#   sum = 0

# if(max1 == max2):
#   print("??")
# else:
#   print(maxch)