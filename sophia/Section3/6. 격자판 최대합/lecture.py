import sys, os
sys.stdin = open(f'{os.path.dirname(os.path.realpath(__file__))}/input.txt', "rt")

N = int(input())
l = [list(map(int, input().split())) for _ in range(N)]
largest = -2147000000

# 각 행, 열의 합 
for i in range(N):
    sum1 = sum2 = 0
    for j in range(N):
        sum1 += l[i][j]
        sum2 += l[j][i]
    if sum1 > largest:
        largest = sum1    
    if sum2 > largest:
        largest = sum2

sum1 = sum2 = 0
# 두 대각선의 합
for i in range(N):
    sum1 += l[i][i]
    sum2 += l[i][N-i-1]
    
if sum1 > largest:
    largest = sum1    
if sum2 > largest:
    largest = sum2
    
print(largest)