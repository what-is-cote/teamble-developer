import sys, os
sys.stdin=open(f'{os.path.dirname(os.path.realpath(__file__))}/input.txt', "rt")
input=sys.stdin.readline

# ----------내 풀이----------#
# def getSum(arr):
#   while len(arr)>1:
#     tmp=[]
#     for i in range(len(arr)-1):
#       tmp.append(arr[i] + arr[i+1])
#     arr=tmp
#   return arr[0]
  
# def DFS(x):
#   if x==n:
#     answer=getSum(res)
#     if answer==f:
#       for j in res:
#         print(j, end=' ')
#       sys.exit(0)
#   else:
#     for i in range(1, n+1):
#       if ch[i]==0:
#         ch[i]=1
#         res[x]=i
#         DFS(x+1)
#         ch[i]=0

# if __name__=="__main__":
#   n, f=map(int, input().split())
#   ch=[0]*(n+1)
#   res=[0]*n
#   DFS(0)


# ----------강의 풀이----------#
def DFS(L, sum):
  if L==n and sum==f:
    for x in p:
      print(x, end=' ')
    sys.exit(0)
  else:
    for i in range(1, n+1):
      if ch[i]==0:
        ch[i]=1
        p[L]=i
        DFS(L+1, sum+(p[L]*b[L]))
        ch[i]=0

if __name__=="__main__":
  n, f=map(int, input().split())
  p=[0]*n # 순열
  b=[1]*n # 이항계수(양 끝==1)
  ch=[0]*(n+1)
  for i in range(1, n): # 이항계수 초기화
    b[i]=b[i-1]*(n-i)//i 
  
  DFS(0, 0)
