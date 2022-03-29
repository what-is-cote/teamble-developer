import sys, os
import heapq as hq
sys.stdin=open(f'{os.path.dirname(os.path.realpath(__file__))}/input.txt', "rt")

# ----------내 풀이----------# 40점-시간초과
# a=[]

# while True:
#   n=int(input())
#   if n==-1:
#     break
#   if n==0:
#     if len(a)==0:
#       print(-1)
#     else:
#       print(hq.heappop(a))
#       hq._heapify_max(a)
#   else:
#     hq.heappush(a, n)
#     hq._heapify_max(a)
        

# ----------강의 풀이----------#
# heapq는 기본적으로 "최소힙"으로 작동 => 부호를 바꾸자!
a=[]

while True:
  n=int(input())
  if n==-1:
    break
  if n==0:
    if len(a)==0:
      print(-1)
    else:
      print(-hq.heappop(a)) # pop할 때 부호 바꾸기
  else:
    hq.heappush(a, -n) # push할 때 부호 바꾸기