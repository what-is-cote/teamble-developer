import sys, os
sys.stdin=open(f'{os.path.dirname(os.path.realpath(__file__))}/input.txt', "rt")

# ----------내 풀이----------# 시간 초과
# N=int(input())

# if N==2:
#   print(1)
# else:
#   res=1
#   for i in range(3, N+1, 2):
#     for j in range(3, i, 2):
#       if i%j==0 and i!=j:
#         break
#     else: res+=1
    
#   print(res)


# ----------강의 풀이----------#
# 에라토스테네스 체: 가장 빠르게 소수의 개수를 구하는 방법

N=int(input())

ch=[0]*(N+1) # 모든 배열을 0으로 초기화

cnt=0
for i in range(2, N+1): # 1은 포함되지 않음
  if ch[i]==0: # 0인 경우 소수
    cnt+=1
    for j in range(i, N+1, i):
      ch[j]=1 # 해당 소수의 배수는 소수가 아니므로 1로 처리

print(cnt)