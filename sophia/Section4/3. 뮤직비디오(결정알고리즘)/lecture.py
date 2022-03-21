import sys, os
sys.stdin = open(f'{os.path.dirname(os.path.realpath(__file__))}/input.txt', "rt")

def Count(capacity):
    cnt = 1
    sum = 0
    for x in song:
        if sum + x > capacity:
            cnt += 1
            sum = x
        else:
            sum += x
    return cnt

N, M = map(int, input().split())
song = list(map(int, input().split()))

maxx = max(song)
l = 1
r = sum(song)
res = 0
 
while l <= r:
    mid = (l + r) // 2
    
    if mid >= maxx and Count(mid) <= M:
        res = mid
        r = mid - 1
    else:
        l = mid + 1

print(res)