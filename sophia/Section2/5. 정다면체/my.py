import sys, os
sys.stdin=open(f'{os.path.dirname(os.path.realpath(__file__))}/input.txt', "rt")

N, M = map(int, input().split())
dice = []

for i in range(1, N+1):
    for j in range(1, M+1):
        dice.append(i + j)
    
max = 0   
sum = []

for i in range(2, N+M+1):
    cnt = dice.count(i)
    if cnt > max:
        max = cnt
        num = i
    elif cnt == max:
        sum.append(i)
sum.append(num)
sum.sort()

for i in list(sum):
    print(i, end = '')
        
        