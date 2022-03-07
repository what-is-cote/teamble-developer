import os
import sys
os.system('clear')
sys.stdin=open("section_2/4.txt", "rt")

N = int(input())
arr = list(map(int,input().split()))
# avg = int(sum(arr) / N + 0.5)
avg = round(sum(arr)/N)
min = 300 
for i, x in enumerate(arr):
  gap = abs(x-avg)
  if( gap < min):
    min = gap
    score = x
    res = i + 1
  
  elif(gap == min):
    if( x > score):
      score = x
      res = i + 1

print(avg, res)




