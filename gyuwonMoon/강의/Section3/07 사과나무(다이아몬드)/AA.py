import sys, os
sys.stdin=open(f'{os.path.dirname(os.path.realpath(__file__))}/input.txt', "rt")

# ----------내 풀이----------#
# n=int(input())
# ground=[list(map(int, input().split())) for _ in range(n)]

# cnt=0
# for i in range(n//2+1): # 다이아몬드 모양이므로 반복횟수는 절반
#   cnt+=sum(ground[i][n//2-i:n//2+1+i]) # 위쪽
#   if i!=n//2: # 마지막(가운데)행이 아닌 경우
#     cnt+=sum(ground[-1-i][n//2-i:n//2+1+i]) # 아래쪽

# print(cnt)

# ----------강의 풀이----------#
n=int(input())
ground=[list(map(int, input().split())) for _ in range(n)]

cnt=0
s=e=n//2
for i in range(n):
  for j in range(s, e+1): # 해당하는 위치만 탐색
    cnt+=ground[i][j]
  if i<n//2:
    s-=1
    e+=1
  else:
    s+=1
    e-=1

print(cnt)