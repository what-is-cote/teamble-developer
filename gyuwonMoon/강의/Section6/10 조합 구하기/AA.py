import sys, os
sys.stdin=open(f'{os.path.dirname(os.path.realpath(__file__))}/input.txt', "rt")
input=sys.stdin.readline

# ----------내 풀이----------#
# def DFS(x):
#   global cnt
#   if x==m:
#     if set(res) not in ch:
#       for j in range(m):
#         print(res[j], end=' ')
#       ch.append(set(res))
#       print()
#       cnt+=1
#   else:
#     for i in range(1, n+1):
#       if i not in res:
#         res[x]=i
#         DFS(x+1)

# if __name__=="__main__":
#   n, m=map(int, input().split())
#   res=[0]*m
#   ch=[]
#   cnt=0
#   DFS(0)
#   print(cnt)


# ----------강의 풀이----------#
def DFS(L, s):
  global cnt
  if L==m:
    for j in range(L):
      print(res[j], end=' ')
    cnt+=1
    print()
  else:
    for i in range(s, n+1):
      res[L]=i
      DFS(L+1, i+1)

if __name__=="__main__":
  n, m=map(int, input().split())
  res=[0]*(n+1)
  cnt=0
  DFS(0, 1)
  print(cnt)