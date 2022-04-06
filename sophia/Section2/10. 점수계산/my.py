import sys, os
sys.stdin=open(f'{os.path.dirname(os.path.realpath(__file__))}/input.txt', "rt")

N = int(input())
result = list(map(int, input().split()))

total = 0
plus = 0

for i in range(N):
    if result[i] == 1:
        if plus > 0:
            plus += 1
            total += plus
        else:
            plus += 1
            total += 1
    else:
        plus = 0
        
print(total)