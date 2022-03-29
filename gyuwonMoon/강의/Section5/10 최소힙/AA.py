import sys, os
sys.stdin=open(f'{os.path.dirname(os.path.realpath(__file__))}/input.txt', "rt")

# ----------내 풀이----------# 40점-시간초과
# q=[]

# while True:
#   c=int(input())
#   if c==-1:
#     break
#   elif c==0:
#     print(q.pop(0))
#   else:
#     q.insert(0, c)
#     tmp=c
#     for i in range(1, len(q)):
#       if tmp>q[i]:
#         q[i-1]=q[i]
#         q[i]=tmp
#       else:
#         break
        

# ----------강의 풀이----------#
import heapq as hq
a=[]

while True:
  n=int(input())
  if n==-1:
    break
  if n==0:
    if len(a)==0:
      print(-1)
    else:
      print(hq.heappop(a)) # 루트 노드값 pop
  else:
    hq.heappush(a, n)