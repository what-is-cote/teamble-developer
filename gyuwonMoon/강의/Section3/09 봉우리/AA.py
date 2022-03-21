import sys, os
sys.stdin=open(f'{os.path.dirname(os.path.realpath(__file__))}/input.txt', "rt")

# ----------내 풀이----------#
n=int(input())
ground=[list(map(int, input().split())) for _ in range(n)]

for i in range(n): # 각 요소의 좌우에 0 추가하기
  ground[i].insert(0, 0)
  ground[i].append(0)

ground.insert(0, [0]*(n+2)) # 맨 첫번째 줄에 0 추가하기
ground.append([0]*(n+2)) # 맨 마지막 줄에 0 추가하기

# 상하좌우 좌표
dx=[-1, +1, 0, 0]
dy=[0, 0, -1, 1]

cnt=0
for i in range(1, n+1):
  for j in range(1, n+1):
    w=0 # 상하좌우로 이동하기 위한 인덱스
    while w<4:
      near=ground[i+dx[w]][j+dy[w]]
      if ground[i][j]>near:
        w+=1
      else: break
    if w==4: # 상하좌우의 땅보다 높으면
      cnt+=1

print(cnt)


# ----------강의 풀이----------#
# n=int(input())
# ground=[list(map(int, input().split())) for _ in range(n)]

# ground.insert(0, [0]*n)
# ground.append([0]*n)

# for g in ground:
#   g.insert(0, 0)
#   g.append(0)

# # 상우하좌(시계방향) 좌표
# dx=[-1, 0, 1, 0]
# dy=[0, 1, 0, -1]

# cnt=0
# for i in range(1, n+1):
#   for j in range(1, n+1):
#     if all(ground[i][j]>ground[i+dx[k]][j+dy[k]] for k in range(4)):
#       cnt+=1      

# print(cnt)