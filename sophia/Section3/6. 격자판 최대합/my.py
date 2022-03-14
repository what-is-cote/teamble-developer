import sys, os
sys.stdin = open(f'{os.path.dirname(os.path.realpath(__file__))}/input.txt', "rt")

N = int(input())
l = [list(map(int, input().split())) for _ in range(N)]
row = col = diag = 0
max_num = tot = 0

# 각 행의 합
for i in range(N):
    for j in range(N):
        tot += l[i][j]
    if tot > max_num:
        max_num = tot
    tot = 0
row = max_num
max_num = 0

# 각 열의 합
for j in range(N):
    for i in range(N):
        tot += l[i][j]
    if tot > max_num:
        max_num = tot
    tot = 0
col = max_num
max_num = 0

# 두 대각선의 합
#1
for i in range(N):
    tot += l[i][i]
max_num = tot
tot = 0

#2
for i in range(N):
    tot += l[i][N-i-1]
if tot > max_num:
    max_num = tot
diag = max_num

num = []
num.append(row)
num.append(col)
num.append(diag)
print(max(num))