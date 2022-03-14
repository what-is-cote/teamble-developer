import sys, os
sys.stdin = open(f'{os.path.dirname(os.path.realpath(__file__))}/input.txt', "rt")

N = int(input())
l = [list(map(int, input().split())) for _ in range(N)]
res = 0
s = e = N // 2
check = 0

for i in range(N):
    for j in range(s, e+1):
        res += l[i][j]
    if i < N//2:
        s -= 1
        e += 1
    else:
        s += 1
        e -= 1
        
print(res)