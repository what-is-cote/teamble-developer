import sys, os
sys.stdin=open(f'{os.path.dirname(os.path.realpath(__file__))}/input.txt', "rt")

a, b=map(int, input().split())

if a>b:
  print('>')
elif a<b:
  print('<')
else:
  print('==')