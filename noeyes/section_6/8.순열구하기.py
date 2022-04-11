import os , sys
from collections import deque
# sys.stdin=open("noeyes/section_6/8.순열구하기.txt", "rt")
# input = sys.stdin.readline
# s = input().rstrip()

def gogo (index):
  global count 
  
  if index == m:
    for key in arr:
      print(key,end=' ')
    print()
    count += 1
    return
  
  for i in range(1,n+1):
    # 중복 체크 추가
    arr[index] = i
    gogo(index+1)
  


if __name__ == "__main__":
  n , m = map(int,input().split())
  arr = [0] * m
  index=0
  count = 0
  gogo(index)
  print(count)


# 100점
