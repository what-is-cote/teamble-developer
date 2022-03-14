import sys, os
sys.stdin=open(f'{os.path.dirname(os.path.realpath(__file__))}/input.txt', "rt")

N = int(input())
str = []
output = 0
index = 1

for i in range(N):
    str.append(input().lower())

for i in list(str):
    f = 0
    e = len(i) - 1
    while(f < e):
        output = 0
        if i[f] != i[e]:
            output = 1
            break
        f += 1
        e -= 1
    print('#%d ' %index, end = '')
    index += 1
    if output == 1:
        print('NO')
    else:
        print('YES')
        