# 오류 있음
import sys, os
sys.stdin=open(f'{os.path.dirname(os.path.realpath(__file__))}/input.txt', "rt")

N, M = map(int, input().split())
l = list(map(int, input().split()))

p1 = p2 = 0
cnt = sum = 0

while p1 < N:
    p2 = p1
    if l[p1] < M:
        p2 += 1
        if p2 == N:
            break
    else:
        if l[p1] == M:
            cnt += 1
        p1 += 1
        p2 += 1
        continue
    while 1:
        sum = 0
        for i in range(p1, p2+1):
            sum += l[i]
        if sum < M:
            p2 += 1
        else:
            if sum == M:
                cnt += 1
            p1 += 1
            break
print(cnt)