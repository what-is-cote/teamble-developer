import sys, os
sys.stdin=open(f'{os.path.dirname(os.path.realpath(__file__))}/input.txt', "rt")

a=int(input())
b=int(input())
c=int(input())

num=list(str(a*b*c))

for i in range(10):
  print(num.count(str(i)))