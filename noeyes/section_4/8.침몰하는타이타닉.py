import os , sys
from collections import deque
# sys.stdin=open("noeyes/section_4/8.침몰하는타이타닉.txt", "rt")

n ,m= map(int,input().split())
people = list(map(int,input().split()))

people.sort(reverse=True)
que = deque(people)

# lt = 0
# rt = n -1
# count = 0

# while lt <= rt:
#   if people[lt] + people[rt] > m:
#     count +=1
#     lt += 1
#   else:
#     lt += 1
#     rt -= 1
#     count +=1

# print(count)

while que:
  
count = 0
  if len(que) == 1:
    count+=1
    break
  
  if que[0] + que[-1] > m:
    count+=1
    que.popleft()
  else:
    count+=1
    que.popleft()
    que.pop();
    
print(count)
    