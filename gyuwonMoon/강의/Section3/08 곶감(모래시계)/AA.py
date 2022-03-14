import sys, os
sys.stdin=open(f'{os.path.dirname(os.path.realpath(__file__))}/input.txt', "rt")

# ----------내 풀이----------#
n=int(input())
ground=[list(map(int, input().split())) for _ in range(n)]
m=int(input())

for _ in range(m):
  r, d, c=map(int, input().split()) # 행번호, 방향, 회전수
  if d==0: # 왼쪽
    for _ in range(c):
      ground[r-1].append(ground[r-1].pop(0))
  elif d==1: # 오른쪽
    for _ in range(c):
      ground[r-1].insert(0, ground[r-1].pop())
      
s=0
e=n

tot=0
for i in range(n):
  tot+=sum(ground[i][s:e])
  
  if i<n//2:
    s+=1
    e-=1
  else:
    s-=1
    e+=1

print(tot)


# ----------강의 풀이----------#
# 동일