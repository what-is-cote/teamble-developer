import sys, os
sys.stdin=open(f'{os.path.dirname(os.path.realpath(__file__))}/input.txt', "rt")

# ----------내 풀이----------#
n, m=map(int, input().split())
w=list(map(int, input().split()))

w.sort()

l=0
r=n-1
cnt=0
while l<=r:
  if w[l]+w[r]<=m:
    l+=1
    r-=1
    cnt+=1
  else:
    r-=1
    cnt+=1
print(cnt)


# ----------강의 풀이----------#
# 1 lsist
# n, m=map(int, input().split())
# w=list(map(int, input().split()))
# w.sort()
# cnt=0

# while w: # p가 빌 때까지
#   if len(w)==1: # 마지막 한 명일 때 예외처리
#     cnt+=1
#     break
#   if w[0]+w[-1]>m:
#     w.pop()
#     cnt+=1
#   else:
#     w.pop(0) # 인수로 index 가능
#     w.pop()
#     cnt+=1
# print(cnt)

#2 deque
# from collections import deque
# n, m=map(int, input().split())
# w=list(map(int, input().split()))
# w.sort()
# w=deque(w) # deque는 pop연산 시 요소 자리 이동X, 포인터 변경O =>효율적
# cnt=0

# while w: # p가 빌 때까지
#   if len(w)==1: # 마지막 한 명일 때 예외처리
#     cnt+=1
#     break
#   if w[0]+w[-1]>m:
#     w.pop()
#     cnt+=1
#   else:
#     w.popleft()
#     w.pop()
#     cnt+=1
# print(cnt)