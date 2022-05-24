import sys, os
sys.stdin=open(f'{os.path.dirname(os.path.realpath(__file__))}/input.txt', "rt")

n=int(input())

for _ in range(n):
  r, s=input().split()
  r=int(r)
  
  for i in s:
    print(i*r, end='')
  print()