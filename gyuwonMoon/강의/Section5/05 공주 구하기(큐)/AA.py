import sys, os
from collections import deque
sys.stdin=open(f'{os.path.dirname(os.path.realpath(__file__))}/input.txt', "rt")

# ----------내 풀이----------# 
n, k=map(int, input().split())
prince=deque(list(range(1, n+1)))

cnt=1
while len(prince)>1:
  if cnt!=k:
    cnt+=1
    prince.rotate(-1) # 왼쪽으로 한 칸씩 이동
  else:
    prince.popleft()
    cnt=1
print(prince[0])


# ----------강의 풀이----------#
# n, k=map(int, input().split())
# dq=(list(range(1, n+1)))
# dq=deque(dq)

# cnt=1
# while dq:
#   for _ in range(k-1):
#     cur=dq.popleft()
#     dq.append(cur)
#   dq.popleft()
#   if len(dq)==1:
#     print(dq[0])
#     dq.popleft()