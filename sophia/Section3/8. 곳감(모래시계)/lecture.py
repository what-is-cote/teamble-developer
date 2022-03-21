import sys, os
sys.stdin = open(f'{os.path.dirname(os.path.realpath(__file__))}/input.txt', "rt")

N = int(input())
l = [list(map(int, input().split())) for _ in range(N)]
M = int(input())
for i in range(M):
    h, t, k = map(int, input().split())
    if t == 0:
        for _ in range(k):
            l[h-1].append(l[h-1].pop(0))   
    else:
        for _ in range(k):
            l[h-1].insert(0, l[h-1].pop())   
s = 0
e = N - 1
tot = 0

for i in range(N):
    for j in range(s, e+1):
        tot += l[i][j]
    if i < N//2:
        s += 1
        e -= 1
    else:
        s -= 1
        e += 1

print(tot)
