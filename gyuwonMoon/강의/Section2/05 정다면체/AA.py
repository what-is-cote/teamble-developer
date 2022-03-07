import sys, os
sys.stdin=open(f'{os.path.dirname(os.path.realpath(__file__))}/input.txt', "rt")

# ----------내 풀이----------#
n, m=map(int, input().split())

maxSum=n+m # 최대 눈의 합
sum=list()
for i in range(n):
  for j in range(m):
    sum.append(i+1 + j+1) # 두 눈의 합

res=[]
max=0
for i in range(maxSum):
  tmp=sum.count(i+1)
  if tmp>max:
    max=tmp # 최대값 갱신
    res.clear()
    res.append(i+1)
  elif tmp==max:
    res.append(i+1)

for r in res:
  print(r, end=' ')
  
  
# ----------강의 풀이----------#
# n, m=map(int, input().split())

# cnt=[0]*(n+m+3) # 3은 넉넉하게
# max=-2147000000

# for i in range(1, n+1):
#   for j in range(1, m+1):
#     cnt[i+j]+=1 # 해당 합의 개수 증가

# # 최대값을 구하는 for문
# for i in range(n+m+1):
#   if cnt[i]>max:
#     max=cnt[i]

# for i in range(n+m+1):
#   if cnt[i]==max:
#     print(i, end=' ')