import sys, os
sys.stdin = open(f'{os.path.dirname(os.path.realpath(__file__))}/input.txt', "rt")

N = int(input())
l = [list(map(int, input().split())) for _ in range(N)]
cnt = 0

tmp = [0] * (N+2)
l.insert(0, tmp)
l.append(tmp)

for i in range(1, N+1):
    l[i].append(0)
    l[i].insert(0, 0)

for i in range(N+2):
    for j in range(N+2):
        if l[i-1][j] < l[i][j]:
            if l[i+1][j] < l[i][j]:
                if l[i][j-1] < l[i][j]:
                    if l[i][j+1] < l[i][j]:
                        cnt += 1
                        
print(cnt)