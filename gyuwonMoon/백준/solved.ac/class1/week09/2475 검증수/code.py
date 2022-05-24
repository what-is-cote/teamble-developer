import sys, os
sys.stdin=open(f'{os.path.dirname(os.path.realpath(__file__))}/input.txt', "rt")

num=list(map(int, input().split()))

for i in range(len(num)):
  num[i]=num[i]**2

print(sum(num)%10)