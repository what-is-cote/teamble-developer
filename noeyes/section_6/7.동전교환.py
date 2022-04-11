import os , sys
from collections import deque
# sys.stdin=open("noeyes/section_6/7.동전교환.txt", "rt")
# input = sys.stdin.readline
# s = input().rstrip()

def gogo (i):
  global cost , count
  
  if i >= len(arr):
    return
  
  while cost - arr[i] >= 0:
    cost -= arr[i]
    count += 1
  
  gogo(i+1)


if __name__ == "__main__":
  n = int(input())
  arr = list(map(int,input().split()))
  cost = int(input())
  count = 0
  arr.sort(reverse=True)
  gogo(0)
  print(count)
# 80점
