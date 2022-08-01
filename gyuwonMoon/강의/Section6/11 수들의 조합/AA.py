import sys, os
sys.stdin=open(f'{os.path.dirname(os.path.realpath(__file__))}/input.txt', "rt")
input=sys.stdin.readline

# ----------내 풀이----------#
# def DFS(L, s):
#   global cnt
#   if L==k:
#     if sum(res)%m==0:
#       cnt+=1
#   else:
#     for i in range(s, len(nums)):
#       res[L]=nums[i]
#       DFS(L+1, i+1)
      

# if __name__=="__main__":
#   n, k=map(int, input().split())
#   nums=list(map(int, input().split()))
#   m=int(input())
  
#   res=[0]*k
#   cnt=0
  
#   DFS(0, 0)
#   print(cnt)
  
  
# ----------강의 풀이----------#
def DFS(L, s, sum): # level, start, sum 
  global cnt
  if L==k:
    if sum%m==0:
      cnt+=1
  else:
    for i in range(s, n):
      DFS(L+1, i+1, sum+a[i])

if __name__=="__main__":
  n, k=map(int, input().split())
  a=list(map(int, input().split()))
  m=int(input())
  cnt=0
  
  DFS(0, 0, 0)
  print(cnt)