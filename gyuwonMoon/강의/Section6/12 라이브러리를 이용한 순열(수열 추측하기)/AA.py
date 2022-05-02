import sys, os
import itertools as it
sys.stdin=open(f'{os.path.dirname(os.path.realpath(__file__))}/input.txt', "rt")
input=sys.stdin.readline

# ----------강의 풀이----------#
n, f=map(int, input().split())
b=[1]*n # 이항계수(양 끝==1)
for i in range(1, n): # 이항계수 초기화
  b[i]=b[i-1]*(n-i)//i

a=list(range(1, n+1))
for tmp in it.permutations(a): # a의 모든 순열의 경우를 구해줌
  sum=0
  for L, x in enumerate(tmp): # L:인덱스, x:값
    sum+=(x*b[L])
  if sum==f:
    for x in tmp:
      print(x, end=' ')
    break