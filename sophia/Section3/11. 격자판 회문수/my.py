import sys, os
sys.stdin = open(f'{os.path.dirname(os.path.realpath(__file__))}/input.txt', "rt")

num = [list(map(int, input().split())) for _ in range(7)]
cnt = 0

for i in range(7):
    for j in range(3):
        for k in range(2):
            if num[i][j+k] != num[i][4+2*j-(j+k)]:
                break
        else:
            cnt += 1
            
for i in range(7):
    for j in range(3):
        for k in range(2):
            if num[j+k][i] != num[4+2*j-(j+k)][i]:
                break
        else:
            cnt += 1

print(cnt)