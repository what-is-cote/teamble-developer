import sys, os
sys.stdin=open(f'{os.path.dirname(os.path.realpath(__file__))}/input.txt', "rt")

# def digit_sum(x):
#     sum = 0
#     while x > 0:
#         sum += x % 10
#         x = x // 10
#     return sum

# string으로 변환시킨 후 한 자리씩 분리
def digit_sum(x):
    sum = 0
    for i in str(x):
        sum += int(i)
    return sum

N = int(input())
a = list(map(int, input().split()))


max = -2147000000
for x in a:
    tot = digit_sum(x)
    if tot > max:
        max = tot
        res = x
print(res)



        