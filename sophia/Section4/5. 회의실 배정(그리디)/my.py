import sys, os
sys.stdin = open(f'{os.path.dirname(os.path.realpath(__file__))}/input.txt', "rt")

n = int(input())
time = []

for _ in range(n):
    s, e = map(int, input().split())
    time.append((s, e))
    
time.sort(key = lambda x:x[1])
    
tmp = time[0][1]
cnt = 1
for i in range(1, n):
    if tmp <= time[i][0]:
        tmp = time[i][1]
        cnt += 1
print(cnt)