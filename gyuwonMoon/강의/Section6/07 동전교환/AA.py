import sys, os
sys.stdin=open(f'{os.path.dirname(os.path.realpath(__file__))}/input.txt', "rt")
input=sys.stdin.readline

# ----------내 풀이----------#
# (1) 40점 시간초과
# def DFS(x):
#   global cnt
#   if x<0:
#     return
#   if x==0:
#     res.append(cnt)
#     cnt=0
#   elif x>0:
#     for i in range(n):
#       x-=coin[i]
#       cnt+=1
#       DFS(x)

# if __name__=="__main__":
#   n=int(input())
#   coin=list(map(int, input().split()))
#   m=int(input())
#   cnt=0
#   res=[]

#   DFS(m)
#   print(min(res))


# (2) 20점
# def DFS(L, sum): # L은 동전의 개수
#   global m, res
#   if sum>m or L>res:
#     return
#   if sum==m and L-1<res:
#     res=L-1
#     sum=0
#     return
#   elif sum<m:
#     for i in range(n):
#       sum+=coin[i]
#       DFS(L+1, sum)

# if __name__=="__main__":
#   n=int(input())
#   coin=list(map(int, input().split()))
#   m=int(input())
#   res=2137000000

#   DFS(0, 0)
#   print(res)


# ----------강의 풀이----------#
def DFS(L, sum): # L은 동전의 개수
  global res
  if sum>m or L>res:
    return
  if sum==m:
    if L<res:
      res=L
  else:
    for i in range(n):
      DFS(L+1, sum+coin[i])

if __name__=="__main__":
  n=int(input())
  coin=list(map(int, input().split()))
  m=int(input())
  res=2147000000
  coin.sort(reverse=True)
  DFS(0, 0)
  print(res)