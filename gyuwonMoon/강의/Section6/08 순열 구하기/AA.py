import sys, os
sys.stdin=open(f'{os.path.dirname(os.path.realpath(__file__))}/input.txt', "rt")
input=sys.stdin.readline

# ----------내 풀이----------#
# def DFS(L):
#   global cnt
#   if L==m:
#     for j in range(m):
#       print(res[j], end=' ')
#     print()
#     cnt+=1
#   else:
#     for i in range(1, n+1):
#       if i in res[:L]: # 중복되는 경우 제외
#         continue
#       res[L]=i
#       DFS(L+1)

# if __name__=="__main__":
#   n, m=map(int, input().split())
#   cnt=0
#   res=[0]*m
#   DFS(0)
#   print(cnt)


# ----------강의 풀이----------#
def DFS(L):
  global cnt
  if L==m:
    for j in range(m):
      print(res[j], end=' ')
    print()
    cnt+=1
  else:
    for i in range(1, n+1): # 가지 뻗기
      if ch[i]==0:
        ch[i]=1 # 사용한 숫자 체크
        res[L]=i
        DFS(L+1)
        ch[i]=0 # 되돌아온 후 체크 취소

if __name__=="__main__":
  n, m=map(int, input().split())
  cnt=0
  ch=[0]*(n+1)
  res=[0]*m
  DFS(0)
  print(cnt)