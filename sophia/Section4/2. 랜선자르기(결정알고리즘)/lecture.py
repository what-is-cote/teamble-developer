import sys, os
sys.stdin = open(f'{os.path.dirname(os.path.realpath(__file__))}/input.txt', "rt")

def Count(len):
    cnt = 0
    for x in line:
        cnt += (x // len)
    return cnt

K, N = map(int, input().split())
line = []
res = 0
largest = 0

for _ in range(K):
    tmp = int(input())
    line.append(tmp)
    largest = max(largest, tmp)

l = 1
r = largest

while(l <= r):
    mid = (r + l) // 2
        
    if Count(mid) >= N:
        res = mid
        l = mid + 1
    else:
        r = mid - 1
print(res)
