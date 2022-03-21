import sys, os
sys.stdin = open(f'{os.path.dirname(os.path.realpath(__file__))}/input.txt', "rt")

K, N = map(int, input().split())
line = []

for _ in range(K):
    line.append(int(input()))

l = 1
r = max(line)
num = 0

while(l <= r):
    mid = (r + l) // 2
    for i in line:
        num += i // mid
        
    if num >= N:
        res = mid
        l = mid + 1
    else:
        r = mid - 1
    num = 0
print(res)

