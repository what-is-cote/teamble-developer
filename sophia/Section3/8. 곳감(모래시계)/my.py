import sys, os
sys.stdin = open(f'{os.path.dirname(os.path.realpath(__file__))}/input.txt', "rt")

N = int(input())
l = [list(map(int, input().split())) for _ in range(N)]
M = int(input())
rot = [list(map(int, input().split())) for _ in range(M)]

for i in range(M):
    rem = rot[i][2] % N
    if rot[i][1] == 0:
        for _ in range(rem):
            tmp = l[rot[i][0]-1]
            num = tmp.pop(0)
            tmp.append(num)
    else:
        for _ in range(rem):
            tmp = l[rot[i][0]-1]
            num = tmp.pop()
            tmp.insert(0, num)
    l[rot[i][0]-1] = tmp
    tmp = 0

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
