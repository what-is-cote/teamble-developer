import sys, os
sys.stdin=open(f'{os.path.dirname(os.path.realpath(__file__))}/input.txt', "rt")
input=sys.stdin.readline

# ----------내 풀이----------#
# n, m=map(int, input().split())
# graph=[[0]*n for _ in range(n)]

# for _ in range(m):
#   s, e, p=map(int, input().split())
#   graph[s-1][e-1]=p

# for i in range(n):
#   for j in range(n):
#     print(graph[i][j], end=' ')
#   print()
  
  
# ----------강의 풀이----------#
# 인접행렬: 행=>열 (1행=>2열 == 1번 노드=>2번 노드)

# 무방향 그래프
# n, m=map(int, input().split())
# g=[[0]*(n+1) for _ in range(n+1)]

# for _ in range(m):
#   a, b=map(int, input().split())
#   # 양쪽 노드 모두 상호 이동 가능
#   g[a][b]=1
#   g[b][a]=1

# for i in range(1, n+1):
#   for j in range(1, n+1):
#     print(g[i][j], end=' ')
#   print()


# 방향 그래프
n, m=map(int, input().split())
g=[[0]*(n+1) for _ in range(n+1)]

for _ in range(m):
  a, b, c=map(int, input().split())
  g[a][b]=c

for i in range(1, n+1):
  for j in range(1, n+1):
    print(g[i][j], end=' ')
  print()