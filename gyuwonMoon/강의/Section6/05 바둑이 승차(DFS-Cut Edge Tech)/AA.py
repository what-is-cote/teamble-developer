import sys, os
sys.stdin=open(f'{os.path.dirname(os.path.realpath(__file__))}/input.txt', "rt")

# ----------내 풀이----------# 80점 -시간초과
# def DFS(i, sum):
#   global max
  
#   if sum<=c and sum>max: # 최댓값 갱신
#     max=sum
#   if i>=n or sum>c:
#     return
#   else:
#     DFS(i+1, sum+w[i]) # i번째 바둑이 포함O
#     DFS(i+1, sum) # i번째 바둑이 포함X


# if __name__=="__main__":
#   c, n=map(int, input().split())
#   w=[]
#   for _ in range(n):
#     a=int(input())
#     w.append(a)
  
#   max=0
#   DFS(0, 0)
#   print(max)


# ----------강의 풀이----------#
def DFS(L, sum, tsum): # tsum: 판단(O/X) 완료한 무게
  global result
  
  # Cut Edge2: 지금까지 구한 합 + 앞으로 더할 수 있는 최대합이 현재 최댓값보다 작다면 
  if sum+(total-tsum)<result: # 더 좋은 답이 나올 가능성X
    return
  if sum>c: # Cut Edge1
    return
  if L==n: # 부분집합 하나가 완성된 경우
    if sum>result:
      result=sum
  else:
    DFS(L+1, sum+a[L], tsum+a[L]) # tsum은 해당값을 판단했으면 무조건 더함
    DFS(L+1, sum, tsum+a[L])


if __name__=="__main__":
  c, n=map(int, input().split())
  a=[0]*n
  result=-2147000000
  for i in range(n):
    a[i]=int(input()) # 바둑이의 몸무게 저장
  total=sum(a)
  DFS(0, 0, 0)
  print(result)