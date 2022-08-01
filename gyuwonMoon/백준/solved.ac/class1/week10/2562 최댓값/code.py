import sys, os
sys.stdin=open(f'{os.path.dirname(os.path.realpath(__file__))}/input.txt', "rt")

num=[]
for _ in range(9):
  num.append(int(input()))

print(max(num))
print(num.index(max(num))+1)