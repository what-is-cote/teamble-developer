import sys, os
from collections import deque
sys.stdin=open(f'{os.path.dirname(os.path.realpath(__file__))}/input.txt', "rt")

# ----------내 풀이----------# 
# n, m=map(int, input().split())
# patient=deque(list(map(int, input().split())))

# cnt=0
# while True:
#   if patient[0]>=max(patient): # 진료 가능
#     patient.popleft()
#     cnt+=1
#     if m==0: # 현재 환자가 m번째 환자인 경우
#       print(cnt)
#       break
#     else:
#       m-=1
#   else:
#     patient.rotate(-1)
#     if m==0: # m번째 환자의 인덱스 이동
#       m=len(patient)-1
#     else:
#       m-=1
#     # patient.append(patient.popleft())


# ----------강의 풀이----------#
# m이라는 고정된 값을 유지하고 싶기 때문에 tuple 자료형으로 변환!
n, m=map(int, input().split())

# [(0, 60), (1,50), (2, 70), ...]
Q=[(pos, val) for pos, val in enumerate(list(map(int, input().split())))]
Q=deque(Q)

cnt=0
while True:
  cur=Q.popleft()
  if any(cur[1]<x[1] for x in Q):
    Q.append(cur)
  else:
    cnt+=1
    if cur[0]==m:
      print(cnt)
      break