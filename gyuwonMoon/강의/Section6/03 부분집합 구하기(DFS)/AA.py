import sys, os
sys.stdin=open(f'{os.path.dirname(os.path.realpath(__file__))}/input.txt', "rt")

# ----------내 풀이----------# 실패
#   for i in x:
#     print(i, end=" ")
#   DFS(x.pop())
  
# if __name__=="__main__":
#   n=int(input())
#   arr=list(range(1, n+1))
#   DFS(arr)


# ----------강의 풀이----------#
# 상태 트리(사용 O/X)
def DFS(v):
  if v==n+1:
    for i in range(1, n+1):
      if ch[i]==1:
        print(i, end=' ')
    print()
  else:
    ch[v]=1 # 원소 1을 포함
    DFS(v+1)
    ch[v]=0 # 원소 1을 포함X
    DFS(v+1)


if __name__=="__main__":
  n=int(input())
  ch=[0]*(n+1) # 원소 사용 여부 체크
  DFS(1)