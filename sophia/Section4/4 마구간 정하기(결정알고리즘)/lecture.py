import sys, os
sys.stdin = open(f'{os.path.dirname(os.path.realpath(__file__))}/input.txt', "rt")

def Count(len):
    cnt = 1
    ep = line[0]
    for i in range(1, N):
        if line[i] - ep >= len:
            cnt += 1
            ep = line[i]
    return cnt

N, C = map(int, input().split())
line = []

for _ in range(N):
    line.append(int(input()))
 
line.sort()
l = 1
r = line[N - 1]

while l <= r:
    mid = (l + r) // 2
    if Count(mid) >= C:
        res = mid
        l = mid + 1
    else:
        r = mid - 1

print(res)
        


    