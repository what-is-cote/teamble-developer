import os
import sys
os.system('clear')
sys.stdin=open("noeyes/section_3/5.txt", "rt")

n , m = map(int,input().split())

arr = list(map(int,input().split()))
count = 0
sum = 0
for i in range(len(arr)):
  for j in range(i,len(arr)):
    sum += arr[j]

    if( sum > m):
      sum = 0 
      break
      
    elif(sum == m):
      count += 1
      sum=0
      break

print(count)