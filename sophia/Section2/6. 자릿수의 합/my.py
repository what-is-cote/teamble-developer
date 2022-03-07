import sys, os
sys.stdin=open(f'{os.path.dirname(os.path.realpath(__file__))}/input.txt', "rt")

def digit_sum(x):
    sum = 0
    while x > 0:
        digit = x % 10
        sum += digit
        x = x // 10
    return sum

N = int(input())
num = list(map(int, input().split()))

max = 0
max_index = 0
digit = []
for i in range(N):
    digit.append(digit_sum(num[i]))

for i in range(N):
    if digit[i] > max:
        max = digit[i]
        max_index = i
        
print(num[max_index])




        