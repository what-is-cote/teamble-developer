import os
import sys
os.system('clear')
sys.stdin=open("section_2/1.txt", "rt")

n, k = map(int,input().split());
count = 0;
for i in range(1,n+1):
  if(n % i == 0): 
    count = count + 1
  
  if(count == k):
    print(k)
    break
