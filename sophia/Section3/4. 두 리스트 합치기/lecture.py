import sys, os
sys.stdin=open(f'{os.path.dirname(os.path.realpath(__file__))}/input.txt', "rt")

N = int(input())
a = list(map(int, input().split()))

M = int(input())
b = list(map(int, input().split()))

p1 = p2 = 0
l = []

while p1 < N and p2 < M:
    if a[p1] <= b[p2]:
        l.append(a[p1])
        p1 += 1
    else:
        l.append(b[p2])
        p2 += 1

if p1 < N:
    l += a[p1:]
else:
    l += b[p2:]

for i in l:
    print(i, end = ' ')