import os , sys
from collections import deque
sys.stdin=open("noeyes/section_5/2.쇠막대기.txt", "rt")

arr = list(map(str,input().split()[0]))
barLeft = 0
result = 0


for i in range(len(arr)):
  
  if(i > 0 and arr[i] == '(' and arr[i-1] == '('):
    barLeft += 1
  elif(arr[i] == ')' and arr[i-1] == '('):
    result += barLeft
  elif(arr[i] == ')' and arr[i-1] == ')'):
    barLeft -= 1
    result += 1
    
print(result)

# 100점