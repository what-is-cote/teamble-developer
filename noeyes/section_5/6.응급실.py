import os , sys
from collections import deque
# sys.stdin=open("noeyes/section_5/6.응급실.txt", "rt")

n, m=map(int, input().split())
q=list(map(int,input().split()))
dq=deque(q)
person = m
order = 0

while True:
  if(dq[0] < max(dq)):
    dq.append(dq.popleft())
    if(person == 0):
      person = len(dq) -1
    else:
      person -= 1
  else:
    dq.popleft()
    order += 1
    
    if(person == 0):
      print(order)
      break
    person -= 1

# 100점