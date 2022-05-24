import sys, os
sys.stdin=open(f'{os.path.dirname(os.path.realpath(__file__))}/input.txt', "rt")

n=int(input())

for i in range(1, 10):
  print(f'{n} * {i} = {n*i}')
  # print('%d * %d = %d' %(n, i, n*i))