import sys, os
sys.stdin = open(f'{os.path.dirname(os.path.realpath(__file__))}/input.txt', "rt")

stick = list(map(str, input()))
stack = []
check = cnt = 0

for x in stick:
    while stack:
        if tmp == '(' and x == ')':
            stack.pop()
            check = 1
            cnt += len(stack)
        elif stack[-1] == '(' and x == ')':
            stack.pop()
            check = 1
            cnt += 1 
        break
    if check != 1:
        stack.append(x)
    check = 0
    tmp = x
    

print(cnt)