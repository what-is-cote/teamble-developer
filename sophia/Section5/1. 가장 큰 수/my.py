import sys, os
sys.stdin = open(f'{os.path.dirname(os.path.realpath(__file__))}/input.txt', "rt")

n,m = map(int, input().split())
num_list = list(map(int, str(n)))
num_stack = []
tmp = max(num_list) + 1
cnt = 0

for x in num_list:
    if cnt < m:
        while(1):
            if tmp < x:
                if cnt == m:
                    break
                num_stack.pop()
                cnt += 1
                if len(num_stack) > 0:
                    tmp = num_stack[-1]
                else:
                    break
            else: 
                break
        tmp = x
        num_stack.append(x)
    else:
        num_stack.append(x)
        
if cnt < m:
    while cnt < m:
        num_stack.pop()
        cnt += 1

print(''.join(str(s) for s in num_stack))