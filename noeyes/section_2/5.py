import os
import sys
os.system('clear')
sys.stdin=open("section_2/5.txt", "rt")

n, m = map(int,input().split())
count = [0] * (n+m+3)
max = 1000

for i in range(1, n+1):
  for j in range(1,m+1):
    count[i+j] += 1

for i in range(n+m+1):
  if( count[i] > max):
    max = count[i]

for i in range(n+m+1):
  if( count[i] == max):
    print(i, end=' ')