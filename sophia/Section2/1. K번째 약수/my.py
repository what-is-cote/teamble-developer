import sys, os
sys.stdin=open(f'{os.path.dirname(os.path.realpath(__file__))}/input.txt', "rt")

n, k = map(int, input().split())

list = []

for i in range (1, n+1):
    if n % i == 0:
        list.append(i)

if k < 0 or k > len(list):
    print(-1)
else:
    print(list[k-1])
    