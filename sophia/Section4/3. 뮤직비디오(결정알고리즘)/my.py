import sys, os
sys.stdin = open(f'{os.path.dirname(os.path.realpath(__file__))}/input.txt', "rt")

def Count(len):
    sum = 0
    cnt = 1
    
    for x in song:
        if sum + x > len:
            sum = x
            cnt += 1
        else:
            sum += x
    return cnt

N, M = map(int, input().split())
song = list(map(int, input().split()))

l = max(song)
r = sum(song)
res = 0

while l <= r:
    mid = (l + r) // 2
    
    if Count(mid) <= M:
        res = mid
        r = mid - 1
    else:
        l = mid + 1

print(res)
