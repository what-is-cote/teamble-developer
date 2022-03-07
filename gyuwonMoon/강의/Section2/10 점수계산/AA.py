import sys, os
sys.stdin=open(f'{os.path.dirname(os.path.realpath(__file__))}/input.txt', "rt")

# ----------내 풀이----------#
n=int(input())
score=list(map(int, input().split()))

total=0
extra=0 # 가산점
for s in score:
  if s==0:
    extra=0
  else:
    total+=s+extra
    extra+=1

print(total)


# ----------강의 풀이----------#
# n=int(input())
# score=list(map(int, input().split()))

# total=0
# extra=0 # 가산점
# for s in score:
#   if s==1:
#     extra+=1
#     total+=extra
#   else:
#     extra=0

# print(total)