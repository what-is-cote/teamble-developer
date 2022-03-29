import sys, os
sys.stdin=open(f'{os.path.dirname(os.path.realpath(__file__))}/input.txt', "rt")

# ----------내 풀이----------#
l=int(input())
h=list(map(int, input().split()))
m=int(input())

for _ in range(m):
  highest=h.index(max(h))
  lowest=h.index(min(h))
  h[highest]-=1
  h[lowest]+=1

print(max(h)-min(h))

  
# ----------강의 풀이----------#
# 가장 높은 것과 가장 낮은 것의 차이가 중요한 것이지
# 인덱스가 중요한 게 아님!! => sorting

# l=int(input())
# h=list(map(int, input().split()))
# m=int(input())

# h.sort()
# for _ in range(m):
#   h[0]+=1
#   h[l-1]-=1
#   h.sort()
# print(h[l-1]-h[0])