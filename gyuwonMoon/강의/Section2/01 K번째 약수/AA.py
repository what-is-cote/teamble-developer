import sys, os
sys.stdin=open(f'{os.path.dirname(os.path.realpath(__file__))}/input.txt', "rt")

# ----------내 풀이---------- #
# 입력 받기
n, k=map(int, input().split())

# n의 약수 찾기
num=[]
for i in range(1, n+1):
  if n%i==0:
    num.append(i)

if num[k-1]: # 틀린 이유: 인덱스 벗어난 경우 에러 발생(False가 아님)
  print(num[k-1])
else:
  print(-1)


# ----------강의 풀이----------#
'''
cnt=0
for i in range(1, n+1):
  if n%i==0:
    cnt+=1
  if cnt==k:
    print(i)
    break
else:
  print(-1)
'''