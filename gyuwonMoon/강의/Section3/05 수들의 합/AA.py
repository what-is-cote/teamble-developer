import sys, os
sys.stdin=open(f'{os.path.dirname(os.path.realpath(__file__))}/input.txt', "rt")

# ----------내 풀이----------# testcase5 Time Limit Exceeded
# n, m=map(int, input().split())
# num=list(map(int, input().split()))

# cnt=0
# for i in range(n):
#   sum=0
#   j=i
#   while j<n and sum<m:
#     sum+=num[j]
#     if sum==m:
#       cnt+=1
#       break
#     else:
#       j+=1

# print(cnt)
    

# ----------강의 풀이----------#
n, m=map(int, input().split())
a=list(map(int, input().split()))
lt=0
rt=1
tot=a[0]
cnt=0

while True:
  if tot<m:
    if rt<n:
      tot+=a[rt]
      rt+=1
    else:
      break
  elif tot==m:
    cnt+=1
    tot-=a[lt] # 시작점 한 칸 오른쪽으로 이동
    lt+=1
  else: # tot>m
    tot-=a[lt] # 시작점 한 칸 오른쪽으로 이동
    lt+=1

print(cnt)