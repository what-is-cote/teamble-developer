import sys, os
from collections import deque
sys.stdin=open(f'{os.path.dirname(os.path.realpath(__file__))}/input.txt', "rt")

# ----------내 풀이----------# 실패
# must=deque(list(input()))
# n=int(input())

# idx=0
# for i in range(n):
#   lesson=deque(list(input()))
#   while lesson:
#     cur=lesson.popleft()
#     if must.count(cur)==0:
#       continue
#     else:
#       if must[idx]==cur:
#         idx+=1
#         continue
#         print("#%d NO" %i)
#         break
#   print("#%d YES" %i)


# ----------강의 풀이----------#
need=input()
n=int(input())
for i in range(n):
  plan=input()
  dq=deque(need) # dq 초기화
  for x in plan:
    if x in dq: # 필수 과목에 해당하면
      if x!=dq.popleft(): # 순서가 맞지 않는 경우
        print('#%d NO' %(i+1))
        break
  else: # 순서가 모두 맞는 경우
    if len(dq)==0:
      print('#%d YES' %(i+1))
    else: # 모든 과목을 수강하지 않은 경우
      print('#%d NO' %(i+1))