import os
import sys
os.system('clear')
sys.stdin=open("section_2/6.txt", "rt")

n = int(input())
arr = list(map(int,input().split()))

def digit_sum(x):
  sum = 0
  for i in str(x):
    sum += int(i)
  
  return sum

max = -1000

for i in range(arr):
  temp = digit_sum(i)
  if(temp > max):
    max = temp
    result = i
  
  print(result)

