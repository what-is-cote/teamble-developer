import sys, os
import itertools as it
sys.stdin=open(f'{os.path.dirname(os.path.realpath(__file__))}/input.txt', "rt")
input=sys.stdin.readline

# ----------강의 풀이----------#
n, k=map(int, input().split())
a=list(map(int, input().split()))
m=int(input())
cnt=0

for x in it.combinations(a, k): # a에서 k개 뽑기
  if sum(x)%m==0:
    cnt+=1

print(cnt)