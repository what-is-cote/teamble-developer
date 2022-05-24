import sys, os
sys.stdin=open(f'{os.path.dirname(os.path.realpath(__file__))}/input.txt', "rt")

n=int(input())

for i in range(1, n+1):
  for j in range(n-i, 0, -1):
    print(' ', end='')
  for j in range(i):
    print('*', end='')
  print()