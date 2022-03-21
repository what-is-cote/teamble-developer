import sys, os
sys.stdin = open(f'{os.path.dirname(os.path.realpath(__file__))}/input.txt', "rt")

def Count(len):
    tmp = stable[0]
    cnt = 1
    
    for i in range(1, N):
        if stable[i] - tmp >= len:
            tmp = stable[i]
            cnt += 1
    return cnt

N, C = map(int, input().split())
stable = []

for _ in range(N):
    stable.append(int(input()))
 
stable.sort()

l = 1
r = stable[N-1] - stable[0]

while l <= r:
    mid = (l + r) // 2
    if Count(mid) >= C:
        res = mid
        l = mid + 1
    else:
        r = mid - 1
print(res)