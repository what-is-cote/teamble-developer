import sys, os
sys.stdin=open(f'{os.path.dirname(os.path.realpath(__file__))}/input.txt', "rt")

# ----------내 풀이----------#
# n=int(input())
# num=list(map(int, input().split()))
# res=[]
# num.reverse()

# for i in num:
#   res.insert(i, n)
#   n-=1

# for r in res:
#   print(r, end=' ')


# ----------강의 풀이----------#
# 1부터 n까지 차례로 처리(오름차순)
# 먼저 처리된 숫자는 무조건 더 작은 숫자임
n=int(input())
a=list(map(int, input().split()))
seq=[0]*n

for i in range(n): # 1~n까지의 수 자리 찾기`
  for j in range(n): # 각각의 수 위치 찾기
    if a[i]==0 and seq[j]==0: # 들어갈 공간을 찾았고, 비어있으면
      seq[j]=i+1 # 자기 자리에 들어감
      break
    elif seq[j]==0: # 빈자리 발견(==자기자신보다 큰 수)
      a[i]-=1
for x in seq:
  print(x, end=' ')