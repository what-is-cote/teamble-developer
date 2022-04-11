import sys, os
sys.stdin=open(f'{os.path.dirname(os.path.realpath(__file__))}/input.txt', "rt")

# ----------내 풀이----------# 실패
# n, m=map(int, input().split())

# def DFS(n, m):
#   print(i+1, end=' ')
#   if m>0:
#     DFS(n, m-1)
#   print(i+1)
  
# for i in range(n):
#   DFS(i, m)


# ----------강의 풀이----------#
input=sys.stdin.readline
# s=input().rstrip()

def DFS(L):
  global cnt
  if L==m:
    for j in range(m):
      print(res[j], end=' ')
    print()
    cnt+=1
  else:
    for i in range(1, n+1):
      res[L]=i
      DFS(L+1)

if __name__=="__main__":
  n, m=map(int, input().split())
  res=[0]*m
  cnt=0
  DFS(0)
  print(cnt)