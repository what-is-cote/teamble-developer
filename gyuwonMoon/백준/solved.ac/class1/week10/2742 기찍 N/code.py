import sys, os
sys.stdin=open(f'{os.path.dirname(os.path.realpath(__file__))}/input.txt', "rt")

n=int(input())

for i in range(n, 0, -1):
  print(i)