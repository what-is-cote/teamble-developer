import sys, os
sys.stdin=open(f'{os.path.dirname(os.path.realpath(__file__))}/input.txt', "rt")

s = input()
res = 0
cnt = 0

for x in s:
    if x.isdecimal():
        res = res * 10 + int(x)
print(res)

for i in range(1, res+1):
    if res % i == 0:
        cnt += 1
print(cnt)